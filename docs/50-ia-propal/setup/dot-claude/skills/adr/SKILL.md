---
name: adr
description: Rédige une fiche de décision d'architecture (ADR) pour Vibro. À utiliser dès qu'un choix technique est à faire ou à justifier, comme un outil, un format, un découpage, une règle de sécurité ou une stratégie de stockage, ou quand l'utilisateur dit « on part sur », « il faut choisir entre » ou « pourquoi X plutôt que Y ».
---

# Rédiger une ADR

Le référentiel exige que chaque choix soit justifié. L'ADR est la trace de cette justification, et la source qu'utilisent les sessions IA suivantes.

## Étapes

1. **Lire** `docs/30-architecture/decisions/index.md` pour vérifier que la décision n'existe pas déjà ou n'en contredit pas une autre.
2. **Lire** les sections pertinentes de `docs/30-architecture/architecture-cible.md` et de `docs/00-cadrage/reponses-client/`. Les réponses client priment.
3. **Numéroter** : prochain numéro libre sur 4 chiffres. Fichier : `docs/30-architecture/decisions/NNNN-titre-en-kebab-case.md`.
4. **Rédiger** avec le modèle ci-dessous. Au moins deux options réellement envisagées, chacune avec ses inconvénients.
5. **Statut `proposed`** : l'IA ne passe jamais une ADR en `accepted`. C'est l'équipe qui tranche.
6. **Ajouter une ligne** dans `index.md`, dans la section « Proposées ».

## Modèle

```markdown
---
title: "NNNN · Titre de la décision"
type: adr
scope: [dev]
status: draft
updated: AAAA-MM-JJ
description: Une phrase qui résume le choix.
---

# NNNN · Titre de la décision

**Statut ADR :** proposed | accepted | rejected | superseded par NNNN
**Date :** AAAA-MM-JJ · **Décideurs :** (prénoms)

## Contexte

Le problème, et les contraintes qui pèsent dessus, avec leur source (lien vers docs/).

## Options envisagées

### Option A · nom
- Pour :
- Contre :

### Option B · nom
- Pour :
- Contre :

## Décision

L'option retenue, en une phrase, puis pourquoi.

## Conséquences

Ce que ça implique : travail, risques, ce qu'on s'interdit, ce qui reste à valider (POC).
```

## Garde-fous

- Ne pas inventer de mesures. Si un chiffre manque, l'écrire comme hypothèse ou proposer un POC.
- Rester factuel sur les outils. En cas de doute sur une fonctionnalité ou une licence, le signaler pour vérification.
