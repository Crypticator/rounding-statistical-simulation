---
title: "Noise and Simulation of Rounded Observations"
subtitle: "Exact scalar classification and the cost of preserving dependencies"
author: "Samir Bouftass"
date: "15 November 2026 · English edition 1.1"
---

## Abstract

We study simulation from one already rounded observation of a noisy scalar state. For $P=LQ$, the observation is $Y=\lfloor[Z+E]_P/Q\rfloor$, and the target is $W=\lfloor[c(Z+E)+b]_P/Q\rfloor$. The noise takes values $-1,0,1$ with probabilities $\eta,1-2\eta,\eta$, where $0\le\eta\le1/4$. We classify every stochastic kernel from $Y$ that reproduces the target channel for all states. Except at the maximal noise level, only constant maps and aligned translations or reflections are possible. At $\eta=1/4$ and even $P$, multiplication by $P/2$ adds one exceptional family: a state-independent fair coin. The exception comes from the alternating mode in the kernel of convolution. For even $Q$, we determine both the optimal error below this noise level and the positive error that remains when the original rounded observation must also be preserved. Explicit finite certificates separate simulation with access to the raw noisy value from simulation based only on its rounded quotient. The results concern a fixed scalar information constraint, not a general impossibility of cryptographic reductions.

## 1. Model and simulation requirement

Write $[x]_P$ for the representative in $\{0,\ldots,P-1\}$. Fix $P=LQ$ with $L,Q\ge2$, and define $F(x)=\lfloor[x]_P/Q\rfloor$. A hidden state $Z\in\mathbb Z_P$ is perturbed by independent noise

$$
\Pr(E=-1)=\Pr(E=1)=\eta,\qquad \Pr(E=0)=1-2\eta,
\quad 0\le\eta\le\tfrac14.
\tag{1}
$$

Let $X=[Z+E]_P$, $Y=F(X)$, and $W=h(X)$, where $h(x)=F(cx+b)$ and $c,b\in\mathbb Z_P$. A simulator receives one value $Y$ and samples an output using a row-stochastic matrix $K(y,w)$. Its randomness is fresh, and it receives neither $Z$ nor the discarded remainder. The same kernel must satisfy

$$
\mathcal L(K(Y)\mid Z=z)=\mathcal L(W\mid Z=z)
\qquad\text{for every }z\in\mathbb Z_P.
\tag{2}
$$

Equivalently, it preserves the joint law of $(Z,W)$ for every prior on $Z$. This requirement does not include preserving $(Z,Y,W)$, which is a stronger task considered in Section 6. There is no rejection, additional observation, or change of parameters in (2).

The target uses the same noisy value as the source. In particular, its noise before rounding is $cE$, not a fresh copy of $E$ added after $cZ$. Substituting fresh noise would define a different channel.

An elementary secret-based interpretation is available without importing any hardness assumption. Suppose a public $A$ is a unit modulo $P$, $S\in\mathbb Z_P$, and $Z=AS$. For each fixed $A$, multiplication by $A$ is a bijection. Thus statewise simulation is equivalent to preserving $(A,S,W)$ for all secret priors, allowing a kernel depending on $A$. This observation does not extend the theorem to nonunits, restricted secret supports, or dense matrix problems.

## 2. Finite channels and convolution

Let $H_{x,y}=\mathbf1\{F(x)=y\}$ and $G_{x,w}=\mathbf1\{h(x)=w\}$. Define the cyclic convolution operator

$$
(C_\eta f)(z)=\eta f(z-1)+(1-2\eta)f(z)+\eta f(z+1).
$$

The source and target channel matrices are $M=C_\eta H$ and $N=C_\eta G$. Condition (2) is precisely

$$
MK=N,\qquad K\ge0,\qquad K\mathbf1=\mathbf1,
\tag{3}
$$

or $C_\eta(HK-G)=0$. This is the standard finite randomization formulation of comparison of experiments [1], applied to a source whose information has already been coarsened by $F$.

The Fourier characters of $\mathbb Z_P$ diagonalize $C_\eta$, with eigenvalues

$$
\lambda_j=1-4\eta\sin^2(\pi j/P),\qquad 0\le j<P.
\tag{4}
$$

