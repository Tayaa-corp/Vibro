---
paths:
  - "transform/**/*.sql"
  - "transform/**/*.yml"
---

# dbt et SQL (ébauche, à valider avec l'ADR sur l'arborescence)

## Structure

```
transform/models/
├── staging/   stg_<source>__<entite>.sql   (lecture du bronze, renommage, typage)
├── silver/    <entite>.sql                 (nettoyé, dédoublonné, réconcilié)
└── gold/      fait_<sujet>.sql, dim_<axe>.sql, agg_<sujet>_<grain>.sql
```

## Conventions

- SQL en minuscules, `snake_case`, une CTE par étape, `select` final explicite (pas de `select *` en gold).
- `sqlfluff` (dialecte trino) sans erreur.
- Chaque modèle a un `.yml` avec une description, les tests `not_null` et `unique` sur la clé, et `relationships` vers les dimensions.
- Horodatages : toujours en UTC **et** en heure locale, plus la date commerciale.
- Comparaison N-1 sur le **jour équivalent** (même jour de la semaine) via `dim_date`, jamais sur la date calendaire.
- Marge brute = CA HT − coût d'achat au tarif centrale, hors remises arrière (réponse client 2.2).
- Toute table gold exposée documente son mode de cloisonnement (voir `data-securite.md`).
- Matérialisation incrémentale ou par partition en silver : un retraitement ne doit jamais dupliquer.
