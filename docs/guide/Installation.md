# Installation

## Prérequis

- Python 3.10 ou plus récent

## Dépendances de la documentation

MkDocs 2.0 est encore en préversion. La version est épinglée dans `requirements-docs.txt`.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-docs.txt
```

## Générer le site

Depuis la racine du dépôt :

```bash
mkdocs build
```

Les fichiers statiques sont écrits dans le dossier `site/`.
