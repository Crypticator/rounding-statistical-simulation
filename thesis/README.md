# Rounding and Statistical Simulation — version 0.6

Samir Bouftass · Scientific manuscript 17 November 2026 · Authorship and disclosure revision 18 November 2026

This complete English manuscript contains eleven chapters and Appendices A–E. Version 0.6 adds Section 1.8 on the complete argument, Chapter 11 on conclusions and open problems, and Appendix E collecting notation and model conventions. All definitions and essential proofs are in the volume. No companion article or private archive is required.

## Authorship and disclosure

Samir Bouftass is the sole named human author. The manuscript contains a front-matter declaration describing extensive assistance from ChatGPT (OpenAI), including mathematical exploration, proof drafting, writing and translation, verification programs, computational checks and AI-assisted critical review. ChatGPT is not listed as an author or metadata contributor. The declaration does not claim that every argument has undergone independent human verification.

This editorial revision changes the author credit, adds that declaration and synchronizes the exported documents and package metadata. The abstract, contents, eleven chapters, appendices, references, scientific programs and recorded data are unchanged. `AUTHORSHIP_REVISION_2026-11-18.md` records the scope and validation. Current document hashes appear in `RELEASE_INFO.json` and `SHA256SUMS`.

## Review status

Parts I–IV received scoped AI-assisted reviews, most recently Chapters 9–10 and Appendix D in the corrected edition 0.5.1. Both reviewer corrections are integrated: T4-E01 preserves explicitly double-struck symbols in native equations; T4-E02 measures and asserts all four errors of the new two-world example. Earlier OMML fixes remain in place. The earlier scientific text is unchanged. The Part IV report, reviewed source, builder and correction diffs are in `prior_reviews/`, outside the manuscript.

The final internal AI-assisted scientific audit of 17 November 2026 approved the preceding version 0.6, including Section 1.8, Chapter 11, Appendix E and complete-volume coherence. Its report records ten controls passing within the stated scope, with no mandatory correction. `final_review/` contains the unmodified historical report and original evidence archive. Their hashes identify the pre-revision documents, not the new documents containing the authorship declaration. The mathematical content retains version 0.6; this is an editorial revision, not a renewed scientific audit.

The package was first consolidated on 18 November 2026 and subsequently updated for authorship disclosure on the same date. The historical reviews and defense preparation materials are preserved as records of that workflow. AI-assisted internal reviews do not constitute independent human peer review, an academic degree, a formal proof certificate or cryptographic security certification.

## Documents

- `deliverables/THESIS_Rounding_Statistical_Simulation_v0_6.pdf`: identified reading edition.
- `deliverables/THESIS_Rounding_Statistical_Simulation_v0_6.docx`: editable native equations.
- `THESIS_Rounding_Statistical_Simulation_v0_6.md`: authoritative scientific source.
- The adjacent `.html` and `.tex` files are alternative exports. The LaTeX export was not compiled.
- `THESIS_WRITING_PLAN_V0_6.md`: completed chapter map and review scope.
- `CONSOLIDATION_REPORT_V0_6.md`: final consolidation report in French.
- `defense/SOUTENANCE_V0_6.md`: a proposed oral presentation and twelve questions, derived from the approved text. It is a preparation aid, not a new scientific chapter.

## New writing and consolidation

Section 1.8 maps the complete argument. Chapter 11 synthesizes the four model families, separates information loss, lost correlations and conserved orbit masses, compares distinct meanings of repetition, and explains computational limits. Its questions for further work are explicitly unresolved by this volume, without asserting that they are universally open. Appendix E defines local notation and resolves symbols reused between models.

## Reproduce the repeated-observation checks

Run from this directory:

```sh
python3 scripts/reproduce_part_iv.py --out fresh_part_iv_results
```

The output directory must not already exist. Add `--skip-lp` for the standard-library exact-only path. The numerical path requires NumPy and SciPy; the comparison report also records installed Matplotlib and ReportLab versions.

The Part IV reviewer executed this full wrapper before and after the correction. For version 0.6, the corrected two-world checker was rerun in the AI-assisted workflow and its output was compared with the reviewed results; the other campaigns were not repeated merely for the synthesis. The exact block campaign contains 24 cases, 76,440 weighted state-and-noise tuples and 33,936 nonzero atoms. Its separate optimizer uses 242 solver calls, including secondary objectives and two excluded-domain controls. The two-world checker enumerates 28 domains, verifies 217 weighted objectives and 1,104 tied rows exactly, and solves 836 small pointwise LPs. Source-law distances and the detailed four-kernel example are also checked. Appendix D states the overlapping domains and all limitations.

The exact tests use integer and rational arithmetic. Numerical optimizations use tolerance `1e-9` and are corroborations, not symbolic certificates. Scientific programs construct their inputs from parameters rather than reading the recorded answers as an oracle. The comparison program deliberately reads independently generated exact and LP results to compare them.

## Rebuild the manuscript

Rebuild in a working copy of this directory to preserve the canonical delivered files. With Pandoc, python-docx, Matplotlib and NumPy installed:

```sh
python3 build_manuscript.py
soffice --headless --convert-to pdf --outdir deliverables deliverables/THESIS_Rounding_Statistical_Simulation_v0_6.docx
python3 tools/check_document.py --docx deliverables/THESIS_Rounding_Statistical_Simulation_v0_6.docx --pdf deliverables/THESIS_Rounding_Statistical_Simulation_v0_6.pdf
```

Six figures are generated. Figures may read recorded exact profiles; the scientific verifiers reconstruct those profiles. The builder marks standalone asterisks, the cardinality hash and positive-part subscript signs as literal OMML tokens, and removes empty optional separators. Ordinary addition signs remain unchanged. The v0.5.1 compatibility fix converts only explicitly double-struck Z, R and E to their equivalent mathematical Unicode characters; ordinary variables are unchanged. The guard compares their DOCX and PDF counts. The new notation tables have dedicated widths, without changing the previous tables.

`validation/` records the actual environment, source invariance, scientific results and page inspection. The document guard checks common export defects and supplements visual review. Pagination and PDF bytes can vary between renderers; the identified reading PDF is the delivered edition.

## Earlier work and integrity

Earlier scientific scripts and data are retained unchanged and were not rerun for this extension. Their commands remain `python3 scripts/verify_first_part.py`, `python3 scripts/reproduce_part_ii.py --out fresh_part_ii`, and `python3 scripts/reproduce_part_iii.py --out fresh_part_iii`. Each later reproduction command requires a new output directory and has an exact-only option.

Verify `SHA256SUMS` before rebuilding. `RELEASE_INFO.json` gives canonical document hashes and review scope. `final_review/` now contains the final verdict and its evidence. `validation/consolidation_20261118/` records the last identity, pagination, equation and preservation checks. Earlier dated reports retain their historical review status. The current editorial revision is described in this README and the authorship revision record; it does not extend the scope of the historical reviews. The originals of the three updated accompanying documents and the earlier source manifest are preserved under that validation directory. No cryptographic security level or general hardness reduction is inferred from these simulations.
