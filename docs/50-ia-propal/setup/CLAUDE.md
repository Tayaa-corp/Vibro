# Vibro · instructions IA

Plateforme décisionnelle de pilotage commercial pour le mouvement E.Leclerc : lakehouse batch open source (ingestion nocturne des caisses → bronze → silver → gold → tableaux de bord). Projet d'école M2 DEV (RNCP 40166) mené en roleplay de prestataire : l'équipe compte 3 devs et 1 chef de projet.

## Lectures obligatoires

Toujours en contexte :

@docs/30-architecture/decisions/index.md

**Avant toute proposition technique** (choix d'outil, modèle de données, découpage) :

- `docs/30-architecture/architecture-cible.md` : architecture de travail (statut `draft`)
- `docs/00-cadrage/reponses-client/index.md` : réponses du client, qui **priment** sur nos hypothèses
- `docs/10-besoins/expression-de-besoin-client.md` : besoin initial

**Avant tout livrable** : `docs/00-cadrage/modalites-apprenant.md` (livrables, périmètre DEV / CDP).

Si une réponse client contredit l'architecture-cible, signale l'écart au lieu de choisir en silence.

## Carte du repo

| Chemin | Contenu |
|---|---|
| `docs/` | Documentation MkDocs, source de vérité. `00-cadrage`, `10-besoins`, `30-architecture`, `40-dev` |
| `docs/30-architecture/decisions/` | Décisions d'architecture (ADR) |
| `data/` | Échantillon client **en lecture seule** (CSV/JSON hétérogènes, encodages variés) |
| `ingestion/`, `orchestration/`, `transform/`, `infra/` | Code (à créer, voir ADR sur l'arborescence) |

## Commandes

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-docs.txt
mkdocs serve            # prévisualiser la doc
mkdocs build --strict   # vérifier liens et structure avant une PR de doc
```

## Règles absolues

1. **Ne jamais modifier `data/`.** Ce sont les fichiers du client, tels que reçus. Copier dans un dossier de test si besoin.
2. **Aucun secret dans le repo** : ni mot de passe, ni clé, ni token, même factice et réaliste.
3. **Commits au format Conventional Commits** en anglais : semantic-release en dépend (voir `.claude/rules/git.md`).
4. **Un choix technique nouveau = une ADR** (skill `adr`). Ne pas introduire d'outil ou de dépendance majeure sans elle.
5. **Le cloisonnement entre magasins se fait dans la couche de données**, jamais seulement dans la BI.
6. **Ne pas inventer de chiffres client.** Toute volumétrie ou règle métier cite sa source dans `docs/`, sinon elle est marquée comme hypothèse.
7. **Rester dans le périmètre DEV** : ne pas rédiger les sections `[CDP]` des livrables.

## Langue

Docs, rules et échanges en français. Code, identifiants, commentaires de code et messages de commit en anglais.
