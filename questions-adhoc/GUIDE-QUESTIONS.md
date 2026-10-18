# Ad-Hoc Questions & Study Guides — Standard Structure Guide (`GUIDE.md`)

This document defines the mandatory folder layout, file naming conventions, script reproducibility rules, and Markdown report standards for all ad-hoc biomedical investigations, deep dives, and study guides inside [`questions-adhoc/`](file:///home/sergiobermudez/local_projects/study-bio/questions-adhoc).

Whenever an agent or contributor solves a new ad-hoc question or creates a study guide in `questions-adhoc/`, they **MUST** follow this specification.

---

## 1. Directory Layout Standard

Every ad-hoc investigation is isolated in its own self-contained topic folder directly under `questions-adhoc/` using **lowercase kebab-case** after a descriptive `<type>_` prefix (`study-guide_`, `question_`, `deep-dive_`, or `analysis_`):

```text
questions-adhoc/
├── GUIDE.md                                      # This standardization guide
└── <type>_<topic-slug>/                          # e.g., study-guide_anterior-uveitis, study-guide_scn1a-gene
    ├── <type>_<topic-slug>.md                    # Main Markdown report (exact same stem as the folder)
    ├── figures/                                  # [When applicable] Rendered figures (.png, .svg) & paired PyMOL sessions (.pse)
    │   ├── fig1_<descriptive_slug>.png
    │   ├── fig1_<descriptive_slug>.pse
    │   ├── fig2_<descriptive_slug>.png
    │   └── ...
    ├── structures/                               # [When applicable] 3D structural coordinate files (.cif, .pdb)
    │   ├── <PDB_ID>.cif
    │   └── AF-<UniProt_ID>-F1-model_v6.cif
    ├── data/                                     # [When applicable] Quantitative datasets, API JSONs, TSV/CSV tables, PAE matrices
    │   └── <descriptive_name>.{json,tsv,csv}
    └── scripts/                                  # [When applicable] Reproducible Python/PyMOL/shell scripts (.py, .sh)
        ├── fetch_<topic>_data.py
        └── render_<topic>_structures.py
```

### Core Structural Rules

1. **One Folder per Question / Study Guide (`<type>_<topic-slug>/`)**:
   - Never place loose `.md`, `.png`, `.cif`, `.json`, or `.py` files directly at the root of `questions-adhoc/`.
   - Use **lowercase letters, digits, and hyphens** for `<topic-slug>` (e.g., `study-guide_anterior-uveitis`, `study-guide_scn1a-gene`, `question_brca1-ring-domain`). Avoid uppercase letters, spaces, or leading articles (`the-`, `a-`) in the slug.
2. **Primary Report (`<type>_<topic-slug>.md`)**:
   - Sits at the root of `<type>_<topic-slug>/` and shares the **exact same stem** as its parent directory.
3. **Semantic Subdirectories (`figures/`, `structures/`, `data/`, `scripts/`)**:
   - **`figures/`**: Holds all rendered images (`.png`, `.svg`, `.jpg`) and interactive PyMOL sessions (`.pse`).
   - **`structures/`**: Holds experimental (`.cif`, `.pdb`) and predicted (`AF-*-model_v6.cif`) 3D macromolecular coordinate files.
   - **`data/`**: Holds structured datasets referenced by or backing the report (`.json`, `.tsv`, `.csv`, `.bed`, `.vcf`, `.fasta`, including AlphaFold PAE JSON files and pathway enrichment exports).
   - **`scripts/`**: Holds the clean, reproducible scripts (`.py`, `.sh`) that fetched the data, computed metrics, or rendered the figures.
   - **On-Demand Creation**: Only create subdirectories (`figures/`, `structures/`, `data/`, `scripts/`) that contain at least one file. Do not leave empty directories.
4. **No Orphaned / Unreferenced Files**:
   - Every file stored in `figures/`, `structures/`, `data/`, and `scripts/` **must** be explicitly referenced or linked in `<type>_<topic-slug>.md` (or loaded by a documented script in `scripts/`).
   - Delete intermediate exploratory downloads (e.g., unused PDB `.cif` structures inspected during triage) before finalizing the answer.

---

## 2. File Naming Conventions

| Artifact Category | Subdirectory | Naming Pattern | Examples |
| :--- | :--- | :--- | :--- |
| **Question Folder** | `questions-adhoc/` | `<type>_<topic-slug>/` (all lowercase) | `study-guide_anterior-uveitis/`, `study-guide_scn1a-gene/` |
| **Main Report** | `<type>_<topic-slug>/` | `<type>_<topic-slug>.md` | `study-guide_anterior-uveitis.md`, `study-guide_scn1a-gene.md` |
| **Rendered Figures** | `figures/` | `fig<N>_<descriptive_slug>.png` (1-indexed sequential) | `fig1_nr3c1_corticosteroid_pocket.png`, `fig4_scn1a_string_channelosome_network.png` |
| **PyMOL Sessions** | `figures/` | `fig<N>_<descriptive_slug>.pse` (**exact same stem** as `.png`) | `fig1_nr3c1_corticosteroid_pocket.pse`, `fig1_alphafold_plddt.pse` |
| **3D Coordinates** | `structures/` | `<PDB_ID>.cif` or `AF-<UniProt>-F1-model_v6.cif` | `1M2Z.cif`, `7DTD.cif`, `AF-P35498-F1-model_v6.cif` |
| **Datasets & Tables** | `data/` | `<descriptive_snake_case>.{json,tsv,csv}` | `scn1a_reactome_enrichment.json`, `AF-P35498-F1-predicted_aligned_error_v6.json` |
| **Scripts** | `scripts/` | `<verb>_<descriptive_snake_case>.py` | `render_scn1a_structures.py`, `fetch_scn1a_data.py` |

> [!IMPORTANT]
> **Paired Figure & PyMOL Session Stems**: Whenever a figure is rendered via PyMOL (`figures/fig1_<slug>.png`), its companion PyMOL session file **must** be saved in `figures/` with the identical stem (`figures/fig1_<slug>.pse`), never `session_1_<slug>.pse`.

---

## 3. Script Reproducibility Standards (`scripts/`)

1. **Always Persist Production Scripts to `scripts/`**:
   - While one-off exploration can happen in `<artifactDir>/scratch/`, any script that generates a final figure in `figures/`, downloads/processes a dataset in `data/`, or computes structural measurements reported in `<type>_<topic-slug>.md` **must** be saved cleanly in `scripts/`.
2. **Use `uv` Inline Script Metadata (PEP 723)**:
   - All standalone Python scripts in `scripts/` must include a PEP 723 header so they can be executed reproducibly via `/home/sergiobermudez/.local/bin/uv run`:
     ```python
     # /// script
     # requires-python = ">=3.10, <3.13"
     # dependencies = [
     #     "pymol-open-source-whl",
     #     "requests",
     # ]
     # ///
     ```
   - For headless PyMOL rendering scripts, set `os.environ.setdefault("PYOPENGL_PLATFORM", "osmesa")` before importing `pymol`.
3. **Use Portable Relative Paths Anchored to the Question Root**:
   - Resolve paths relative to the parent of `scripts/` (`BASE_DIR = Path(__file__).resolve().parent.parent`) so the script works regardless of the caller's working directory:
     ```python
     from pathlib import Path

     BASE_DIR = Path(__file__).resolve().parent.parent
     STRUCTURES_DIR = BASE_DIR / "structures"
     FIGURES_DIR = BASE_DIR / "figures"
     DATA_DIR = BASE_DIR / "data"
     ```

---

## 4. Markdown Report Structure & Formatting Standards

Every `<type>_<topic-slug>.md` report should be self-contained, quantitatively rigorous, and formatted for effortless reading and review:

### 4.1 Recommended Report Skeleton

```markdown
# <Title>: <Descriptive Subtitle>

> **Scope & Focus:** <1-paragraph executive summary of the biological/clinical question, key molecular identifiers (MONDO/EFO, HGNC/Ensembl, UniProt, ChEMBL, PDB), and core sections covered.>

---

## 1. <Core Biology / Pathophysiology / Mechanism>
### 1.1 <Subsection>
...

## 2. <Genetics / Structural Biology / Pharmacology / Multi-Omics Analysis>
### 2.1 <Subsection>
...

## N-1. Synthesis & Self-Assessment Review Questions
### Question 1: <Focused Conceptual or Clinical-Molecular Question>
**<Question prompt>**

<details>
<summary><b>Click to reveal detailed answer</b></summary>

1. **<Point 1>:** ...
2. **<Point 2>:** ...
</details>

---

## N. Data Sources, Literature Citations & Mandatory Database Licensing Notices
### N.1 Primary Open-Access Literature Citations
1. **Author et al. (Year).** *Title.* **Journal**. (`PMID:...`, `PMC...`).

### N.2 Database Provenance, Reproducible Artifacts & Mandatory Licensing Notices
- **Reproducible Scripts & Data:** [`scripts/...`](scripts/...) | [`data/...`](data/...)
- **<Database Name> ([`.licenses/<skill>_LICENSE.txt`](../../.licenses/<skill>_LICENSE.txt)):** <Attribution & license summary>.
```

### 4.2 Link & Formatting Hygiene Checklist

- **Clickable Relative Links (Never Wrap Links in Outer Backticks)**:
  - ✅ Correct: `[`figures/fig1_alphafold_plddt.png`](figures/fig1_alphafold_plddt.png)` or `[`1M2Z.cif`](structures/1M2Z.cif)`
  - ❌ Incorrect: `` `[figures/fig1_alphafold_plddt.png](figures/fig1_alphafold_plddt.png)` `` (outer backticks turn the entire link into dead code text!)
  - ❌ Incorrect: `[fig1](file:///home/sergiobermudez/...)` (hardcoded machine-specific paths inside workspace `.md` files break portability; use relative paths like `figures/...` or `../../.licenses/...`).
- **Sequential Figure Numbering**:
  - Number all embedded images sequentially (`Figure 1`, `Figure 2`, `Figure 3`, `Figure 4`, ...) matching their `fig<N>_` filename prefix in `figures/`.
- **Consistent Subsection Numbering**:
  - Use `## 1.`, `## 2.`, `## 3.` for top-level sections and `### 1.1`, `### 1.2`, `### 2.1` for subsections throughout the document (avoid mixing `### A.` in one section and `### 8.1` in another).
- **Mandatory Licensing Attribution**:
  - Every database queried during the investigation (UniProt, AlphaFold DB, RCSB PDB, ChEMBL, PubChem, Open Targets, gnomAD, ClinVar, dbSNP, GTEx, HPA, STRING, Reactome, Ensembl, UCSC, Europe PMC, ClinicalTrials.gov) must be cited in the final section with a relative link to its local license record in `[`.licenses/<skill>_LICENSE.txt`](../../.licenses/<skill>_LICENSE.txt)` as well as its official terms URL.

