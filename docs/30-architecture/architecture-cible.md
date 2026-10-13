---
title: Architecture cible (proposition de travail)
type: architecture
scope: [dev]
status: draft
updated: 2026-10-13
description: Lakehouse batch open source sur stockage objet S3, mono-client, avec bonnes pratiques d'ingestion, qualité, sécurité, sauvegarde et observabilité.
---

# Architecture cible : lakehouse batch open source

> **Statut : brouillon de travail.** Les choix d'outils sont des propositions à valider par un POC (section 12) et à consigner sous forme de décisions d'architecture (section 13). Les chiffres de volumétrie sont des hypothèses issues de l'échantillon `data/`, à refaire sur des données réelles.

Ce document alimente le Dossier d'architecture technique (DAT). Il s'appuie sur l'[expression de besoin](../10-besoins/expression-de-besoin-client.md) et sur le [cadre de travail](../00-cadrage/modalites-apprenant.md).

## 1. Contraintes qui structurent l'architecture

| Contrainte | Source | Conséquence |
|---|---|---|
| Batch nocturne, **pas de streaming** | Décision d'équipe | Pipeline planifié, fenêtre de traitement, pas de broker de messages |
| **Mono-client** (pas de multi-tenant) | Décision d'équipe | Une seule plateforme, pas d'isolation d'infrastructure par client |
| **Open source** et moderne | Décision d'équipe | Formats et briques ouverts, pas de verrouillage éditeur |
| Volume important, **historique pluriannuel** | Besoin client §6.1 | Stockage objet + format colonne, partitionnement, rétention par zones |
| Fraîcheur : fin de la semaine de retard | Besoin client §6.5 | Données de la veille disponibles chaque matin (cible à valider, voir §14) |
| **Cloisonnement entre adhérents**, non contournable | Besoin client §6.4 | Sécurité au niveau des lignes, dans la couche de données |
| Hétérogénéité des caisses | Besoin client §6.2 | Un adaptateur par éditeur, bronze fidèle, silver normalisé |
| Données personnelles (RGPD) | Besoin client §6.3 | Pas de donnée nominative cette année, zone réservée prévue pour la suite |
| **Sobriété** et budget (~3 M€ / 3 ans) | Besoin client §6.6, §6.7 | Dimensionnement raisonné, calcul éteint hors fenêtre, formats compressés |
| Hébergement en France, souveraineté | Besoin client §5 | Stockage S3 compatible hébergé en France |
| Livraisons régulières | Besoin client §6.6 | Construction par incréments (section 11) |

## 2. Vue d'ensemble

```
 ~750 magasins · plusieurs éditeurs de caisse · export nocturne (CSV, JSON...)
                                  │
                                  ▼
 ┌─ ZONE D'ÉCHANGE ──────────────────────────────────────────────────────┐
 │ Point de dépôt (SFTP / HTTPS) · identifiants par magasin · antivirus  │
 └───────────────────────────────┬───────────────────────────────────────┘
                                 ▼
 ┌─ PLATEFORME DE DONNÉES (stockage objet S3, France) ───────────────────┐
 │                                                                       │
 │  LANDING ──► BRONZE ──► SILVER ──► GOLD                               │
 │  original    Parquet    typé,       agrégats,                         │
 │  immuable    fidèle     nettoyé,    modèle en étoile,                 │
 │  (.gz)       (texte)    réconcilié  indicateurs                       │
 │                                                                       │
 │  Adaptateurs (Python)   dbt (SQL)         dbt (SQL)                   │
 │  ───────────────────────────────────────────────────────────────      │
 │  Catalogue de tables (Iceberg) · Moteur de requête (Trino)            │
 └───────┬───────────────────────────────────────────────┬───────────────┘
         │ orchestration (Dagster)                       │ requêtes
         │ qualité · lignage · observabilité             ▼
         │                                  ┌─ RESTITUTION ───────────┐
         │                                  │ BI (Superset) · SSO     │
         │                                  │ Keycloak · rôles/lignes │
         │                                  └───────────┬─────────────┘
         ▼                                              ▼
 Supervision (Prometheus, Grafana, Loki) · Sauvegarde        Directeurs de magasin,
 Secrets (Vault/OpenBao) · IaC (OpenTofu) · CI/CD            régions, national
```

