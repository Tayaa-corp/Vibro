---
title: Cartographie du système d'information
type: ressource-client
scope: [cdp, dev]
status: validated
updated: 2026-11-23
description: Applications nationales et en magasin, échéances contractuelles, flux existants, référentiels et identifiants, exploitation.
---

# Cartographie du système d'information

> **Émetteur :** Équipe informatique nationale, mouvement E.Leclerc · **Objet :** recensement applicatif et flux · **Périmètre :** national et magasins · **Version :** 1.0, état au 15 septembre 2026

Pièce jointe aux [réponses du 7 novembre 2026](index.md).

## 1. Portée et limites du recensement

Ce document recense les applications du national et, pour les magasins, ce que l'équipe informatique nationale connaît des systèmes en place. Les magasins étant des entreprises indépendantes, le national n'a pas accès à leurs systèmes et ne dispose d'aucun inventaire exhaustif.

Le recensement magasin repose sur trois sources : les déclarations des éditeurs de caisse, un questionnaire adressé aux adhérents en 2025 (596 réponses sur 762 magasins) et la connaissance des directions régionales. **Les chiffres donnés sont des ordres de grandeur.**

Les applications de gestion propres à chaque adhérent (paie, comptabilité, ressources humaines) ne sont pas recensées : elles sortent du périmètre du mouvement.

## 2. Applications nationales

| Application | Fonction | Éditeur | Technologie | Hébergement | Propriétaire métier | Criticité |
|---|---|---|---|---|---|---|
| REFNAT | Référentiel des produits référencés au national : fiches, EAN, familles, fournisseurs | Développement spécifique | .NET 6, SQL Server 2019 | Centre de données France, prestataire B | Direction des achats | Forte |
| PROMONAT | Construction et diffusion des campagnes nationales, mécaniques et périodes | Développement spécifique | .NET Framework 4.8, SQL Server 2016 | Centre de données France, prestataire B | Direction marketing | Moyenne |
| FIDELIS | Programme de fidélité : cartes, cagnottes, historique d'achat porteur | Éditeur externe, logiciel en service | Non communiquée | Cloud éditeur, Union européenne | Direction marketing | Forte |
| PORTAIL | Extranet des adhérents : documents, catalogues, notes de service | Développement spécifique | PHP 7.4, MySQL | Centre de données France, prestataire B | Direction générale | Moyenne |
| SITE | Site public de l'enseigne et espace client | Agence externe | Contenu géré par l'agence | Cloud public, Union européenne | Direction marketing | Moyenne |
| MOBILE | Application mobile : catalogue, carte de fidélité, drive | Agence externe | iOS et Android natifs | Cloud public, Union européenne | Direction marketing | Moyenne |
| ANNUAIRE | Annuaire des magasins, des régions et des contacts | Développement spécifique | PHP 7.4, MySQL | Centre de données France, prestataire B | Direction générale | Faible |
| CONSO | Classeurs de consolidation régionale, reconstitués à la main chaque semaine | Sans objet | Tableur | Postes de travail des régions | Directions régionales | Forte dans les faits |

!!! note "CONSO"
    CONSO n'est pas une application. Ce sont des classeurs tenus par les assistantes de direction régionales, avec des macros écrites localement et des formules qui diffèrent d'une région à l'autre. C'est pourtant **la source de la plupart des chiffres présentés en comité**. Voir [consolidation régionale](consolidation-regionale.md).

### 2.1 Échéances contractuelles

| Objet | Prestataire | Échéance | Conditions de sortie |
|---|---|---|---|
| Maintenance des applications nationales | Prestataire A | 31 décembre 2028 | Préavis de six mois, reprise du code documentée prévue au contrat |
| Hébergement du centre de données | Prestataire B | 30 juin 2027, reconduction tacite annuelle | Préavis de trois mois, export des données à la charge du mouvement |
| Développements spécifiques à la commande | Prestataire C | Bons de commande à l'unité | Sans objet |
| Fidélité | Éditeur FIDELIS | 31 mars 2029 | Préavis de douze mois, export au format propriétaire, reprise facturée |

## 3. Applications en magasin

### 3.1 Encaissement

| Solution | Éditeur | Magasins équipés | Sortie de données | Format | Fréquence possible |
|---|---|---|---|---|---|
| ALPHACAISSE | Alpharetail | environ 310 | Export de fichiers sur partage réseau du magasin | CSV, séparateur point-virgule, encodage variable | Nocturne, paramétrable |
| BETAPOS | Betapos Systems | environ 260 | Base de données accessible en lecture sur le réseau local | SQL Server, schéma documenté partiellement | Continue si autorisée par l'adhérent |
| GAMMASOFT | Gammasoft Retail | environ 180 | Export de fichiers, plus une interface applicative sur les ventes du jour | XML pour l'export, JSON pour l'interface | Nocturne pour l'export, à la demande pour l'interface |
| Autres | Éditeurs locaux et solutions anciennes | environ 12 | Variable, parfois aucune sortie automatisée | Variable | Variable |

Les versions installées diffèrent d'un magasin à l'autre. Sur ALPHACAISSE, quatre versions majeures cohabitent, dont une qui n'est plus maintenue par l'éditeur. Sur BETAPOS, la mise à jour est à l'initiative de l'adhérent et deux magasins sur dix ont plus de deux ans de retard.

### 3.2 Gestion de stock et back-office

