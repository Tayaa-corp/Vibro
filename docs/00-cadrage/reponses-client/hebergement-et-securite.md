---
title: Hébergement, niveaux de service et règles de sécurité
type: ressource-client
scope: [cdp, dev]
status: validated
updated: 2026-11-23
description: Localisation des données, SLA du contrat d'hébergement, sauvegardes, supervision, règles de sécurité appliquées de fait, échéances contractuelles.
---

# Hébergement, niveaux de service et règles de sécurité

> **Émetteur :** Responsable de l'équipe informatique nationale, mouvement E.Leclerc · **Objet :** relevé des éléments contractuels et des règles appliquées · **Date :** octobre 2026 · **Diffusion :** interne

Pièce jointe aux [réponses du 7 novembre 2026](index.md).

## 1. Objet de cette note

Cette note a été établie à la demande de la direction générale, en réponse à une question sur les règles imposées par l'hébergeur et sur la politique de sécurité du mouvement. Elle reprend les éléments des contrats en cours et des pratiques appliquées ; les contrats eux-mêmes restent en interne.

L'équipe informatique nationale compte douze personnes, dont deux sur l'exploitation et la relation avec les prestataires et une sur la sécurité et la conformité, à temps partiel. Elle est rattachée à la direction générale et n'a pas d'autorité fonctionnelle sur les systèmes des magasins.

## 2. Localisation des données

| Application | Hébergement | Localisation |
|---|---|---|
| Référentiel produit, campagnes, portail des adhérents, annuaire | Centre de données d'un prestataire, machines virtuelles dédiées | France |
| Programme de fidélité | Cloud de l'éditeur, logiciel en service | Union européenne |
| Site public et application mobile | Cloud public | Union européenne |

Les données restent dans l'Union européenne. Tout transfert hors de l'UE est soumis à la direction juridique, qui n'en a jamais autorisé.

## 3. Niveaux de service du contrat d'hébergement

| Engagement | Valeur contractuelle |
|---|---|
| Disponibilité des machines virtuelles | 99,5 %, mesurée en heures ouvrées, du lundi au vendredi de 8 h à 19 h |
| Disponibilité hors heures ouvrées | **Aucun engagement** |
| Délai de prise en compte d'un incident bloquant | Quatre heures en heures ouvrées |
| Délai de rétablissement (RTO) | **Aucun engagement chiffré** |
| Perte de données maximale admise (RPO) | **Aucun engagement chiffré** |
| Disponibilité des flux applicatifs | Hors du périmètre du contrat |
| Pénalités | Plafonnées à un mois de redevance par année contractuelle |
| Réversibilité | Export des données à la charge du mouvement |

!!! warning "Conséquences"
    Le contrat porte sur l'**infrastructure**, pas sur les traitements ni sur les flux. Et sans délai de rétablissement ni perte de données maximale contractualisés, **un incident majeur n'a pas de borne de durée opposable au prestataire**. À noter : la fenêtre de traitement nocturne (23 h – 6 h) tombe entièrement hors des heures couvertes.

## 4. Sauvegardes et restauration

Les sauvegardes sont quotidiennes, avec une rétention de trente jours. Elles couvrent les machines virtuelles, **pas les exports de fichiers** déposés sur les serveurs de fichiers.

Aucun test de restauration n'a été conduit depuis dix-huit mois. Une demande de restauration se fait par ticket auprès du prestataire, sans délai contractuel associé.

Les environnements de recette existent pour le référentiel produit et pour les campagnes. Le portail des adhérents et l'annuaire n'en ont pas.

## 5. Supervision

La supervision se limite à la disponibilité des machines. Aucune supervision applicative ni de flux n'est en place.

Une rupture de la diffusion hebdomadaire du référentiel produit vers les caisses, survenue en 2025, a été détectée par un adhérent **onze jours** après son interruption.

## 6. Règles de sécurité appliquées

Le mouvement **n'a pas de politique de sécurité écrite**. Les règles ci-dessous sont celles que l'équipe informatique applique et fait appliquer à ses prestataires, sans figurer dans un document approuvé.

| Règle | État |
|---|---|
| Chiffrement des échanges entre applications nationales et prestataires | Appliquée |
| Chiffrement des données au repos | Appliquée sur les bases hébergées, pas sur les dépôts de fichiers |
| Accès nominatif aux environnements de production | Appliquée pour l'équipe informatique, partielle pour les prestataires |
| Traçabilité des interventions du prestataire d'exploitation | Appliquée, journal tenu par le prestataire |
| Revue annuelle des habilitations | Prévue, non tenue depuis 2024 |
| Authentification à plusieurs facteurs sur les accès d'administration | Appliquée sur le centre de données, absente du portail des adhérents |
| Cloisonnement des données entre adhérents | Exigence contractuelle, détaillée dans la [note de la direction juridique](donnees-personnelles-et-cloisonnement.md#4-regles-de-cloisonnement) |
| Analyse de risque avant mise en service | Pas de procédure établie |

## 7. Échéances contractuelles

| Objet | Échéance | Conditions de sortie |
|---|---|---|
| Maintenance des applications nationales | 31 décembre 2028 | Préavis de six mois, reprise du code documentée prévue au contrat |
| Hébergement du centre de données | **30 juin 2027**, reconduction tacite annuelle | Préavis de trois mois, export des données à la charge du mouvement |
| Développements spécifiques à la commande | Bons de commande à l'unité | Sans objet, aucune clause de reprise |
| Programme de fidélité | 31 mars 2029 | Préavis de douze mois, export au format propriétaire, reprise facturée |

L'échéance d'hébergement du 30 juin 2027 est la plus proche (préavis à donner avant le **31 mars 2027**), et le mouvement n'a pas arrêté sa position sur sa reconduction.

## 8. Ce que cette note ne couvre pas

- Les contrats eux-mêmes.
- Le réseau et l'infrastructure des magasins, sous la responsabilité de chaque adhérent, ainsi que les contrats liant un adhérent à son éditeur de caisse et à son informaticien local.
- Le coût de l'hébergement, qui figure au référentiel de coûts internes de la direction financière (ordre de grandeur donné dans la réponse : environ 140 000 € par an).

!!! note
    Cette note est un relevé. Les valeurs contractuelles qui y figurent sont celles des contrats en cours au mois d'octobre 2026.
