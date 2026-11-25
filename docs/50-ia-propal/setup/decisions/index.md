---
title: Décisions d'architecture
type: adr
scope: [dev]
status: draft
updated: 2026-11-24
description: Résumé des décisions d'architecture actées et proposées. Chargé automatiquement dans chaque session IA.
---

# Décisions d'architecture

Ce fichier est importé dans `CLAUDE.md` : il doit rester **court** (une ligne par décision). Le détail est dans chaque fiche.

## Actées

Ces décisions s'imposent. Ne pas proposer d'alternative sans nouvelle ADR.

| # | Décision | Fiche |
|---|---|---|
| | *Aucune décision actée pour l'instant* | |

## Proposées

En discussion. Peuvent être challengées.

| # | Sujet | Fiche |
|---|---|---|
| 0001 | Arborescence du code (`ingestion/`, `orchestration/`, `transform/`, `infra/`) | à rédiger |
| 0002 | Lakehouse batch plutôt que base relationnelle unique | à rédiger |
| 0003 | Landing immuable + bronze Parquet en texte | à rédiger |
| 0004 | Format de table Iceberg et catalogue | à rédiger |
| 0005 | Moteur de requête Trino (ClickHouse en option) | à rédiger |
| 0006 | Orchestrateur Dagster ou Airflow | à rédiger |
| 0007 | Cloisonnement dans la couche de données | à rédiger |

Liste issue de la section 13 de `docs/30-architecture/architecture-cible.md`.

## Remplacées

| # | Décision | Remplacée par |
|---|---|---|
