# Dense and Toeplitz Matrices under Signed Row Permutations

Samir Bouftass  
English edition 1.1 · 16 November 2026

This is an independent paper and its reproducibility supplement. The manuscript contains all definitions and essential proofs. No other paper by the author is required. External references are public sources listed in the manuscript. The supplied code and finite calculations support the proofs; they do not establish a cryptographic security level.

## Authorship revision

The author attribution and AI disclosure were revised on 18 November 2026. The paper credits Samir Bouftass as the sole author and describes the extensive assistance of ChatGPT in a dedicated section. AI-assisted reviews are not independent human peer review. The mathematical content, scientific verification programs and recorded data are unchanged; the original computation dates and environment files remain historical records. The source and publication metadata distinguish this editorial revision from English edition 1.1's original distribution.

## Contents

- `Dense_to_Toeplitz_Row_Transformations.pdf`: typeset paper.
- `Dense_to_Toeplitz_Row_Transformations.md`: editable source used to generate the PDF.
- `Dense_to_Toeplitz_Row_Transformations.tex`: standalone LaTeX source exported from the same manuscript.
- `Dense_to_Toeplitz_Row_Transformations.html`: standalone HTML with MathML equations.
- `scripts/`: exact verification and, where applicable, independent numerical checks, sampling, plotting, and document-building programs.
- `data/`: outputs retained from the scientific edition and the observed dependency versions.
- `figures/`: generated figures, if used in the paper.
- `requirements.txt`: versions used for numerical checks and PDF production.
- `SHA256SUMS`: checksums of the delivered files, excluding the checksum file itself.

## Mathematical domain

P = 2^p with p >= 2; m,n >= 2. Only adaptive signed row permutations are allowed. Rejection is introduced explicitly as a separate one-draw model.

## Verification coverage

274,688 dense matrices, complete accessible-orbit profiles, and six independent matrix-transport linear programs.

Exact domains (P,m,n): (4,2,2), (4,2,3), (4,3,2), (4,3,3), (8,2,2). Canonical row-orbit counting is checked against direct signed-row path search. LP domains use (4,2,2) and (4,3,2), three acceptance rates each, with tolerance 1e-8. Enumeration uses only the standard library. `scripts/check_structure.py` adds direct finite checks of the scalar cell lemma and affine-row classification, small invertible affine maps, and the row-reversal equivalence between Toeplitz and Hankel targets. It imports neither of the other scientific scripts nor any delivered result file; its domains and counters are recorded in `data/structure_results.json`.

## Reproduce the calculations

Use Python 3.12 or a compatible Python 3 version. Run commands from the package directory. The complete environment used for this edition is recorded in `data/environment.json`.

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

This rebuilds the PDF and exports LaTeX and HTML. The LaTeX source can also be compiled in a suitable Unicode-capable TeX environment. It is an alternative source format; its pagination is not asserted to match the supplied ReportLab PDF.

## Integrity

The current PDF is identified by `publication.json` and `SHA256SUMS`. Its copy at the root of the complete distribution and its copy in the updated collection archive are byte-identical. Previously downloaded files retain their original author credits and hashes.

```sh
sha256sum -c SHA256SUMS
```

Verify the delivered files before rebuilding. Rebuilding can change binary hashes even when the mathematical content is unchanged. The scientific campaigns were not rerun solely for this authorship revision. `AUTHORS_AND_AI.md` in the complete distribution explains the disclosure and responsibility statement.
