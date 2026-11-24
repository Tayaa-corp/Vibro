---
title: Lectures obligatoires
type: ia
scope: [dev]
status: draft
updated: 2026-11-24
description: Les trois mécanismes pour que l'IA connaisse le projet (import, rule par chemin, consigne), leur garantie, leur coût, et la répartition proposée.
---

# Lectures obligatoires

On ne peut pas forcer l'IA à lire un fichier en écrivant « lis-le ». Il faut choisir le bon mécanisme selon l'importance du document et sa taille.

## Les trois mécanismes

| Niveau | Mécanisme | Garantie | Coût en contexte |
|---|---|---|---|
| Toujours lu | `@chemin` dans `CLAUDE.md` (import) | Totale | Permanent, à chaque message |
| Lu selon le fichier touché | Rule avec `paths:` | Forte | Seulement quand c'est pertinent |
| Lu sur consigne | « Avant X, lire Y » dans `CLAUDE.md` ou un skill | Faible | Seulement si la consigne est suivie |

## Répartition proposée

| Document | Mécanisme | Raison |
|---|---|---|
| `docs/30-architecture/decisions/index.md` | **Import `@`** | Une page, stable, et c'est ce qui doit absolument être respecté |
| `docs/30-architecture/architecture-cible.md` | Consigne : avant toute proposition technique | En `draft`, va bouger, environ 5k tokens |
| `docs/00-cadrage/reponses-client/index.md` | Consigne : avant toute proposition technique | Les réponses client priment sur nos hypothèses |
| `docs/10-besoins/expression-de-besoin-client.md` | Consigne : avant toute proposition technique | Contexte métier |
| `docs/00-cadrage/modalites-apprenant.md` | Consigne dans le skill `livrable` | Utile seulement pour les rendus évalués |
| Conventions de doc | Rule `docs.md` (`paths: docs/**`) | Chargée seulement quand on écrit de la doc |

## Le frontmatter comme index

Les docs ont déjà un frontmatter (`type`, `scope`, `status`, `description`). La rule `docs.md` le rend obligatoire. L'IA peut ainsi trier les documents (par exemple écarter ce qui est `superseded`, ou ne lire que le `scope: [dev]`) sans tout ouvrir.

## La page de décisions

[`setup/decisions/index.md`](setup/decisions/index.md) est le seul document chargé en permanence. Pour que ça tienne, elle doit rester courte : une ligne par décision, le détail dans chaque fiche ADR. Une décision passée en « Actée » s'impose à toutes les sessions suivantes, pour tout le monde.