Consequently, $C_\eta$ is invertible if $\eta<1/4$, or if $P$ is odd. At $\eta=1/4$ and even $P$, its kernel is the one-dimensional space spanned by $v(x)=(-1)^x$.

**Lemma 1.** The matrix $M$ has full column rank $L$ throughout the parameter range.

**Proof.** If convolution is invertible, this follows from the disjoint nonempty columns of $H$. In the singular case, $Mu=0$ implies $Hu=av$. The left side is constant on each cell of length $Q\ge2$, while the right side alternates unless $a=0$. Therefore $a=0$, and then $u=0$. $\square$

There is thus at most one matrix $K$ satisfying (3), even before its positivity is checked.

## 3. A scalar factorization lemma

The following elementary statement provides all deterministic cases.

**Lemma 2.** The function $x\mapsto F(cx+b)$ is constant on every cell of $F$ if and only if one of the following holds: $c=0$; $c=1$ and $b\equiv0\pmod Q$; or $c=-1$ and $b\equiv Q-1\pmod Q$.

**Proof.** Write $x=Qy+r$, $0\le r<Q$. Then

$$
F(cx+b)=\left[cy+\left\lfloor\frac{cr+b}{Q}\right\rfloor\right]_L.
\tag{5}
$$

It suffices to study the first cell. If $c\ne0$, put $d=\gcd(c,P)$ and $\ell=P/d$. When $\ell<Q$, the $Q$ terms $[b+cr]_P$ contain a full subgroup coset, whose canonical representatives have diameter $P-d\ge P/2\ge Q$, preventing containment in a length-$Q$ interval. When $\ell=Q$, the $Q$ distinct terms occupy all $Q$ points of the cell, so the presence of consecutive points forces $d=1$, a contradiction. When $\ell>Q$, the $Q$ distinct terms occupy all $Q$ points of the cell and again force $d=1$. Shifting the progression by $c$ gives an overlap of $Q-1$ points with that interval. For a length-$Q$ interval $I$,

$$
|I\cap(I+c)|=\max(0,Q-[c]_P)+\max(0,Q-(P-[c]_P)).
$$

Since $Q\le P/2$, equality with $Q-1$ forces $c=1$ or $c=-1$. The first or last point must align with a cell endpoint, giving the two congruences. Formula (5) proves sufficiency, and the case $c=0$ is immediate. $\square$

## 4. Exact classification

**Theorem 1.** A stochastic kernel satisfying (2) exists exactly in the following cases. All coefficients are interpreted modulo $P$.

| Coefficient and translation | Kernel output on input $y$ |
|---|---|
| $c=0$, any $b$ | Constant $F(b)$ |
| $c=1$, $b\equiv0\pmod Q$ | $[y+\lfloor[b]_P/Q\rfloor]_L$ |
| $c=-1$, $b\equiv Q-1\pmod Q$ | $[-y+\lfloor[b]_P/Q\rfloor]_L$ |
| $c=P/2$, even $P$, $\eta=1/4$, any $b$ | Equal mixture of $F(b)$ and $F(b+P/2)$ |

Every listed kernel is unique.

**Proof.** If $C_\eta$ is invertible, (3) implies $HK=G$. Thus $h$ is constant on each cell, and Lemma 2 applies.

In the singular case, there is a row vector $a$ such that

$$
K(F(x),\cdot)-\delta_{h(x)}=(-1)^x a.
\tag{6}
$$

If $a=0$, Lemma 2 again gives the deterministic cases. Suppose $a\ne0$. Each cell contains both parities. Equation (6) implies that $h$ is constant on the even points of each cell and on the odd points of each cell. If those two values are $u_y,v_y$, then $\delta_{u_y}-\delta_{v_y}=-2a$. A nonzero difference of two point masses uniquely determines its ordered pair. Hence there are global distinct values $u,v$, independent of the cell. Averaging the two equations in (6) gives $K(y,\cdot)=(\delta_u+\delta_v)/2$ for every $y$.

The images of all even inputs under $x\mapsto cx+b$ form the coset $b+\langle2c\rangle$, contained in one rounding cell. A nontrivial subgroup coset has representative span at least $P/2\ge Q$, which is impossible. Thus $2c=0$ modulo $P$. Since $c=0$ would make $u=v$, necessarily $c=P/2$.

