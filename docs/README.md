# Vibro

Documentation du projet Vibro.

## Contenu

- [Installation](guide/Installation.md) — prérequis et mise en route
- [Utilisation](guide/Utilisation.md) — commandes courantes

## Prévisualiser ce site

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-docs.txt
mkdocs serve
```

Le site est alors disponible sur [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Publication

Chaque push sur `main` construit le site et le publie sur GitHub Pages.
