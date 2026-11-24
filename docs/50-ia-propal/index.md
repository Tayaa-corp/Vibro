---
title: Proposition de setup IA partagé
type: ia
scope: [dev]
status: draft
updated: 2026-11-24
description: Comment l'équipe travaille avec une IA commune (Claude Code), avec les mêmes connaissances, règles, procédures et garde-fous pour tous.
---

# Proposition de setup IA partagé

> **Statut : v1 à challenger.** Rien dans cette section n'est actif. Les fichiers proposés sont rangés dans [`setup/`](#contenu-de-la-section) et ne seront déplacés à la racine du repo (`CLAUDE.md`, `.claude/`) qu'après validation de l'équipe.

## Objectif

On développe Vibro avec l'IA. Si chacun configure son propre assistant, on obtient trois façons de nommer, de commiter, de structurer le code et de rédiger la doc. L'objectif est d'avoir **une seule IA, partagée par toute l'équipe**, avec :

- les mêmes **connaissances** du projet : architecture, décisions, contraintes client ;
- les mêmes **règles** de code, de doc et de git ;
- les mêmes **procédures** (skills) pour les tâches qui reviennent ;
- les mêmes **garde-fous**, appliqués automatiquement et pas seulement demandés.

Tout est versionné dans le repo : cloner le repo, c'est récupérer le setup.

## Principes

| # | Principe | Ce que ça veut dire |
|---|---|---|
| 1 | **La doc fait foi, pas le prompt** | L'IA lit `docs/`. On ne recopie pas l'architecture dans les règles, on y renvoie |
| 2 | **Charger le minimum, au bon moment** | Plus il y a de texte en contexte permanent, plus l'IA en ignore une partie. Chaque info est rangée dans le format qui la charge seulement quand elle sert |
| 3 | **Plus c'est critique, plus c'est automatisé** | Une consigne écrite peut être oubliée, un hook ne peut pas l'être |
| 4 | **Un fichier = un sujet** | Des fichiers de règles courts et ciblés plutôt qu'un gros `CLAUDE.md` |
| 5 | **Le setup se modifie par PR** | Relue par au moins un autre dev, comme du code |
| 6 | **L'humain reste responsable** | L'IA produit, on relit, on comprend, on sait justifier. Le jury évalue nos choix, pas ceux de l'IA |

## Contenu de la section

| Page | Contenu |
|---|---|
| [Architecture du setup](architecture.md) | Arborescence, rôle de chaque format, où ranger une info |
| [Lectures obligatoires](lectures-obligatoires.md) | Comment garantir que l'IA connaît le projet |
| [Cycle de travail](cycle-de-travail.md) | Une session type, de la demande à la PR, et la gouvernance du setup |
| [Composants proposés](composants.md) | Le catalogue des fichiers de la v1 et leur état |
| [Points à trancher](points-a-trancher.md) | Les décisions à prendre en équipe, et la procédure d'activation |
