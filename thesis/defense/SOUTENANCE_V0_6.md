# Préparation de la soutenance de Rounding and Statistical Simulation

**Samir Bouftass et ChatGPT (OpenAI) — édition v0.6 — 18 novembre 2026**

Ce document prépare une discussion scientifique de la thèse en onze chapitres. Il organise l'exposé et les réponses possibles à partir des résultats du manuscrit. La soutenance reste à tenir ; le tampon interne déjà obtenu ne constitue pas son déroulement ni son verdict.

## Ouverture proposée

Nous étudions ce qu'une procédure peut calculer ou simuler après un arrondi modulaire. L'arrondi conserve une cellule et efface une position dans cette cellule. Notre question dépend alors de quatre choix : l'information disponible, la loi de l'expérience, les transformations autorisées et les variables dont on doit conserver la loi jointe.

La thèse donne des classifications et des erreurs optimales dans quatre familles précises. Elle distingue la factorisation déterministe, la simulation de canaux bruités, la conversion de lois matricielles et la simulation d'observations répétées. Sa contribution réside dans les calculs explicites, les cas limites et les séparations entre objectifs, avec des preuves contenues dans le volume.

## Déroulement proposé en quinze minutes

| Durée indicative | Passage | Message et appui |
|---|---|---|
| 2 minutes | Chapitres 1–3 | Définir observation, cible et vue conservée. Expliquer le critère des fibres. |
| 2 minutes | Chapitre 4 | Présenter la classification affine et les alignements indispensables. |
| 2 minutes | Chapitres 5–6 | Montrer pourquoi une simulation marginale exacte peut échouer sur la loi jointe. |
| 3 minutes | Chapitres 7–8 | Expliquer les masses d'orbites et le compromis entre rejet et erreur. |
| 3 minutes | Chapitres 9–10 | Distinguer optimum fort et optimum public dans deux expériences. |
| 2 minutes | Chapitre 11 | Délimiter la portée, la complexité et les prolongements. |
| 1 minute | Conclusion | Rappeler les résultats établis et ouvrir les questions du jury. |

Les durées sont une proposition d'organisation de l'exposé, pas un horaire imposé.

## Premier résultat à défendre la classification affine

Posons $P=LQ$, avec $L,Q\ge2$, et $F(x)=\lfloor[x]_P/Q\rfloor$, appliqué coordonnée par coordonnée. Sur le domaine complet $\mathbb Z_P^m$, l'identité

$$F(Uz+b)=g(F(z))$$

est possible exactement lorsque chaque ligne de $U$ est nulle, ou sélectionne une seule coordonnée avec coefficient $+1$ ou $-1$. Pour $+1$, la translation vérifie $b_i\equiv0\pmod Q$ ; pour $-1$, elle vérifie $b_i\equiv Q-1\pmod Q$. Une ligne nulle permet toute translation. Plusieurs lignes peuvent sélectionner la même colonne.

**Idée de preuve.** La cible doit être constante sur chaque fibre de $F$. On fait varier un reste à la fois dans la cellule zéro ; le lemme scalaire impose les coefficients et les alignements. Deux coefficients de même signe créent une retenue variable ; deux signes différents imposent des alignements incompatibles. Les lignes restantes donnent directement la fonction cherchée. La surjectivité de $F$ assure son unicité. Le cas carré inversible force une permutation signée ; si $b=0$, les signes négatifs sont exclus.

**Point à préciser au jury.** La classification utilise le domaine complet. Restreindre les entrées peut changer la réponse. Elle ne repose sur aucune hypothèse de difficulté algorithmique.

## Deuxième résultat à défendre le rôle de la loi jointe

Le bruit à trois points a les probabilités $(\eta,1-2\eta,\eta)$ sur $-1,0,1$, avec $0\le\eta\le1/4$. Hors du cas singulier, l'opérateur de bruit est inversible et la simulation exacte à chaque état ramène à la compatibilité déterministe. Lorsque $P$ est pair et $\eta=1/4$, le coefficient affine $c=P/2$ produit une loi cible équitable sur deux valeurs, indépendante de l'état.

