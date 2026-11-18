# Contre-audit de la Partie IV — chapitres 9–10 et annexe D

**Manuscrit :** *Rounding and Statistical Simulation*, Samir Bouftass et ChatGPT (OpenAI).  
**Soumission :** version 0.5, 17 novembre 2026.  
**Édition livrée après intégration directe :** version 0.5.1, même date, 75 pages.  
**Périmètre nouveau :** chapitres 9–10, annexe D, références [10]–[11], calculs associés et fidélité des exports.  
**Décision : TAMPON PARTIE IV ACCORDÉ DANS L’ÉDITION CORRIGÉE 0.5.1.**

Aucune correction obligatoire ne reste ouverte. Le fond mathématique résiste à la lecture contradictoire, aux calculs rationnels indépendants et aux contrôles numériques exécutés. Deux améliorations ont été directement intégrées : compatibilité des symboles double barre dans l’export et renforcement du test de régression de l’exemple nouveau. Ni les théorèmes, ni leurs preuves, ni les tableaux scientifiques n’ont été modifiés. La source scientifique ne diffère de la soumission que par son numéro de version.

Le présent tampon est un verdict de contrôle mathématique dans un périmètre défini. Ce n’est ni une certification formelle par assistant de preuve, ni une décision universitaire, ni une certification de sécurité cryptographique ou de priorité universelle. Le chapitre 11 et la synthèse finale ne sont pas approuvés ici.

## 1. Corpus, intégrité et indépendance

Les deux manifestes SHA-256 de la mission et du manuscrit soumis ont été contrôlés avant toute reconstruction : aucun échec. Les originaux sont conservés sans modification. Le programme indépendant ne lit aucun JSON fourni et n’importe aucune routine scientifique de l’auteur. Le test de l’échantillonneur importe volontairement l’échantillonneur à tester ; il est séparé de la reconstruction scientifique indépendante.

Les sections des chapitres 1–8 ont été comparées à la source effectivement approuvée v0.4.1, et non seulement à une déclaration de l’auteur. Leur empreinte de section est inchangée : `8ace045f28672c565a0f1e330b665949b3d5cbdd107eacac54404ea7a9e6d7b3`. Il en va de même des annexes A–C : `4d58cd3c594a80a5ad74b97e9211aed6e235f2bf54958fe5815b75958532f2d1`. Les anciennes campagnes scientifiques n’ont pas été relancées : la vérification nouvelle concerne la Partie IV et la reconstruction du document cumulatif.

### Empreintes des documents

| Pièce | SHA-256 |
|---|---|
| Source Markdown soumise v0.5 | `6f7e2676e91f637d00ba0788cf9f612f421aa5b41dd1a1a34487f3fc00eb497c` |
| PDF soumis v0.5 | `aabdbe1fc66dfd4f3a9df0cb85d80c1c2a8d521413b508e7f7edb2fd2270986a` |
| DOCX soumis v0.5 | `0659d6085a74f60dd5bfa1afe3aa1a5cd79ff8655655cf4052083f5f9a68ac38` |
| Source Markdown livrée v0.5.1 | `faa0065e343f728394a4841b82b8c967f8b6eb9ad4ca54c05c8255c3a94c6406` |
| PDF livré v0.5.1 | `b4e922ff5f9f9673961c71b29c9d637337ec7787c7a8a8101dc2462dece92de3` |
| DOCX livré v0.5.1 | `5952edf839324b34bb33787abaf1eaf42c70c36775d792798623a961e7fa2382` |

Les empreintes complètes des exports, scripts et preuves sont dans les manifestes et `RELEASE_INFO.json`. Les rapports antérieurs servent à délimiter le corpus déjà examiné, jamais à démontrer un résultat nouveau.

## 2. Les douze contrôles demandés

