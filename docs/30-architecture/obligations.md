---
title: Obligations prestataire
type: architecture
scope: [dev]
status: draft
updated: 2026-11-24
description: Liste de contrôle des obligations légales, contractuelles et techniques de l'architecte prestataire, avec leur état dans Vibro et les écarts à traiter.
---

# Obligations de l'architecte et du prestataire

Cette liste sert de contrôle avant chaque livrable. Chaque ligne donne l'obligation, sa source, la section du livrable où la montrer et son état dans Vibro.

!!! abstract "En bref"
    - Pour la consolidation, le national est responsable de traitement. Nous sommes son sous-traitant (RGPD art. 28).
    - Le prestataire doit conseiller et mettre en garde par écrit, y compris sur la solution suggérée par le client.
    - Les chiffres des adhérents sont des secrets d'affaires, même sans donnée personnelle.
    - Un engagement chiffré a un périmètre, une mesure et des exclusions.
    - La réversibilité se prépare dès la conception : domaine, clés, code, données, documentation.

**État dans Vibro :** **Fait** (traité dans la documentation, avec le lien), **Partiel**, **À faire**, **À demander** (question écrite au client), **CDP** (porté par le chef de projet, notre part indiquée).

**Où :** section du livrable (CDC, DAT, DCT, REC, TBD, PMP, VEI) selon les [modalités](../00-cadrage/modalites-apprenant.md#5-detail-des-livrables). Les références A.x renvoient à l'annexe A de l'ISO/IEC 27001:2022.

!!! note "Portée"
    Document interne à l'équipe. Il ne part pas tel quel chez le client : il alimente le CDC, le DAT et le cahier de recette. Ce n'est pas un avis juridique : un point de droit se fait confirmer par écrit par la direction juridique du client.

## À traiter en priorité

Relevé du 24 novembre 2026 sur l'[architecture cible](architecture-cible.md) et l'[ingestion](ingestion.md). Chaque écart se suit dans une issue GitHub Projects.

1. **Le dépôt GitHub et le site sont publics.** Les pièces du client marquées « Diffusion : interne » sont en ligne sur GitHub Pages. L'échantillon de `data/`, « ni diffusable ni réutilisable », contient des matricules d'opérateurs, et GitHub l'héberge hors de l'UE. Retirer une page du site ne la retire pas de l'historique Git. Un site GitHub Pages reste public même si le dépôt devient privé, sauf avec GitHub Enterprise Cloud.
2. **Telle que décrite, la clé age n'existe que sur `orchestration`.** Si la VM disparaît, les secrets du dépôt deviennent illisibles. Même question pour la clé qui chiffre l'état OpenTofu.
3. **`orchestration` concentre tous les droits** : runner, OpenTofu, Ansible, clé age, SSH vers toutes les VM. Elle fait aussi tourner Dagster, qui lit les fichiers de 762 magasins. Une faille dans la lecture d'un fichier (un XML par exemple) donnerait accès à toute l'infrastructure.
4. **Le seuil de 5 magasins ne suffit pas seul.** La différence entre deux agrégats publiés peut isoler moins de 5 magasins. Un adhérent qui possède une partie des magasins d'un agrégat déduit la somme des autres.
5. **Le domaine du point de dépôt (à définir) sera l'adresse de 762 magasins.** S'il appartient au prestataire, un changement de prestataire oblige à reconfigurer chaque magasin.
6. **L'object lock du landing entre en conflit avec deux règles.** Un verrou en mode conformité interdit la purge d'un magasin retiré. Les fichiers de la voie 2 contiennent l'opérateur et doivent disparaître à 13 mois : la voie 2 ne se rejoue donc pas sur 5 ans.
7. **Ni l'empreinte ni le coût annuel ne sont chiffrés**, alors que le client demande une comparaison des options en énergie et en coût.
8. **Personne n'est désigné pour intervenir entre 23 h et 6 h.** Une intervention de nuit est une astreinte. Les montées de version « la nuit » tombent dans la fenêtre du batch.
9. **Les fiches de décision annoncées n'existent pas.**
10. **L'adhérent multi-magasins n'est pas traité** : vue consolidée, vue par magasin, drive séparable.

## 1. Conseil, engagements et contrat

| Obligation | Source | Où | Vibro |
|---|---|---|---|
| Mettre en garde le client par écrit sur ce qui est risqué : sa solution suggérée (filtre dans l'outil de BI, historique dans une seule table), et les risques connus hors de sa demande (stock théorique faux de 2 à 8 %, aucun RTO chez l'hébergeur actuel). | Devoir de conseil et de mise en garde du prestataire (jurisprudence constante) ; C. civ. art. 1112-1 | CDC 4.1 | **À faire** |
| Tracer chaque question posée, sa réponse ou son absence, et son impact. Le client doit collaborer, et il impose l'écrit. | Obligation de collaboration du client (jurisprudence) ; [réponses client](../00-cadrage/reponses-client/index.md) | PMP 5.1 | **Partiel** : réponses archivées, pas de registre des questions ouvertes |
| Ne promettre que ce qui se mesure : périmètre, méthode de mesure, exclusions. Exemple : « prêt à 7 h 30 pour les magasins livrés avant 23 h 30 ». | C. civ. art. 1231-1 (inexécution) | CDC 5.3 | **Partiel** : 7 h 30 annoncé sans exclusion |
| Ne pas promettre plus que les fournisseurs dont on dépend (cloud, PostgreSQL managé, éditeurs), sauf redondance qui le justifie. | Engagements en cascade | DAT 8.1 | **À faire** : SLA du fournisseur cloud à relever |
| Faire passer toute demande hors périmètre par un avenant. En 2023, quatre avenants ont porté le dépassement à 39 %. | [Modalités §2.3](../00-cadrage/modalites-apprenant.md#23-regles-du-jeu) ; [clôture 2023 §5](../00-cadrage/compte-rendu-cloture-projet-2023.md#5-depenses) | PMP | **CDP** : notre part, chiffrer l'impact technique de chaque demande |
| Écrire les critères d'acceptation avant de développer, et la durée de garantie après le PV de recette. | Contrat | CDC 5, REC 2 | **CDP** : notre part, critères et scénarios de recette |
| Caler les décisions sur le calendrier du client : préavis d'hébergement avant le 31 mars 2027, commission informatique trimestrielle, point d'étape trimestriel promis aux adhérents. | [Hébergement §7](../00-cadrage/reponses-client/hebergement-et-securite.md#7-echeances-contractuelles) ; [organisation §6 et §8](../00-cadrage/reponses-client/organisation-gouvernance.md#6-instances-et-pouvoir-de-decision) | DAT 10 | **À faire** : décisions « Ouvert » sans échéance |

Hors de notre périmètre (CDP) : prix, pénalités, responsabilité, assurance.

## 2. Données personnelles

| Obligation | Source | Où | Vibro |
|---|---|---|---|
| Signer les clauses de sous-traitance avant toute donnée réelle : instructions, confidentialité, sécurité, sous-traitants ultérieurs, aide aux droits et à l'AIPD, sort des données en fin de contrat, audit. | RGPD art. 28 ; [note juridique §1](../00-cadrage/reponses-client/donnees-personnelles-et-cloisonnement.md#1-qui-est-responsable-de-quoi) | CDC 7.3, DAT 5.2 | **CDP** : notre part, la liste des traitements et des mesures |
| Ne charger aucun magasin sans l'acte écrit par lequel l'adhérent confie ses données au national. | [Note juridique §1](../00-cadrage/reponses-client/donnees-personnelles-et-cloisonnement.md#1-qui-est-responsable-de-quoi) | DAT 3.1 | **Fait** : [ajout d'un magasin](ingestion.md#registre-des-sources) |
| Tenir le registre des traitements faits pour le compte du national. | RGPD art. 30.2 | DAT 5.2 | **À faire** |
| Lister les sous-traitants ultérieurs (fournisseur cloud, outils) et obtenir l'accord écrit du national. | RGPD art. 28.2 ; [note juridique §6](../00-cadrage/reponses-client/donnees-personnelles-et-cloisonnement.md#6-points-sur-lesquels-la-direction-juridique-doit-etre-saisie) | DAT 5.2 | **À faire** : fournisseur cloud **Ouvert** |
| Aucun transfert hors UE sans accord de la direction juridique. Vérifier aussi les outils de l'équipe : dépôt, CI, télémétrie. | RGPD ch. V ; [hébergement §2](../00-cadrage/reponses-client/hebergement-et-securite.md#2-localisation-des-donnees) | DAT 5.2 | **À faire** : échantillon sur GitHub |
| Retirer l'opérateur et l'identifiant de ticket au plus tôt. | RGPD art. 5.1.c et 25 | DAT 6.2 | **Fait** : [données personnelles](ingestion.md#donnees-personnelles), empreinte à faire valider |
| Appliquer chaque durée par une purge automatique : 5 ans pour les lignes et les stocks, 13 mois pour l'opérateur. Dire quand une donnée purgée sort des sauvegardes. | RGPD art. 5.1.e ; [note juridique §2](../00-cadrage/reponses-client/donnees-personnelles-et-cloisonnement.md#2-donnees-concernees-et-qualification) | DAT 3.2 | **Partiel** : passage au froid à 13 mois décrit, suppression à 5 ans non décrite |
| Vérifier que l'object lock ne bloque pas une purge obligatoire. Préférer le mode gouvernance au mode conformité. | RGPD art. 17 et 28.3.g | DAT 3.2 | **À faire** |
| Faire dire par la direction juridique si une AIPD est requise (grande échelle, données de salariés), et y contribuer. | RGPD art. 35 et 28.3.f | DAT 5.2 | **À demander** |
| Prévenir le national sans délai en cas de violation : il a 72 h pour notifier la CNIL. Écrire qui prévient qui, et l'exercer. | RGPD art. 33 | DAT 6, 8.2 | **À faire** |
| Ne mettre aucune donnée métier dans les journaux. Fixer leur durée de conservation, de 6 mois à 1 an selon la CNIL. | CNIL, recommandation sur la journalisation (2021) | DAT 7.3 | **À faire** : durée de Loki non fixée |
| Ne déposer que des cookies strictement nécessaires (session, authentification). Couper la télémétrie des outils : Dagster, dbt, Grafana, Superset, NocoDB, ClickHouse. | Loi Informatique et Libertés art. 82 (ePrivacy art. 5.3) ; RGPD ch. V | DAT 5.2 | **À faire** : à vérifier au POC |
| Garder les journaux d'accès des salariés pour la sécurité seulement. Ne fournir à l'employeur aucun suivi d'usage nominatif. | C. trav. L1222-4 et L2312-38 | DAT 6.1 | **À faire** |

## 3. Confidentialité et cloisonnement

| Obligation | Source | Où | Vibro |
|---|---|---|---|
| Protéger les chiffres des adhérents comme des secrets d'affaires, même sans donnée personnelle : engagement de confidentialité de l'équipe, accès au besoin d'en connaître. | C. com. L151-1 et suivants ; [note juridique §4](../00-cadrage/reponses-client/donnees-personnelles-et-cloisonnement.md#4-regles-de-cloisonnement) (exigence contractuelle) | DAT 6 | **Partiel** : cloisonnement décrit, engagement de l'équipe non écrit |
| Respecter les conditions d'usage des pièces du client : « Diffusion : interne », échantillon « ni diffusable ni réutilisable ». | `data/README.md` §6 ; en-têtes des pièces | — | **À faire** : dépôt et site publics |
| N'accéder aux données en exploitation que pour une intervention tracée et motivée : comptes nominatifs, aucun compte `default`, journal des requêtes conservé. | [Note juridique §4](../00-cadrage/reponses-client/donnees-personnelles-et-cloisonnement.md#4-regles-de-cloisonnement) (prestataire d'exploitation) | DAT 6.1 | **À faire** |
| Seuil de 5 magasins : bloquer aussi la différence entre deux agrégats (secret secondaire) et l'agrégat dominé par un seul magasin. Compter les magasins des autres adhérents seulement. | [Note juridique §4](../00-cadrage/reponses-client/donnees-personnelles-et-cloisonnement.md#4-regles-de-cloisonnement) ; règles du secret statistique (INSEE) | DAT 6.2 | **Partiel** : `HAVING uniq(magasin_id) >= 5` seul |
| Adhérent multi-magasins : vue consolidée et vue par magasin, drive séparable, rien d'un confrère. | [Remontées terrain §5](../00-cadrage/reponses-client/remontees-terrain.md#5-reponses-des-adherents-multi-magasins) | DAT 6.1 | **À faire** |
| Réserver la marge d'un magasin à son adhérent. | [Réponse 4.3](../00-cadrage/reponses-client/index.md#43-acces-regional-et-national) | DAT 6.1 | **À demander** : exclue pour la région, le national l'est-il aussi ? |
| Aucun classement nominatif, quelle que soit la maille. | [Note juridique §5](../00-cadrage/reponses-client/donnees-personnelles-et-cloisonnement.md#5-ce-qui-a-deja-pose-probleme) | DAT 6.1 | **Fait** : [cloisonnement](architecture-cible.md#cloisonnement) |
| Magasin qui change d'adhérent : qui voit l'historique, à quelle date les droits basculent. | [Registre des sources](ingestion.md#registre-des-sources) | DAT 6.1 | **À demander** : question posée pour le flux, pas pour les droits |
| Vérifier le cloisonnement par un test automatique à chaque livraison, par toutes les voies (BI, SQL, export). | [Besoin §6.4](../10-besoins/expression-de-besoin-client.md#64-cloisonnement-entre-adherents) (« solide et non contournable ») | REC 5 | **Fait** : [cloisonnement](architecture-cible.md#cloisonnement), [POC](architecture-cible.md#a-valider-au-poc) |

## 4. Sécurité

| Obligation | Source | Où | Vibro |
|---|---|---|---|
| Analyser les risques avant la mise en service, en quatre étapes : identification, gravité, probabilité, points critiques. Le client n'a aucune procédure. | [Modalités C3.2](../00-cadrage/modalites-apprenant.md#64-matrice-de-tracabilite-des-competences) ; [hébergement §6](../00-cadrage/reponses-client/hebergement-et-securite.md#6-regles-de-securite-appliquees) ; EBIOS RM (ANSSI) | CDC 7.2 | **À faire** |
| Chiffrer au repos tous les stockages : buckets, disques ClickHouse, sauvegardes. Le client ne chiffre pas ses dépôts de fichiers. | A.8.24 ; [hébergement §6](../00-cadrage/reponses-client/hebergement-et-securite.md#6-regles-de-securite-appliquees) | DAT 6 | **Partiel** : secrets et état OpenTofu chiffrés, buckets et disques non précisés |
| Exiger l'authentification multifacteur sur tous les accès d'administration. La décider pour les adhérents, qui voient leur marge. | A.8.5 ; [hébergement §6](../00-cadrage/reponses-client/hebergement-et-securite.md#6-regles-de-securite-appliquees) | DAT 6.1 | **À faire** |
| Désigner la source de vérité des droits (adhérent, magasin, région) et son propriétaire. L'annuaire « n'est pas un référentiel technique ». | [Annuaire §1](../00-cadrage/reponses-client/annuaire-magasins.md#1-objet) ; [cartographie §5.2](../00-cadrage/reponses-client/cartographie-si.md#52-magasin) | DAT 6.1 | **À faire** |
| Automatiser arrivée, mutation, départ et revue des habilitations. L'adhérent gère les comptes de ses salariés, dont il est l'employeur. | A.5.16 et A.5.18 ; revue non tenue depuis 2024 ([hébergement §6](../00-cadrage/reponses-client/hebergement-et-securite.md#6-regles-de-securite-appliquees)) | DAT 6.1 | **À faire** |
| Traiter chaque fichier de magasin comme hostile : XML sans entités externes (XXE), noms de fichiers contrôlés, taille bornée. Protéger les exports CSV contre l'injection de formules. | OWASP (XXE, CSV injection) | DAT 6.3, DCT 4.4 | **À faire** |
| Séparer ce qui lit des fichiers venus de l'extérieur de ce qui détient les clés de l'infrastructure. | A.8.2 et A.8.22 ; ANSSI, administration sécurisée des SI | DAT 6.3 | **À faire** : tout est sur `orchestration` |
| Lister et automatiser les règles de diagnostic : code, dépendances, secrets, IaC, images, TLS, test dynamique de `restitution` (Semgrep, Trivy, gitleaks, testssl.sh, OWASP ZAP). | Modalités C20.1 ; A.8.8 et A.8.29 | DAT 6.3, DCT 5.4 | **À faire** |
| Épingler versions et images, n'installer que des binaires signés, livrer un SBOM (CycloneDX ou SPDX) à chaque version. | A.5.21 | DAT 7.2 | **Partiel** : fait pour rclone seulement |
| Suivre les vulnérabilités de chaque composant (CERT-FR, avis GitHub) et écrire le délai de correctif par gravité. | A.8.8 | DAT 7.3, VEI | **À faire** |
| Synchroniser les horloges (NTP) de toutes les VM. Sans elles, les journaux ne se recoupent pas. | A.8.17 | DAT 7.3 | **À faire** |
| Séparer développement, recette et production. Aucune donnée réelle hors production sans les mêmes protections. | A.8.31 et A.8.33 | DAT 7.1 | **Partiel** : recette citée dans l'ingestion, non décrite |

## 5. Continuité, exploitation et niveaux de service

| Obligation | Source | Où | Vibro |
|---|---|---|---|
| Faire valider RPO et RTO par écrit. L'hébergeur actuel n'en garantit aucun. | [Hébergement §3](../00-cadrage/reponses-client/hebergement-et-securite.md#3-niveaux-de-service-du-contrat-dhebergement) | DAT 8.1 | **À demander** : RPO 24 h, RTO 4 à 8 h proposés |
| Lister tous les points de défaillance unique : `ch-1`, mais aussi `orchestration`, `restitution`, `depot`, PostgreSQL, DNS. | Modalités C20.2 | DAT 8.1 | **Partiel** : `ch-1` traité |
| Tester la restauration et la chronométrer. Le client n'en a fait aucune depuis 18 mois. | A.8.13 ; [hébergement §4](../00-cadrage/reponses-client/hebergement-et-securite.md#4-sauvegardes-et-restauration) | DAT 8, REC 5 | **Fait** : [sauvegarde](architecture-cible.md#sauvegarde) |
| Rendre les sauvegardes immuables et hors de portée des identifiants qui administrent la production. | A.8.13 ; ANSSI, rançongiciels | DAT 8.2 | **À faire** : `backups` répliqué, pas verrouillé |
| Mettre en lieu sûr, hors ligne, les clés sans lesquelles rien ne se reconstruit : clé age, clé de l'état OpenTofu, clé d'hôte SSH de `depot`. | A.8.24 (gestion des clés) | DAT 8.2 | **À faire** |
| Écrire et tester la reconstruction d'`orchestration`. Le runner qui lance OpenTofu tourne sur la VM à reconstruire. | A.5.30 | DAT 8.2 | **À faire** |
| Faire un exercice de reprise en région 2. | A.5.30 | DAT 8.2 | **À faire** : réplication décrite, reprise non décrite |
| Écrire la fenêtre de maintenance. La nuit est au batch, le matin aux directeurs, le premier mardi du mois au comité de direction. | [Volumétrie §4](../00-cadrage/reponses-client/volumetrie-et-contraintes.md#4-fenetres-dexploitation) | DAT 8.1 | **À faire** |
| Planifier en heure de Paris et tester la nuit du changement d'heure : en mars, la fenêtre perd une heure et 2 h 30 n'existe pas ; en octobre, 2 h 30 passe deux fois. Tester aussi la fenêtre réduite du dimanche. | [Volumétrie §4](../00-cadrage/reponses-client/volumetrie-et-contraintes.md#4-fenetres-dexploitation) | DAT 3.1 | **À faire** |
| Dire qui intervient entre 23 h et 6 h. Une intervention de nuit est une astreinte : accord, contrepartie, coût. Sinon, écrire que le mode dégradé est le bandeau « données de la veille », avec reprise à 8 h. | C. trav. L3121-9 et suivants | DAT 8.1, CDC 9 | **À faire** |
| Écrire une procédure par alerte, testée, à la portée des deux exploitants du client. | A.5.37 | DCT 7.4 | **À faire** |
| Poser une alerte de fraîcheur sur chaque source, référentiels nationaux compris. En 2025, la panne du flux F1 a duré 11 jours avant d'être vue. | [Hébergement §5](../00-cadrage/reponses-client/hebergement-et-securite.md#5-supervision) | DAT 7.3 | **Partiel** : magasins couverts, REFNAT, annuaire et tarifs non cités |

## 6. Réversibilité, propriété et licences

| Obligation | Source | Où | Vibro |
|---|---|---|---|
| Faire enregistrer au nom du client le domaine que connaissent les magasins (à définir). Lui remettre la clé d'hôte SSH de `depot`. | [Besoin §6.9](../10-besoins/expression-de-besoin-client.md#69-perennite-et-reversibilite) ; [découplage](ingestion.md#decouplage) | DAT 10 | **À faire** |
| Écrire le plan de réversibilité : ce qui est rendu (données en format ouvert, code, IaC, documentation, clés, registres), en combien de temps, à quel coût. | [Besoin §6.9](../10-besoins/expression-de-besoin-client.md#69-perennite-et-reversibilite) ; [hébergement §7](../00-cadrage/reponses-client/hebergement-et-securite.md#7-echeances-contractuelles) | DAT 10 | **Partiel** : composants open source et IaC, plan non écrit |
| Régler la propriété du code : cession des droits, ou licence large avec remise des sources (ou dépôt sous séquestre). | CPI L131-3 et L113-9 | Contrat | **CDP** : notre part, un code qui se construit et se déploie sans nous |
| Inventorier les licences. SFTPGo, Grafana et Loki sont en AGPL-3.0 : les modifier oblige à fournir le code modifié à ceux qui les utilisent par le réseau. Sans modification, l'usage en service ne crée pas cette obligation. NocoDB est sous Sustainable Use License depuis janvier 2026 : usage interne gratuit, revente ou hébergement pour des tiers interdits. Superset est sous Apache-2.0. | Licences des projets | DAT 5.1 | **À faire** |
| Relever la fin de support de chaque composant (endoflife.date) et la comparer à la durée de vie visée. | Modalités C2.2 | CDC 2.3, DAT 5.1 | **À faire** |
| Choisir un fournisseur qu'aucune loi extraterritoriale n'atteint. Le critère est le siège de sa maison mère. Le pays du centre de données ne suffit pas. | [Hébergement §2](../00-cadrage/reponses-client/hebergement-et-securite.md#2-localisation-des-donnees) ; Data Act art. 32 | DAT 5.2 | **Partiel** : « français, 2 régions », **Ouvert** |
| Prévoir la fin de vie dès maintenant : désinstallation en magasin, suppression des comptes, purge ou restitution des données. En 2023, le module a été désactivé sans être désinstallé. | [Clôture 2023 §7](../00-cadrage/compte-rendu-cloture-projet-2023.md#7-decision) ; RGPD art. 28.3.g ; Modalités C19.2 | DCT 6.2 | **Partiel** : retrait d'un magasin décrit, fin de contrat non décrite |

## 7. Accessibilité et cadres de référence

| Obligation | Source | Où | Vibro |
|---|---|---|---|
| Appliquer le RGAA 4.1.2 comme méthode et grille, en partant de l'usage réel : debout, avec des gants, en faible éclairage, sur écran ancien. L'adhérent doit aménager le poste d'un salarié handicapé, et un outil inaccessible l'en empêche. | [Organisation §9](../00-cadrage/reponses-client/organisation-gouvernance.md#9-accessibilite-et-diffusion-de-linformation) ; C. trav. L5213-6 | CDC 6.3, DAT 5.4 | **Partiel** : écrans tablette décrits |
| Tester Superset au clavier et au lecteur d'écran (NVDA). Donner à chaque graphique sa vue en tableau. | RGAA ; modalités DAT 5.4 | DAT 5.4 | **À faire** : à ajouter au POC |
| Ne porter aucune information par la couleur seule (alertes, écarts N-1). | RGAA critère 3.1 | DCT 4.3 | **À faire** |
| Sous-titrer les vidéos de démonstration et de formation. | RGAA thème 4 ; modalités DAT 5.4 | DAT 5.4 | **À faire** |
| Situer l'architecture dans les cadres communs, même si le client n'y est pas tenu : RGI (interopérabilité), RGAA et ISO 9241-11 (utilisabilité), RGESN (durabilité), RGS (sécurité). | Modalités DAT 5.3 | DAT 5.3 | **À faire** |
| Échanger en formats ouverts et versionnés : JSON Schema, UTF-8 en sortie, dates ISO 8601, GTIN pour les produits. | RGI | DAT 5.3 | **Partiel** : JSON Schema du manifeste |
| Lister navigateurs et postes cibles. 15 % des postes en magasin ont un système dont le support s'arrête en 2027. | [Volumétrie §5](../00-cadrage/reponses-client/volumetrie-et-contraintes.md#5-postes-de-consultation) | DAT 5.4 | **À faire** |

## 8. Sobriété et coûts

| Obligation | Source | Où | Vibro |
|---|---|---|---|
| Estimer l'énergie, le CO2e et le coût annuel de chaque option d'architecture, et les comparer. Partir des repères du client : 96 MWh par an, PUE 1,6, 0,14 € par kWh, 140 000 € par an d'hébergement. | [Volumétrie §6](../00-cadrage/reponses-client/volumetrie-et-contraintes.md#6-sobriete-et-cout-dexploitation) | DAT 9, CDC 8.1 | **À faire** |
| Chiffrer le coût de fonctionnement complet : infrastructure, connecteurs éditeurs, forfait des informaticiens locaux, temps des deux exploitants, astreinte. Le coût annuel inquiète le client plus que l'investissement. | [Besoin §4.8](../10-besoins/expression-de-besoin-client.md#48-moyens-financement-et-calendrier-de-decision) | CDC 9, DAT 9 | **À faire** |
| Mesurer la consommation réelle chaque mois (relevé du fournisseur) et la reporter dans le tableau de bord. | Modalités TBD 4.1 ; RGESN | TBD 4.1 | **À faire** |
| Prévoir des lignes pour l'accompagnement des magasins et la formation. Il n'y en avait aucune en 2023. | [Clôture 2023 §5](../00-cadrage/compte-rendu-cloture-projet-2023.md#5-depenses) | CDC 9 | **CDP** : notre part, le coût technique du déploiement |

## 9. Gouvernance et qualité des données

| Obligation | Source | Où | Vibro |
|---|---|---|---|
| Nommer un propriétaire pour chaque donnée et chaque définition (rupture, marge, rayon). La rupture n'a pas encore de définition. | [Réponse 2.1](../00-cadrage/reponses-client/index.md#21-definition-de-la-rupture) ; modalités C3.1 | CDC 7.1, DAT 3.3 | **À faire** |
| Isoler chaque définition en attente dans un modèle versionné, pour qu'une décision du comité ne casse rien. | [Réponse 2.1](../00-cadrage/reponses-client/index.md#21-definition-de-la-rupture) | DAT 4 | **Partiel** : une définition par métrique dans dbt |
| Réconcilier avec un chiffre auquel le client croit déjà (total de caisse, classeur CONSO) et publier l'écart expliqué. En 2023, des chiffres jugés faux par une région ont pesé dans l'arrêt. | [Besoin §8.3](../10-besoins/expression-de-besoin-client.md#83-une-tentative-precedente) ; [clôture 2023 §6](../00-cadrage/compte-rendu-cloture-projet-2023.md#6-constats) | DAT 3.3, REC 3 | **À faire** : contrôle par le manifeste seulement |
| Montrer la qualité à l'utilisateur : part du CA couverte par le tarif (82,6 % à Bel-Air), lignes non classées, écart du stock théorique. | [Réponses 2.2 et 2.3](../00-cadrage/reponses-client/index.md#22-prix-dachat-et-marge) | DAT 3.4 | **Partiel** : bandeau et « non classé » prévus |

## 10. Documentation et décisions

| Obligation | Source | Où | Vibro |
|---|---|---|---|
| Écrire une fiche par décision (ADR au format MADR) : contexte, options, choix, conséquences. | Modalités DAT 10 | DAT 10 | **À faire** : fiches annoncées dans les [décisions](architecture-cible.md#decisions), non créées |
| Donner un identifiant à chaque exigence du CDC, repris dans le DAT et le cahier de recette. | Modalités REC 1 | CDC 5.3, REC 1 | **À faire** |
| Donner à chaque exigence non fonctionnelle une cible chiffrée et sa mesure, classée selon les qualités de l'ISO/IEC 25010. | ISO/IEC 25010:2023 | CDC 5.3 | **Partiel** : cibles du [POC](architecture-cible.md#a-valider-au-poc) |
| Documenter pour que le client installe, exploite et fasse évoluer sans nous. | Modalités C21.1 | DCT 7 | **Partiel** : pas encore de documentation d'exploitation |

## 11. Textes à surveiller

| Texte | Ce qu'il change pour nous | Vibro |
|---|---|---|
| NIS2, directive (UE) 2022/2555 | La distribution alimentaire en gros figure à son annexe II. Si le mouvement y entre, la sécurité de ses fournisseurs (art. 21) nous concerne. | **À demander** |
| Cyberrésilience (CRA), règlement (UE) 2024/2847 | Il vise les produits vendus. Un service exploité pour un seul client en est a priori exclu. Pour un produit (connecteur, paquet installé en magasin) : signalement des vulnérabilités exploitées depuis le 11 septembre 2026, toutes les obligations au 11 décembre 2027. | **À faire** : analyser le paquet rclone, écrire la conclusion au DAT |
| IA, règlement (UE) 2024/1689 | Si une IA arrive (prévision, anomalies), classer le système. Évaluer ou surveiller des salariés le classe à haut risque (annexe III). | Année 2 |
| Données, Data Act, règlement (UE) 2023/2854 | Le fournisseur cloud doit permettre de partir : export des données, plus aucun frais de changement à partir du 12 janvier 2027. | **À faire** : critère de choix du fournisseur |
| Accessibilité, directive (UE) 2019/882 | Elle vise des produits et services destinés aux consommateurs. Vibro, outil interne, n'y entre pas. Le RGAA reste la méthode retenue par le client. | Hors champ |
