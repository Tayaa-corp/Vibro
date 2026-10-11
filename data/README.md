# Échantillon de données · année 1

> **Émetteur :** Mouvement E.Leclerc, direction des systèmes d'information · **Destinataire :** équipes candidates · **Périmètre :** ventes et stocks, quatrième trimestre 2025

## 1. Objet

Cet échantillon est transmis pour permettre de comprendre la donnée disponible, d'expérimenter et de démontrer une proposition. Il ne donne pas accès au réseau, il en donne un aperçu représentatif.

Cinq magasins ont accepté de fournir une extraction. Chacun a produit le fichier que son système de caisse sait produire, sans travail de mise en forme préalable. Le mouvement transmet ces fichiers tels qu'il les a reçus.

## 2. Magasins représentés

| Magasin | Format | Remarque |
| --- | --- | --- |
| Bel-Air | Hypermarché périurbain | Drive actif |
| Les Portes | Supermarché de périphérie | Drive actif |
| Centre-Ville | Magasin urbain de proximité | Pas de drive |
| Grand Large | Hypermarché de zone touristique | Drive actif, forte saisonnalité |
| Le Marché | Petit format de centre-bourg | Pas de drive |

## 3. Contenu

```
ventes-bel-air.csv
ventes-les-portes.csv
ventes-centre-ville.json
ventes-grand-large.csv
ventes-le-marche.csv
stock-bel-air.csv
stock-les-portes.csv
stock-centre-ville.csv
stock-grand-large.csv
stock-le-marche.csv
referentiel-national-partiel.csv
```

Les ventes couvrent du 1er octobre au 31 décembre 2025, à la ligne de ticket. Les états de stock ont été relevés au cours de la même période, au rythme de chaque magasin.

Le fichier `referentiel-national-partiel.csv` est le référencement produit tenu par la centrale. Il est transmis dans sa version en service.

## 4. Périmètre de l'extraction

L'extraction porte sur une partie de l'assortiment, de l'ordre de cent vingt références représentatives des grands rayons. Les montants observés ne reflètent donc pas le chiffre d'affaires réel des magasins concernés, ils reflètent l'activité de ce sous-ensemble de références.

Les magasins ont exporté ce que leur système leur permettait d'exporter. Aucune harmonisation, aucun contrôle et aucune correction n'ont été appliqués en amont.

## 5. Données personnelles

Aucune donnée permettant d'identifier un client n'est présente. La carte de fidélité n'est indiquée que par sa présence ou son absence sur le ticket. Les noms des opérateurs de caisse ont été remplacés par un matricule interne.

Le mouvement attend que le traitement de cet échantillon respecte le même niveau d'exigence que celui d'une donnée de production.

## 6. Conditions d'usage

Cet échantillon est transmis dans le cadre de la consultation. Il n'est ni diffusable ni réutilisable en dehors de ce cadre.

## 7. Questions

Les questions relatives à la donnée sont adressées par courriel aux interlocuteurs du mouvement, au même titre que les autres questions de la consultation.