Cette exactitude concerne la vue état–cible. Elle ne suffit pas à reproduire l'observation réellement obtenue et sa corrélation avec la cible. Avec un état uniforme et $Q$ pair, l'erreur optimale conservant $(Z,Y,W)$ au point singulier vaut $1/(2Q)$. Le théorème 6.3 donne cette valeur ; l'exemple du §6.6 compare plusieurs vues du même modèle.

**Idée de preuve.** La convolution annule le mode alternant. La cible devient équitable à chaque état, mais les observations aux frontières des cellules renseignent sur le pas de bruit. Une nouvelle pièce équitable ne restitue pas automatiquement cette dépendance. L'objectif se décompose conditionnellement à l'observation.

## Troisième résultat à défendre les capacités des orbites

Pour une action finie autorisée, notons $p_O$ et $q_O$ les masses de l'orbite $O$ dans les lois source et cible. Toute sortie reste dans l'orbite de son entrée. Sans rejet,

$$\delta_* = \frac12\sum_O |p_O-q_O|.$$

Avec un taux d'acceptation fixé $0<\alpha\le1$, en autorisant des sorties acceptées hors du support cible,

$$\delta(\alpha)=\sum_O\left(q_O-\frac{p_O}{\alpha}\right)_+.$$

**Idée de preuve.** La projection sur l'indice d'orbite donne la borne inférieure. L'égalité est atteinte en reproduisant les lois conditionnelles cibles à l'intérieur des orbites. Avec rejet, la masse acceptée dans $O$ est bornée par $p_O$ ; après conditionnement, la capacité est $p_O/\alpha$. Les déficits qui dépassent ces capacités donnent l'erreur optimale.

Dans la spécialisation dense uniforme vers Toeplitz uniforme, $P=2^p$, $p\ge2$, $m,n\ge2$, et les transformations sont les permutations signées des lignes. La conversion exacte a pour taux maximal

$$\alpha_{\mathrm{exact}}=P^{-(m-1)(n-1)}.$$

L'orbite de la matrice nulle donne la borne supérieure. Accepter une matrice source si elle est déjà Toeplitz l'atteint. Si toute sortie acceptée doit être Toeplitz, la formule d'erreur s'applique seulement aux taux réalisables $\alpha\le s_*$.

**Point à préciser au jury.** Atteindre un élément du support ne garantit pas la bonne distribution sur ce support. Le calcul d'un invariant pour une matrice ne résout pas nécessairement le comptage de toutes les masses d'orbites.

## Quatrième résultat à défendre les objectifs de simulation répétés

Le modèle des chapitres 9–10 fixe un état uniforme commun, des bruits indépendants de paramètre $\eta=1/4$, $Q\ge4$ pair et $L\ge3$. Le simulateur peut lire tout le bloc avant de produire ses bits.

Le théorème 9.1 donne l'optimum de la vue complète pour tout $k\ge1$. Cet optimum tend vers zéro. Les bits équitables indépendants conservent une erreur tendant vers $2/Q$. Pour deux observations,

$$\delta_2^*=\frac7{16Q}.$$

Tout optimiseur fort paie au moins $1/(8Q)$ dans l'expérience publique réelle et $5/(6L)$ dans l'expérience publique nulle ; le noyau équilibré atteint les deux bornes. Sans imposer l'optimalité forte, la meilleure somme publique vaut

$$\inf_K(\varepsilon_1(K)+\varepsilon_0(K))
=\frac1{L(8Q-6)}+\min\left\{\frac5{16Q},\frac5{6L}\right\}.$$

Pour $L=Q=4$, l'optimum fort est $7/64$. Le noyau qui minimise la somme publique a pour erreur forte $77/416$, pour erreurs publiques $5/64$ et $1/104$, et pour somme $73/832$. Les objectifs choisissent donc des solutions différentes.

**Idée de preuve à exposer.** Pour un même noyau appliqué à deux expériences, si une observation $y$ a masses $a_y,b_y$ et lois conditionnelles cibles $\nu_y,\omega_y$, alors

