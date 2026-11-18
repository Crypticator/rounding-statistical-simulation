# Contrôle de fermeture — Partie II, version 0.3.1

**Ouvrage :** *Rounding and Statistical Simulation — Parts I and II: Foundations of affine compatibility and noisy simulation*  
**Auteurs :** Samir Bouftass et ChatGPT (OpenAI)  
**Édition examinée :** 0.3.1, 17 novembre 2026, 42 pages  
**Date du contrôle :** 17 novembre 2026  
**Rapporteur :** GPT, contradicteur dans le cadre de ce travail  
**Décision : TAMPON PARTIE II V0.3.1 ACCORDÉ.**  
**T2-E01 : CLOSED.**

## 1. Décision et périmètre

La seule réserve ouverte par l’audit de la version 0.3 concernait l’export du symbole de cardinalité `#` au §5.8, page 30, sous LibreOffice 25.2.3.2. Le PDF alors livré était correct, mais sa reconstruction remplaçait le signe par un marqueur rouge. Le présent contrôle constate l’intégration effective du correctif, reproduit son effet dans ce même moteur et vérifie l’absence de modification scientifique incidente.

Le tampon porte sur la **Partie II : chapitres 5–6 et annexe B**, avec les adaptations documentaires de cette édition cumulative. Il lève la suspension documentaire attachée au verdict scientifique favorable antérieur. La Partie I demeure couverte par son contrôle précédent ; son texte est conservé dans le volume. Ce rapport n’est ni un nouvel audit scientifique intégral des six chapitres, ni une validation de chapitres non rédigés, ni une évaluation doctorale institutionnelle, ni une certification de sécurité cryptographique.

Les chapitres 7 et suivants ne sont pas engagés par ce contrôle. **Boom peut poursuivre la rédaction ; les résultats à venir devront être examinés séparément.**

## 2. Identification des pièces effectivement examinées

Paquet reçu : `RECHECK_GPT_THESIS_PART_II_V0_3_1.zip`. Son dossier `MANUSCRIPT/` contient les documents canoniques. Le dossier `BASELINE_V0_3/` contient la version antérieure utilisée pour les comparaisons.

| Pièce | SHA-256 calculé |
|---|---|
| Archive de fermeture reçue | `a59e5dd8cc2a6c606ca395b46611b9b862cc24f4eb04bafef6abd77ee2804647` |
| Source Markdown v0.3.1 | `82de7615f87745eb4061bf1ca513418ca27d3f6366085debf14ba86a86a0dc66` |
| DOCX canonique v0.3.1 | `f26cdbd7a1e253244254d02842ee1bcbf60e09b9f5f618134a2b2ef0945b4962` |
| PDF canonique v0.3.1 | `cc1871d323fcc40a49bfa4ecae1aae0f82398c0119c0e30f0e84df8c57b95183` |
| Archive de référence v0.3 | `c832b8ffac1880fdc15dd9fd7c4807555cea7e60652f9f2c33663d723621bba5` |

Le manifeste extérieur comporte **43 entrées**, celui du manuscrit révisé **38 entrées**, celui de la référence **29 entrées**. Tous les contrôles passent. Ces nombres correspondent à des manifestes partiellement imbriqués, pas à autant de fichiers distincts. Le manifeste extérieur passe de nouveau après les opérations sur les copies : les originaux sont restés intacts.

Les empreintes source, DOCX, PDF, HTML et LaTeX correspondent aux valeurs de `RELEASE_INFO.json`. Le rapport d’audit antérieur inclus dans le paquet est identique octet pour octet au rapport disponible dans cette conversation. Il est utilisé pour définir la réserve à fermer, pas comme preuve nouvelle.

## 3. Vérification de l’étendue de la correction

### 3.1 Texte, programmes, résultats et figures

Le diff complet des sources Markdown ne contient qu’un changement de la ligne de version/date de la couverture. **Tout le corps scientifique est inchangé**, notamment les définitions, énoncés, démonstrations, formules, tableaux, annexes et références.