| Contrôle | Statut final | Passage et justification |
|---|---|---|
| T4-R01 | PASS | §9.1–9.2 : état partagé uniforme, bruits indépendants, hypothèses de parité et de taille, accès hors ligne, fraîcheur et vues retenues explicitement distingués. Encodage binaire vérifié aussi pour L impair. |
| T4-R02 | PASS | §9.3 : Q−2 intérieurs, quatre états de bord distincts, vraisemblances et lois reconstruites ; dominance non stricte au cas limite et stricte à k≥2 correctement employées. |
| T4-R03 | PASS | §9.4 : orientation unique même à L=3 et au raccordement cyclique ; deux états, support commun singleton, distance et comptage exacts. Choix de loi à égalité effectué pour tout le bloc. |
| T4-R04 | PASS | §9.5–9.6 : optimum obtenu par somme des minima conditionnels ; petites valeurs, borne exponentielle et limite des pièces indépendantes correctes. Deux contrôles exclus réfutent l’extrapolation hors domaine. |
| T4-R05 | PASS | §9.7–9.8 : exactitude publique du posterior et facteur deux par convexité ; poids entiers et temps polynomial espéré justifiés. Le sampler livré a été testé par parcours exact de ses branches. |
| T4-R06 | PASS | §10.1–10.3 : masses des observations, lois conditionnelles, six erreurs publiques et comportement sur observations impossibles recalculés depuis la loi jointe. |
| T4-R07 | PASS | §10.4 : optimalité de chaque ligne nécessaire ; famille mixte complète, bornes simultanées et seuil vérifiés. Aucune compensation entre lignes ne permet de contourner une borne. |
| T4-R08 | PASS | Théorème 10.3 : séparation exacte de l’objectif pondéré, atteinte simultanée, masses et poids nuls traités. 1 600 cas généraux rationnels indépendants corroborent l’identité. |
| T4-R09 | PASS | §10.5–10.6 : deux seuils, trois régimes, fractions 73/832 et 77/416, distances intermédiaires et frontière de compromis vérifiés indépendamment. |
| T4-R10 | PASS | §10.7 et §10.1 : support 3L, distance des sources, test d’égalité et convention d’avantage corrects ; aucune confusion avec une attaque ou une réduction de difficulté. |
| T4-R11 | PASS | Annexe D : campagnes fournies reproduites ; reconstruction indépendante des lois, optimisation rationnelle et LP séparés ; résultats et limites détaillés ci-dessous. |
| T4-R12 | PASS après correction | Autonomie, références nouvelles, invariance antérieure et exports contrôlés. T4-E01 corrigée directement ; 75 pages rendues et inspectées, 1 800 objets mathématiques conservés. |

## 3. Reconstruction des arguments scientifiques

### 3.1 Optimum fort pour les blocs

L’expérience conserve le vrai état Z et le vrai bloc Y. Conditionner sur leur valeur donne un objectif de la forme somme_y somme_z w(z,y) Δ(μ(z,y),K_y). Les lignes du noyau sont libres indépendamment, mais les contributions des états dans une même ligne ne peuvent pas être fusionnées avant la norme. C’est précisément ce qui distingue ce problème du rééchantillonnage public.

Pour un bloc constant, les Q−2 états intérieurs contribuent la même loi uniforme U_k, chacun de vraisemblance un. Les deux extrémités intérieures ont chacune vraisemblance (3/4)^k et des lois produits complémentaires de paramètre 2/3. Les voisins extérieurs ont vraisemblance (1/4)^k et des lois ponctuelles. La somme des poids autres que U_k est au plus deux, donc au plus Q−2. L’inégalité triangulaire établit l’optimalité de U_k. Lorsque Q=4 et k=1, cette preuve ne donne pas l’unicité ; le texte ne la revendique pas. Pour k≥2, la somme est au plus 5/4, et l’unicité requise au chapitre 10 est acquise.

Sur un bloc mixte, les états possibles sont les deux côtés d’une frontière. Une paire de cellules distinctes a une orientation cyclique unique pour L≥3, y compris L=3. Au raccordement vers zéro, l’état inférieur vaut P−1 et reste impair. Avec ℓ occurrences dans la cellule inférieure et r dans la supérieure, les vraisemblances sont 3^ℓ/4^k et 3^r/4^k. Les supports des deux lois de bits se rencontrent uniquement au vecteur ayant des uns sur les premières positions et des zéros sur les secondes. Les masses communes sont (2/3)^ℓ et (2/3)^r ; leur minimum donne la distance 1−(2/3)^max(ℓ,r).

