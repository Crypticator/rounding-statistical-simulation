# Rounding and Statistical Simulation — writing plan

Samir Bouftass and ChatGPT (OpenAI) · 17 November 2026

This plan is separate from the scientific manuscript. Version 0.6 contains the complete draft: eleven chapters and five appendices. Parts I–IV have received independent scoped approvals, most recently Part IV in the corrected v0.5.1 edition. Both reviewer corrections T4-E01 and T4-E02 are integrated. Section 1.8, Chapter 11, Appendix E and global coherence await final independent review. The earlier page estimate was a planning estimate, not a quota; the length follows the exposition.

## I. Foundations and affine compatibility — approved in version 0.2

1. **Questions and scope.** Information available to a computation, universal factorization, prediction and distributional simulation; precise claims and limitations.
2. **Modular rounding and its fibers.** Integer representatives, quotient cells, remainders, the fiber criterion, signed carry identities and restricted input supports.
3. **Finite probability and simulation.** Total variation, tests, kernels, conditional decomposition, optimal prediction, coupling, posterior sampling, channel comparison and two-world bounds.
4. **Affine maps compatible with rounding.** A complete row classification for rectangular maps, the invertible-square consequence, exact counts and missing-carry error.

The manuscript supplies the proofs needed for these four chapters. Its finite verification program corroborates examples and selected parameter domains. The independent recheck of 16 November 2026 closed all three required corrections and granted the Part I v0.2 stamp. This approval does not extend automatically to the new chapters.

## II. Noise and statewise simulation — approved in version 0.3.1

5. **Noisy rounded channels.** Define the secret law, noise law and available observation before comparing source and target channels. Develop exact statewise feasibility, the role of uniform noise, and the difference between averaging under one prior and preserving every state. Prove each scalar classification in place.
6. **Approximate simulation and optimal error.** Derive the relevant finite optimization problems, identify cases with exact solutions, and distinguish a small explicit table from a succinctly specified large state space. Give transparent worked examples and computational limitations.

## III. Structured matrix distributions — approved in version 0.4.1

7. **Row transformations and matrix structure.** Define Toeplitz matrices and the permitted signed row operations. Establish the preserved invariants and orbit structure with complete proofs. Keep matrix-law conversion separate from simulation of rounded observations.
8. **Exact and approximate conversion of distributions.** Prove support and orbit-mass obstructions, quantify total variation and rejection tradeoffs, and state the models in which each bound is sharp. Give finite examples that can be checked without outside material.

The independent Part III audit grants its stamp in v0.4.1. Its only required correction concerns the document export; the scientific text and programs remain unchanged.

## IV. Repeated observations — approved in version 0.5.1

9. **Repeated rounding of a shared hidden state.** Specify the joint experiment, fresh randomness and retained coordinates. Derive observation-preserving simulation bounds and explain when repetitions reveal information about the common state.
10. **The cost in a second experiment.** Analyze real and null laws with the same simulator. Prove the unavoidable public cost of every strong optimizer at two observations, then solve the unrestricted weighted public objective explicitly. Track both errors in a composed test and separate expected running time from all statistical errors.

## V. Synthesis — drafted in version 0.6; final review pending

11. **Conclusions and open problems.** State what has been proved, which restrictions are essential, and what remains open. Separate information-theoretic obstructions from claims about computational hardness. Do not infer a cryptographic security level from a simulation theorem or a finite experiment.

Appendices A–E contain worked examples, exact verification domains, reproduction instructions and consolidated notation. Public literature supplies context and attribution. All definitions and proofs required for the thesis's own conclusions appear within the volume; no unpublished companion article or private archive will be a prerequisite.

## Revision discipline

- Keep the quantifiers, input support and retained joint view explicit in every theorem.
- Introduce notation once and use the same convention across chapters.
- Rewrite related results into a continuous exposition; avoid repeated introductions and duplicated proofs.
- Add examples only when they explain a hypothesis, a boundary case or an obstruction.
- Distinguish drafted, checked and independently reviewed material.
- Review the final unified manuscript as a whole, including cross-chapter dependencies.
