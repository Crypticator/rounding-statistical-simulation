# Rounding and Statistical Simulation

**Samir Bouftass and ChatGPT (OpenAI)**

Mathematical foundations of modular rounding and statistical simulation: proofs, exact algorithms, and reproducible experiments.

This repository contains an independent research manuscript and four self-contained English papers. The central question is what can be computed or simulated after an observation has been rounded. Each result specifies the information available to the simulator, the permitted transformations, and the joint distribution to preserve.

## Read the manuscript and papers

| Work | Edition | PDF | Sources and reproduction |
|---|---|---|---|
| **Rounding and Statistical Simulation** | Manuscript 0.6, 17 November 2026 | [Thesis PDF](thesis/deliverables/THESIS_Rounding_Statistical_Simulation_v0_6.pdf) | [Thesis directory](thesis/) |
| **Affine Maps Compatible with Modular Rounding** | English 1.1, 15 November 2026 | [Paper 1](papers/Affine_Maps_Modular_Rounding/Affine_Maps_Modular_Rounding.pdf) | [Supplement](papers/Affine_Maps_Modular_Rounding/) |
| **Noise and Simulation of Rounded Observations** | English 1.1, 15 November 2026 | [Paper 2](papers/Noise_and_Simulation_of_Rounded_Observations/Noise_and_Simulation_of_Rounded_Observations.pdf) | [Supplement](papers/Noise_and_Simulation_of_Rounded_Observations/) |
| **Dense and Toeplitz Matrices under Signed Row Permutations** | English 1.1, 16 November 2026 | [Paper 3](papers/Dense_to_Toeplitz_Row_Transformations/Dense_to_Toeplitz_Row_Transformations.pdf) | [Supplement](papers/Dense_to_Toeplitz_Row_Transformations/) |
| **Repeated Rounded Observations** | English 1.1, 16 November 2026 | [Paper 4](papers/Repeated_Rounded_Observations/Repeated_Rounded_Observations.pdf) | [Supplement](papers/Repeated_Rounded_Observations/) |

The thesis includes eleven chapters and Appendices A-E. Each paper contains its own definitions and essential proofs and can be read without the companion papers or private archives. Public references are listed in the manuscripts. Editable Markdown, alternative LaTeX and HTML exports, and the thesis DOCX are included in the directories above.

## Main topics

- Affine maps that factor through modular rounding, and exact losses caused by missing carries.
- Simulation of noisy rounded channels, their spectral exception, and the cost of retaining dependencies.
- Dense-to-Toeplitz conversion under signed row permutations: orbit masses, optimal total variation, and rejection.
- Repeated observations of one hidden state, exact block simulation, and errors across two public experiments.

These are results in specified finite models. They do not establish a general impossibility of cryptographic reductions or a cryptographic security level. Exact proofs, finite exact computations, and floating-point corroboration have distinct roles.

## Reproduce a paper

Use Python 3.12 or a compatible Python 3 version. From the repository root, the first paper requires only the standard library:

```sh
cd papers/Affine_Maps_Modular_Rounding
python3 scripts/reproduce.py --out fresh_results
```

For Papers 2-4, enter the corresponding paper directory and run:

```sh
python3 -m pip install -r requirements.txt
python3 scripts/reproduce.py --out fresh_results
```

Every output directory must be new. The scripts reconstruct their inputs from the model parameters; the recorded answers are not used as an oracle. Each supplement README specifies the exact parameter domain, dependencies, numerical tolerances, and build requirements. Use a separate Python environment if desired. The recorded dependency versions and execution environments are preserved with the original results.

## Reproduce the thesis

From the repository root, the exact-only checks are:

```sh
cd thesis
python3 scripts/verify_first_part.py
python3 scripts/reproduce_part_ii.py --out fresh_part_ii --skip-lp
python3 scripts/reproduce_part_iii.py --out fresh_part_iii --skip-lp
python3 scripts/reproduce_part_iv.py --out fresh_part_iv --skip-lp
```

For the additional numerical LP checks, install NumPy and SciPy, then omit `--skip-lp` and choose fresh output directories. The Part IV comparison report also records Matplotlib and ReportLab versions. See [the thesis README](thesis/README.md) for the complete commands and document-building instructions.

## Integrity and provenance

The contents of `papers/` and `thesis/` are unpacked from the identified source distributions and preserved byte for byte. Their existing `SHA256SUMS` files remain valid. Check a distribution before rebuilding it, from that distribution's directory:

```sh
sha256sum -c SHA256SUMS
```

From the repository root, the assembly manifest can also be checked with:

```sh
sha256sum -c PACKAGE_SHA256SUMS
```

See [PACKAGE_PROVENANCE.json](PACKAGE_PROVENANCE.json) for input hashes and [PACKAGE_CHECKS.json](PACKAGE_CHECKS.json) for the checks performed when assembling this package. Dated internal review and preparation notes are retained as historical records. Their status language reflects the date on which they were written. Such records are not mathematical premises or substitutes for the proofs.

## Citation and authorship

Use [CITATION.cff](CITATION.cff) for machine-readable citation metadata. Its preferred citation identifies the research manuscript, and its references identify the four papers. No DOI, journal acceptance, or institutional affiliation is asserted.

The author line follows the manuscripts: **Samir Bouftass and ChatGPT (OpenAI)**. ChatGPT is an AI system used in the research and writing collaboration; its attribution is represented as an entity in the citation metadata. Samir Bouftass maintains this repository under the account `Crypticator`.

## License

Licenses apply to different materials; they are not alternative licenses for every file:

- **Software and executable scripts:** [MIT](LICENSE-CODE.txt).
- **Project-authored manuscripts, documentation, original figures, and research-data compilations, to the extent rights apply:** [Creative Commons Attribution 4.0 International](LICENSE-DOCUMENTS.txt).

Both licenses permit commercial reuse subject to their conditions. Preserve the applicable attribution and notices. Third-party materials retain their own rights and licenses. [LICENSING.md](LICENSING.md) defines the scope, including the corresponding materials inside ZIP archives.
