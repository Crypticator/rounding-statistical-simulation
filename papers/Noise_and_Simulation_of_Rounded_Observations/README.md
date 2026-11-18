# Noise and Simulation of Rounded Observations

Samir Bouftass and ChatGPT (OpenAI)  
English edition 1.1 · 15 November 2026

This is an independent paper and its reproducibility supplement. The manuscript contains all definitions and essential proofs. No other paper by the authors is required. External references are public sources listed in the manuscript. The supplied code and finite calculations support the proofs; they do not establish a cryptographic security level.

## Contents

- `Noise_and_Simulation_of_Rounded_Observations.pdf`: typeset paper.
- `Noise_and_Simulation_of_Rounded_Observations.md`: editable source used to generate the PDF.
- `Noise_and_Simulation_of_Rounded_Observations.tex`: standalone LaTeX source exported from the same manuscript.
- `Noise_and_Simulation_of_Rounded_Observations.html`: standalone HTML with MathML equations.
- `scripts/`: exact verification and, where applicable, independent numerical checks, sampling, plotting, and document-building programs.
- `data/`: outputs recomputed for this edition and the observed dependency versions.
- `figures/`: generated figures, if used in the paper.
- `requirements.txt`: versions used for numerical checks and PDF production.
- `SHA256SUMS`: checksums of the delivered files, excluding the checksum file itself.

## Mathematical domain

P = LQ, L,Q >= 2; noise probabilities (eta, 1-2 eta, eta), 0 <= eta <= 1/4. The two distance theorems additionally require even Q; the full-view theorem uses uniform Z and eta = 1/4.

## Verification coverage

8,049 exact classification cases, 57 rank checks, 1,235 feasible kernels, 6,814 exclusions established by exact linear-consistency checks (eight representative witnesses are recorded), 72 numerical linear programs, and two exact comparison certificates.

Classification covers P = 4,...,16, all proper divisors Q >= 2, eta in {0, 1/8, 1/4}, and every c,b modulo P. Distance checks include 34 even-divisor pairs with P <= 32 and 280 unit-secret bijection checks. Linear programs use tolerance 1e-9. The exact and comparison scripts use only the standard library.

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

The PDF named in `publication.json` is the canonical publication copy. The standalone PDF and the copies inside the individual supplement and the collection archive are byte-identical. Its SHA-256 is recorded in `publication.json` and `SHA256SUMS`.

```sh
sha256sum -c SHA256SUMS
```

Rebuilding files may change their binary hashes even when their scientific content is unchanged. Verify delivered files before rebuilding. All mathematical conventions, parameter restrictions, and limits of the results are stated in the paper.
