---
title: Export de l'annuaire des magasins
type: ressource-client
scope: [cdp, dev]
status: validated
updated: 2026-11-23
description: Structure et contenu de l'export de l'annuaire (762 magasins, régions, adhérents, équipements), réserves, et fiche des cinq magasins de l'échantillon.
---

# Export de l'annuaire des magasins

> **Émetteur :** Direction générale, mouvement E.Leclerc · **Objet :** extraction de l'annuaire du réseau, rattachements et équipements · **Date :** état au 15 septembre 2026 · **Diffusion :** interne

Pièce jointe aux [réponses du 7 novembre 2026](index.md). Fichier : `data/annuaire-magasins.csv`.

## 1. Objet

L'annuaire recense les magasins, leur région de rattachement, leur adhérent et leurs équipements. Il sert à l'animation du réseau et aux convocations d'assemblée, **et non de référentiel technique**.

L'export joint porte sur l'ensemble du réseau, 762 magasins.

## 2. Structure de l'export

Format : CSV, séparateur point-virgule, texte ASCII (noms sans accents), fins de ligne CRLF.

| Colonne | Contenu |
|---|---|
| `code_national` | Identifiant attribué par l'annuaire, stable |
| `nom` | Nom d'usage du magasin |
| `region` | Région d'animation de rattachement |
| `code_region` | Code utilisé par la région dans ses classeurs de consolidation |
| `format` | Hypermarché, supermarché, magasin urbain de proximité, petit format de centre-bourg |
| `zone_touristique` | `oui` pour les magasins dont l'activité suit une saison touristique, vide sinon |
| `code_adherent` | Identifiant de l'entreprise adhérente |
| `adherent` | Dirigeant de l'entreprise adhérente |
| `solution_caisse` | Solution d'encaissement installée |
| `version_caisse` | Version majeure déclarée lors du dernier recensement |
| `solution_stock` | Solution de gestion de stock et de back-office |
| `drive` | Solution de drive, ou `Sans drive` |
| `points_retrait` | Nombre de points de retrait exploités |

!!! warning "Donnée personnelle"
    La colonne `adherent` contient le nom du dirigeant. À traiter comme une donnée personnelle : ne pas l'exposer dans les restitutions ni la propager hors du besoin.

## 3. Ce que l'export contient

| Donnée | Valeur dans l'export |
|---|---|
| Magasins | 762 |
| Régions | 12, de 44 à 88 magasins |
| Hypermarchés | 188 |
| Supermarchés | 431 |
| Magasins urbains de proximité | 81 |
| Petits formats de centre-bourg | 62 |
| Magasins en zone touristique | 90 |
| Entreprises adhérentes | 610 |
| Adhérents exploitant plusieurs magasins | 140, dont 10 à trois magasins et 1 à quatre |
| Magasins équipés d'un drive | 680, pour 880 points de retrait |
| Magasins sans drive | 82 |

Répartition par région (calculée sur le fichier) :

| Région | Magasins |
|---|---:|
| Auvergne Rhône-Alpes | 88 |
| Sud-Ouest | 79 |
| Nord | 74 |
| Occitanie | 71 |
| Est | 68 |
| Provence | 66 |
| Ouest | 60 |
| Normandie | 58 |
| Bretagne | 55 |
| Centre | 52 |
| Île-de-France | 47 |
| Bourgogne Franche-Comté | 44 |

!!! note "Écart avec la note de volumétrie"
    La [note de volumétrie](volumetrie-et-contraintes.md#1-volumetrie-des-ventes) annonce 548 hypermarchés et 214 supermarchés. L'annuaire (vérifié sur le CSV) donne 188 / 431 / 81 / 62. Point à faire confirmer par écrit.

## 4. Réserves sur le contenu

- **Trois codifications de magasin coexistent** : le code national de l'annuaire, le code région des classeurs de consolidation, et le code client de l'éditeur de caisse. Aucune table de correspondance complète n'existe entre les trois. L'export porte les deux premières ; le code client de l'éditeur n'a jamais été recensé.
- La colonne `code_region` est tenue à jour manuellement par l'animation du réseau. **38 magasins n'en ont pas**, et 9 portent un code dont la région ne reconnaît pas la séquence. Ces écarts sont connus et n'ont pas été corrigés.
- La colonne `adherent` suit les changements de dirigeant avec retard : une cession de magasin met plusieurs semaines à y apparaître.
- Les colonnes `solution_caisse`, `version_caisse` et `solution_stock` proviennent d'un **recensement déclaratif**, sans accès aux systèmes. Un relevé exact supposerait de le demander à 762 entreprises.

## 5. Les cinq magasins de l'échantillon

Les trois solutions de caisse du réseau y sont représentées.

| Magasin | Code national | Région | Format | Caisse | Version | Stock | Drive |
|---|---|---|---|---|---|---|---|
| Bel-Air | 1144 | Ouest | Hypermarché | ALPHACAISSE | 7.1 | BETASTOCK | DRIVEPLUS, deux points de retrait |
| Les Portes | 1139 | Ouest | Supermarché | BETAPOS | 4.2 | BETASTOCK | Intégré à la caisse, un point de retrait |
| Centre-Ville | 1154 | Ouest | Magasin urbain de proximité | GAMMASOFT | 3.3 | Tenue manuelle ou tierce | Sans drive |
| Grand Large | 1217 | Bretagne | Hypermarché, zone touristique | ALPHACAISSE | 5.4 | ALPHASTOCK | DRIVEPLUS, deux points de retrait |
| Le Marché | 1136 | Ouest | Petit format de centre-bourg | Éditeur local | Non déclarée | Tenue manuelle ou tierce | Sans drive |

La version 5.4 installée à Grand Large n'est plus maintenue par son éditeur, d'où le format de sortie particulier de ce magasin.

!!! note
    Cet export est transmis en l'état. Il constitue la source la plus complète dont le mouvement dispose sur le rattachement et les équipements de son réseau.
