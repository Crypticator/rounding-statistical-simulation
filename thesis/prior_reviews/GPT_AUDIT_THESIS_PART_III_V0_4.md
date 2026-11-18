# Contre-audit et correction directe — Thèse, Partie III

**Date :** 17 novembre 2026.  
**Manuscrit :** *Rounding and Statistical Simulation*, Samir Bouftass et ChatGPT (OpenAI).  
**Entrée examinée :** version 0.4 ; **édition corrigée livrée :** version 0.4.1.  
**Périmètre nouveau :** chapitres 7–8, annexe C et références [8]–[9]. Le volume cumulatif comporte huit chapitres, trois annexes et 59 pages. Aucun chapitre 9 ou suivant n'est examiné ni validé ici.

## 1. Décision

**TAMPON ACCORDÉ À LA PARTIE III DANS L'ÉDITION CORRIGÉE 0.4.1.**

Les arguments généraux, les dénombrements, la distinction entre support atteignable et loi cible, les formules de rejet et les exemples résistent au contrôle. Les douze points de la mission sont clos dans le périmètre explicité ci-dessous. Aucun théorème, tableau scientifique ni programme scientifique de l'auteur n'a dû être modifié.

Une réserve documentaire a été trouvée lors de la reconstruction : **T3-E01**, rendu incorrect de cinq indices « + » de partie positive sous LibreOffice 25.2.3.2. Conformément à la demande expresse du commanditaire, le correctif a été intégré directement dans une nouvelle copie du constructeur, puis contrôlé et fermé. Aucun aller-retour de correction à l'auteur n'est nécessaire pour cette réserve. L'archive reçue et son contenu d'origine restent conservés sans modification.

Ce tampon est le verdict de ce contre-audit, pas une certification formelle par assistant de preuve, un arbitrage éditorial externe, une garantie de sécurité cryptographique ou une certification universelle de priorité scientifique. La thèse entière n'est pas déclarée achevée.

## 2. Identité des fichiers

| Pièce | SHA-256 |
|---|---|
| Archive de mission v0.4 | `0c9bff2ae8dbe8234aed134bb0f59200a4fee01ab136785cf1f4afc9ee4cba8e` |
| Markdown v0.4 | `97dd28689cb4393b32a418dc1daa20776ecbbbe79814709a88887a436b2f24b6` |
| PDF livré v0.4 | `93378bf9cb9bed36b715c555a34a5957a2942abe761a167932fc8dd1f36284e2` |
| DOCX livré v0.4 | `d7b2b8eb92e4db1bab9f7d9e54c0273305efb050eb8b43a29a6dd2adcdf9ef3b` |
| Markdown corrigé v0.4.1 | `0eac7aeb65c2b0dec9db4dfa58e2b6fd7e003736730757a4b50046a8a786756a` |
| PDF corrigé v0.4.1 | `ab72de29aeedb1129dc9e32f71399ce5fc07020d2075711209ed0c07013f14d3` |
| DOCX corrigé v0.4.1 | `2356a2696ab4a6201b63700524ccc27dc22b21edba0626a1edb678e8575bcb4c` |

Les deux manifestes d'entrée — paquet de mission et manuscrit — ont été contrôlés avant reconstruction ; les journaux ne signalent aucun échec. Les documents corrigés portent une identité distincte. Les manifestes de sortie sont régénérés après la rédaction des métadonnées et du présent rapport.

## 3. Matrice des douze contrôles