Pour deux lois de poids a,b, l’objectif minimal vaut min(a,b) fois leur distance. La loi de plus grand poids l’atteint. À égalité, une mixture choisie une seule fois pour le bloc convient. Multiplier par la probabilité de chaque observation et compter L fois le coefficient binomial fournit exactement M_k. Les autres observations sont impossibles. On obtient ainsi δ*_k=C_k+M_k, sans recours aux sorties des programmes.

Les valeurs δ*_1=1/(2Q) et δ*_2=7/(16Q), ainsi que l’indépendance en L, suivent des facteurs L/P=1/Q. La borne exponentielle annoncée utilise S_k≤1, min(ℓ,k−ℓ)≤k/2 et la somme binomiale 2^k ; ses bases sont strictement inférieures à un. Elle prouve la convergence, non une affirmation générale de monotonie ou de sécurité.

### 3.2 Pièces indépendantes, posterior et coût

Au bord, les quatre catégories sont une relabellisation bijective de la paire observation/bit. Les masses réelles sont (1/2,1/4,1/4,0), et celles du simulateur indépendant (3/8,3/8,1/8,1/8). La somme multinomiale de leur masse commune est correcte. La quatrième catégorie donne une distance au moins 1−(7/8)^k ; après multiplication par la proportion 2/Q des états de bord, la limite vaut 2/Q. Le test utilise l’état : ce n’est pas une attaque publique.

Le posterior est par définition exact pour (Y,B). Pour la vue forte, sa distance à une ligne optimale est au plus la moyenne des distances des composantes à cette ligne. Une seconde application de l’inégalité triangulaire donne δ*≤δ(posterior)≤2δ*. Aucune optimalité forte du posterior n’en découle.

Le choix des cinq classes de poids (Q−2)4^k,3^k,3^k,1,1 sur un bloc constant, et des deux poids 3^ℓ,3^r sur un bloc mixte, reproduit les bonnes mixtures. Les entiers ont une longueur O(k+log Q). Le rejet pour tirer un tiers exact et le rejet pour tirer un entier borné terminent presque sûrement et ont une espérance bornée par tentative. La complexité annoncée est en espérance, avec coûts binaires explicités. Le texte décrit le sampler posterior ; le sampler exécutable spécifiquement livré et testé est celui du noyau fort optimal. La démonstration à graine fixe ne constitue pas une source cryptographique d’aléa.

### 3.3 Tous les optimiseurs forts à deux observations

Les lignes constantes sont uniformes par stricte dominance. Elles imposent une erreur publique réelle 1/(8Q). Pour une paire mixte, l’égalité dans l’inégalité triangulaire L1 exige que chaque coordonnée de la ligne soit entre celles des deux lois extrêmes. Dans l’ordre orienté du manuscrit, cela donne exactement (t,0,2/3,1/3−t), 0≤t≤1/3.

La masse commune avec U_2 vaut min(t,1/4)+1/4+min(1/3−t,1/4), au plus 7/12. La distance est donc au moins 5/12. Le poids nul total 2/L des paires mixtes impose ε0≥5/(6L). La valeur équilibrée t=1/6 atteint simultanément les deux bornes. Sur les observations impossibles dans le réel, un autre choix ne peut qu’ajouter du coût nul. Le seuil comparant la somme minimale forte avec celle des pièces indépendantes est bien L<8Q/3.

### 3.4 Nouveau théorème public pondéré

À observation y fixée, les poids sont a_y dans le réel et λb_y dans le nul. La perte vaut

`a_y Δ(ν_y,K_y) + λ b_y Δ(ω_y,K_y)`.

L’inégalité triangulaire donne le minimum `min(a_y,λb_y) Δ(ν_y,ω_y)`. Choisir la loi du poids le plus grand l’atteint. Les lignes étant indépendantes, les minima se somment. Si les deux poids sont nuls, la contribution est nulle pour toute ligne ; si un seul est nul, reproduire l’autre loi suffit. La preuve du théorème 10.3 est complète et ne dépend ni d’une dualité non démontrée ni d’un ancien tampon.