## 3. Couches de données

| Zone | Contenu | Format | Écriture | Rétention proposée |
|---|---|---|---|---|
| **landing** | Fichier original reçu, compressé (`.gz` ou `.zst`), jamais modifié | Fichier d'origine | Ajout seul, verrou de suppression | Durée de l'historique, stockage froid après 90 jours |
| **bronze** | Copie fidèle, **toutes colonnes en texte** + colonnes techniques (`_source_file`, `_file_sha256`, `_ingested_at`, `_batch_id`, `_row_number`) | Parquet zstd, partition `ingest_date=` | Ajout seul | 13 à 24 mois au chaud, reconstructible depuis landing |
| **silver** | Données typées, dédoublonnées, horodatées en UTC et en heure locale, produits réconciliés, rejets isolés | Iceberg (Parquet zstd) | Idempotente (upsert / remplacement de partition) | Pluriannuelle (≥ 3 à 5 ans) |
| **gold** | Modèle en étoile et agrégats pour les tableaux de bord | Iceberg | Reconstruite depuis silver | Pluriannuelle |
| **quarantaine** | Fichiers ou lignes rejetés avec motif | Parquet | Ajout seul | 90 jours après correction |

Pourquoi garder le **texte** au bronze : l'échantillon montre cinq encodages, séparateurs, formats de date et d'heure différents, et des codes comme `0042` que le typage ferait devenir `42`. Typer au bronze fait perdre l'original en cas d'erreur de lecture. Mesures sur l'échantillon (252 039 lignes) : compression ×12 en gzip, ×18 en Parquet zstd (texte), requête d'agrégation ~20 fois plus rapide en Parquet qu'en CSV.

Nommage : `landing/source=<éditeur>/magasin=<id>/date=YYYY-MM-DD/`. **Pas de partition par magasin** : 750 magasins × 365 jours × 5 ans représente environ 1,4 million de petits fichiers. Partitionnez par date, triez par magasin à l'intérieur, visez 128 à 512 Mo par fichier et compactez.

## 4. Ingestion

1. **Dépôt** : chaque magasin envoie son export vers le point de dépôt avec ses propres identifiants (révocables individuellement). Les magasins qui ne peuvent pas pousser peuvent être interrogés (pull) si le client l'autorise.
2. **Contrôles à l'arrivée** : fichier complet (taille, somme de contrôle, nombre de lignes si fourni), format reconnu, pas déjà reçu (déduplication par hash). En cas d'échec : quarantaine et alerte, sans bloquer les autres magasins.
3. **Adaptateur par éditeur** (Python, une classe par format et par version) : encodage, séparateur, JSON imbriqué, vers un schéma bronze commun en texte.
4. **Manifeste** : liste des magasins attendus par jour. Un magasin absent à l'heure limite déclenche une alerte, et ses données sont intégrées à la nuit suivante (rattrapage).
5. **Idempotence** : retraiter un fichier ne crée jamais de doublon (clé de lot et de fichier).

Un contrat d'échange par éditeur (schéma attendu, version, exemples) doit être documenté avec le client.

## 5. Transformation, qualité et modélisation

**Transformation** : dbt (SQL versionné, testé, documenté) sur Trino et Iceberg, pour le silver et le gold. Python uniquement pour les adaptateurs d'ingestion.

**Qualité (contrôles à chaque étape)** :