| Contrôle | Verdict | Passage et justification |
|---|---|---|
| T3-R01 | PASS | §7.1–7.3, pp. 38–40 : quantificateur universel conservé, translations des lignes négatives explicites, pas de transfert automatique aux supports restreints ; marginalisation du choix dépendant de Y correcte. |
| T3-R02 | PASS | §7.4, pp. 40–41 : multiensemble canonique complet ; facteur de signe par occurrence ; tailles et stabilisateurs retrouvés par images de groupe explicites. Exemple supplémentaire à stabilisateur 16. |
| T3-R03 | PASS | §7.5, pp. 41–42 : saturation, union appariée U/−U et test du support ; aucune hypothèse d'action libre ou d'images disjointes. |
| T3-R04 | PASS | §7.6, p. 42 : orientation suffixe/préfixe exacte, occurrences distinctes dans la récurrence ; contrôles sur 28 518 représentants d'orbites ; coût exponentiel annoncé correctement. |
| T3-R05 | PASS | §7.7–7.8, pp. 42–43 : renversement des lignes dans G, bijection Toeplitz/Hankel dans chaque orbite ; exemple de colonne A²=I vérifié modulo huit. |
| T3-R06 | PASS | Théorème 8.1, p. 44 : masses d'orbites nécessaires et suffisantes, construction au niveau des points ; sources ou cibles nulles traitées. |
| T3-R07 | PASS | §8.2–8.3, pp. 45–46 : majoration par les cosets de {I,−I}, condition seulement suffisante, cinq valeurs de table et quatre orbites d'excès recalculées. |
| T3-R08 | PASS | §8.4, p. 47 : capacités αq≤p, singleton nul, filtre identité ; extension aux lignes inversibles limitée au taux exact. |
| T3-R09 | PASS | Théorème 8.4 et corollaire 8.5, pp. 48–49 : allocation initiale, déficit et capacité restante ; distinction entre sorties hors cible permises et sorties obligatoirement Toeplitz. |
| T3-R10 | PASS | §8.6–8.8, pp. 49–51 : redémarrages indépendants, coût 1/α, convexité en B et non en α, cinq points du tableau, figure et filtrage sous indépendance A,S,E. |
| T3-R11 | PASS | Annexe C, pp. 56–58 : reproduction fournie complète ; implémentation indépendante sur huit domaines ; calculs rationnels séparés des optimisations flottantes. |
| T3-R12 | PASS après correction | Volume, source et exports inspectés ; reconstruction effective du DOCX/PDF ; T3-E01 corrigé et testé ; invariance des parties précédentes et références [8]–[9] contrôlées. |

## 4. Vérification des arguments mathématiques

### 4.1 Information disponible et invariants

L'argument affine antérieur porte sur tous les vecteurs d'entrée. Le §7.1 explique correctement pourquoi il ne classifie pas automatiquement des transformations sur un support plus petit de la forme As+e. Il identifie également l'erreur effective Ue+b : la symétrie d'une loi de bruit ne justifie pas à elle seule la translation nécessaire à une réflexion compatible avec l'arrondi.

Pour une loi fixée de (A,Y), la moyenne κ_A(U)=Σ_y Pr(Y=y|A)κ_{A,y}(U) est bien un noyau sur les opérations de lignes. Elle préserve la loi marginale de la matrice produite. Elle ne constitue pas une simulation de toute la vue secrète.

Le multiensemble des lignes modulo leur signe est un invariant complet : apparier chaque occurrence fournit une permutation, puis chaque signe peut être choisi séparément. Après placement des types, chaque occurrence non fixe admet deux orientations ; une occurrence fixe n'en admet qu'une. Le produit m!/(∏c_i!)·2^{r_0} ne doit donc pas être divisé une seconde fois pour les répétitions.

Contrôle supplémentaire : modulo huit, les quatre lignes (0,0),(0,0),(1,2),(7,6) donnent une orbite de 24 matrices. Le groupe comporte 384 opérateurs, d'où un stabilisateur de 16 éléments. Cet exemple contient à la fois des occurrences fixes répétées et un type non fixe répété.

La récurrence de recherche garde un sous-ensemble d'occurrences et la dernière ligne orientée. Ajouter une ligne dont le suffixe égale le préfixe de la précédente impose exactement les égalités diagonales Toeplitz. Les bornes O(2^m m²n) en comparaisons et O(2^m m) en états booléens sont des majorations correctes pour cette version directe ; les coûts en log P sont distincts. Aucune efficacité polynomiale en m n'est déduite.

### 4.2 Support, masses et rejet

Un convertisseur ne quitte jamais l'orbite d'entrée. La saturation donne donc exactement le maximum s_* de réussite dans le support. L'identité U𝒯=(−U)𝒯 permet de regrouper les opérateurs par paires, mais ne rend pas leurs images disjointes. La borne s_*≤min(1,2^{m−1}m!P^{−d}) est correctement utilisée comme majoration, pas comme formule exacte.

Toute loi conservant les masses d'orbites est réalisable : à partir de chaque entrée, on tire une destination avec la loi conditionnelle désirée dans son orbite, puis on choisit un opérateur qui l'atteint. Il en résulte δ_*=½Σ_O|p_O−q_O|. Dans une orbite où q_O=0, la masse p_O est placée arbitrairement ; dans une orbite où p_O=0, aucune masse ne peut être créée. Ces cas sont couverts par les preuves et les tests.

Pour le sous-groupe {I,−I}, l'orbite est couverte par h=2^{m−1}m! translatés de {T,−T}. Même lorsque T=−T, on conserve |O|≤h|O∩𝒯|. Ainsi P^d≥h implique p_O≤q_O sur les orbites accessibles. La réciproque n'est pas affirmée.

