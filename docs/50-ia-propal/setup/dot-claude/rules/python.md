---
paths:
  - "ingestion/**/*.py"
  - "orchestration/**/*.py"
  - "tests/**/*.py"
---

# Python (ébauche, à valider avec l'ADR sur l'arborescence)

Python sert à l'ingestion (adaptateurs par éditeur de caisse) et à l'orchestration. Les transformations silver et gold sont en dbt, pas en Python.

## Outillage

- Python ≥ 3.11, dépendances via `pyproject.toml` (gestionnaire à trancher : `uv` proposé).
- `ruff format` + `ruff check` : aucun avertissement toléré en CI.
- Typage complet des fonctions publiques. `mypy --strict` sur `ingestion/`.
- Tests : `pytest`, un test par adaptateur qui lit le vrai fichier de `data/`.

## Conventions

- Modules et fonctions en `snake_case`, classes en `PascalCase`, constantes en `UPPER_SNAKE_CASE`.
- Un adaptateur = une classe par éditeur **et par version de format** : `ingestion/adapters/<editeur>/v<n>.py`.
- Le bronze garde **toutes les colonnes en texte** et ajoute `_source_file`, `_file_sha256`, `_ingested_at`, `_batch_id`, `_row_number`.
- Pas de `print` : module `logging` avec des logs structurés (magasin, fichier, lot).
- Ne jamais avaler une erreur : une ligne illisible va en quarantaine avec son motif, et le compte `lues = écrites + rejetées` doit tomber juste.
- Idempotence : retraiter un fichier ne crée pas de doublon.
- Fonctions pures pour le parsing, I/O en bordure (facilite les tests).
