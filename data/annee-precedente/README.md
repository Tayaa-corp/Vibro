# Échantillon de données · exercice précédent

> **Émetteur :** Mouvement E.Leclerc, direction générale · **Destinataire :** équipes candidates · **Périmètre :** ventes et stocks, quatrième trimestre 2024, deux magasins

## 1. Objet

Cet échantillon complète celui du quatrième trimestre 2025, sur un périmètre restreint à deux magasins. Les systèmes de caisse conservent entre six mois et deux ans de détail selon l'éditeur et le paramétrage du magasin, et les trois autres magasins de l'échantillon initial ne disposent plus de ce trimestre en ligne.

## 2. Magasins représentés

| Magasin | Format | Solution de caisse | Remarque |
| --- | --- | --- | --- |
| Bel-Air | Hypermarché périurbain | ALPHACAISSE | Drive actif |
| Les Portes | Supermarché de périphérie | BETAPOS | Drive actif |

## 3. Contenu

```
ventes-bel-air.csv
ventes-les-portes.csv
stock-bel-air.csv
stock-les-portes.csv
```

Les fichiers sont dans le format que le système de chaque magasin produit, identique à celui du trimestre 2025. Aucune harmonisation, aucun contrôle et aucune correction n'ont été appliqués.

## 4. Période couverte

Du 2 octobre au 31 décembre 2024.

L'extraction a été calée sur le même jour de semaine que celle de 2025, de façon à ce que les samedis et les dimanches se comparent entre eux. Le décalage avec le 1er octobre est d'un jour.

## 5. Périmètre de références

L'extraction porte sur l'assortiment de chaque magasin à la date concernée. Cet assortiment a changé entre les deux exercices.

| Magasin | Codes présents en 2024 | Dont absents de 2025 | Codes de 2025 absents de 2024 |
| --- | --- | --- | --- |
| Bel-Air | 109 | 8 | 10 |
| Les Portes | 94 | 8 | 10 |

Les références présentes sur un seul des deux exercices correspondent à des produits déréférencés, à des produits locaux introduits par l'adhérent, ou à des articles saisonniers.

## 6. Données personnelles

Aucune donnée permettant d'identifier un client n'est présente. La carte de fidélité n'est indiquée que par sa présence ou son absence sur le ticket. Les noms des opérateurs de caisse ont été remplacés par un matricule interne.

## 7. Conditions d'usage

Cet échantillon est transmis dans le cadre de la consultation. Il n'est ni diffusable ni réutilisable en dehors de ce cadre.
