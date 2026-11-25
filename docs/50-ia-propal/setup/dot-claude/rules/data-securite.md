# Données client et sécurité

## Données de `data/`

- Lecture seule (garanti par permission + hook). Ce sont les fichiers tels que reçus du client, défauts compris.
- Les défauts sont **le sujet** : encodages multiples, séparateurs différents, dates hétérogènes, codes à zéros initiaux (`0042`). Ne jamais les « corriger » à la source. Le code doit les absorber.
- Pour un test, référencer le fichier de `data/` en lecture, ou copier un extrait minimal dans `tests/fixtures/`.

## Cloisonnement entre magasins

Exigence client non contournable : un magasin ne voit jamais les données d'un autre.

- Le filtrage se fait dans la couche de données (moteur de requête, sécurité au niveau des lignes), **pas seulement** dans la BI.
- Toute nouvelle table gold ou vue exposée doit dire comment elle est cloisonnée.
- Moyennes de pairs : **5 magasins minimum**, jamais de classement nominatif (réponse client 4.2).
- Tout changement qui touche l'accès aux données s'accompagne d'un test de cloisonnement.

## Données personnelles

- Aucune donnée nominative traitée cette année. Ne pas ajouter de colonne identifiante (nom, carte fidélité, e-mail) sans ADR.
- Minimisation : ne charger que les colonnes utiles à un indicateur identifié.

## Secrets

- Jamais dans le code, la doc, les tests ni les exemples. Variables d'environnement ou coffre (Vault/OpenBao).
- Fichiers `.env`, `*.pem` et `*.key` : non lisibles par l'IA, non versionnés.