Pour le modèle répété, a_c=(Q−3/4)/(LQ), a_m=3/(8LQ), b=1/L², d_c=1/(8Q−6) et d_m=5/12. Les seuils sont λ_m=3L/(8Q) et λ_c=L(1−3/(4Q)), avec λ_m<λ_c dans le domaine. À λ=1, a_c>b puisque L(1−3/(4Q))≥39/16. Il faut donc reproduire le posterior sur les lignes constantes. Sur les lignes mixtes, le choix dépend du signe de 3L−8Q. On obtient

`inf_K (ε1+ε0) = 1/[L(8Q−6)] + min{5/(16Q), 5/(6L)}`.

Cette identité optimise sur tous les noyaux admissibles, sans contrainte d’optimalité forte. Elle n’est pas une simple comparaison de trois choix préexistants.

### 3.5 Exemple exact et frontière

Pour P=16, Q=L=4, la reconstruction indépendante donne :

| Noyau | Erreur forte | Erreur publique réelle | Erreur publique nulle | Somme publique |
|---|---:|---:|---:|---:|
| Pièces indépendantes | 11/64 | 7/64 | 0 | 7/64 |
| Équilibré fort | 7/64 | 1/32 | 5/24 | 23/96 |
| Posterior | 51/416 | 0 | 17/78 | 17/78 |
| Optimal pour la somme | 77/416 | 5/64 | 1/104 | 73/832 |

Les distances conditionnelles 1/26,41/234,19/26 et la contribution constante 19/208 sont retrouvées directement. Les deux segments inférieurs de la figure sont atteints par mixtures de lignes ; les poids supports 13/4 et 3/8 en certifient la borne inférieure. Dix points rationnels de ces segments ont été recalculés. L’optimiseur fort équilibré est au-dessus : optimiser la vue forte et optimiser la somme publique sont réellement deux questions distinctes.

À la frontière 3L=8Q, des mixtures non triviales de poids 1/7 et 1/2, ainsi que les deux extrémités, sont contrôlées. Pour (L,Q)=(16,6), leur somme commune est 3/56 ; pour (32,12), elle vaut 19/720. Aucun choix arbitraire au seuil n’est traité comme une unicité.

Le calcul de Δ(D1,D0) additionne les différences positives : les constantes ont toujours un excès réel, les mixtes ont un signe déterminé par 3L−8Q, et les observations impossibles ont un déficit. La formule du §10.7 et le test 13/16 contre 1/3 pour L=3,Q=4 en résultent. Une borne de somme d’erreurs reste une borne additive pour un test composé, pas l’avantage réel d’un adversaire.

## 4. Contrôles effectivement exécutés

### 4.1 Reproduction fournie

La commande `python3 scripts/reproduce_part_iv.py --out <dossier neuf>` a été exécutée sur le corpus soumis, puis sur le corpus corrigé. Les deux exécutions terminent avec succès.

La première campagne couvre 24 cas exacts : 76 440 tuples état/bruits pondérés et 33 936 atomes non nuls. L’optimiseur séparé exécute 182 problèmes conditionnels et 60 optimisations secondaires, soit 242 appels au solveur. Le programme nouveau reconstruit 28 domaines à deux observations, 44 160 tuples de bits de bruit, 217 objectifs pondérés, 1 104 lignes d’égalité et 836 LP ponctuels.

Les trois sorties `exact_results.json`, `lp_results.json` et `two_worlds.json` sont identiques octet pour octet aux résultats soumis. Le fichier `validation.json` diffère seulement par la version de Python de l’environnement, 3.12.14 contre 3.13.5. Après T4-E02, les quatre sorties sont identiques à la première réexécution dans ce même environnement. Les domaines se recouvrent : leurs nombres de tuples ne sont pas additionnés comme autant d’observations distinctes.

### 4.2 Implémentation indépendante

`independent_audit.py` reconstruit les lois depuis les transitions d’une observation, puis leurs produits conditionnels, avec `fractions.Fraction`. L’optimum conditionnel fort n’est pas obtenu en insérant la formule du manuscrit : le programme minimise une somme de fonctions convexes affines par morceaux sur le simplexe. Pour chaque coordonnée, il construit les points de rupture et les pentes exactes, puis alloue la masse unité dans l’ordre croissant des pentes. La monotonie des pentes par coordonnée garantit une allocation admissible ; l’objectif est recomputé à partir de la loi trouvée et comparé au coût des segments.

