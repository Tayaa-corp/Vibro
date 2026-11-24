---
title: Tarifs d'achat de la centrale et calcul de la marge
type: ressource-client
scope: [cdp, dev]
status: validated
updated: 2026-11-23
description: Socle tarifaire national sur le périmètre de l'échantillon, structure du fichier tarif, règle de calcul de la marge et exemple Bel-Air octobre 2025.
---

# Tarifs d'achat de la centrale et calcul de la marge

> **Émetteur :** Direction des achats, mouvement E.Leclerc · **Objet :** socle tarifaire national sur le périmètre de l'extraction, règle de calcul de la marge · **Exercice :** 2025 · **Diffusion :** interne

Pièce jointe aux [réponses du 7 novembre 2026](index.md). Fichier : `data/tarif-achat-centrale-t4-2025.csv`.

## 1. Objet et portée

La marge figure parmi les indicateurs de pilotage du mouvement. Ce document donne le tarif d'achat négocié par la centrale sur le périmètre des références de l'échantillon, la règle de calcul appliquée, et un exemple de calcul produit par un magasin.

La direction des achats (78 personnes) porte le référencement, la négociation fournisseurs et les conditions d'achat. Le tarif relève de son périmètre. **Il n'est pas diffusé aux caisses**, qui reçoivent les fiches produits et les prix conseillés.

## 2. Ce que la centrale négocie

L'offre d'un magasin combine deux composantes :

- le **socle national** : produits référencés et négociés par la centrale pour l'ensemble du réseau (grandes marques, marques de distributeur, gammes communes). Une négociation pour plus de 750 magasins définit un socle de produits, de tarifs et d'accords ;
- l'**assortiment local** : choisi par l'adhérent, qui référence et négocie parfois en direct des produits régionaux ou attendus par sa clientèle. Un magasin peut compter jusqu'à 25 000 références de ce type.

## 3. Ce que le tarif joint ne couvre pas

| Cas | Situation |
|---|---|
| Assortiment local | Aucun tarif national. Les conditions sont celles que l'adhérent a négociées, le national ne les connaît pas |
| Produits vendus au poids | Aucun tarif national. Le code est interne au magasin et diffère d'un magasin à l'autre |
| Articles saisis sans code en caisse | Aucun tarif. Ces lignes portent un libellé générique |
| Références déréférencées en cours d'exercice | Le tarif disparaît du fichier à la date de sortie du socle |
| Remises arrière et accords de volume | Hors du tarif. Elles se constatent en fin d'exercice, dans la comptabilité de chaque adhérent |
| Prix réellement payé par un magasin | Non connu du national. Chaque adhérent passe ses commandes et négocie ses conditions ; son prix figure dans sa gestion de stock |

## 4. Structure du fichier joint

`tarif-achat-centrale-t4-2025.csv` : extraction du socle tarifaire sur le périmètre de l'échantillon. CSV, **séparateur point-virgule, décimale à la virgule**, UTF-8, dates au format `JJ/MM/AAAA`. 124 lignes pour 112 EAN.

| Colonne | Contenu |
|---|---|
| `ean` | Code à barres de la référence nationale |
| `libelle_national` | Libellé du référentiel de la centrale |
| `rayon` | Rayon du référentiel national |
| `unite` | Unité de vente de la référence au socle national |
| `fournisseur` | Code fournisseur interne à la direction des achats |
| `tva_pct` | Taux de TVA appliqué à la référence |
| `prix_conseille_ttc` | Prix conseillé au réseau, TTC, non opposable |
| `tarif_achat_ht` | Tarif d'achat négocié, HT, quatre décimales |
| `date_effet` | Premier jour de validité du tarif |
| `date_fin` | Dernier jour de validité du tarif |

!!! warning "Deux points d'attention"
    - **Le prix conseillé n'est pas le prix pratiqué.** Chaque adhérent fixe ses prix de vente ; les prix observés dans les fichiers de ventes s'en écartent.
    - **Douze références ont été révisées au 1er novembre 2025.** Elles apparaissent sur deux lignes (validité 01/09 → 31/10 puis 01/11 → 31/12). Le tarif applicable à une vente est celui dont la période couvre la date de la vente : la jointure se fait sur `ean` **et** sur la date.

## 5. La règle de calcul de la marge

La règle appliquée dans le mouvement tient en cinq points :

1. La **marge brute** est le chiffre d'affaires HT diminué du coût d'achat des marchandises vendues, au tarif facturé.
2. Le **taux de marge** est la marge brute rapportée au chiffre d'affaires HT.
3. Le **chiffre d'affaires HT** est obtenu à partir du montant encaissé, duquel est retirée la TVA au taux de la référence.
4. Pour le socle national, le **tarif facturé** retenu est le tarif de la centrale en vigueur à la date de la vente.
5. Les **remises arrière** et les accords de volume restent hors de ce calcul.

Traduction en formules (interprétation de l'équipe, à faire confirmer) :

```text
CA HT          = montant encaissé TTC / (1 + tva_pct / 100)
Coût d'achat   = quantité × tarif_achat_ht (tarif en vigueur à la date de vente)
Marge brute    = CA HT − Coût d'achat
Taux de marge  = Marge brute / CA HT
```

Dans les faits, cette règle n'est appliquée qu'en magasin, et à la main.

## 6. Comment un magasin produit son calcul aujourd'hui

Le directeur, son adjoint ou une personne de la comptabilité extrait l'état des ventes du système du magasin, le colle dans un tableur, rapproche chaque référence du tarif qu'il connaît, et obtient une marge par rayon. La mise en forme est propre à chaque magasin. Le chef de rayon tient le même exercice sur son seul rayon.

Extrait d'un de ces tableurs, magasin **Bel-Air, octobre 2025**, établi à partir des données transmises aux équipes (utilisable comme **jeu de test** du calcul) :

| Ligne du tableur | Valeur |
|---|---|
| Lignes de vente du mois | 22 032 |
| Chiffre d'affaires TTC | 117 864,41 € |
| Dont lignes rapprochées d'un tarif national | 18 394 lignes, 97 410,86 € TTC |
| Chiffre d'affaires HT de ces lignes | 90 816,77 € |
| Coût d'achat des marchandises vendues, au tarif centrale | 69 569,97 € |
| Marge brute | 21 246,79 € |
| Taux de marge | **23,40 %** |
| Lignes sans tarif national | 3 638 lignes, 20 453,55 € TTC, soit 17,4 % du CA |
| Dont lignes saisies sans code en caisse | 277 lignes, 1 824,91 € TTC |

Le directeur de ce magasin applique de mémoire un taux estimé aux lignes sans tarif, noté en commentaire dans son fichier, et ce taux varie d'un mois à l'autre.

## 7. Les limites de cet exemple

- Le taux obtenu porte sur **82,6 % du chiffre d'affaires** du mois.
- L'extraction transmise couvre de l'ordre de cent vingt références représentatives des grands rayons : les montants reflètent ce sous-ensemble, pas le CA réel du magasin.
- Le tarif centrale n'est pas le prix payé. Un adhérent qui commande en volume ou négocie en direct obtient d'autres conditions, et l'écart n'est pas connu du national.
- Aucune marge consolidée n'existe aujourd'hui, ni en région ni au national. Les régions remontent du CA et des volumes par rayon.

!!! danger "Confidentialité"
    La marge estimée d'un magasin reste **réservée à son adhérent**, y compris vis-à-vis de sa direction régionale ([réponse 4.3](index.md#43-acces-regional-et-national)).

!!! note
    Ce document donne un socle tarifaire et une règle de calcul. La marge constatée relève de la comptabilité de chaque entreprise adhérente.
