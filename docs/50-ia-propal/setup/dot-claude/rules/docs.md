---
paths:
  - "docs/**/*.md"
---

# Documentation

La doc est la source de vérité pour l'équipe **et** pour l'IA. Elle doit rester triable sans être lue en entier.

## Frontmatter obligatoire

```yaml
---
title: Titre lisible
type: cadrage | besoins | architecture | adr | dev | ia | cr | livrable
scope: [dev] | [cdp] | [dev, cdp]
status: draft | review | validated | superseded
updated: AAAA-MM-JJ
description: Une phrase qui dit ce que le lecteur y trouve.
---
```

- Mettre `updated` à jour à chaque modification de fond.
- `status: superseded` : ajouter en tête un lien vers le document qui remplace celui-ci. Ne pas supprimer.

## Rangement

| Dossier | Contenu |
|---|---|
| `00-cadrage/` | Cadre, modalités, réponses client (on ne réécrit pas les réponses client) |
| `10-besoins/` | Besoin exprimé et analysé |
| `30-architecture/` | Architecture, `decisions/` (ADR) |
| `40-dev/` | Installation, utilisation, conventions de dev |
| `50-ia-propal/` | Proposition de setup IA (temporaire) |

Toute nouvelle page est reliée depuis une page existante (la navigation MkDocs suit les fichiers). Vérifier avec `mkdocs build --strict`.

## Style

- Français, phrases courtes, voix active. Pas d'emoji.
- Tableaux pour comparer, listes pour énumérer, prose pour expliquer.
- Toute donnée chiffrée cite sa source (lien relatif vers `docs/` ou `data/`), sinon elle est écrite « hypothèse ».
- Diagrammes : Mermaid ou draw.io (plugins déjà configurés).

## Livrables

Les sections marquées `[CDP]` relèvent du chef de projet : ne pas les rédiger. Pour `[DEV+CDP]`, ne rédiger que la contribution DEV. Voir le skill `livrable`.