La campagne forte comprend 20 domaines : (P,Q)=(12,4),(16,4),(18,6),(24,8),(20,4), avec k=1,…,4. Elle résout 468 lignes conditionnelles exactement. Le contrôle public porte sur 33 domaines, dont Q=10 et des valeurs de L absentes de la campagne de l’auteur ; 293 objectifs pondérés, 78 784 optimisations rationnelles de lignes et 1 440 lignes d’égalité sont vérifiés. Une grille supplémentaire de 1 600 problèmes généraux à deux lois, dont 700 avec au moins un poids nul, contrôle le théorème 10.3 indépendamment de l’arrondi.

Au total, 1 447 LP supplémentaires corroborent les optima. L’écart maximal observé d’objectif et le résidu maximal contrôlé valent chacun environ 1,11×10⁻¹⁶, avec tolérance de comparaison 10⁻⁹. Ces LP sont numériques, non des certificats symboliques. Les solutions rationnelles et les démonstrations sont distinguées de cette confirmation.

Les deux contrôles exclus sont également recalculés exactement. Pour (P,Q,k)=(6,2,2), le vrai optimum vaut 29/144, contre 7/32 pour la formule étendue abusivement. Pour (8,4,2), il vaut 11/64, contre 7/64. Ces différences ne réfutent pas le théorème dans son domaine ; elles confirment l’importance de ses hypothèses.

### 4.3 Test exact du sampler

`sampler_probe.py` explore les branches de l’échantillonneur livré, avec masses rationnelles. Le rejet des trits est traité par sa série géométrique, qui donne exactement 1/3 à chaque valeur acceptée. Une seconde exécution de chaque branche force deux rejets avant chaque trit accepté. Les lois finales coïncident dans les deux chemins et avec la construction attendue.

Le contrôle couvre 1 240 blocs, 37 328 feuilles de parcours, 66 blocs cycliques, 96 ex æquo et 928 motifs impossibles dans le réel ; huit entrées invalides sont rejetées. Ce n’est pas un contrôle de fréquences empiriques. Il reste fini et ne se substitue pas à la preuve de la construction pour tous les paramètres.

## 5. Corrections intégrées et fermeture

### T4-E01 — Export des caractères double barre : CLOSED

**Localisation :** `build_manuscript.py`, `tools/check_document.py`, puis DOCX/PDF cumulatif.  
**Nature :** fidélité documentaire, sans changement de résultat.

Le PDF soumis affiche correctement les symboles. En revanche, LibreOffice 25.2.3.2 perd la propriété double barre de certains objets OMML pourtant correctement balisés. L’ancien contrôle générique, centré sur les marqueurs d’erreur, ne détectait pas ce changement silencieux. Trente occurrences sont concernées : 28 symboles ℤ, un ℝ et un 𝔼. Les variables ordinaires Z,R,E ne doivent pas être transformées.

Le correctif n’agit que sur les runs explicitement marqués `double-struck`, remplace leur lettre par le caractère mathématique Unicode équivalent et le marque littéral. Les équations restent natives et éditables. Le garde documentaire compte désormais les caractères attendus dans le DOCX et vérifie leur présence dans le PDF. Ce garde renforcé échoue sur la reconstruction non corrigée et réussit sur la version finale.

Le document final comporte toujours 75 pages, 1 800 objets mathématiques natifs et 12 indices de partie positive. La suite normalisée des 1 800 objets est identique à celle du soumis. Le texte extrait est identique sur chaque page après les seules normalisations déclarées : espaces, numéro de version et représentations double barre/lettre. Cette comparaison n’est pas une revendication d’identité binaire des PDF.

Les 75 pages finales ont été rendues à 108 dpi et inspectées. Aucun défaut restant de troncature, chevauchement, symbole d’erreur, fraction, indice, tableau ou légende n’a été observé. Dans une comparaison en pixels avec la reconstruction non corrigée sous le même moteur, seules la couverture et les pages contenant les caractères réparés diffèrent. Les détails de toutes les pages modifiées figurent dans `final_preservation.json`.

