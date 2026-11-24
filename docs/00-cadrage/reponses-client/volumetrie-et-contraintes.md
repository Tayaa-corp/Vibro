---
title: Volumétrie, contraintes techniques et fenêtres d'exploitation
type: ressource-client
scope: [cdp, dev]
status: validated
updated: 2026-11-23
description: Ordres de grandeur des ventes et des données, réseau des magasins, fenêtres d'exploitation, postes de consultation, coût et énergie de l'hébergement actuel.
---

# Volumétrie, contraintes techniques et fenêtres d'exploitation

> **Émetteur :** Équipe informatique nationale, mouvement E.Leclerc · **Objet :** ordres de grandeur et contraintes d'exploitation · **Périmètre :** national et magasins · **Version :** 1.0, état au 15 septembre 2026

Pièce jointe aux [réponses du 7 novembre 2026](index.md).

## 1. Volumétrie des ventes

| Grandeur | Valeur | Source |
|---|---|---|
| Magasins du réseau | 762, dont 548 hypermarchés et 214 supermarchés | Annuaire national |
| Tickets par jour, moyenne annuelle | environ 3,4 millions | Estimation à partir des déclarations de chiffre d'affaires |
| Lignes par ticket, moyenne | 11,2 en hypermarché, 6,8 en supermarché | Échantillon de quarante magasins |
| Lignes de vente par jour, moyenne | environ 34 millions | Calcul |
| Lignes de vente par an | environ 12,4 milliards | Calcul |
| Journée la plus chargée observée | 24 décembre, 2,6 fois la moyenne | Déclarations régionales |
| Semaine la plus chargée | semaine 51, 1,9 fois la moyenne | Déclarations régionales |
| Creux annuel | première quinzaine de février, 0,7 fois la moyenne | Déclarations régionales |

!!! warning "Incohérence à signaler"
    Cette note compte **548 hypermarchés et 214 supermarchés**, alors que l'[export de l'annuaire](annuaire-magasins.md#3-ce-que-lexport-contient) donne **188 hypermarchés, 431 supermarchés, 81 magasins urbains de proximité et 62 petits formats** (762 au total). À clarifier par écrit avec le client avant tout dimensionnement par format.

## 2. Taille des données

| Objet | Ordre de grandeur | Remarque |
|---|---|---|
| Ligne de vente brute | environ 180 octets en CSV | Champs variables selon l'éditeur |
| Volume brut quotidien | environ 6 gigaoctets | Avant transformation |
| Volume brut annuel | environ 2,2 téraoctets | Avant transformation |
| Historique attendu | 5 ans glissants au minimum | Exigence de comparaison saisonnière |
| Fiches produits actives | environ 92 000 au national, jusqu'à 25 000 supplémentaires en local par magasin | REFNAT et déclarations |
| Porteurs de carte actifs | environ 4,1 millions | FIDELIS |

## 3. Réseau et accès

| Contrainte | Situation |
|---|---|
| Liaison des magasins | Accès internet du commerce, fibre pour environ 80 %, cuivre pour le reste |
| Débit montant typique | 20 à 200 Mbit/s en fibre, 1 à 8 en cuivre |
| Disponibilité de la liaison | Aucune garantie, aucun contrat de service souscrit par le mouvement |
| Coupures observées | Plusieurs heures par an et par magasin, davantage en zone rurale |
| Accès distant aux systèmes du magasin | Soumis à l'accord de l'adhérent, refusé par une partie d'entre eux |
| Ouverture de flux sortants | Possible, à négocier magasin par magasin avec l'informaticien local |

## 4. Fenêtres d'exploitation

| Fenêtre | Plage | Contrainte |
|---|---|---|
| Fermeture des magasins | 21 h à 8 h 30 en semaine | Les caisses sont clôturées entre 21 h et 22 h |
| Fenêtre de traitement nocturne disponible | **23 h à 6 h** | Après clôture et sauvegarde locale |
| Dimanche | Ouverture le matin pour une partie du réseau | Fenêtre réduite le dimanche soir |
| Disponibilité attendue des restitutions | **7 h 30, avant l'ouverture** | Exigence des directions de magasin |
| Comités de direction | Premier mardi du mois, 9 h | Les chiffres doivent être arrêtés la veille au soir |

## 5. Postes de consultation

| Public | Équipement | Contrainte |
|---|---|---|
| Direction de magasin | Poste bureautique, parfois tablette | Navigateur récent, connexion depuis le magasin |
| Chef de rayon | Poste partagé en réserve, parfois aucun | Consultation debout, sessions courtes |
| Direction régionale | Poste bureautique | Consultation depuis le bureau et en déplacement |
| National | Poste bureautique | Vidéoprojection en comité |

Environ 15 % des postes des magasins tournent encore sur une version de système d'exploitation dont le support étendu s'achève en 2027.

## 6. Sobriété et coût d'exploitation

Le mouvement attend une **estimation de l'empreinte de la solution, en énergie et en coût**, et une **comparaison entre les options d'architecture** retenues.

| Repère | Valeur |
|---|---|
| Coût de l'hébergement actuel des applications nationales | environ 140 000 € par an |
| Consommation du centre de données du prestataire B, part imputée au mouvement | environ 96 MWh par an |
| Indicateur d'efficacité énergétique (PUE) annoncé par le prestataire B | 1,6 |
| Prix moyen de l'électricité retenu pour les calculs | 0,14 € par kWh |

!!! note
    Ces ordres de grandeur proviennent de déclarations et de calculs internes. Ils ne constituent pas une mesure certifiée.