Conversely, at $\eta=1/4$, the parity of $Z+E$ is fair for every $Z$. Multiplication by $P/2$ depends only on this parity, giving the equal mixture in the table. The two output values are distinct because points separated by $P/2\ge Q$ cannot lie in one cell. Uniqueness follows from Lemma 1. $\square$

The exceptional kernel erases state information. Its existence is not evidence of a hard learning problem: its target distribution is independent of $Z$.

## 5. Exact error below the exceptional noise level

Assume now that $Q$ is even, so $P=LQ$ is even, and let $c=P/2$. Put $\alpha=F(b)$, $\beta=F(b+P/2)$, and $d=1-4\eta$. For each state,

$$
t_z=\Pr(W=\alpha\mid Z=z)=\frac{1+d(-1)^z}{2}.
$$

Define the average and worst-state errors

$$
\delta_{\mathrm{av}}=\inf_K\frac1P\sum_z\Delta(N_z,(MK)_z),\qquad
\delta_{\max}=\inf_K\max_z\Delta(N_z,(MK)_z),
$$

where $\Delta$ denotes half the $\ell^1$ distance.

**Theorem 2.** Both errors equal $d/2=(1-4\eta)/2$.

**Proof.** For any kernel set $k_y=K(y,\alpha)$ and $q=Mk$. Each cell has even length, so $\sum_x(-1)^x k_{F(x)}=0$. Convolution preserves the alternating mode up to the factor $d$, hence $\sum_z(-1)^zq_z=0$. Testing the event $\{\alpha\}$ and averaging gives

$$
\frac1P\sum_z\Delta(N_z,(MK)_z)
\ge\frac1P\sum_z|t_z-q_z|
\ge\left|\frac1P\sum_z(-1)^z(t_z-q_z)\right|=\frac d2.
$$

This argument allows the kernel to output values outside $\{\alpha,\beta\}$. A constant fair coin on these two values has distance $d/2$ for every state. It attains both lower bounds. $\square$

## 6. Preserving the original observation

Let $Z$ be uniform, $\eta=1/4$, $Q$ even, and $c=P/2$. Exactness for $(Z,W)$ does not imply exactness for $(Z,Y,W)$.

**Theorem 3.** Among all fresh $Y$-only kernels,

$$
\inf_K\Delta\bigl(\mathcal L(Z,Y,W),\mathcal L(Z,Y,K(Y))\bigr)=\frac1{2Q}.
\tag{7}
$$

The constant fair coin attains this value and also reproduces the public law of $(Y,W)$ exactly.

**Proof.** Mapping every output outside $\{\alpha,\beta\}$ to $\alpha$ fixes the real distribution and cannot increase total variation. We may therefore describe a kernel by $p_y=K(y,\alpha)$. For a fixed observed cell $y$, reflect

$$
z\longmapsto[(2y+1)Q-1-z]_P,\qquad E\longmapsto-E.
$$

This preserves the conditional law given $Y=y$ and swaps the parity of $X$, hence swaps $\alpha$ and $\beta$. The contribution of cell $y$ to the objective is convex in $p_y$ and invariant under $p_y\mapsto1-p_y$. It is minimized at $p_y=1/2$.

For an interior state, whose residue modulo $Q$ is in $\{1,\ldots,Q-2\}$, the rounded cell is fixed and the target is fair, so the conditional error is zero. At either boundary state of a cell, the outward noise step has mass $1/4$ and a deterministic target; replacing it by a fair coin contributes $1/8$ to total variation. Within the original cell, the two target masses are $1/2,1/4$, replaced by $3/8,3/8$, contributing another $1/8$. Thus each boundary state contributes $1/4$. Boundary states constitute a fraction $2/Q$ of all states, yielding (7), including $Q=2$.

Finally, $X$ is uniform, and each even-length cell contains equally many values of either parity. Hence $(Y,W)$ is exactly a uniform quotient paired with an independent fair coin. $\square$

For example, with $P=8$, $Q=2$, $b=0$, and $z=0$, the real masses on $(Y,W)$ are $(3,2):1/4$, $(0,0):1/2$, and $(0,2):1/4$. The simulated masses are $1/8$ at each of $(3,0),(3,2)$ and $3/8$ at each of $(0,0),(0,2)$, at distance $1/4$.

The optimum depends on the view being compared:

| View retained in the comparison | Minimum total variation |
|---|---|
| $(Y,W)$ | $0$ |
| $(Z,W)$ | $0$ |
| $(Z,Y,W)$ | $1/(2Q)$ |
| $(X,W)$ | $1/2$ |

The last row follows because $W$ is deterministic given $X$, while each cell contains equal proportions of the two possible targets. A $Y$-only prediction is therefore wrong with probability at least $1/2$.

## 7. Comparison with output-dependent error models

Learning with Errors with Output Dependencies (LWE-OD) permits the error distribution to depend on the underlying inner product [2]. Any finite target channel $N$ in this paper can be encoded in that language. Extend $N_{z,w}$ by zero outside $0\le w<L$, and define an error law on $\mathbb Z_P$ by

$$
\phi_z(e)=N_{z,[z+e]_P}.
\tag{8}
$$

Then adding this error modulo $P$ gives exactly the output channel $N$. The same construction applies to $M$. Expressibility as an output-dependent error model does not, however, settle which already coarsened source can simulate the channel.

Hoffmann et al. [2] give reductions through an intermediate problem called qLWE. Their reductions assume, in particular, that the modulus $q$ is polynomial in the dimension $n$ and that the secret has at least one coordinate invertible modulo $q$. Their Algorithm 1 uses rejection, and their Algorithm 2 and Proposition 5 use additional independent noise on unrounded LWE samples. Their sufficient Fourier conditions in Theorems 2–3 include both spectral support and nonnegativity constraints. In particular, they already account for zeros of the noise spectrum. Our exceptional alternating mode is not a new general treatment of spectral zeros. The extra constraint here is that the simulator acts through the fixed quotient matrix $H$ in (3).

Two exact certificates make this distinction concrete. They use the symmetric noise law $\psi$ from (1). For a positive output mass, write

$$
\rho(w)=\frac1P\sum_zN_{z,w},\qquad
\xi_w(j)=\frac{N_{[w-j]_P,w}}{P\rho(w)}.
\tag{9}
$$

At inactive outputs, a conditional law may be chosen freely, as in Remark 1 of [2]. A probability distribution $\tau_w$ satisfying $\tau_w*\psi=\xi_w$ supplies an explicit convolution certificate for the corresponding sufficient condition in [2].

**Raw information can suffice when the quotient does not.** Take $P=8$, $Q=2$, $c=2$, $b=0$, and $\eta=1/8$. Then $h(x)=[x]_4$, the active outputs have $\rho(w)=1/4$, and each active $\xi_w$ equals $\psi*\tau$ with $\tau=(\delta_0+\delta_4)/2$. Thus a nonnegative convolution certificate exists. Direct access to $X$ also plainly suffices to compute $h(X)$. Yet no kernel from $Y$ exists: convolution is invertible, while $F(0)=F(1)$ and $h(0)\ne h(1)$, so $HK=G$ is impossible. Exact elimination gives $\operatorname{rank}(M)=4$ and $\operatorname{rank}([M\mid N_{\cdot,0}])=5$. This is a separation between source information models, not a counterexample to [2].

**The singular case also fits the earlier framework.** For $P=8$, $Q=2$, $c=4$, $b=0$, and $\eta=1/4$, every target row is the fair distribution on $\{0,2\}$. Both active conditional laws $\xi_w$ are uniform on $\mathbb Z_8$. Taking $\tau_w$ uniform gives $\tau_w*\psi=\xi_w$, despite the spectral zero at frequency $4$. The quotient kernel is also exact for $(Z,W)$, but Theorem 3 still gives error $1/4$ for $(Z,Y,W)$.

The relevant distinction is therefore an exhaustive classification under the already rounded, single-observation constraint, together with the distances for specified views. No general LWE-OD hardness statement is inferred from these finite examples. The asymptotic hypotheses and access models of the reductions in [2] remain separate.

## 8. Cryptographic scope

LWR provides an important motivation for studying rounded observations [3,4], but the scalar theorems here neither prove a cryptographic reduction nor rule out broader ones. They exclude changes of secrets, dimensions, moduli, sample counts, and information access; computational rather than statistical simulation is also outside the model.