Le rejet exact impose αq_O≤p_O. Pour le singleton nul, p=1/N et q=1/t, donc α≤t/N=P^{−d}. L'acceptation de l'entrée uniquement lorsqu'elle est déjà Toeplitz atteint ce taux et produit exactement la cible uniforme. La même borne reste vraie pour toute opération de lignes inversible, parce qu'aucune entrée non nulle ne peut alors devenir nulle ; les autres formules ne sont pas transférées à ce groupe plus grand.

Pour une acceptation fixée, l'allocation initiale r_O=min(αq_O,p_O) laisse un déficit D=Σ(αq_O−p_O)_+. Les capacités restantes totalisent 1−α+D≥D. Ajouter la masse manquante là où une capacité subsiste n'introduit pas de nouveau déficit. La réalisation dans les orbites atteint donc

\[
\delta(\alpha)=\sum_O\left(q_O-\frac{p_O}{\alpha}\right)_+.
\]

Si chaque sortie acceptée doit être Toeplitz, seules les orbites accessibles sont utilisables. Leur capacité totale est s_*. La construction reste possible exactement pour 0<α≤s_*, avec le même optimum. Une valeur de la formule à α>s_* n'est pas présentée comme une sortie toujours structurée.

### 4.3 Exemple rectangulaire et limites de transfert

Pour P=4,m=3,n=2, les quatre orbites d'excès ont chacune taille 48 et deux cibles Toeplitz. Leur surplus p_O−q_O=1/256 produit au total 1/64. Les listes de représentants sont retrouvées exactement par l'énumération indépendante. Dans la première, l'ordre des types doit être c,b,a ; les deux seules orientations compatibles sont toutes positives ou toutes négatives, ce qui donne les deux cibles annoncées.

On obtient s_*=501/1024 et δ_*=539/1024, alors que 1−s_*=523/1024. Les cinq points de rejet sont :

| α | δ(α) | Sortie toujours Toeplitz possible ? |
|---|---|---|
| 1/16 | 0 | Oui |
| 1/8 | 1/256 | Oui |
| 1/4 | 1/16 | Oui |
| 1/2 | 139/512 | Non |
| 1 | 539/1024 | Non |

Le renversement des lignes est une involution autorisée qui relie chaque intersection Toeplitz à l'intersection Hankel de la même orbite. Il préserve donc les masses cibles, mais n'identifie pas les supports point par point. L'exemple A=((1,0),(2,3)) modulo huit ne peut devenir Toeplitz par permutation signée de lignes, alors que A²=I. Autoriser une multiplication à droite par A change donc bien la classe des opérations ; cela ne produit pas une loi Toeplitz uniforme.

Les redémarrages indépendants donnent Pr(J>k)=(1−α)^k et E[J]=1/α. La loi du premier échantillon accepté est la loi conditionnelle d'une seule proposition. La convexité affine par morceaux est correctement formulée en B=1/α : chaque terme (q_O−Bp_O)_+ est le maximum de deux fonctions affines. La figure montre le bon seuil 501/1024 et le coût exact 16. Le raisonnement n'exclut pas les procédures choisissant conjointement parmi plusieurs propositions.

Enfin, la projection vers la matrice fournit une borne inférieure pour une vue plus grande, pas une construction automatiquement correcte pour cette vue. Le cas positif du filtre identité est correctement limité à A,S,E indépendants et à une cible ne changeant que la loi de A.

## 5. Calculs réellement exécutés

### 5.1 Reproduction des programmes fournis

La commande `python scripts/reproduce_part_iii.py --out <répertoire neuf>` a terminé avec succès. Les trois JSON reproduits sont identiques octet pour octet aux fichiers fournis : `orbits.json`, `extensions.json`, `matrix_lp.json`. La même reproduction a ensuite été relancée depuis le paquet corrigé v0.4.1 dans un autre répertoire neuf : les trois fichiers sont de nouveau identiques, sans nouveau cas ajouté au décompte.

La campagne comporte 274 688 matrices denses dans cinq domaines, un contrôle supplémentaire de 12 544 matrices **déjà incluses** dans ces domaines, 900 allocations rationnelles générales et 600 allocations avec support obligatoire réalisables. Les 1 800 programmes numériques de partition incluent 300 infaisabilités attendues ; les six programmes sur matrices passent également. Les 1 806 appels numériques ne sont pas présentés comme des certificats symboliques. La tolérance annoncée est 10^{-8}.