- **Rapprochement** : lignes lues = lignes écrites + lignes rejetées, par fichier ; CA par magasin et par jour comparé au total de contrôle si la source en fournit un.
- **Contrôles de cohérence** : quantités négatives, prix absurdes, dates futures, produit sans équivalent national, doublons de ticket.
- **Détection d'anomalie de volume** : un magasin qui chute de 80 % par rapport à son jour équivalent est signalé.
- **Quarantaine** plutôt que suppression silencieuse, avec taux de rejet publié dans le tableau de bord de qualité.

**Réconciliation des produits** : table de correspondance code local → produit national (EAN/GTIN en priorité, sinon règles et validation manuelle). Les produits locaux sans équivalent restent visibles, marqués « local ».

**Modèle en étoile (gold)** :

| Faits | Dimensions |
|---|---|
| `fait_ligne_vente` (ticket, ligne, quantité, prix, remise, montant) | `dim_magasin` (hiérarchie magasin / région / national, historisée SCD2) |
| `fait_stock` (état par produit et par magasin) | `dim_produit` (national + local, historisée SCD2) |
| Agrégats : CA jour × magasin × rayon, comparaison N-1 | `dim_date` (calendrier commercial, jour équivalent N-1, fêtes mobiles) |
| | `dim_paiement`, `dim_caisse` |

Le temps est géré explicitement : horodatage en UTC et en heure locale, date commerciale, et comparaison N-1 sur le **jour équivalent** (même jour de la semaine), pas sur la date calendaire.

## 6. Orchestration

