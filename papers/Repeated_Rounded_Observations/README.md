# Repeated Rounded Observations

Samir Bouftass  
English edition 1.1 · 16 November 2026

This is an independent paper and its reproducibility supplement. The manuscript contains all definitions and essential proofs. No other paper by the author is required. External references are public sources listed in the manuscript. The supplied code and finite calculations support the proofs; they do not establish a cryptographic security level.

## Authorship revision

The author attribution and AI disclosure were revised on 18 November 2026. The paper credits Samir Bouftass as the sole author and describes the extensive assistance of ChatGPT in a dedicated section. AI-assisted reviews are not independent human peer review. The mathematical content, scientific verification programs and recorded data are unchanged; the original computation dates and environment files remain historical records. The source and publication metadata distinguish this editorial revision from English edition 1.1's original distribution.

## Contents

- `Repeated_Rounded_Observations.pdf`: typeset paper.
- `Repeated_Rounded_Observations.md`: editable source used to generate the PDF.
- `Repeated_Rounded_Observations.tex`: standalone LaTeX source exported from the same manuscript.
- `Repeated_Rounded_Observations.html`: standalone HTML with MathML equations.
- `scripts/`: exact verification and, where applicable, independent numerical checks, sampling, plotting, and document-building programs.
- `data/`: results from English edition 1.0, unchanged in this editorial revision, and the observed dependency versions.
- `figures/`: generated figures, if used in the paper.
- `requirements.txt`: versions used for numerical checks and PDF production.
- `SHA256SUMS`: checksums of the delivered files, excluding the checksum file itself.

## Mathematical domain

P = LQ, even Q >= 4, L >= 3, k >= 1; one shared uniform state, independent three-point noises (1/4,1/2,1/4). The kernel sees the complete block and retains the observations.

## Verification coverage

24 exact cases; 76,440 state/noise tuples; 33,936 joint atoms; 242 numerical solver calls; exact Q = 4 curves through k = 64.

Exact domains (P,Q): (12,4), (16,4), (18,6), (24,8), each with k = 1,...,6. Independent LP checks cover nine valid cases and two invalid-domain controls (Q = 2 and L = 2). Comparison tolerance is 1e-9; secondary optimization allows 1e-12 feasibility slack. The exact verifier and optimal sampler use only the standard library. The sampler uses expected-time rejection for unbiased thirds; its seeded demo is for reproducibility, not cryptographic randomness.

## Reproduce the calculations

Use Python 3.12 or a compatible Python 3 version. Run commands from the package directory. The computation environment for the retained results is recorded in `data/environment.json`. The scientific programs and result files are unchanged from English edition 1.0.

```sh
python3 -m pip install -r requirements.txt
python3 scripts/reproduce.py --out fresh_results
```

The output directory must not already exist. Each scientific computation reconstructs its channels or distributions; it does not read the delivered result files. Logs and new JSON results are placed in the requested directory. The follow-up consistency checker, when present, compares the newly generated exact and numerical outputs. Floating-point LP results are numerical corroboration, distinct from rational calculations and proofs. Platform/version strings and source-code checksums may differ across reproductions.

## Rebuild the documents

Install Pandoc and the DejaVu TrueType fonts in addition to the Python requirements. The PDF renderer expects the standard Linux font location `/usr/share/fonts/truetype/dejavu`; adjust `fontroot` in `scripts/build_pdf.py` for another installation. No network connection or TeX installation is needed for the delivered PDF renderer.

```sh
python3 scripts/build.py
```

This rebuilds the PDF and exports LaTeX and HTML. The LaTeX source can also be compiled in a suitable Unicode-capable TeX environment. It is an alternative source format; its pagination is not asserted to match the supplied ReportLab PDF. For the block-observation paper, the build also regenerates the figure directly from the exact formulas.

## Integrity

The current PDF is identified by `publication.json` and `SHA256SUMS`. Its copy at the root of the complete distribution and its copy in the updated collection archive are byte-identical. Previously downloaded files retain their original author credits and hashes.

```sh
sha256sum -c SHA256SUMS
```

Verify the delivered files before rebuilding. Rebuilding can change binary hashes even when the mathematical content is unchanged. The scientific campaigns were not rerun solely for this authorship revision. `AUTHORS_AND_AI.md` in the complete distribution explains the disclosure and responsibility statement.