| Solution | Éditeur | Magasins équipés | Ce qu'elle contient |
|---|---|---|---|
| ALPHASTOCK | Alpharetail | environ 290 | Stock théorique, commandes fournisseurs, inventaires |
| BETASTOCK | Betapos Systems | environ 240 | Stock théorique, réceptions, démarque |
| Solutions tierces ou tenue manuelle | Variable | environ 232 | Selon le magasin, parfois un tableur |

Le stock théorique diverge du stock réel dans des proportions que les adhérents estiment entre **2 et 8 %** selon les familles de produits. La démarque et les erreurs de réception en sont les causes principales.

### 3.3 Drive

| Solution | Magasins équipés | Particularité |
|---|---|---|
| DRIVEPLUS | environ 430 | Solution nationale recommandée, connectée à MOBILE |
| Solutions éditeur de caisse | environ 250 | Intégrée à ALPHACAISSE ou BETAPOS |
| Sans drive | environ 82 | Sans objet |

Les 680 magasins équipés exploitent environ 880 points de retrait, une partie des hypermarchés en tenant deux (un accolé au magasin, un déporté).

### 3.4 Périphériques

Balances de pesée et étiquetage, terminaux de paiement, terminaux portables d'inventaire. Ces équipements ne produisent pas de données exploitables au national.

## 4. Flux existants

| Flux | Source | Destination | Contenu | Fréquence | Format et transport | Volumétrie |
|---|---|---|---|---|---|---|
| F1 | REFNAT | Caisses des magasins | Fiches produits référencées, prix conseillés | Hebdomadaire | CSV déposé sur serveur de fichiers, récupéré par l'éditeur | environ 92 000 lignes |
| F2 | PROMONAT | Caisses des magasins | Mécaniques promotionnelles nationales | Hebdomadaire | CSV, même canal que F1 | environ 2 000 lignes |
| F3 | Magasins volontaires | Directions régionales | Chiffre d'affaires et volumes, par rayon | Hebdomadaire, quand le magasin le fait | Courriel, pièce jointe tableur | environ 400 magasins sur 762 |
| F4 | Directions régionales | Direction générale | Consolidation régionale | Hebdomadaire | Courriel, classeur CONSO | 12 régions |
| F5 | FIDELIS | MOBILE et SITE | Solde de cagnotte et offres porteur | Continue | Interface applicative de l'éditeur | environ 4,1 millions de porteurs actifs |
| F6 | Caisses | FIDELIS | Tickets porteurs de carte | Nocturne | Interface applicative de l'éditeur, connecteur fourni par l'éditeur de caisse | environ 40 % des tickets |
| F7 | Magasins | REFNAT | Demandes de référencement local | À la demande | Formulaire du PORTAIL | quelques centaines par an |

!!! warning
    **Aucun flux ne remonte aujourd'hui le détail des ventes au national.** Le flux F3 transporte des totaux saisis à la main, et un magasin sur deux ne l'alimente pas.

## 5. Référentiels et identifiants

### 5.1 Produit

Le code à barres (EAN à treize chiffres) est présent dans tous les systèmes de caisse. Il ne suffit pourtant pas à identifier un produit de façon fiable :

- les produits vendus au poids portent un code interne au magasin, différent d'un magasin à l'autre ;
- les libellés sont saisis localement, un même produit peut porter huit libellés différents dans le réseau ;
- les produits locaux, référencés par l'adhérent seul, n'existent pas dans REFNAT ;
- le rattachement à une famille est celui de l'éditeur de caisse, et les nomenclatures des trois éditeurs ne coïncident pas ;
- les unités de vente ne sont pas codifiées de la même façon : la pièce, le kilogramme et le lot cohabitent sans convention commune.

### 5.2 Magasin

Trois codifications coexistent : le code national attribué par ANNUAIRE, le code région utilisé dans les classeurs CONSO, et le code client de l'éditeur de caisse. Aucune table de correspondance complète n'existe ; celle qui circule est tenue à jour manuellement et comporte des écarts connus.

### 5.3 Client

Le porteur de carte est identifié dans FIDELIS. Le ticket sans carte n'est rattaché à personne. Aucun identifiant client ne circule entre magasins.

## 6. Environnements et exploitation

Le centre de données du prestataire B héberge REFNAT, PROMONAT, PORTAIL et ANNUAIRE, sur des machines virtuelles dédiées. Des environnements de recette existent pour REFNAT et PROMONAT, pas pour les deux autres.

Les sauvegardes sont quotidiennes, avec une rétention de trente jours. Aucun test de restauration n'a été conduit depuis dix-huit mois.

La supervision se limite à la disponibilité des machines. Aucune supervision applicative ni de flux n'est en place. Une rupture du flux F1 a été détectée en 2025 par un adhérent, **onze jours après son interruption**.

L'équipe informatique nationale compte douze personnes :

| Activité | Effectif |
|---|---|
| Exploitation et relation avec les prestataires | 2 |
| Référencement et campagnes | 4 |
| Support aux magasins et aux régions | 3 |
| Projets | 2 |
| Sécurité et conformité (temps partiel) | 1 |

## 7. Ce que ce recensement ne couvre pas

Le réseau et l'infrastructure des magasins, sous la responsabilité de chaque adhérent. Les postes de travail des magasins et des régions. Les contrats liant chaque adhérent à son éditeur et à son informaticien local. Les applications de gestion propres à chaque entreprise adhérente.

!!! note
    Ce recensement comporte les approximations d'un relevé mené sans accès aux systèmes des magasins. Il est diffusé en l'état, le mouvement ne disposant pas d'une source plus précise.
