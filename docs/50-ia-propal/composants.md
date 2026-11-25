---
title: Composants proposés
type: ia
scope: [dev]
status: draft
updated: 2026-11-24
description: Catalogue des fichiers de la v1 du setup IA (CLAUDE.md, permissions, hook, rules, skills, agent), avec leur rôle et leur état.
---

# Composants proposés

Les fichiers ci-dessous sont les vrais fichiers de la v1, prêts à être déplacés à la racine du repo après validation. Ils sont relisibles directement sur ce site.

## Socle

| Fichier | Rôle | État |
|---|---|---|
| [`CLAUDE.md`](setup/CLAUDE.md) | Lu à chaque session : présentation du projet, lectures obligatoires, carte du repo, commandes, 7 règles absolues | Prêt à relire |
| [`settings.json`](setup/dot-claude/settings.json) | Permissions partagées (autorisé seul / à demander / interdit) et branchement du hook | Prêt à relire |
| [`hooks/guard.py`](setup/dot-claude/hooks/guard.py) | Bloque toute écriture dans `data/` et tout contenu qui ressemble à un secret | Testé |
| [`decisions/index.md`](setup/decisions/index.md) | Page de décisions importée dans `CLAUDE.md`, avec les 7 ADR à rédiger | Exemple |

### Permissions

| Niveau | Exemples |
|---|---|
| Autorisé sans demander | `git status`, `git diff`, `git log`, `mkdocs build`, `pytest`, `ruff`, `sqlfluff`, `dbt compile`, `dbt test` |
| Demande de confirmation | `git commit`, `git push`, `git reset`, `git rebase`, `pip install`, `dbt run`, `tofu apply` |
| Interdit | Écrire dans `data/`, lire `.env`, `*.pem`, `*.key` |

L'écriture dans `data/` est bloquée deux fois : par une permission et par le hook. Si l'un des deux est mal configuré, l'autre tient.

## Rules

| Rule | S'applique à | Contenu | État |
|---|---|---|---|
| [`git.md`](setup/dot-claude/rules/git.md) | Toujours | Conventional Commits (requis par semantic-release), branches, PR | Prêt à relire |
| [`data-securite.md`](setup/dot-claude/rules/data-securite.md) | Toujours | `data/` en lecture seule, cloisonnement entre magasins, RGPD, secrets | Prêt à relire |
| [`docs.md`](setup/dot-claude/rules/docs.md) | `docs/**/*.md` | Frontmatter obligatoire, rangement, style, périmètre DEV / CDP | Prêt à relire |
| [`python.md`](setup/dot-claude/rules/python.md) | `ingestion/**`, `orchestration/**`, `tests/**` | Outillage, conventions des adaptateurs, bronze en texte, quarantaine | **Ébauche** |
| [`dbt-sql.md`](setup/dot-claude/rules/dbt-sql.md) | `transform/**` | Structure staging / silver / gold, nommage, tests, N-1 jour équivalent, marge | **Ébauche** |

Les deux ébauches dépendent de l'arborescence du code, qui n'est pas encore décidée.

## Skills

| Skill | Se déclenche quand | Produit | État |
|---|---|---|---|
| [`adr`](setup/dot-claude/skills/adr/SKILL.md) | Un choix technique est à faire ou à justifier | Une fiche ADR `proposed` + une ligne dans l'index | Prêt à relire |
| [`adaptateur`](setup/dot-claude/skills/adaptateur/SKILL.md) | Un nouveau format de caisse est à ingérer | Un adaptateur, ses tests sur `data/`, le contrat d'échange documenté | **Ébauche** |
| [`livrable`](setup/dot-claude/skills/livrable/SKILL.md) | On rédige une section de rendu évalué | Un brouillon sourcé, limité au périmètre DEV, avec une liste « à vérifier » | Prêt à relire |

## Agent

| Agent | Rôle | État |
|---|---|---|
| [`reviewer`](setup/dot-claude/agents/reviewer.md) | Relit un diff avant PR, sans rien modifier. Vérifie, du plus grave au moins grave : cloisonnement, données et secrets, perte silencieuse, idempotence, ADR, conventions, tests | Prêt à relire |

## Limites connues

- La détection de secrets du hook ne couvre que les cas courants (clés privées, clés AWS, tokens GitHub, `password = "…"` en dur). Elle ne remplace pas un scanner en CI.
- Les chemins `ingestion/`, `transform/`, etc. sont des hypothèses à confirmer par l'ADR 0001.
