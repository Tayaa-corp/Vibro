---
name: adaptateur
description: Crée ou modifie un adaptateur d'ingestion pour un éditeur de caisse (ALPHACAISSE, BETAPOS, GAMMASOFT, logiciel local) qui transforme un export brut en bronze. À utiliser quand l'utilisateur veut ingérer un nouveau format de fichier de ventes ou de stock, ou qu'un fichier de data/ n'est pas encore lu.
---

# Créer un adaptateur éditeur (ébauche)

## Étapes

1. **Identifier la source** : éditeur, version de format, magasins concernés (`data/annuaire-magasins.csv`, `docs/00-cadrage/reponses-client/cartographie-si.md`).
2. **Profiler le fichier** dans `data/`, en lecture seule : encodage réel, séparateur, en-têtes, format des dates et des heures, décimales, codes à zéros initiaux, lignes de total ou de pied de page. Noter chaque particularité.
3. **Créer** `ingestion/adapters/<editeur>/v<n>.py` en implémentant l'interface commune des adaptateurs.
4. **Sortie bronze** : toutes les colonnes en texte, valeurs inchangées, plus les colonnes techniques (`_source_file`, `_file_sha256`, `_ingested_at`, `_batch_id`, `_row_number`).
5. **Rejets** : toute ligne illisible part en quarantaine avec son motif. Rien n'est supprimé en silence.
6. **Tests** dans `tests/ingestion/test_<editeur>_v<n>.py`, sur le vrai fichier de `data/` :
   - nombre de lignes lues = écrites + rejetées ;
   - un code à zéros initiaux est conservé tel quel ;
   - les caractères accentués sont lus correctement (pas de mojibake) ;
   - retraiter le même fichier ne produit pas de doublon.
7. **Documenter** le format dans `docs/40-dev/` (contrat d'échange de l'éditeur) avec les particularités relevées à l'étape 2.

## À ne pas faire

- Typer ou normaliser au bronze : c'est le rôle du silver (dbt).
- Modifier le fichier source pour « le rendre lisible ».
- Écrire un adaptateur générique « qui devine » : un format = une classe explicite.