Les campagnes des parties I–II n'ont pas été relancées : leurs sources, leurs programmes et leurs données ont été comparés aux fichiers v0.3.1 et restent inchangés.

### 5.2 Implémentation indépendante

`independent_audit.py` n'importe aucun programme scientifique de l'auteur et ne lit pas ses résultats. Il parcourt l'espace dense, prend chaque matrice non encore couverte, construit explicitement toutes ses images signées, puis teste les égalités Toeplitz et Hankel point par point. Le dénombrement des orbites est ensuite confronté à la formule, et non utilisé comme oracle de construction. Les résultats sont comparés aux cinq tables fournies seulement après cette reconstruction.

| P | Dimensions | Matrices couvertes | Orbites | s_* | δ_* |
|---|---|---:|---:|---|---|
| 4 | 2 × 2 | 256 | 55 | 39/64 | 25/64 |
| 4 | 2 × 3 | 4 096 | 666 | 211/1024 | 813/1024 |
| 4 | 3 × 2 | 4 096 | 220 | 501/1024 | 539/1024 |
| 4 | 3 × 3 | 262 144 | 8 436 | 4269/65536 | 61267/65536 |
| 8 | 2 × 2 | 4 096 | 595 | 399/1024 | 625/1024 |
| 4 | 4 × 2 | 65 536 | 715 | 3541/8192 | 4843/8192 |
| 16 | 2 × 2 | 65 536 | 8 515 | 3615/16384 | 12769/16384 |
| 4 | 2 × 4 | 65 536 | 9 316 | 947/16384 | 15437/16384 |

Total : **471 296 matrices distinctes dans huit domaines**, dont 196 608 dans trois domaines supplémentaires par rapport à la campagne de l'auteur. La récurrence de recherche est testée sur les **28 518 représentants d'orbites**, et non annoncée comme relancée séparément sur toutes les matrices. Les bijections Toeplitz/Hankel sont contrôlées pour toutes les intersections rencontrées. Les cinq tables originales concordent exactement.

Une seconde campagne indépendante construit 62 couples de lois sur six points, dont des zéros au niveau des points, des lois non uniformes au sein des blocs et un cas de supports d'orbites disjoints. Quatre taux donnent 248 problèmes, chacun sous deux conventions de support. Elle produit **475 réalisations rationnelles faisables** et établit **21 insuffisances de capacité** ; les **496 programmes linéaires point par point** confirment ces cas. L'écart maximal d'objectif est 1.12×10^{-16} et le résidu maximal contrôlé 2.23×10^{-16} (bornes arrondies vers le haut). L'optimisation flottante reste une corroboration distincte des constructions rationnelles et des preuves générales.

Les trois domaines supplémentaires ne sont pas incorporés aux tableaux de la thèse : ils figurent uniquement dans les preuves de cet audit. Aucune amplification de la contribution publique n'est revendiquée à partir de ces tests.

## 6. Correction directe T3-E01 — CLOSED

**Localisation :** constructeur DOCX, cinq indices de partie positive au §8.2, au §8.5 et au §8.6 ; pages 45, 48 et 49.

**Constat :** le PDF fourni par l'auteur compose correctement ces formules. Mais la reconstruction effective sous LibreOffice 25.2.3.2 transforme les indices « + » en opérateurs incomplets et produit dix marqueurs « ¿ » parasites dans le texte extrait, visibles en rouge sur les pages rendues. Les équations du DOCX restent des objets mathématiques natifs ; le problème est une incompatibilité d'import/export, pas un résultat faux.

**Correction intégrée :** le constructeur marque comme littéraux (`m:lit=1`) uniquement les runs constitués du signe « + » à l'intérieur d'un indice `m:sub` dont le contenu entier est « + ». Les additions ordinaires ne sont pas modifiées. Les correctifs antérieurs pour les astérisques, le cardinal # et les séparateurs optionnels de délimiteurs sont conservés.

**Contrôle après correction :**