### T4-E02 — Test de régression du nouvel exemple : CLOSED

**Localisation :** `scripts/verify_two_worlds.py`.  
**Nature :** renforcement préventif non bloquant de la vérification.

Le programme initial calculait l’erreur forte 77/416 sans assertion explicite à cet endroit et consignait certaines fractions publiques sous forme de chaînes littérales, alors que d’autres contrôles les vérifiaient. Le programme corrigé mesure directement l’erreur réelle et l’erreur nulle du noyau construit, puis impose l’égalité du quadruplet mesuré à `(77/416,5/64,1/104,73/832)`. Le JSON consigne les valeurs mesurées. Le résultat scientifique est inchangé, et la reproduction complète après correction réussit avec sorties identiques.

## 6. Autonomie, références et originalité bornée

Les définitions et arguments essentiels sont présents dans le volume. Les renvois aux chapitres 3,5,6 sont internes à un texte disponible ; aucun article compagnon ni document privé ne comble une preuve manquante. L’anglais est lisible et le vocabulaire privé est absent du corps scientifique.

Les deux références nouvelles ont été confrontées aux notices et résumés primaires accessibles le 17 novembre 2026. La notice arXiv `https://arxiv.org/abs/1402.4884v2` confirme van Rooyen et Williamson, le titre, et la révision du 21 février 2014. La notice éditeur associée à `https://doi.org/10.3982/ECTA17548` confirme Mu, Pomatto, Strack et Tamuz, *Econometrica* 89(1), 2021, pages 475–506, et le contexte de comparaison d’expériences répétées. Leur rôle est contextuel. Aucun théorème de dualité pour les noyaux restreints n’est importé de ces notices. Les neuf références antérieures n’ont pas fait l’objet d’un nouvel audit bibliographique complet.

Le théorème pondéré est une application d’un outil élémentaire de minimisation à deux lois, explicitement présenté comme tel. La contribution propre est sa spécialisation complète au modèle, ses seuils, ses exemples rationnels, et la séparation des objectifs publics et forts. La recherche bibliographique n’est pas une recherche systématique de priorité ; aucune première universelle n’est certifiée. Les preuves ne revendiquent ni cryptosystème, ni réduction LWE, ni niveau de sécurité.

## 7. Fabrication, environnement et limites de la décision

Environnement exécuté : Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, Matplotlib 3.10.8, ReportLab 4.4.9, python-docx 1.2.0, PyMuPDF 1.26.7, Pandoc 3.1.11.1 et LibreOffice 25.2.3.2. Les journaux enregistrent les chemins et commandes réellement utilisés. Les exemples de relance portables sont dans le README des preuves.

Le DOCX, le HTML et le LaTeX ont été régénérés depuis la source corrigée. Le PDF livré provient de la conversion du nouveau DOCX, puis du contrôle visuel et automatique. L’export LaTeX n’a pas été compilé. Aucun examen n’est revendiqué sous Microsoft Word ni sous tous les moteurs possibles. Les fichiers de polices ne sont pas distribués.

Les correctifs sont fournis en diff. L’archive d’origine est conservée dans `ORIGINAL/`. Les validations antérieures de l’auteur sont conservées séparément des nouveaux fichiers `reviewer_*`. Les résultats exacts, les résultats numériques et les images de contrôle sont identifiés distinctement. Les programmes finis ne prouvent pas des quantificateurs illimités ; le verdict repose aussi sur l’examen direct des démonstrations.

## 8. Décision de remise

**Science : PASS. Reproductibilité : PASS dans l’environnement décrit. Autonomie : PASS. Originalité : contribution spécialisée, sans revendication générale de priorité. Corrections T4-E01 et T4-E02 : CLOSED.**

**TAMPON ACCORDÉ — Partie IV, édition corrigée 0.5.1.**

La rédaction peut continuer depuis la source livrée. Les approbations des parties I–III restent attachées à leur contenu inchangé ; le tampon nouveau couvre les chapitres 9–10 et l’annexe D. La synthèse du chapitre 11 et la lecture globale finale auront leur propre examen. Aucun travail ultérieur n’est engagé automatiquement par ce rapport.
