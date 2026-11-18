# Rounding and Statistical Simulation

Samir Bouftass · Complete research package · 18 November 2026

This package brings together the complete English thesis, four self-contained papers, editable sources, verification programs, recorded results and publication metadata. The research studies what finite modular rounding preserves, what randomized simulation can reproduce, how matrix transformations constrain distributions, and what changes when one hidden state is observed repeatedly. The results concern explicitly specified mathematical models; they do not establish a general cryptographic hardness reduction or a security level.

## Read the publications

| Publication | Download | Scientific version and length | Editable sources and reproduction |
|---|---|---|---|
| Rounding and Statistical Simulation | [PDF](THESIS_Rounding_Statistical_Simulation_v0_6.pdf) | 0.6 · 86 pages | [Word](thesis/deliverables/THESIS_Rounding_Statistical_Simulation_v0_6.docx), [Markdown](thesis/THESIS_Rounding_Statistical_Simulation_v0_6.md), [complete thesis materials](thesis/README.md) |
| Affine Maps Compatible with Modular Rounding | [PDF](Affine_Maps_Modular_Rounding.pdf) | 1.1 · 6 pages | [Sources and supplement](papers/Affine_Maps_Modular_Rounding/README.md) |
| Noise and Simulation of Rounded Observations | [PDF](Noise_and_Simulation_of_Rounded_Observations.pdf) | 1.1 · 7 pages | [Sources and supplement](papers/Noise_and_Simulation_of_Rounded_Observations/README.md) |
| Dense and Toeplitz Matrices under Signed Row Permutations | [PDF](Dense_to_Toeplitz_Row_Transformations.pdf) | 1.1 · 8 pages | [Sources and supplement](papers/Dense_to_Toeplitz_Row_Transformations/README.md) |
| Repeated Rounded Observations | [PDF](Repeated_Rounded_Observations.pdf) | 1.1 · 7 pages | [Sources and supplement](papers/Repeated_Rounded_Observations/README.md) |

All publications identify Samir Bouftass as their sole human author. The thesis and papers include a declaration of extensive ChatGPT assistance, including mathematical exploration, proof drafting, writing, translation, verification programs, computational checks and critical review. See [Authorship and AI assistance](AUTHORS_AND_AI.md). AI-assisted audits do not constitute independent human peer review.

## Package contents

- `thesis/`: complete thesis sources and PDF, Word, HTML and LaTeX exports; six figures; scientific scripts; recorded results; historical review records; preservation checks.
- `papers/`: four complete paper directories, each with its own sources, PDF, scripts, data, requirements, citation file and checksums.
- [supplementary_data/](supplementary_data/README.md): collected copies of all 24 data and environment files, with a CSV mapping to the canonical data directories.
- `CITATION.cff`: machine-readable citation for the package, the thesis and all four papers. No DOI has been assigned by this package.
- `LICENSE`, `LICENSE-CODE.txt`, `LICENSE-DOCUMENTS.txt`, `LICENSING.md`: license scope and full texts.
- `tools/verify_package.py`, `SHA256SUMS`, `PACKAGE_PROVENANCE.json`: integrity checks and provenance.
- [DEPLOYMENT_FR.md](DEPLOYMENT_FR.md): instructions for replacing the repository files and preparing a deposit.

The root PDF files are byte-identical convenience copies of the corresponding PDFs in the manuscript directories. The root archives provide a [complete thesis package](THESIS_Rounding_Statistical_Simulation_v0_6_CONSOLIDATED.zip) and a [four-paper collection](Four_English_Papers_and_Supplements.zip). The thesis archive uses one enclosing thesis directory; the paper archive contains the four paper directories directly.

## Verify and reproduce

Check the delivered package before rebuilding or generating new results:

```sh
python3 tools/verify_package.py
```

The integrity checker uses only the Python standard library. The calculations have their own requirements and recorded environments. To reproduce the first paper, whose scientific verifier uses only the standard library:

```sh
cd papers/Affine_Maps_Modular_Rounding
python3 scripts/reproduce.py --out fresh_results
```

For the other papers, follow their README and requirements files. Their runners distinguish exact calculations from numerical LP checks. New output directories must not already exist. Thesis reproduction commands and build dependencies are described in [thesis/README.md](thesis/README.md). The thesis includes the additional two-world results and its own supporting scripts and data.

This package revision changed author attribution, disclosure and publication packaging. The mathematical text, scientific verification algorithms and recorded results were preserved. The four article PDFs were rebuilt, and their scientific source and data preservation were checked. The numerical campaigns were not rerun solely for this editorial revision. Historical audit reports retain their original scope and hashes and are not evidence of independent human peer review. See [package validation](package_validation/README.md).

## Cite and reuse

Use [CITATION.cff](CITATION.cff) for the thesis or select the relevant article from its references. Each article supplement also has a local citation file. Version 0.6 identifies the thesis's mathematical text; edition 1.1 identifies each paper's mathematical text. The authorship and disclosure revision is dated 18 November 2026; the complete package version is `2026.11.18`.

Executable code and software configuration use **MIT**. Project-authored texts, original figures and research-data compilations use **CC BY 4.0**, to the extent rights apply. These licenses cover different materials; they are not interchangeable options for every file. Third-party rights remain unaffected. Read [LICENSING.md](LICENSING.md) for attribution and the precise scope.