$$\inf_K\{\varepsilon_1(K)+\lambda\varepsilon_0(K)\}
=\sum_y\min(a_y,\lambda b_y)\Delta(\nu_y,\omega_y).$$

L'inégalité triangulaire donne la borne pour chaque ligne. On la réalise en choisissant la loi du terme de poids supérieur. À égalité, un mélange convient. Les lignes se choisissent indépendamment. Cette identité classique élémentaire sert à calculer les seuils du modèle ; elle n'est pas revendiquée comme un nouveau principe général.

## Questions à préparer

**Quelle est l'unité de la thèse ?** Le choix de ce qui doit être conservé. Les fibres, les lois conditionnelles et les masses invariantes rendent explicites des contraintes différentes sur une transformation.

**Où se situe la contribution ?** Dans les classifications spécialisées, les erreurs exactes, les constantes, les contre-exemples et les procédures qui les atteignent. La thèse n'attribue pas à ses auteurs les outils généraux de variation totale ou de comparaison d'expériences.

**Pourquoi une simulation exacte peut-elle ne rien prédire ?** Une nouvelle sortie peut avoir la bonne loi sans coïncider avec la valeur du tirage original. Reproduire une loi et retrouver une réalisation sont deux critères différents.

**Quelle est l'hypothèse la plus facile à oublier ?** La vue conservée. Deux affirmations apparemment opposées peuvent concerner $(Z,W)$ et $(Z,Y,W)$. Il faut aussi annoncer le prior, la parité de $Q$ et l'accès au bloc complet.

**Pourquoi l'orbite zéro contraint-elle un problème de grande dimension ?** Toute conversion exacte doit fournir la masse cible de cette orbite, même si elle est très petite. Sa masse source ne peut pas être augmentée par une transformation qui conserve l'orbite ; seul le conditionnement par acceptation la renormalise.

**Davantage d'itérations supprime-t-il cette obstruction ?** Des opérations supplémentaires sur la même matrice restent dans la même orbite. Des propositions indépendantes après rejet changent le coût en nombre de tirages, pas la loi conditionnelle d'une règle fixée.

**Pourquoi les observations répétées facilitent-elles la simulation ?** Elles apportent de l'information supplémentaire sur l'état commun. Ce phénomène ne signifie pas que l'état est mieux caché.

**L'optimum hors ligne reste-t-il atteignable en ligne ?** Ce n'est pas établi. Les noyaux causaux forment une sous-classe ; leur infimum ne peut donc pas être inférieur à l'optimum hors ligne. Aucun écart strict n'est revendiqué.

**Un algorithme fini est-il efficace ?** Il faut mesurer la taille de sa description. Une énumération polynomiale dans un tableau explicite peut être exponentielle dans la longueur binaire du module. Le coût d'une proposition et le nombre de propositions sont également distincts.

**Que signifie un échantillonnage exact en temps polynomial espéré ?** La loi produite est exacte et le coût moyen est borné comme annoncé. Cela ne fixe pas un nombre maximal de bits aléatoires sur toutes les exécutions possibles.

**Que prouvent les programmes ?** Ils corroborent des instances dans leurs domaines déclarés. Les preuves générales sont dans les chapitres. Une tolérance numérique ne devient pas une preuve symbolique.

**Quelle suite défendre en priorité ?** Le modèle causal ou les deux expériences publiques pour des blocs plus longs sont des prolongements précis du volume. Ils demandent de nouveaux calculs ; le tampon v0.6 ne les couvre pas.

## Conclusion proposée

Les résultats établissent que préserver une valeur, une marginale, une loi jointe ou une distribution structurée impose des contraintes distinctes. Pour les modèles étudiés, nous avons identifié ces contraintes, calculé des optima et construit des procédures qui les atteignent. Les restrictions sont explicites : elles rendent les résultats vérifiables et donnent des questions précises pour la suite.

Les preuves de référence restent celles des chapitres 2–10. Cette préparation ajoute une organisation orale et des réponses synthétiques ; elle n'ajoute aucun nouveau théorème au manuscrit approuvé.