Dagster (ou Airflow si l'équipe le connaît déjà), avec une vue par actif de données (landing → bronze → silver → gold) et le lien avec dbt.

Fenêtre nocturne type (à valider) :

| Heure | Étape |
|---|---|
| 22:00 – 02:00 | Dépôts des magasins |
| 02:00 | Contrôles d'arrivée, rapport des manquants |
| 02:30 | Landing → bronze |
| 03:30 | Bronze → silver |
| 04:30 | Silver → gold |
| 05:30 | Contrôles de qualité, publication, rapport matinal |
| Avant 07:00 | **Objectif de disponibilité des données de la veille** |

Exigences : reprise automatique avec limites, **retraitement historique** possible (« on corrige une règle, on rejoue deux ans »), alertes sur retard par rapport à l'objectif, journal de chaque exécution.

## 7. Restitution

- **Moteur de requête** : Trino sur les tables Iceberg. Les tables gold sont petites et pré-agrégées, ce qui limite la latence. Si le POC montre des temps de réponse insuffisants sous charge, évaluer ClickHouse comme couche de service pour le gold.
- **BI** : Apache Superset, authentification par SSO.
- **Performance** : agrégats pré-calculés, cache, partitionnement par date, tailles de fichiers maîtrisées.
- **Simultanéité** : tester un pic de consultation (comité à 9 h) avec des dizaines d'utilisateurs en parallèle.
- **Exports** (Excel, PDF) et API selon les besoins confirmés par le client.

## 8. Sécurité et cloisonnement

**Le cloisonnement est une exigence forte et se traite dans la couche de données**, pas dans l'outil de BI.

- **Identité** : Keycloak (SSO, OIDC). La hiérarchie magasin → région → national est une donnée de référence, importée comme groupes et attributs.
- **Sécurité au niveau des lignes** : politiques appliquées par le moteur de requête (Trino avec règles de filtre par utilisateur, via OPA par exemple), l'outil de BI transmettant l'identité réelle de l'utilisateur. À valider par POC.
- **Tests automatisés de cloisonnement** : un utilisateur du magasin A ne lit rien du magasin B, par aucune voie (BI, SQL direct, export). Ces tests tournent à chaque livraison.
- **Comparaison entre pairs** : le sujet évoque le manque de point de comparaison. Proposition : moyennes agrégées sur un minimum de magasins (seuil, par exemple ≥ 5), sans jamais exposer un magasin identifiable. À valider avec le client.
- **Chiffrement** au repos (côté stockage) et en transit (TLS partout), **secrets** dans Vault ou OpenBao, jamais dans le code.
- **Réseau** : zone d'échange isolée de la plateforme, flux minimaux, aucun accès direct de l'extérieur au stockage.
- **Moindre privilège** : comptes de service séparés par composant, accès nominatifs journalisés.
- **Vulnérabilités** : analyse des dépendances et du code en intégration continue, correctifs planifiés.

## 9. Conformité et RGPD

- L'échantillon ne contient qu'un **indicateur** de fidélité (oui/non), pas de numéro de carte. Aucune donnée nominative n'est donc traitée aujourd'hui, et le sujet place la donnée porteur hors périmètre cette année.
- Pour la suite : **zone réservée** (bucket, clés de chiffrement et droits distincts), pseudonymisation par clé secrète (HMAC) tenue dans le coffre de secrets, durées de conservation définies avec le DPO, procédure de droit à l'effacement, journal des accès.
- Minimisation : ne charger que les colonnes utiles à un indicateur identifié.
- Registre des traitements et analyse d'impact : portés par le chef de projet.

## 10. Exploitation : sauvegarde, continuité, observabilité

### Sauvegarde et reprise

| Élément | Protection |
|---|---|
| `landing` (source de reconstruction) | Versionnement, verrou de suppression, copie sur un second site ou fournisseur (règle 3-2-1) |
| Bronze / silver / gold | Reconstructibles depuis landing ; réplication selon l'objectif de reprise |
| Catalogue de tables, bases (Keycloak, Superset, orchestrateur) | PostgreSQL avec archivage continu (reprise à un instant donné) et copies hors site |
| Code, configuration, définitions de sécurité | Git (source de vérité), infrastructure décrite en code |
| Secrets | Sauvegarde chiffrée du coffre |

Hypothèses à valider avec le client : **RPO 24 h** (un magasin peut renvoyer son export), **RTO de 4 à 8 h** pour la restitution. **Tester la restauration** régulièrement (par exemple chaque trimestre) et consigner le résultat. Identifier les points de défaillance uniques et les traiter dans le plan de continuité.

### Observabilité

| Niveau | Éléments suivis |
|---|---|
| Infrastructure | CPU, mémoire, disque, réseau, état du stockage |
| Pipelines | Durée, échecs, reprises, volumes, **fraîcheur par source**, magasins manquants |
| Qualité des données | Taux de rejet, écarts de rapprochement, anomalies de volume |
| Usage | Requêtes lentes, nombre d'utilisateurs, coût par requête |

Outils : Prometheus (métriques), Grafana (tableaux et alertes), Loki (journaux), OpenTelemetry (traces). Objectifs de service (SLO) à définir, par exemple « 95 % des jours, données de la veille disponibles avant 7 h », avec alertes actionnables qui portent un lien vers la procédure de résolution.

### Exploitation courante

Procédures d'exploitation (runbooks), gestion des incidents et retours d'expérience, astreinte à définir avec le client, plan de montée de version des composants.

## 11. Industrialisation et plan de livraison

**Industrialisation** :

- Code et infrastructure dans Git, dépôt unique ou par domaine, revues de code obligatoires.
- Intégration continue (le dépôt utilise déjà GitHub Actions et semantic-release) : tests unitaires des adaptateurs avec les fichiers de `data/` comme jeux d'essai, tests dbt, contrôles de cloisonnement, analyse de sécurité.
- Infrastructure décrite en code (OpenTofu / Ansible), déploiement reproductible, trois environnements : développement (échantillon), recette, production.
- Les tests de bout en bout peuvent tourner sur l'échantillon pour un coût très faible.

**Livraisons régulières** (le client refuse une livraison unique en fin de projet) :

| Incrément | Contenu | Valeur visible |
|---|---|---|
| I0 | Socle : dépôt, stockage, CI/CD, supervision minimale | Chaîne de bout en bout sur un fichier |
| I1 | Ingestion des 5 magasins pilotes, bronze, silver ventes | Données propres consultables en SQL |
| I2 | Gold CA par jour, magasin, rayon, comparaison N-1, premier tableau de bord, SSO, cloisonnement | Premier tableau de bord utilisable, **démonstration de l'étanchéité** |
| I3 | Stock et indicateurs de rupture, qualité publiée | Premiers signaux d'alerte |
| I4 | Montée en charge, sauvegarde testée, exploitation, recette | Dossier de recette, décision Go/NoGo |

## 12. POC à mener pour valider les choix

| Question | Critère de réussite |
|---|---|
| Le cloisonnement par ligne tient-il, par toutes les voies d'accès ? | Zéro fuite sur la batterie de tests |
| Trino + Iceberg tient-il la charge de consultation ? | Temps de réponse cible sous N utilisateurs simultanés |
| La fenêtre nocturne est-elle tenue au volume cible ? | Données de la veille disponibles avant l'heure visée, avec marge |
| Les adaptateurs absorbent-ils les formats dégradés ? | Aucune perte silencieuse, tout rejet tracé |
| Quelle est la compression réelle ? | Mesure sur données réelles ou fournies par le client |

Méthode : générer des données synthétiques à l'échelle visée à partir de l'échantillon, mesurer, puis **documenter l'extrapolation comme telle**.

## 13. Décisions d'architecture à consigner

À tracer sous forme de fiches courtes (contexte, options, choix, conséquences), car le référentiel exige la justification des choix :

1. Lakehouse batch plutôt que base relationnelle unique (critique de l'orientation du client).
2. Landing immuable + bronze Parquet texte fidèle.
3. Format de table Iceberg (silver, gold) et choix du catalogue.
4. Moteur de requête : Trino, avec ClickHouse en option.
5. Orchestrateur : Dagster ou Airflow.
6. Mécanisme de cloisonnement (couche de données, pas outil de BI).
7. Hébergement et stockage objet (sur site, ou fournisseur souverain).
8. Stratégie de sauvegarde et objectifs RPO/RTO.
9. Politique de rétention par zone.

## 14. Hypothèses et points ouverts

| Sujet | État |
|---|---|
| Volume quotidien réel (lignes ou tickets, pic de décembre) | À confirmer par le client. Hypothèse de travail : 50 à 200 millions de lignes par jour |
| Heure limite de disponibilité (7 h ?) | À valider |
| Nombre d'éditeurs de caisse et part de chacun | Recensement à obtenir |
| Mode de dépôt réalisable par les petits magasins | À valider avec le client |
| Hébergement : centre de données existant ou stockage S3 souverain | À trancher, avec le coût |
| Année d'historique à charger et durée de conservation légale | À valider avec le client et le DPO |
| Objectifs RPO / RTO / disponibilité | Hypothèses ci-dessus à valider |
| Qui exploite après la livraison | À définir |

### Ordre de grandeur de stockage (à refaire sur données réelles)

Avec les mesures de l'échantillon (127 octets/ligne brut, ~10 gzip, ~7 Parquet zstd texte) :

| Lignes / jour | Landing / an | Bronze / an |
|---|---|---|
| 50 millions | ~190 Go | ~130 Go |
| 200 millions | ~750 Go | ~530 Go |

Le silver et le gold s'ajoutent, du même ordre de grandeur. Sur cinq ans, comptez de quelques To à une dizaine de To avant redondance. Le coût de stockage est secondaire face au coût de calcul et d'exploitation, à chiffrer dans le business case par le chef de projet.

## 15. Sobriété (Green IT)

- Calcul **éteint hors fenêtre nocturne** et consultation légère le jour (montée et descente automatiques des ressources).
- Formats compressés (zstd), colonnes lues à la demande, partitionnement qui évite de relire l'historique.
- Pas de duplication inutile, rétention par zone, stockage froid pour l'ancien.
- Mesure : énergie ou ressources consommées par Go traité, publiée dans le tableau de bord de projet.
- Dimensionnement raisonné : démarrer petit, mesurer, grandir. Pas de cluster surdimensionné dès le départ.
