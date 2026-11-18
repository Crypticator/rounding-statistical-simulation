# Dense and Toeplitz Matrices under Signed Row Permutations

Samir Bouftass and ChatGPT (OpenAI)  
English edition 1.1 · 16 November 2026

This is an independent paper and its reproducibility supplement. The manuscript contains all definitions and essential proofs. No other paper by the authors is required. External references are public sources listed in the manuscript. The supplied code and finite calculations support the proofs; they do not establish a cryptographic security level.

## Contents

- `Dense_to_Toeplitz_Row_Transformations.pdf`: typeset paper.
- `Dense_to_Toeplitz_Row_Transformations.md`: editable source used to generate the PDF.
- `Dense_to_Toeplitz_Row_Transformations.tex`: standalone LaTeX source exported from the same manuscript.
- `Dense_to_Toeplitz_Row_Transformations.html`: standalone HTML with MathML equations.
- `scripts/`: exact verification and, where applicable, independent numerical checks, sampling, plotting, and document-building programs.
- `data/`: outputs recomputed for this edition and the observed dependency versions.
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

The canonical PDF is identified by its SHA-256 in `publication.json`. The standalone PDF and the copies in the individual supplement and collection archive use those same bytes.

```sh
sha256sum -c SHA256SUMS
```

Rebuilding files may change their binary hashes even when their scientific content is unchanged. Verify delivered files before rebuilding. All mathematical conventions, parameter restrictions, and limits of the results are stated in the paper.
