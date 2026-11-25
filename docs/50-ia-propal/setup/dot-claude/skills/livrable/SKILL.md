---
name: livrable
description: Aide à rédiger une section d'un livrable évalué (CDC, DAT, DCT, carnet de veille, PMP, tableau de bord, cahier de recette, support de comité) en respectant le périmètre DEV. À utiliser dès que l'utilisateur parle d'un livrable, d'un rendu, d'un comité ou d'une section à rédiger pour César.
---

# Rédiger une section de livrable

Ces documents sont **évalués**. L'IA produit un brouillon structuré et sourcé, que l'équipe réécrit et doit pouvoir défendre à l'oral.

## Étapes

1. **Lire** `docs/00-cadrage/modalites-apprenant.md` : la liste des livrables, les dates, et les marqueurs `[DEV]`, `[CDP]` et `[DEV+CDP]` de la section demandée.
2. **Vérifier le périmètre** :
   - `[DEV]` : rédiger ;
   - `[DEV+CDP]` : rédiger uniquement la contribution DEV, et laisser un encart `> [CDP] à compléter par le chef de projet` ;
   - `[CDP]` : **ne pas rédiger**. Le dire à l'utilisateur et proposer à la place les éléments techniques à transmettre au chef de projet.
3. **Identifier la compétence évaluée** (section 6 des modalités) et faire en sorte que la section la démontre explicitement.
4. **Rassembler les sources** : besoin, réponses client, ADR, architecture. Chaque affirmation chiffrée ou chaque choix renvoie à sa source.
5. **Rédiger le brouillon** dans `docs/` (frontmatter `type: livrable`, `status: draft`), dans le registre demandé (roleplay prestataire ou pédagogique).
6. **Terminer par** une liste « À vérifier par l'équipe » : hypothèses, points faibles, questions qu'un jury pourrait poser.

## Garde-fous

- Ne pas inventer de retour client, de mesure ou de décision. Ce qui n'est pas sourcé est marqué « hypothèse ».
- Garder un ton de prestataire qui challenge le besoin, sans se contenter de le reformuler.
- Ne pas produire le PDF final. La mise en forme du rendu est faite par l'équipe.
