---
title: Cas d'utilisation
type: besoin
scope: [cdp, dev]
status: draft
updated: 2026-11-25
description: Diagramme UML des cas d'utilisation de l'année 1, acteurs, règles par cas, usages hors périmètre et questions ouvertes. Section 4.4 du CDC.
---

# Cas d'utilisation

Ce document alimente la section 4.4 du cahier des charges (CDC). Il décrit ce que chaque acteur fait avec la plateforme en année 1. La technique est dans l'[architecture cible](../30-architecture/architecture-cible.md).

!!! abstract "En bref"
    - 11 acteurs et 21 cas d'utilisation, en trois paquetages : usages métier, alimentation de nuit, exploitation et gouvernance.
    - Chaque acteur voit son périmètre seulement. La marge d'un magasin reste à son adhérent.
    - Le magasin ne fait rien : son émetteur dépose, la plateforme contrôle et publie.
    - Prévision du frais, drive en temps réel, promotions et données porteur sortent de l'année 1.

![Cas d’utilisation](cas-utilisation.drawio)

La source est le fichier `cas-utilisation.drawio` de ce dossier. Modifiez-le dans draw.io : le rendu de cette page suit.

## Acteurs

| Acteur | Qui | Périmètre | Outil |
|---|---|---|---|
| Adhérent | Directeur de magasin, chef d'entreprise | Son magasin au détail, sa marge | Superset |
| Adhérent multi-magasins | 140 adhérents, de 2 à 4 magasins | Ses magasins, ensemble et un par un | Superset |
| Chef de rayon | Salarié de l'adhérent | Ce que l'adhérent lui ouvre | Superset |
| Direction régionale | 12 régions, de 44 à 88 magasins | Ses magasins au détail, sans la marge | Superset |
| Direction nationale | Direction générale et directions du national | Agrégats du réseau | Superset |
| Direction des achats | Spécialise la direction nationale | Agrégats par fournisseur et par région | Superset |
| Émetteur du magasin | Connecteur de l'éditeur de caisse, ou rclone | Livraisons de son magasin | SFTP vers `depot.<domaine>` |
| SI national | REFNAT, annuaire, tarifs de la centrale | Référentiels | SFTPGo (SFTP ou interface web) |
| Horloge | Déclenchement de chaque nuit | Publication du jour | Dagster |
| Exploitant | Équipe d'exploitation | Flotte, alertes, rejeux, inscriptions | Grafana, Dagster, interface d'administration SFTPGo |
| Responsable de la donnée | Rôle que le national crée | Correspondances produits, définitions | NocoDB (correspondances), pull request dbt (définitions) |

