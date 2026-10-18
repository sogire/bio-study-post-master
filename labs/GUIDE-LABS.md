# Laboratory Results Standardization Guide (`result_labs/`)

This guide defines the mandatory directory structure, file naming conventions, report anatomy, and script hygiene rules for all laboratory exercises and capstones in the `labs/` suite. 

Whenever the AI agent executes a laboratory prompt, generates data assets, writes helper scripts, or answers biological discussion questions, it **must** follow this specification.

---

## 1. Directory Hierarchy

Every module directory (`labs/01_structural_bioinformatics` through `labs/06_agentic_workflows`) and `labs/capstones` contains a `result_labs/` folder organized into **self-contained, per-exercise subdirectories**:

```text
labs/<XX_module_name>/
├── lab_guide.md                      # Module background, prompts, and discussion questions
└── result_labs/
    ├── discussion_questions.md       # Module-level biological discussion Q&A and synthesis
    ├── lab_X-1/                      # Self-contained folder for Exercise X.1
    │   ├── result_lab_X-1.md         # Primary scientific report for Exercise X.1
    │   ├── output/                   # Final data files (.json, .tsv, .cif, .pse) & figures (.png)
    │   └── scripts/                  # Reproducible Python analysis/visualization scripts (.py)
    ├── lab_X-2/
    │   ├── result_lab_X-2.md
    │   ├── output/
    │   └── scripts/
    └── lab_X-3/
        ├── result_lab_X-3.md
        ├── output/
        └── scripts/
```

For Capstone projects (`labs/capstones/result_labs/`):

```text
labs/capstones/
├── capstone1_gwas_to_drug.md
├── capstone2_variant_curation.md
└── result_labs/
    ├── capstone_1/
    │   ├── result_capstone_1.md      # End-to-end Capstone 1 scientific report
    │   ├── output/                   # Supporting multi-omics data, structures, and plots
    │   └── scripts/                  # Pipeline and rendering scripts
    └── capstone_2/
        ├── result_capstone_2.md      # End-to-end Capstone 2 curation report & validation
        ├── output/
        └── scripts/
```

---

## 2. File Naming & Asset Rules

1. **Exercise Reports (`result_lab_X-Y.md`)**:
   - Always name the primary report `result_lab_X-Y.md` (e.g., `result_lab_1-1.md`, `result_lab_2-3.md`) inside its `lab_X-Y/` folder, or `result_capstone_N.md` inside `capstone_N/`.
   - Keeping the exercise identifier in the filename ensures each tab or search result is immediately recognizable in the IDE.

2. **Discussion Questions (`discussion_questions.md`)**:
   - Place module-level Biological Discussion Questions and study Q&A syntheses in `labs/<XX_module_name>/result_labs/discussion_questions.md`.
   - If the user asks a discussion question during an exercise prompt, you may also include the discussion section inline within `result_lab_X-Y.md`, and mirror/update `result_labs/discussion_questions.md` so the module-level reference stays complete.

3. **Output Assets (`lab_X-Y/output/`)**:
   - Store all **final, report-referenced** data files (`.cif`, `.pdb`, `.pse`, `.json`, `.tsv`, `.csv`, `.bed`, `.fasta`) and figures (`.png`, `.svg`, `.pdf`) inside `lab_X-Y/output/`.
   - **No Scratch Clutter**: Never leave intermediate test renders (e.g., `test_*.png`), temporary debugging dumps, or unreferenced trial files inside `output/`. Write temporary scratch files to the agent's scratch directory or delete them before completing the task.
   - **Cross-Exercise Asset Reuse**: If Exercise `X-3` reuses a file downloaded in Exercise `X-2` (such as an AlphaFold `.cif` structure), copy the required file into `lab_X-3/output/` so that `lab_X-3/` and its scripts remain 100% self-contained.

4. **Reproducible Scripts (`lab_X-Y/scripts/`)**:
   - Store all custom Python scripts (e.g., PyMOL rendering scripts, AlphaGenome scoring scripts, custom data parsers) in `lab_X-Y/scripts/`—**never** inside `output/`.
   - **Dynamic Relative Paths**: Scripts must resolve their base directory relative to `__file__` rather than relying on hardcoded working directory paths:
     ```python
     base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
     output_dir = os.path.join(base_dir, "output")
     os.makedirs(output_dir, exist_ok=True)
     ```
   - **PEP 723 Inline Metadata**: When writing standalone scripts executed via `uv run`, include PEP 723 script metadata headers at the top of the `.py` file.

---

## 3. Standard Report Template (`result_lab_X-Y.md`)

Every exercise report must be written as a rigorous, publication-grade scientific document following this standardized structure:

```markdown
# Exercise X.Y: <Descriptive Scientific Title>

> [!IMPORTANT]
> **<Database/Tool> Terms & License Notice**: <Brief attribution statement and link to official usage policies>. License acknowledgments are recorded in [.licenses/<skill_name>_LICENSE.txt](../../../../.licenses/<skill_name>_LICENSE.txt).

## 1. Executive Summary
Concise synthesis of the biological question, target identifiers (UniProt, Ensembl, rsID, genomic coordinates in GRCh38), tools/skills invoked, and top-line quantitative findings.

---

## 2. Generated Assets & Outputs
Bulleted inventory of local files generated during the exercise using relative links:
- **<Asset Description>**: [`filename.ext`](output/filename.ext)
- **<Analysis/Render Script>**: [`script_name.py`](scripts/script_name.py)

---

## 3. Quantitative Results & Data Analysis
Structured subsections presenting empirical metrics, tables, and visual evidence:
- Use Markdown tables with clear units, thresholds, and biological interpretations.
- Embed generated plots or molecular renderings directly via `![Alt Text](output/figure.png)`.
- Include ASCII architecture diagrams or Mermaid flowcharts to illustrate domain boundaries, genomic loci, or biochemical pathways.

---

## 4. Biological Synthesis & Mechanistic Interpretation
Connect the quantitative outputs back to cellular physiology, structural biophysics, evolutionary selection, or clinical pathology (addressing the "why" and "how" behind the numbers).

---

## 5. Methods, Tooling & Data Provenance
Document the exact skills used, database releases/endpoints, genome assembly (e.g., GRCh38/hg38), and license compliance files.
```

---

## 4. Relative Path Cheat Sheet

Because `result_lab_X-Y.md` sits at `labs/<XX_module_name>/result_labs/lab_X-Y/result_lab_X-Y.md` (4 levels deep from workspace root):

| Target Resource | Relative Link from `result_lab_X-Y.md` |
| :--- | :--- |
| File in same exercise `output/` | `[filename.ext](output/filename.ext)` |
| Image in same exercise `output/` | `![Caption](output/figure.png)` |
| Script in same exercise `scripts/` | `[script.py](scripts/script.py)` |
| Module `discussion_questions.md` | `[discussion_questions.md](../discussion_questions.md)` |
| Sibling exercise report (`lab_X-1`) | `[result_lab_X-1.md](../lab_X-1/result_lab_X-1.md)` |
| Module `lab_guide.md` | `[lab_guide.md](../../lab_guide.md)` |
| Workspace `.licenses/` directory | `[<skill>_LICENSE.txt](../../../../.licenses/<skill>_LICENSE.txt)` |

