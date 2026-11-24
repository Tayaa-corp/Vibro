---
title: Réponses du client aux questions de cadrage (7 novembre 2026)
type: cr
scope: [cdp, dev]
status: validated
updated: 2026-11-23
description: Réponses de la direction générale aux 14 questions de cadrage (flux, règles métier, référentiels, gouvernance, hébergement), avec dix pièces jointes.
---

# Réponses aux questions de cadrage

> **Émetteur :** Direction générale, mouvement E.Leclerc · **Destinataire :** Antoine Leray, chef de projet · **Date :** 7 novembre 2026 · **Objet :** réponses aux 14 questions de cadrage · **Pièces jointes :** dix documents internes

Le client précise que ses pièces jointes « sont plus précises que [lui] sur les chiffres » ; chaque réponse renvoie à la pièce qui la détaille.

## Synthèse

| # | Question | Réponse courte | Détail |
|---|---|---|---|
| 1.1 | Heure de disponibilité, délai d'un jour | **7 h 30**. J+1 suffit pour le sec, **pas pour le frais** (besoin intrajournalier). Fenêtre nocturne 23 h – 6 h | [Volumétrie §4](volumetrie-et-contraintes.md#4-fenetres-dexploitation) |
| 1.2 | Export automatique des caisses | **Aucune remontée automatisée aujourd'hui** : fichiers faits à la main, envoyés par courriel | [Consolidation](consolidation-regionale.md), [Cartographie §3.1](cartographie-si.md#31-encaissement) |
| 1.3 | Volume réel | **3,4 M tickets / 34 M lignes par jour**, pic 24 décembre ×2,6, ~6 Go/jour, ~2,2 To/an | [Volumétrie §1-2](volumetrie-et-contraintes.md) |
| 2.1 | Définition de la rupture | **Aucune définition retenue**. Le « trou dans le linéaire » est celui qui coûte. Décision : responsable de la donnée → commission informatique → comité de direction | — |
| 2.2 | Prix d'achat et type de marge | **Tarif centrale** (fourni). Marge brute = CA HT − coût d'achat au tarif facturé, **hors remises arrière** | [Tarifs §5-6](tarifs-achat-centrale.md#5-la-regle-de-calcul-de-la-marge) |
| 2.3 | Nature et fréquence des relevés de stock | **Stock théorique** du back-office (pas un inventaire), écart 2 à 8 % au réel. État quotidien possible | [Cartographie §3.2](cartographie-si.md#32-gestion-de-stock-et-back-office) |
| 3.1 | Logiciels de caisse | ALPHACAISSE ~310, BETAPOS ~260, GAMMASOFT ~180, locaux ~12 (déclaratif) | [Cartographie §3.1](cartographie-si.md#31-encaissement), [Annuaire](annuaire-magasins.md) |
| 3.2 | Référentiel national complet | **Existe** : ~92 000 fiches, diffusé chaque semaine (flux F1). Ne couvre pas l'assortiment local | [Cartographie §4](cartographie-si.md#4-flux-existants) |
| 3.3 | Correspondance codes internes / EAN | **N'existe ni en magasin ni en centrale**. La direction des achats pourrait la tenir ; méthode à proposer | [Cartographie §5.1](cartographie-si.md#51-produit) |
| 4.1 | Historique et conservation | Caisses : **6 mois à 2 ans**. Données 2023 : **perdues**. Cible : **5 ans glissants** | [Données personnelles §2](donnees-personnelles-et-cloisonnement.md#2-donnees-concernees-et-qualification), [Exercice précédent](#pieces-jointes) |
| 4.2 | Moyennes de pairs | **Oui**, seuil **5 magasins minimum**. Jamais de classement nominatif | [Données personnelles §4-5](donnees-personnelles-et-cloisonnement.md#4-regles-de-cloisonnement) |
| 4.3 | Accès régional et national | Région : détail produit de **sa** région, sauf la marge. National : agrégats à toute maille, pas de détail porteur | [Données personnelles §4](donnees-personnelles-et-cloisonnement.md#4-regles-de-cloisonnement) |
| 5.1 | Hébergement, SecNumCloud | **Rien de décidé**, comparer les scénarios. **Pas de SecNumCloud**. Données en France / UE. Contrat actuel jusqu'au **30 juin 2027** | [Hébergement](hebergement-et-securite.md) |
| 5.2 | Magasins pilotes, entretiens | **Pas un dispositif pilote**. Participation décidée par l'adhérent seul. Entretiens **par écrit uniquement** | [Organisation §6.1](organisation-gouvernance.md#61-qui-decide-quoi) |

!!! warning "Mode d'échange"
    Le client refuse un point dédié « de façon à garder la trace de ce qui a été dit ». Toute question passe **par écrit** à la direction générale, qui la transmet à son destinataire (y compris en magasin) et renvoie la réponse.

## 1. Remontée des flux et fraîcheur des données

### 1.1 Heure de disponibilité

> À quelle heure les données de la veille doivent-elles être disponibles (ouverture du magasin, 7 h, 9 h) ? Un délai d'une journée suffit-il pour cette année ?

**Sept heures trente, avant l'ouverture.** C'est l'exigence des directions de magasin ([note de volumétrie, §4](volumetrie-et-contraintes.md#4-fenetres-dexploitation)).

**Un délai d'une journée ne suffit pas.** Sur le sec, la veille au matin va. Sur le frais, non : le chef de rayon a besoin de l'information pendant sa journée, et c'est là que la rupture se joue.

La fenêtre de traitement nocturne disponible va de **23 h à 6 h**, après la clôture des caisses et la sauvegarde locale. Elle se réduit le dimanche, une partie du réseau ouvrant le matin.

### 1.2 Export automatique des caisses

> Les caisses peuvent-elles produire leur export automatiquement chaque nuit, sans action du magasin ? Si non, qui le fait aujourd'hui ?

**Aucune remontée automatisée du détail des ventes n'existe aujourd'hui.** Ce qui circule, ce sont des fichiers produits à la main et envoyés par courriel.

Ils sont produits par le directeur ou son adjoint, plusieurs heures chaque semaine, souvent en dehors des heures ouvrées. Le [document de consolidation](consolidation-regionale.md) montre ce que quatre magasins d'une même région ont envoyé pour une même semaine : un tableur recopié de la caisse, un tableau tapé dans le corps d'un courriel, une édition PDF du back-office et la photographie d'un état de caisse.

Sur ce qui est techniquement possible, le précédent de 2023 est le seul élément dont dispose le client. Un module d'extraction installé dans 43 magasins produisait un export nocturne. Il tombait en panne, le directeur le relançait à la main (20 à 30 minutes par semaine) et l'informaticien local intervenait deux à trois fois par an, facturé à l'adhérent.

Les capacités d'export des trois solutions figurent dans la [cartographie, §3.1](cartographie-si.md#31-encaissement). Ce que les éditeurs documentent relève de leurs contrats avec chaque adhérent, et le mouvement n'en a pas copie.

### 1.3 Volume réel

> Quel est le volume réel constaté : nombre de tickets et de lignes par jour en moyenne et lors du pic d'activité de décembre ?

| Grandeur | Valeur |
|---|---|
| Tickets par jour (moyenne annuelle) | 3,4 millions |
| Lignes par jour (moyenne annuelle) | environ 34 millions |
| Lignes par ticket | 11,2 en hypermarché, 6,8 en supermarché |
| Journée la plus chargée | 24 décembre, **2,6 ×** la moyenne |
| Semaine la plus chargée | semaine 51, 1,9 × la moyenne |
| Creux | première quinzaine de février, 0,7 × la moyenne |
| Volume brut | environ 6 Go par jour, 2,2 To par an avant transformation |

Ces valeurs sont des totaux de parc ([note de volumétrie](volumetrie-et-contraintes.md)).

## 2. Règles de gestion métier et indicateurs

### 2.1 Définition de la rupture

> Comment définissez-vous une rupture : stock à zéro, stock sous le seuil d'alerte magasin, ou absence de vente anormale ?

**Aucune définition n'est retenue aujourd'hui.** Les trois existent dans le réseau, et celle du **trou dans le linéaire** est celle qui coûte, parce qu'un client reparti sans son produit ne revient pas le lendemain.

Deux des trois pistes portent une limite de fait :

- le **seuil d'alerte** est paramétré par le chef de rayon, parfois recalculé automatiquement par l'éditeur, et il varie d'un produit à l'autre dans un même magasin ;
- le **stock théorique** s'écarte du stock réel de 2 à 8 % selon les familles de produits.

La définition passera par le **responsable de la donnée** que le national crée, puis en **commission informatique**, et sera arrêtée en **comité de direction**.

### 2.2 Prix d'achat et marge

> D'où pouvons-nous obtenir les prix d'achat (centrale d'achat, gestion commerciale magasin, factures) pour calculer la marge ? Quelle marge attendez-vous : brute, arrière, ou après remises ?

**Du tarif de la centrale**, joint avec son fichier ([tarifs d'achat](tarifs-achat-centrale.md), `data/tarif-achat-centrale-t4-2025.csv`). Il couvre le socle national sur le périmètre de l'extraction.

**Marge attendue** : chiffre d'affaires HT moins coût d'achat au tarif facturé ; taux rapporté au CA HT ; **remises arrière exclues**. La règle et un exemple complet sont aux [§5 et §6](tarifs-achat-centrale.md#5-la-regle-de-calcul-de-la-marge) du document. Sur l'exemple (Bel-Air, octobre 2025), le calcul tient sur **82,6 % du CA** du mois.

Ce que le tarif ne couvre pas : l'assortiment local, les produits au poids, les lignes sans code et les remises arrière.

Le prix réellement payé par un magasin et ses conditions négociées ne sont pas communiqués : ils appartiennent à l'adhérent, comme sa gestion commerciale et ses factures.

### 2.3 Relevés de stock

> Les relevés de stock constatés montrent des rythmes variables et parfois des valeurs négatives : que représente exactement un relevé (inventaire physique, stock théorique du logiciel) et à quelle fréquence pouvons-nous l'obtenir ?

**Un stock théorique global**, celui que tient le back-office du magasin. **Pas un inventaire physique.**

Les valeurs négatives viennent de là : un stock théorique se déduit des entrées et des sorties, et il passe sous zéro quand une entrée n'a pas été saisie. L'écart avec le stock réel va de 2 à 8 % selon les familles.

Fréquence : les back-offices savent produire un **état quotidien**. Les **mouvements** de stock, non : les deux principaux éditeurs n'enregistrent pas les mêmes, et **232 magasins n'ont aucune solution de gestion de stock**.

## 3. Hétérogénéité des systèmes et référentiels

### 3.1 Logiciels de caisse

> Pouvez-vous nous communiquer la liste des logiciels de caisse en service ainsi que la répartition approximative du nombre de magasins équipés ?

| Solution | Magasins |
|---|---|
| ALPHACAISSE | ~310 |
| BETAPOS | ~260 |
| GAMMASOFT | ~180 |
| Éditeurs locaux | ~12 |

Détail en [cartographie §3.1](cartographie-si.md#31-encaissement) ; l'[export de l'annuaire](annuaire-magasins.md) porte la solution déclarée magasin par magasin.

!!! note "Réserve"
    Ces colonnes proviennent d'un recensement **déclaratif** conduit auprès des magasins, sans accès à leurs systèmes. Un relevé exact des versions installées supposerait de s'adresser à 762 entreprises indépendantes.

### 3.2 Référentiel national

> Le référentiel national transmis étant partiel (112 références), existe-t-il une version complète, à quelle fréquence est-elle mise à jour et son envoi peut-il être automatisé ?

**Le référentiel complet existe** : environ **92 000 fiches actives**, déjà diffusé **chaque semaine** aux magasins par un flux interne (flux F1, [cartographie §4](cartographie-si.md#4-flux-existants)). L'extrait de 112 fiches est ce que le national a produit sur le périmètre de l'échantillon pour cette consultation.

Limites :

- il ne décrit qu'une partie des rayons ;
- un magasin tient jusqu'à **25 000 références locales** qui n'y figurent pas ;
- dans l'extrait, **14 fiches sur 112** portent un libellé générique.

### 3.3 Table de correspondance codes internes / EAN

> Certains magasins utilisent leurs propres codes internes (ex. Grand Large sans code-barres, Les Portes avec 2 produits sur 3 en code interne) : existe-t-il, en magasin ou en centrale, une table de correspondance vers les codes-barres nationaux ?

**Elle n'existe ni en magasin, ni en centrale.**

Les deux constats correspondent à ce que le client mesure sur le même échantillon. Un produit vendu au poids porte un code interne au magasin, différent d'un magasin à l'autre, et un même produit peut porter jusqu'à **huit libellés**.

La **direction des achats** tient le référentiel national et pourrait tenir cette correspondance une fois établie. Son établissement est un autre travail, et **la méthode reste à proposer**.

## 4. Gouvernance, droits d'accès et historique

### 4.1 Historique et durée de conservation

> Sur combien d'années d'historique pouvons-nous compter (exports magasins, données archivées du projet 2023), et quelle durée de conservation visez-vous ?

- **Exports magasins** : les caisses conservent entre **6 mois et 2 ans** de détail selon l'éditeur et le paramétrage. C'est ce qui borne une reprise d'historique. Un extrait du trimestre équivalent de l'exercice précédent est joint : deux magasins, du 2 octobre au 31 décembre 2024 (`data/annee-precedente/`).
- **Données du projet 2023** : **il n'en reste rien**. Le [compte rendu de clôture](../compte-rendu-cloture-projet-2023.md) décrit l'état de janvier 2024 ; l'environnement qui les portait a été décommissionné depuis.
- **Durée visée** : **5 ans glissants au minimum**, pour la comparaison saisonnière. La [note juridique](donnees-personnelles-et-cloisonnement.md#2-donnees-concernees-et-qualification) retient 5 ans sur la ligne de vente sans porteur et sur les stocks.

### 4.2 Moyennes de pairs

> Un directeur de magasin peut-il consulter des moyennes de pairs comparables (même typologie, même région), sous réserve d'anonymat strict ? Si oui, à partir de quel seuil minimal de magasins agrégés ?

**Oui.** C'est ce qu'un directeur de magasin n'a pas aujourd'hui : il connaît ses chiffres et pas ceux de magasins semblables au sien.

**Seuil : 5 magasins.** Aucun agrégat portant sur moins de cinq magasins, parce qu'il permet de déduire les chiffres d'un confrère. La règle a été présentée à l'assemblée de 2024.

!!! danger "Règle"
    Une moyenne de pairs est admise. **Un classement nominatif ne l'est pas, quelle que soit la maille.**

### 4.3 Accès régional et national

> Le niveau régional doit-il accéder au détail produit par produit pour chaque magasin ou uniquement à des données consolidées ? Le niveau national a-t-il un accès exhaustif ?

- **Direction régionale** : voit le détail des magasins de **sa** région, produit par produit compris, et rien du détail des autres régions.
- **Exception** : la **marge estimée** d'un magasin reste réservée à son adhérent, y compris calculée au tarif de la centrale.
- **National** : voit des agrégats à toute maille, et **pas le détail nominatif d'un porteur de carte**.

La règle acteur par acteur figure dans la [note juridique, §4](donnees-personnelles-et-cloisonnement.md#4-regles-de-cloisonnement).

## 5. Infrastructure et démarche pilote

### 5.1 Hébergement et SecNumCloud

> L'infrastructure actuelle (datacenter français) doit-elle impérativement être conservée, ou un hébergement cloud souverain français est-il envisageable ? Une qualification SecNumCloud est-elle requise ?

**Comparer les scénarios.** Rien n'est décidé, ni pour l'hébergement ni pour la maintenance, et le client ne veut pas être enfermé chez un prestataire.

**Aucune qualification n'est exigée**, le mouvement n'étant pas assujetti aux obligations du secteur public. Ce qui est exigé : les données restent **en France ou dans l'Union européenne** selon l'application, et toute sortie de l'UE passe par la direction juridique.

| Contrat d'hébergement actuel | |
|---|---|
| Échéance | **30 juin 2027**, préavis de 3 mois |
| Réversibilité | export des données à la charge du mouvement |
| Coût | environ 140 000 € par an |
| Énergie | 96 MWh par an imputés au mouvement |

Détail des niveaux de service contractés et des huit règles de sécurité appliquées : [note hébergement et sécurité](hebergement-et-securite.md).

### 5.2 Magasins pilotes et entretiens utilisateurs

> Les cinq magasins de l'échantillon peuvent-ils constituer notre panel de magasins pilotes ? Serait-il possible d'échanger avec un directeur volontaire pour des entretiens utilisateurs et le test des maquettes ?

Les cinq magasins ont accepté de produire une extraction. **Ce n'est pas un dispositif pilote** et cela ne les engage pas pour la suite.

Le client peut demander, il ne peut pas désigner : **la participation d'un magasin relève de l'adhérent seul** ([organisation §6.1](organisation-gouvernance.md#61-qui-decide-quoi)).

**Entretiens et maquettes : par écrit.** Questions et maquettes sont adressées à la direction générale, qui les transmet à un directeur de magasin volontaire et renvoie ses retours.

## Pièces jointes

| Pièce | Émetteur | Page |
|---|---|---|---|
| Volumétrie, contraintes techniques et fenêtres d'exploitation | Équipe informatique nationale | [Lire](volumetrie-et-contraintes.md) |
| Cartographie du système d'information | Équipe informatique nationale | [Lire](cartographie-si.md) |
| Organisation, gouvernance et interlocuteurs | Direction générale | [Lire](organisation-gouvernance.md) |
| Protection des données et règles de cloisonnement | Direction juridique et conformité | [Lire](donnees-personnelles-et-cloisonnement.md) |
| Hébergement, niveaux de service et règles de sécurité | Responsable informatique nationale | [Lire](hebergement-et-securite.md) |
| Remontées des magasins et consolidation régionale | Direction générale | [Lire](consolidation-regionale.md) |
| Remontées de terrain, consultation interne de juin 2026 | Direction générale | [Lire](remontees-terrain.md) |
| Export de l'annuaire des magasins + `data/annuaire-magasins.csv` | Direction générale | [Lire](annuaire-magasins.md) |
| Tarifs d'achat de la centrale + `data/tarif-achat-centrale-t4-2025.csv` | Direction des achats | [Lire](tarifs-achat-centrale.md) |
| Extrait des ventes de l'exercice précédent (T4 2024, deux magasins) | Direction générale | `data/annee-precedente/README.md` | — |