Sources : [cloisonnement](../00-cadrage/reponses-client/donnees-personnelles-et-cloisonnement.md#4-regles-de-cloisonnement), [accès régional et national](../00-cadrage/reponses-client/index.md#43-acces-regional-et-national), [adhérents multi-magasins](../00-cadrage/reponses-client/remontees-terrain.md#5-reponses-des-adherents-multi-magasins), [liens hiérarchiques](../00-cadrage/reponses-client/organisation-gouvernance.md#5-liens-hierarchiques-et-liens-fonctionnels), [ingestion](../30-architecture/ingestion.md).

## Usages métier

| Cas d'utilisation | Acteurs | Règle |
|---|---|---|
| Suivre ventes et stock de son magasin, N-1 compris | Adhérent, chef de rayon | Stock théorique du back-office. 232 magasins n'ont pas de logiciel de stock |
| Repérer ruptures et produits en perte de vitesse | Adhérent, chef de rayon | Définition de la rupture paramétrable : le comité ne l'a pas encore arrêtée |
| Consulter la marge estimée de son magasin | Adhérent | Réservée à l'adhérent. Part du CA couverte par le tarif affichée |
| Se situer face à des magasins comparables | Adhérent | 5 magasins d'autres adhérents au minimum. Aucun classement nominatif |
| Gérer les accès de ses salariés | Adhérent | L'adhérent est l'employeur : il ouvre et ferme les comptes de son magasin |
| Consolider et comparer ses magasins, drive à part | Adhérent multi-magasins | Rien d'un confrère |
| Suivre les magasins de sa région, hors marge | Direction régionale | Rien des autres régions |
| Consulter les chiffres arrêtés pour le comité | Direction nationale, direction régionale | Chiffres figés la veille au soir, nombre de magasins contributeurs affiché |
| Consulter les agrégats du réseau | Direction nationale | Aucun détail de porteur de carte |
| Analyser volumes et ruptures par fournisseur et région | Direction des achats | Agrégats seulement |

Toute consultation passe par Keycloak (SSO, MFA). Le compte fixe le périmètre visible.

Sources : [rupture](../00-cadrage/reponses-client/index.md#21-definition-de-la-rupture), [marge](../00-cadrage/reponses-client/index.md#22-prix-dachat-et-marge), [stock](../00-cadrage/reponses-client/cartographie-si.md#32-gestion-de-stock-et-back-office), [moyennes de pairs](../00-cadrage/reponses-client/index.md#42-moyennes-de-pairs), [comités](../00-cadrage/reponses-client/volumetrie-et-contraintes.md#4-fenetres-dexploitation), [classeur régional](../00-cadrage/reponses-client/consolidation-regionale.md#32-extrait-du-classeur-de-la-region-ouest), [achats](../00-cadrage/reponses-client/remontees-terrain.md#41-responsable-des-achats).

## Alimentation de nuit

| Cas d'utilisation | Acteurs | Règle |
|---|---|---|
| Déposer une livraison | Émetteur du magasin | 0 minute demandée au directeur. Opérateur retiré, ticket remplacé par une empreinte |
| Contrôler la livraison : manifeste, empreinte, totaux | Inclus dans le dépôt | Quarantaine si un contrôle échoue. Les autres magasins continuent |
| Fournir les référentiels | SI national | Alerte si un flux n'arrive pas |
| Publier les indicateurs du jour avant 6 h | Horloge | Inclut la vérification de l'étanchéité et du seuil de 5 magasins |
| Garder la veille en ligne avec un bandeau | Étend la publication | Si un test échoue |

Sources : [règles de chargement](../30-architecture/ingestion.md#regles-de-chargement), [une nuit type](../30-architecture/architecture-cible.md#une-nuit-type).

## Exploitation et gouvernance

| Cas d'utilisation | Acteurs | Règle |
|---|---|---|
| Enregistrer un magasin après l'acte signé | Exploitant | Aucun magasin chargé sans l'acte écrit de l'adhérent |
| Superviser la flotte et traiter les alertes | Exploitant | L'alerte va à l'exploitant, jamais au directeur |
| Rejouer une livraison depuis le landing | Étend la supervision | Livraison en quarantaine, après correction de l'adaptateur |
| Valider la correspondance des codes produits | Responsable de la donnée | Cette correspondance n'existe aujourd'hui ni en magasin ni en centrale |
| Arrêter la définition d'un indicateur | Responsable de la donnée | Avis de la commission informatique, décision du comité de direction |

Sources : [registre des sources](../30-architecture/ingestion.md#registre-des-sources), [correspondance des codes](../00-cadrage/reponses-client/index.md#33-table-de-correspondance-codes-internes-ean), [qui décide quoi](../00-cadrage/reponses-client/organisation-gouvernance.md#61-qui-decide-quoi).

## Hors année 1

| Usage | Raison |
|---|---|
| Prévoir les ruptures du jour sur le frais | Le client dit que J+1 ne suffit pas pour le frais. L'expression de besoin repousse la prévision et le quasi temps réel. À faire acter par écrit |
| Suivre le drive en temps réel | Étape suivante dans l'expression de besoin |
| Mesurer l'effet des promotions | Hors des priorités de l'année 1 |
| Exploiter les données porteur | Hors périmètre de l'année 1. Toute finalité nouvelle passe par la direction juridique |

Sources : [périmètre et priorités](expression-de-besoin-client.md#7-perimetre-et-priorites), [heure de disponibilité](../00-cadrage/reponses-client/index.md#11-heure-de-disponibilite).

## Questions ouvertes

À poser par écrit à la direction générale :

- Le national voit-il chaque magasin nommément, ou des agrégats seulement ? La note juridique interdit tout affichage comparatif nominatif, « quel que soit le destinataire ».
- La marge d'un magasin est-elle aussi fermée au national ?
- Le chef de rayon voit-il tout le magasin, ou ses rayons seulement ? Quel réglage par défaut l'adhérent reçoit-il ?
- Après une cession, le nouvel adhérent voit-il l'historique du magasin ?
