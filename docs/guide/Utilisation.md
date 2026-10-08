# Utilisation

## Serveur de prévisualisation

Depuis la racine du dépôt :

```bash
source .venv/bin/activate
mkdocs serve
```

Le contenu d’une page déjà connue est relu à chaque requête. Après l’ajout d’un nouveau fichier, relancez `mkdocs serve`.

## Ajouter une page

1. Créez un fichier `.md` dans `docs/`.
2. Reliez-le depuis une autre page avec un lien relatif, par exemple `[Titre](guide/Page.md)`.
3. Relancez `mkdocs serve`.

La navigation reprend le nom de chaque fichier, sans extension. `README.md` et `index.md` sont servis comme page d’accueil de leur dossier.
