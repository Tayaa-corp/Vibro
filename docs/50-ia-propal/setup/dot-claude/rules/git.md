# Git

semantic-release calcule les versions à partir des messages de commit. Un message mal formé, c'est une release manquée.

## Messages de commit

Format [Conventional Commits](https://www.conventionalcommits.org/), en anglais, à l'impératif :

```
<type>(<scope optionnel>): <résumé en minuscules, sans point final>
```

Limites de longueur :

| Partie | Limite | Pourquoi |
|---|---|---|
| Première ligne (type, scope et résumé compris) | **72 caractères max**, viser 50 | Lisible dans `git log --oneline`, GitHub et le changelog sans être tronquée |
| Corps | Lignes de **72 caractères max**, séparé du titre par une ligne vide | Convention git, lisible dans un terminal |

Si le résumé ne tient pas en 72 caractères, c'est souvent que le commit fait plusieurs choses : le découper.

| Type | Usage | Release |
|---|---|---|
| `feat` | Nouvelle fonctionnalité ou nouveau contenu de livrable | minor |
| `fix` | Correction | patch |
| `perf` | Performance | patch |
| `docs` | Documentation seule | aucune |
| `refactor`, `test`, `chore`, `ci`, `build` | Le reste | aucune |

Changement cassant : `feat!:` ou une ligne `BREAKING CHANGE:` dans le corps.

Scopes conseillés : `ingestion`, `transform`, `orchestration`, `infra`, `docs`, `ai` (setup IA).

## Branches et PR

- Jamais de commit direct sur `main`. Une branche par sujet : `<type>/<sujet-court>`, par exemple `feat/adapter-betapos`.
- Une PR = un sujet. Au moins une relecture humaine avant le merge.
- Ne pas `push`, `rebase` ni `reset` sans demande explicite.
