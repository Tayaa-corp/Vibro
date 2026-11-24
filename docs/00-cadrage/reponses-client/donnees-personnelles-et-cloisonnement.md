---
title: Protection des données et règles de cloisonnement
type: ressource-client
scope: [cdp, dev]
status: validated
updated: 2026-11-23
description: Responsabilités RGPD, qualification et durées de conservation des données, engagements aux porteurs, règles de cloisonnement par acteur, seuil des cinq magasins.
---

# Protection des données et règles de cloisonnement

> **Émetteur :** Direction juridique et conformité, mouvement E.Leclerc · **Objet :** cadre applicable aux données du projet · **Périmètre :** national, régions et magasins · **Version :** 1.0, état au 15 septembre 2026

Pièce jointe aux [réponses du 7 novembre 2026](index.md).

## 1. Qui est responsable de quoi

| Traitement | Responsable de traitement | Sous-traitant |
|---|---|---|
| Encaissement et ticket de caisse | L'adhérent, pour son magasin | Son éditeur de caisse |
| Programme de fidélité | Le national | L'éditeur FIDELIS |
| Consolidation des ventes au national | Le national, pour les données qui lui sont confiées | Le futur prestataire de la plateforme |

!!! warning "Prérequis juridique"
    La qualification du national en responsable de traitement pour la consolidation suppose que **chaque adhérent lui confie ses données par un acte écrit**. Cet acte n'existe pas aujourd'hui. Sa mise en place fait partie du chantier.

## 2. Données concernées et qualification

| Donnée | Caractère personnel | Base légale retenue | Durée de conservation |
|---|---|---|---|
| Ligne de vente sans porteur | Non, après suppression de l'identifiant de transaction | Intérêt légitime | 5 ans |
| Ticket avec carte de fidélité | Oui | Consentement du porteur, recueilli à l'adhésion | 3 ans après le dernier achat |
| Identité et coordonnées du porteur | Oui | Consentement | 3 ans après le dernier achat |
| Données de l'employé encaisseur | Oui | Obligation légale et intérêt légitime | 13 mois |
| Stock et commandes | Non | Sans objet | 5 ans |

## 3. Engagements pris aux porteurs de carte

L'adhésion au programme de fidélité comporte trois engagements, rappelés dans les conditions générales acceptées par le porteur :

- les données d'achat servent à personnaliser les offres et à calculer la cagnotte ;
- elles ne sont ni cédées ni louées à un tiers ;
- le porteur obtient sur demande l'effacement de son historique et la portabilité de ses données.

Toute utilisation nouvelle des données porteur, analyse de comportement d'achat comprise, suppose une information du porteur et, selon la finalité, un consentement distinct.

## 4. Règles de cloisonnement

Le cloisonnement entre adhérents est une **exigence contractuelle** du mouvement, indépendante de la réglementation sur les données personnelles.

| Acteur | Ce qu'il voit | Ce qu'il ne voit pas |
|---|---|---|
| Adhérent | Le détail de son magasin, à la ligne de vente | Le détail de tout autre magasin, sous quelque forme que ce soit |
| Adhérent | Des agrégats régionaux et nationaux, à condition qu'aucun magasin ne soit identifiable | Un agrégat portant sur moins de cinq magasins |
| Direction régionale | Le détail des magasins de sa région | Les magasins des autres régions, au détail |
| National | Des agrégats à toute maille | Le détail nominatif d'un porteur |
| Prestataire d'exploitation | Rien, hors intervention tracée et motivée | Les données en clair sans habilitation nominative |

La **règle des cinq magasins** a été présentée à l'assemblée de 2024. Un agrégat régional portant sur moins de cinq magasins est refusé, parce qu'il permet de déduire les chiffres d'un confrère.

!!! note "Précision apportée dans la réponse du 7 novembre"
    La **marge estimée** d'un magasin reste réservée à son adhérent, y compris vis-à-vis de la direction régionale et y compris calculée au tarif de la centrale ([réponse 4.3](index.md#43-acces-regional-et-national)).

## 5. Ce qui a déjà posé problème

En 2023, un tableau de bord régional affichait un classement des magasins par chiffre d'affaires, avec les noms. Trois adhérents ont cessé d'envoyer leurs fichiers dans les deux semaines. Le chantier s'est arrêté trois mois plus tard.

!!! danger "Règle posée depuis par la direction juridique"
    **Aucun affichage comparatif nominatif entre adhérents**, quelle que soit la maille et quel que soit le destinataire.

## 6. Points sur lesquels la direction juridique doit être saisie

- Toute finalité nouvelle appliquée aux données porteur.
- Tout transfert de données hors de l'Union européenne.
- Tout recours à un sous-traitant qui accède aux données en clair.
- Toute conservation au-delà des durées du tableau de la section 2.
- Toute fonction de profilage, y compris une segmentation automatique.

!!! note
    La direction juridique est saisie par courriel. Elle ne valide pas une conception, elle indique ce qui est permis et ce qui ne l'est pas.