- DOCX régénéré à partir de la source ; PDF réellement exporté et 59 pages rendues par `render_docx.py` à 120 dpi.
- Lecture visuelle de toutes les pages rendues, puis examen agrandi des trois emplacements corrigés ; aucun défaut supplémentaire de troncature ou de symbole n'a été constaté.
- 1 438 objets mathématiques natifs avant et après ; séquences de tokens mathématiques inchangées ; cinq indices « + » marqués littéraux.
- Aucun ancien marqueur d'erreur détecté dans le PDF corrigé.
- Comparaison pixel à pixel à 108 dpi avec **la v0.4 reconstruite dans le même environnement** : 55 pages identiques ; seuls changent la couverture (version) et les pages 45, 48, 49. Cette comparaison n'affirme pas l'identité binaire ou pixel du PDF corrigé avec le PDF livré par l'auteur dans un autre environnement.
- Le texte scientifique Markdown est identique à la v0.4, sauf l'étiquette de version en en-tête. Les chapitres 1–6 et annexes A–B sont également identiques à la v0.3.1 approuvée. Tous les programmes scientifiques et résultats fournis sont conservés octet pour octet.

Un garde-fou `tools/check_document.py` accompagne la nouvelle édition. Il détecte les cinq indices non protégés et les marqueurs dans l'ancienne reconstruction (contrôle négatif), puis renvoie PASS sur la nouvelle. Il ne remplace ni l'inspection visuelle ni une vérification mathématique.

## 7. Autonomie, références et originalité bornée

Les définitions, preuves et restrictions utiles aux nouveaux chapitres sont présentes dans le volume. Les rapports antérieurs sont des documents de suivi, pas des prémisses des théorèmes. Le texte est en anglais, sans jargon de campagne nécessaire à sa compréhension. Les calculs sur matrices ne sont pas présentés comme une réduction générale LWE, une certification de niveau de sécurité ou une impossibilité pour des transformations disposant d'autres ressources.

Les nouvelles références ont été vérifiées sur les pages primaires des actes PMLR et sur la première page de leurs PDF :

[8] Alexandre Verine, Muni Sreenivas Pydi, Benjamin Negrevergne et Yann Chevaleyre, *Optimal Budgeted Rejection Sampling for Generative Models*, AISTATS 2024, PMLR 238:3367–3375. Source primaire : https://proceedings.mlr.press/v238/verine24a.html . Le travail traite le rejet sous budget et l'optimalité pour des divergences ; il fournit un contexte légitime, sans être utilisé pour combler la preuve de capacité de la thèse.

[9] Adam Block et Yury Polyanskiy, *The Sample Complexity of Approximate Rejection Sampling With Applications to Smoothed Online Learning*, COLT 2023, PMLR 195:228–273. Source primaire : https://proceedings.mlr.press/v195/block23a.html . Le modèle décrit la sélection d'un échantillon parmi plusieurs tirages indépendants ; la distinction avec une proposition et ses redémarrages indépendants est justifiée. La page PMLR donne la pagination des actes ; le PDF est paginé intérieurement sur 46 pages.

La contribution est une spécialisation mathématique précise et utile : profils d'orbites de lignes signées, exemples de stabilisateurs, écart support/loi dans le cas rectangulaire, et interprétation des capacités de rejet pour cette conversion. Les principes généraux de variation totale et de capacités ne sont pas annoncés comme une découverte générale. La vérification bibliographique a été ciblée sur les références citées ; aucune recherche systématique de priorité universelle n'est revendiquée.

## 8. Reproduction du contrôle et remise à l'auteur

Depuis le dossier du manuscrit corrigé :

```sh
sha256sum -c SHA256SUMS
python3 scripts/reproduce_part_iii.py --out fresh_part_iii
python3 build_manuscript.py
soffice --headless --convert-to pdf --outdir deliverables \
  deliverables/THESIS_Rounding_Statistical_Simulation_v0_4_1.docx
python3 tools/check_document.py \
  --docx deliverables/THESIS_Rounding_Statistical_Simulation_v0_4_1.docx \
  --pdf deliverables/THESIS_Rounding_Statistical_Simulation_v0_4_1.pdf \
  --expected-pages 59
```

Depuis le dossier de preuves :

```sh
python3 independent_audit.py --out fresh_independent
```

Les sorties doivent être neuves. Le contrôle indépendant nécessite NumPy et SciPy pour ses programmes linéaires ; les calculs de matrices et les certificats d'allocation utilisent des entiers et fractions exactes. Le contrôle documentaire nécessite PyMuPDF. Les versions réellement utilisées figurent dans `environment.json`. Une pagination différente avec un autre moteur doit être examinée ; elle n'est pas, à elle seule, une réfutation scientifique.

**Conclusion de remise :** édition 0.4.1 corrigée, fichiers régénérés, réserve T3-E01 fermée, tampon Partie III accordé. L'auteur peut poursuivre le plan de rédaction sans refaire ces chapitres. Le prochain contenu devra recevoir son propre examen ; la présente correction n'engage aucun chapitre supplémentaire.