L’empreinte du suffixe UTF-8 situé immédiatement après les caractères `# Abstract`, en conservant les retours à la ligne suivants, est :

`e3a9cc97283ee5fff2f04f6ffb5f9b21721ec2e9ca1303d7d984ff1a47efb98f`

Elle correspond à celle annoncée dans le fichier d’identification. Le vérificateur enregistre aussi une empreinte incluant le titre du résumé ; les deux découpages sont explicitement distingués.

Les **cinq programmes scientifiques**, les **trois JSON de résultats de la Partie II**, `verification_results.json` et les **trois figures** sont identiques octet pour octet à la version 0.3. Leurs empreintes figurent dans `evidence/integrity/integrity_results.json`.

**Aucune campagne scientifique n’a été relancée pendant ce contrôle.** Il s’agit d’une fermeture ciblée : les preuves et les programmes inchangés ne sont pas présentés comme nouvellement audités ou réexécutés.

### 3.2 Générateur et équations natives

La modification fonctionnelle de `build_manuscript.py` consiste à remplacer :

```python
text_node.text == '*'
```

par :

```python
text_node.text in ('*', '#')
```

Le traitement existant ajoute alors `m:lit=1` au jeton `#`. Le seul autre changement exécutable est le nom de version utilisé pour les fichiers. Une comparaison des arbres syntaxiques, après ces substitutions précises, confirme l’absence d’autre modification fonctionnelle ; les commentaires sont sans effet.

Les DOCX ancien et révisé contiennent chacun **1 063 objets mathématiques natifs**. Un seul objet diffère, celui d’indice 781 en numérotation à partir de zéro : il reçoit l’attribut littéral au signe de cardinalité. Après retrait diagnostique de ce seul ajout, les deux objets ont la même sérialisation XML canonique. Les neuf astérisques littéraux restent présents. La version révisée contient un signe `#` traité littéralement.

Après reconstruction depuis la source, les **1 063 objets mathématiques du nouveau DOCX sont identiques à ceux du DOCX livré**. Aucun objet n’a été supprimé ni transformé en image.

## 4. Reconstructions réellement exécutées

Environnement : Linux x86-64 ; **LibreOffice 25.2.3.2 520(Build:2)** ; Pandoc 3.1.11.1 ; Python 3.13.5 ; python-docx 1.2.0 ; lxml 6.1.1 ; Matplotlib 3.10.8 ; NumPy 2.3.5 ; PyMuPDF 1.26.7. Les versions sont obtenues dans l’environnement d’exécution, non déduites des déclarations du candidat.

Trois chemins ont été exécutés avec des profils LibreOffice séparés :

1. **Reconstruction v0.3.1 depuis la source**, dans une copie du dossier : exécution de `build_manuscript.py`, puis export du nouveau DOCX en PDF.
2. **Export direct du DOCX v0.3.1 livré**, sans reconstruction intermédiaire du DOCX.
3. **Contrôle négatif avec le DOCX v0.3 livré** : export avec le même LibreOffice.

Les trois exports réussissent et produisent **42 pages**. Le contrôle négatif reproduit le marqueur `¿` à la page 30 et n’y contient aucun `#`. Les deux chemins corrigés contiennent chacun le `#` attendu et ne contiennent ni ce marqueur ni le caractère de remplacement Unicode `�`.

La couverture reconstruite et les pages 30 corrigée et témoin ont été inspectées en images. Dans la version corrigée, le symbole `#`, les accolades et la fraction `1/Q` sont lisibles ; le marqueur rouge a disparu. La page 30 du PDF canonique a également été inspectée. Cette lecture visuelle complète la recherche de caractères : une absence de marqueur textuel n’est pas, à elle seule, une preuve de rendu correct.

## 5. Comparaisons de rendu et absence de régression

