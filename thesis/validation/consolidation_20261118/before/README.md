# Rounding and Statistical Simulation — version 0.6

Samir Bouftass and ChatGPT (OpenAI) · 17 November 2026

This complete drafted English manuscript contains eleven chapters and Appendices A–E. Version 0.6 adds Section 1.8 on the complete argument, Chapter 11 on conclusions and open problems, and Appendix E collecting notation and model conventions. All definitions and essential proofs are in the volume. No companion article or private archive is required.

## Review status

Parts I–IV have received their independent scoped approvals, most recently Chapters 9–10 and Appendix D in the corrected edition 0.5.1. Both reviewer corrections are integrated: T4-E01 preserves explicitly double-struck symbols in native equations; T4-E02 measures and asserts all four errors of the new two-world example. Earlier OMML fixes remain in place. The earlier scientific text is unchanged. The Part IV report, approved source, builder and correction diffs are in `prior_reviews/`, outside the manuscript.

The complete draft's new synthesis, notation, organization and global coherence await final independent review. Earlier approvals do not constitute a final approval of the whole thesis. Chapter 11 is now drafted. It adds no claimed classification or cryptographic theorem; the causal-kernel comparison is the elementary inclusion-of-feasible-sets observation justified in the text.

## Documents

- `deliverables/THESIS_Rounding_Statistical_Simulation_v0_6.pdf`: identified reading edition.
- `deliverables/THESIS_Rounding_Statistical_Simulation_v0_6.docx`: editable native equations.
- `THESIS_Rounding_Statistical_Simulation_v0_6.md`: authoritative scientific source.
- The adjacent `.html` and `.tex` files are alternative exports. The LaTeX export was not compiled.
- `THESIS_WRITING_PLAN_V0_6.md`: plan and review scope.

## New writing and consolidation

Section 1.8 maps the complete argument. Chapter 11 synthesizes the four model families, separates information loss, lost correlations and conserved orbit masses, compares distinct meanings of repetition, and explains computational limits. Its questions for further work are explicitly unresolved by this volume, without asserting that they are universally open. Appendix E defines local notation and resolves symbols reused between models.

## Reproduce the repeated-observation checks

Run from this directory:

```sh
python3 scripts/reproduce_part_iv.py --out fresh_part_iv_results
```

The output directory must not already exist. Add `--skip-lp` for the standard-library exact-only path. The numerical path requires NumPy and SciPy; the comparison report also records installed Matplotlib and ReportLab versions.

The Part IV reviewer executed this full wrapper before and after the correction. For version 0.6, the author reran the corrected two-world checker and compared its output with the reviewed results; the other campaigns were not repeated merely for the synthesis. The exact block campaign contains 24 cases, 76,440 weighted state-and-noise tuples and 33,936 nonzero atoms. Its separate optimizer uses 242 solver calls, including secondary objectives and two excluded-domain controls. The two-world checker enumerates 28 domains, verifies 217 weighted objectives and 1,104 tied rows exactly, and solves 836 small pointwise LPs. Source-law distances and the detailed four-kernel example are also checked. Appendix D states the overlapping domains and all limitations.

The exact tests use integer and rational arithmetic. Numerical optimizations use tolerance `1e-9` and are corroborations, not symbolic certificates. Scientific programs construct their inputs from parameters rather than reading the recorded answers as an oracle. The comparison program deliberately reads independently generated exact and LP results to compare them.

## Rebuild the manuscript

With Pandoc, python-docx, Matplotlib and NumPy installed:

```sh
python3 build_manuscript.py
soffice --headless --convert-to pdf --outdir deliverables deliverables/THESIS_Rounding_Statistical_Simulation_v0_6.docx
python3 tools/check_document.py --docx deliverables/THESIS_Rounding_Statistical_Simulation_v0_6.docx --pdf deliverables/THESIS_Rounding_Statistical_Simulation_v0_6.pdf
```

Six figures are generated. Figures may read recorded exact profiles; the scientific verifiers reconstruct those profiles. The builder marks standalone asterisks, the cardinality hash and positive-part subscript signs as literal OMML tokens, and removes empty optional separators. Ordinary addition signs remain unchanged. The v0.5.1 compatibility fix converts only explicitly double-struck Z, R and E to their equivalent mathematical Unicode characters; ordinary variables are unchanged. The guard compares their DOCX and PDF counts. The new notation tables have dedicated widths, without changing the previous tables.

`validation/` records the actual environment, source invariance, scientific results and page inspection. The document guard checks common export defects and supplements visual review. Pagination and PDF bytes can vary between renderers; the identified reading PDF is the delivered edition.

## Earlier work and integrity

Earlier scientific scripts and data are retained unchanged and were not rerun for this extension. Their commands remain `python3 scripts/verify_first_part.py`, `python3 scripts/reproduce_part_ii.py --out fresh_part_ii`, and `python3 scripts/reproduce_part_iii.py --out fresh_part_iii`. Each later reproduction command requires a new output directory and has an exact-only option.

Verify `SHA256SUMS` before rebuilding. `RELEASE_INFO.json` gives canonical document hashes and review scope. The separate final-review package contains this same manuscript, the approved v0.5.1 source and report, and a mission to examine the synthesis and complete argument. No cryptographic security level or general hardness reduction is inferred from these simulations.
