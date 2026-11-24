---
title: Points à trancher et activation
type: ia
scope: [dev]
status: draft
updated: 2026-11-24
description: Décisions à prendre en équipe avant d'activer le setup IA, et procédure d'activation.
---

# Points à trancher

| # | Question | Proposition | Décision |
|---|---|---|---|
| 1 | **Claude seulement, ou multi-outils ?** | Si quelqu'un utilise Cursor ou Codex, le contenu de `CLAUDE.md` passe dans `AGENTS.md` (lu par la plupart des outils) et `CLAUDE.md` se limite à `@AGENTS.md`. Les rules, skills et hooks restent propres à Claude | |
| 2 | **Arborescence du code** | `ingestion/`, `orchestration/`, `transform/`, `infra/`, `tests/`, à acter par l'ADR 0001 avant de finaliser les rules `python` et `dbt-sql` | |
| 3 | **Langue** | Docs, rules et échanges en français. Code, identifiants et commits en anglais, comme l'historique git actuel | |
| 4 | **Validation du setup** | PR obligatoire, un relecteur, scope de commit `ai` | |
| 5 | **IA et livrables évalués** | Le skill `livrable` ne produit qu'un brouillon. Chacun réécrit et doit pouvoir défendre sa partie à l'oral | |
| 6 | **Modèle commun** | Fixer un modèle dans `settings.json` pour avoir des résultats comparables, ou laisser chacun choisir | |

# Activation

Une fois les points ci-dessus tranchés, depuis la racine du repo :

```bash
git mv docs/50-ia-propal/setup/CLAUDE.md CLAUDE.md
git mv docs/50-ia-propal/setup/dot-claude .claude
mkdir -p docs/30-architecture/decisions
git mv docs/50-ia-propal/setup/decisions/index.md docs/30-architecture/decisions/index.md
printf 'CLAUDE.local.md\n.claude/settings.local.json\n' >> .gitignore
```

Ensuite :

1. Ouvrir Claude Code et lancer `/memory` pour vérifier que `CLAUDE.md` et les rules sont chargés.
2. Tenter une écriture dans `data/` pour vérifier que le hook bloque.
3. Passer le statut des pages de cette section à `superseded`, avec un lien vers `CLAUDE.md`.
