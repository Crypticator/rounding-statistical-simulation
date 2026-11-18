# Affine Maps Compatible with Modular Rounding

Samir Bouftass and ChatGPT (OpenAI)  
English edition 1.1 · 15 November 2026

This is an independent paper and its reproducibility supplement. The manuscript contains all definitions and essential proofs. No other paper by the authors is required. External references are public sources listed in the manuscript. The supplied code and finite calculations support the proofs; they do not establish a cryptographic security level.

## Contents

- `Affine_Maps_Modular_Rounding.pdf`: typeset paper.
- `Affine_Maps_Modular_Rounding.md`: editable source used to generate the PDF.
- `Affine_Maps_Modular_Rounding.tex`: standalone LaTeX source exported from the same manuscript.
- `Affine_Maps_Modular_Rounding.html`: standalone HTML with MathML equations.
- `scripts/`: exact verification, a reproduction runner, and document-building programs.
- `data/`: outputs recomputed for this edition and the observed dependency versions.
- `requirements-core.txt` and `requirements.txt`: standard-library-only verification.
- `requirements-build.txt`: optional dependencies for PDF construction.
- `SHA256SUMS`: checksums of the delivered files, excluding the checksum file itself.

## Mathematical domain

P = KQ, K,Q >= 2; positive input/output dimensions. Universal identities range over all inputs modulo P.

## Verification coverage

15,082 affine rows; 1,923,906 evaluated points; 14,578 excluded maps for which the verifier finds a collision; 1,451,375 carry-identity checks; 45 exact prediction laws.

The core verifier needs only the Python standard library. It checks all proper divisors Q >= 2 for 4 <= P <= 12 in dimensions 1 and 2, and dimension 3 for P <= 6. Prediction checks use Q = 2,...,16 and K = 2,3,4.

## Reproduce the calculations

Use Python 3.12 or a compatible Python 3 version. Run commands from the package directory. The complete environment used for this edition is recorded in `data/environment.json`.

```sh
python3 scripts/reproduce.py --out fresh_results
```

No third-party package installation is needed for these calculations. The output directory must not already exist. The verifier reconstructs the finite maps and laws; it does not read the delivered result files. Logs and new JSON results are placed in the requested directory. The JSON records how many excluded maps have a detected collision; it does not store the witness coordinates. Environment metadata may differ across reproductions.

## Rebuild the documents

Install Pandoc and the DejaVu TrueType fonts in addition to the optional build dependencies. The PDF renderer expects the standard Linux font location `/usr/share/fonts/truetype/dejavu`; adjust `fontroot` in `scripts/build_pdf.py` for another installation. No network connection or TeX installation is needed for the delivered PDF renderer.

```sh
python3 -m pip install -r requirements-build.txt
python3 scripts/build.py
```

This rebuilds the PDF and exports LaTeX and HTML. The LaTeX source can also be compiled in a suitable Unicode-capable TeX environment. It is an alternative source format; its pagination is not asserted to match the supplied ReportLab PDF.

## Integrity

```sh
sha256sum -c SHA256SUMS
```

The PDF in this supplement is the canonical distribution copy, identical to the standalone PDF and the copy in the collection archive. The SHA256SUMS entry identifies its exact bytes. Rebuilding can change provenance metadata even when the rendered pages are identical. Verify delivered files before rebuilding. All mathematical conventions, parameter restrictions, and limits of the results are stated in the paper.