Les comparaisons automatisées couvrent **toutes les pages à 108 dpi**, avec le même moteur de rasterisation :

| Comparaison | Résultat |
|---|---|
| PDF reconstruit depuis la source v0.3.1 / PDF obtenu par export direct du DOCX v0.3.1 | **42 pages identiques en pixels et en texte extrait** |
| Reconstruction corrigée v0.3.1 / export témoin v0.3 sous LibreOffice 25.2 | Seules les **pages 1 et 30** diffèrent ; les 40 autres pages sont identiques |
| PDF canonique livré v0.3.1 / PDF canonique livré v0.3 | Seule la **couverture** diffère ; les 41 pages suivantes sont identiques |

La modification de page 1 correspond à l’identification de l’édition. La modification de page 30 dans la comparaison avec le contrôle négatif correspond à la réparation attendue.

Le PDF canonique, produit dans l’environnement du candidat, **n’est pas pixel-identique** à notre export LibreOffice 25.2 : 38 pages présentent des différences de rendu et d’extraction de texte entre ces moteurs. Cela n’est pas présenté comme une identité binaire ou visuelle. La non-régression est établie séparément à moteur constant, et les objets mathématiques natifs sont comparés indépendamment. L’inspection visuelle manuelle de ce contrôle reste ciblée sur la couverture et la page litigieuse ; elle n’est pas un nouvel examen typographique à fort grossissement de chaque page du volume.

Empreintes des exports de contrôle :

| Export | SHA-256 |
|---|---|
| Reconstruit depuis la source corrigée | `78812f1dcbb6268fd3c374186f8a4a69578f435b6856f706b8f0cad0fa3e886e` |
| Export direct du DOCX corrigé | `580cf28b60e05170f2a004d3b3fdbf29b35c4e436f63748a49d4be3ba69d4e3a` |
| Contrôle négatif, DOCX v0.3 | `8288594cc5bcaab307052702f3a1b8af988961afbefb31fed7c9dc2ba3274d1d` |

Même les deux premiers fichiers, identiques en texte et pixels au niveau vérifié, ont des empreintes binaires différentes. Ces PDF sont des **pièces de contrôle**, pas des éditions substituées aux fichiers canoniques du candidat.

## 6. Tableau de fermeture

| Contrôle | Statut |
|---|---|
| Manifestes et identification canonique | PASS |
| Correction fonctionnelle limitée à T2-E01 | PASS |
| Corps scientifique, programmes et résultats inchangés | PASS |
| Conservation des 1 063 objets mathématiques | PASS |
| Reconstruction sous LibreOffice 25.2.3.2 | PASS |
| Export direct du DOCX livré | PASS |
| Reproduction de l’ancien défaut comme contrôle négatif | PASS |
| Signe `#`, accolades et absence du marqueur rouge | PASS |
| Pagination et non-régression à moteur constant | PASS |
| **T2-E01** | **CLOSED** |

## 7. Pièces jointes et conclusion

Le ZIP de vérification contient les trois programmes de contrôle, les commandes, l’environnement, les journaux, les différences de source et de générateur, les résultats JSON, les images de contrôle et les trois PDF exportés. Le paquet reçu est conservé pour permettre la reproduction des comparaisons. Un manifeste SHA-256 identifie les pièces du dossier.

Aucune preuve nouvelle n’est déduite d’un simple `PASS` fourni par l’auteur. La fermeture repose sur les comparaisons et exports exécutés dans ce contrôle. Il n’a été fait ni compilation LaTeX indépendante, ni nouvel audit bibliographique, ni nouvelle campagne scientifique : ces opérations ne sont pas nécessaires pour la réserve documentaire isolée, en l’absence de changement scientifique.

**Décision finale : TAMPON PARTIE II V0.3.1 ACCORDÉ.** La réserve T2-E01 est levée. La validation est limitée au périmètre identifié ; elle ne vaut pas tampon de la thèse complète ou des chapitres à venir.