There is a further obstacle to interpreting the exceptional fair coin as a reduction. In the binary-modulus setting $P=2^p$, $Q=2^q$, its two outputs differ by $L/2$. If the null target is uniform on $\mathbb Z_L$, this two-point distribution is not the null law when $L>2$. If $L=2$, both real and null targets are uniform and the resulting target problem is trivial. The aligned translations and reflections permute quotient values and preserve a uniform null law, but this fact alone says nothing about structured matrix distributions.

More generally, if a transformation has errors $\varepsilon_0,\varepsilon_1$ in the two worlds of a distinguishing experiment, the triangle inequality gives the acceptance-gap bound

$$
\operatorname{Adv}_{\mathrm{source}}\ge
\operatorname{Adv}_{\mathrm{target}}-\varepsilon_0-\varepsilon_1.
\tag{10}
$$

Exact simulation of only the real marginal leaves the second error uncontrolled.

## 9. Reproducible verification

The supplement supplies three independent checks. The exact verifier constructs the channels directly using `fractions.Fraction`, selects independent source rows, solves for the unique candidate kernel, and checks all equations and stochastic constraints. It evaluates **8,049** coefficient-and-translation cases for $4\le P\le16$, all proper divisors $Q\ge2$, and $\eta\in\{0,1/8,1/4\}$. The **1,235** feasible cases consist of 645 constants, 207 positive maps, 207 reflections, and 176 parity cases. All **6,814** excluded cases fail exact linear consistency. There are **57** full-column-rank checks.

The distance calculations cover 34 even-divisor pairs with $P\le32$. Exact piecewise-linear optimization checks the stronger-view distance; 280 unit-multiplication checks verify the elementary secret reparameterization. A separate numerical implementation solves 72 linear programs for the average and worst-state errors, with tolerance $10^{-9}$. Finally, a third program verifies the two convolution and rank certificates in Section 7 without importing the classification. Negative controls detect fresh target noise, omitted reflection translations, subcritical parity bias, and the null-world mismatch. The delivered results identify their exact or floating-point arithmetic; only the mathematical proofs justify the unrestricted theorems.

## References

[1] David Blackwell. *Equivalent Comparisons of Experiments*. The Annals of Mathematical Statistics 24(2) (1953), 265–272. [DOI: 10.1214/aoms/1177729032](https://doi.org/10.1214/aoms/1177729032).

[2] Clément Hoffmann, Pierrick Méaux, Mélissa Rossi, and François-Xavier Standaert. *Learning with Errors with Output Dependencies: LWE, LWR, and Physical Learning Problems under the Same Umbrella*. PQCrypto 2026, LNCS 16491, pp. 287–318. [IACR ePrint 2025/2225](https://eprint.iacr.org/2025/2225), author version revised 25 February 2026. [DOI: 10.1007/978-3-032-22695-2_10](https://doi.org/10.1007/978-3-032-22695-2_10). Definitions 5–6, Algorithms 1–2, Proposition 5, and Theorems 1–3.

[3] Abhishek Banerjee, Chris Peikert, and Alon Rosen. *Pseudorandom Functions and Lattices*. EUROCRYPT 2012, pp. 719–737. [Author version](https://web.eecs.umich.edu/~cpeikert/pubs/prf-lattice.pdf).

[4] Joël Alwen, Stephan Krenn, Krzysztof Pietrzak, and Daniel Wichs. *Learning with Rounding, Revisited: New Reduction, Properties and Applications*. CRYPTO 2013, pp. 57–74. [Author version](https://crypto.ethz.ch/publications/files/AKPW13.pdf). DOI: 10.1007/978-3-642-40041-4_4.

## Authorship and use of generative AI

Samir Bouftass directed this research and is the sole named human author. The paper and its supporting programs were developed with extensive assistance from ChatGPT (OpenAI), including mathematical exploration, formulation and examination of arguments, proof drafting, writing and English translation, generation of verification programs, computational checks, and AI-assisted critical review. This assistance extends beyond language editing.

ChatGPT is disclosed as an AI tool and is not listed as an author or metadata contributor. AI-assisted reviews are not independent human peer review, and computational checks do not replace mathematical proofs. Responsibility for the final manuscript and its publication rests with the human author. This declaration does not certify that every argument has been independently checked by a human reviewer.

This authorship and disclosure revision is dated 18 November 2026. The mathematical text, scientific verification programs and recorded results of English edition 1.1 are unchanged.
