# 🛠️ Technical Issues, Complications & Solutions Log (`to-improve.md`)

**Scope:** Study-Guide-Agnostic Technical Retrospective & Skill Improvement Reference  
**Skills Covered:** `uv`, `pymol`, `pdb-database`, `alphafold-database-fetch-and-analyze`, `uniprot-database`, `chembl-database`, `pubchem-database`, `opentargets-database`, `clinical-trials-database`, `literature-search-europepmc`, `clinvar-database`, `dbsnp-database`, `gnomad-database`, `credentials`

---

## Executive Summary

Across multi-modal biomedical workflows—spanning **scientific literature mining**, **3D structural biology & headless PyMOL rendering**, **cheminformatics & target pharmacology**, and **clinical & population genetics**—we encountered **14 recurring technical complications**. These issues fall into five systemic categories:
1. **Sandbox & Environment Isolation:** User-space binaries (`~/.local/bin/uv`), pre-cached wheels, and `.git/index.lock` write locks behaving differently inside vs. outside the terminal sandbox.
2. **CLI Argument & Output Flag Inconsistencies:** Heterogeneous flag names (`--chembl-id` vs. `--molecule`, `--ids` vs. `--variant_ids`, space-separated vs. comma-separated lists, `stdout` vs. required `--output`) across skill scripts.
3. **External API Quirks & Silent Error Payloads:** EBI `HTTP 403` blocks on empty `User-Agent` headers, GraphQL `"Service overloaded"` responses returning HTTP `200` (`exit code 0`), and overly restrictive Entrez boolean property filters.
4. **Genomic & Chemical Data Schema Traps:** `0-based SPDI` vs. `1-based VCF` coordinate offsets, minus-strand reverse-complementation, gene-level `<SequenceLocation>` tags masking allele-level coordinates in XML records, fuzzy chemical name searches returning salts/analogues, and deeply nested JSON trees.
5. **3D Structure & Headless PyMOL Pitfalls:** Engineered/mutant receptor constructs in PDB search results, and multi-atom selection exceptions (`cmd.get_distance`, duplicate labels) caused by alternate conformations (`altloc`) or multiple asymmetric-unit copies in mmCIF (`.cif`) files.

This document records each technical complication, its root cause, the verified solution pattern, and concrete recommendations for improving the underlying skills—written completely agnostically of any specific disease, gene, or study guide.

---

## Summary Matrix of Technical Issues & Solutions

| # | Category | Skill / Component | Technical Issue / Complication | Agnostic Solution Pattern |
| :-: | :--- | :--- | :--- | :--- |
| **1** | Setup & Sandbox | `uv` / Terminal Sandbox | `~/.local/bin/uv` is invisible inside the default sandbox (`BypassSandbox: false`), causing `exit 127` (`No such file or directory`) and triggering unnecessary reinstallation attempts. | Invoke `/home/sergiobermudez/.local/bin/uv` with `BypassSandbox: true` and codify workspace rules in [`GEMINI.md`](file:///home/sergiobermudez/local_projects/study-bio/GEMINI.md) to never reinstall `uv` or `pymol`. |
| **2** | Setup & Sandbox | `git` / Command Shapes | `.git/index.lock` is read-only inside the default sandbox (`exit 128`), and chaining commands with `&&` / `;` disables prefix-based command auto-approval. | Run standalone single-binary commands (avoiding `&&` chains); when `git add` or `git commit` hits a read-only `.git` lock in the sandbox, re-run the single command with `BypassSandbox: true` and identical `toolAction`/`toolSummary`. |
| **3** | Literature & JSON | `literature-search-europepmc` | Multi-hundred-KB JSON outputs combined with missing `jq` (`command not found`) and `view_file` byte limits (`46,080` bytes). | Parse and rank JSON files using sandboxed `python3 -c "import json..."` scripts or `grep -n`, and paginate large full-text files via `ContentOffset` in `view_file`. |
| **4** | 3D Structure | `alphafold-database-fetch-and-analyze` | `fetch_alphafold.py <UNIPROT_ID>` fails with `HTTP Error 403 Forbidden` because `POLITE_HTTP_USER_AGENT` defaults to `""`. | Export a non-empty `POLITE_HTTP_USER_AGENT` header when invoking `fetch_alphafold.py`. |
| **5** | 3D Structure | `alphafold-database-fetch-and-analyze` | `analyze_plddt.py` names its argument `metadata_file` but actually expects `*_summary.json` (failing on `*-metadata.json`), and only outputs a global mean pLDDT. | Pass `*_summary.json` to `analyze_plddt.py`, and compute domain-resolved pLDDT distributions directly from `.cif` B-factor columns using Python/PyMOL along UniProt domain boundaries. |
| **6** | 3D Structure | `pdb-database` & `pymol` | Keyword PDB searches can return engineered/mutant constructs alongside wild-type complexes; `.cif` files with `altloc` (`A`/`B`) or multiple asymmetric-unit copies cause `cmd.get_distance` to crash (`selections must each contain a single atom`) and duplicate labels. | Inspect bound ligand IDs and active-site residues before rendering; strip altlocs (`cmd.remove("not alt ''+A"); cmd.alter("all", "alt=''")`), use `first (...)` in `cmd.label()`, and compute contact distances in Python from `cmd.get_model().atom` coordinates (`math.dist`). |
| **7** | Cheminformatics | `chembl-database` | `chembl_tools.py` uses inconsistent flags across subcommands (`--chembl-id` vs. `--molecule` vs. `--target`), and `search-molecule --query` performs broad substring matching that ranks salts/mixtures ahead of the parent molecule. | Check subcommand flags explicitly; filter `search-molecule` JSON outputs by case-insensitive exact match on `pref_name` (`max_phase`, `canonical_smiles`) before querying `mechanisms` or `activities`. |
| **8** | Cheminformatics | `pubchem-database` | `pubchem_S.py properties` rejects comma-separated `--properties "A,B,C"` (`exit 2: invalid choice`), and `pug-view` outputs deeply nested `60–150 KB` JSON trees. | Pass space-separated property names (`--properties MolecularFormula MolecularWeight XLogP TPSA ...`) and traverse `pug-view` JSONs with a recursive Python generator over `TOCHeading` and `StringWithMarkup`. |
| **9** | Target Discovery | `opentargets-database` | `query_opentargets.py --disease <id> --drugs` returns duplicate rows per drug across clinical trial phases and indications, and requires exact ontology ID prefixes (`MONDO_`/`EFO_` vs. `ENSG` vs. `CHEMBL`). | Resolve canonical IDs with `--search` first, then deduplicate `knownDrugs.rows` in Python keyed by `(drug.id, maxClinicalTrialPhase, mechanismOfAction)`. |
| **10** | Cross-Skill CLI | `uniprot`, `pdb`, `clinvar`, `dbsnp`, `gnomad` | Inconsistent CLI script names and output flags (`stdout` vs. required `-o`/`--output`, space-separated `nargs='+'` vs. comma-separated IDs, `.cif.gz` compressed downloads). | Verify `--help` / `SKILL.md` before first invocation, decompress `.cif.gz` via `gunzip -f`, and direct all intermediate outputs to `scratch/`. |
| **11** | Clinical Genetics | `clinvar-database` | `clinvar_api.py evidence` often parses `<Gene>`-level `<SequenceLocation>` tags from ClinVar XML, returning gene-wide start/stop intervals with `None>None` alleles instead of exact VCF coordinates. | Extract `dbsnp_rsid` from the ClinVar evidence JSON and resolve exact GRCh38 coordinates and alleles via `dbsnp_cli.py`. |
| **12** | Population Genetics | `dbsnp-database` & `gnomad-database` | **0-based SPDI vs. 1-based VCF off-by-one trap:** `dbsnp_cli.py get-variant` returns 0-based SPDI coordinates, which fail (`"Variant not found"`) in 1-based VCF tools (`gnomAD`) unless incremented by `+1` and strand-normalized. | Cross-check with `dbsnp_cli.py resolve-rsid` (`1-based HGVS g.`), convert `pos_vcf = pos_spdi + 1`, and verify plus-strand reference alleles before querying `gnomAD`. |
| **13** | Population Genetics | `gnomad-database` | Concurrent `get_variant_frequency.py` calls trigger GraphQL `"Service overloaded"` errors inside the JSON payload while exiting with shell code `0`. | Inspect output JSON files for `"errors"` keys rather than relying on `exit 0`, and cap concurrency at $\le 2$ parallel requests. |
| **14** | Clinical Genetics | `clinvar-database` | Combining multiple quoted Entrez `[Properties]` and `[Molecular consequence]` clauses in `clinvar_api.py search` frequently returns `0` hits due to Entrez index aliasing. | Query Entrez with broader gene + consequence or variant terms and filter by `review_status` (star rating) locally in the returned `summary` JSON. |

---

## Detailed Analysis & Actionable Skill Improvements

### 1. Terminal Sandbox Isolation Hiding `~/.local/bin/uv` & Pre-Cached Packages
* **Component:** `uv` & `pymol` execution in the terminal sandbox
* **The Complication:**
  * Running `uv --version` or `/home/sergiobermudez/.local/bin/uv --version` inside the default terminal sandbox (`BypassSandbox: false`) returns `exit code 127: No such file or directory`.
  * Following the default fallback in `uv/SKILL.md` (`curl -LsSf https://astral.sh/uv/install.sh | sh`) fails in the sandbox due to network isolation and unnecessarily prompts to reinstall `uv`.
* **Root Cause:**
  * The default sandbox (`BypassSandbox: false`) mounts only the workspace directory, `/tmp`, and standard system directories (`/usr/bin`, `/bin`). User-level paths outside the workspace (`~/.local/bin/uv`, `~/.cache/uv`, `~/.local/share/uv`) are unmounted in the sandbox even when `uv` and cached wheels (`pymol-open-source-whl`) are already installed on the host.
* **Agnostic Solution Pattern:**
  1. Invoke `/home/sergiobermudez/.local/bin/uv` with `BypassSandbox: true` whenever executing skill scripts or headless PyMOL scripts.
  2. Maintain explicit workspace rules in [`GEMINI.md`](file:///home/sergiobermudez/local_projects/study-bio/GEMINI.md) prohibiting reinstallation of `uv` or `pymol`.
* **What to Improve in Skills:**
  * Update `uv/SKILL.md` to warn agents that `No such file or directory` on `~/.local/bin/uv` inside a sandboxed environment indicates mount isolation rather than a missing binary, and instruct agents to test `~/.local/bin/uv --version` with `BypassSandbox: true` before attempting installation.

---

### 2. Command Shape Auto-Approval & Sandbox Read-Only `.git` Locks
* **Component:** Terminal command construction (`run_command`) & Git operations
* **The Complication:**
  1. Joining multiple commands with `&&`, `;`, `||`, or subshells (`$(...)`) disables prefix-matching for user command approvals, forcing manual confirmation on every new invocation.
  2. Running `git add` or `git commit` inside the default sandbox (`BypassSandbox: false`) fails with `fatal: Unable to create '.../.git/index.lock': Read-only file system` (`exit code 128`).
* **Root Cause:**
  * The approval system generalizes permissions by matching the leading binary and subcommand only when shell control operators (`&&`, `;`, `|`, `$()`) are absent. Additionally, `.git` is protected as read-only inside the default sandbox.
* **Agnostic Solution Pattern:**
  1. Issue each CLI tool call as a standalone, single-binary command (using parallel tool calls when commands are independent) and perform multi-file post-processing in a single sandboxed Python script (`python3 scratch/parse_data.py`).
  2. Run read-only Git commands (`git status`, `git log`, `git diff`) inside the sandbox (`BypassSandbox: false`), and escalate write-modifying Git commands (`git add`, `git commit`) to `BypassSandbox: true` while keeping `toolAction` and `toolSummary` identical across retries.

---

### 3. Missing `jq` Utility & Large JSON / Full-Text Payloads
* **Component:** `literature-search-europepmc` & general JSON post-processing
* **The Complication:**
  * Literature and database searches frequently generate `100–400 KB` JSON files (`5,000–10,000+` lines).
  * The host environment does not have `jq` installed (`jq: command not found`), and `view_file` truncates text past `800` lines or `46,080` bytes.
* **Root Cause:**
  * `jq` is not part of the base Linux image, and API responses embed full abstracts, author arrays, or nested ontology hierarchies.
* **Agnostic Solution Pattern:**
  1. Use sandboxed `python3` scripts (`BypassSandbox: false`) with Python's built-in `json` module to parse, filter, sort, and summarize all downloaded JSON files in `scratch/` into compact Markdown/text summaries.
  2. When reading long full-text XML/text articles via `view_file`, use the `ContentOffset` parameter (`46080`, `92160`, etc.) to paginate through the entire document without truncation.
* **What to Improve in Skills:**
  * Replace `jq` examples in skill documentation with `python3 -c "import json..."` recipes or add `--summary` flags to CLI scripts.

---

### 4. AlphaFold EBI API `HTTP 403 Forbidden` on Empty `User-Agent`
* **Component:** `alphafold-database-fetch-and-analyze` (`scripts/fetch_alphafold.py`)
* **The Complication:**
  * Running `fetch_alphafold.py <UNIPROT_ID>` fails with `HTTP Error 403 while fetching https://alphafold.ebi.ac.uk/api/prediction/<ID>` when `POLITE_HTTP_USER_AGENT` is unset.
* **Root Cause:**
  * `fetch_alphafold.py` initializes the HTTP `User-Agent` header from `os.environ.get("POLITE_HTTP_USER_AGENT", "")`. When unset, it sends an empty `User-Agent: ""`, which EBI's edge firewall blocks with `HTTP 403 Forbidden`.
* **Agnostic Solution Pattern:**
  * Always pass a non-empty `POLITE_HTTP_USER_AGENT` environment variable (or set it in a persistent terminal session) when invoking `fetch_alphafold.py`.
* **What to Improve in Skills:**
  * Change the default fallback in `fetch_alphafold.py` from `""` to a valid user-agent string such as `"DeepMind-Science-Skills/1.0 (python-urllib)"`.

---

### 5. Misleading `metadata_file` Argument & Global-Only Metrics in `analyze_plddt.py`
* **Component:** `alphafold-database-fetch-and-analyze` (`scripts/analyze_plddt.py`)
* **The Complication:**
  * `analyze_plddt.py` defines its positional argument as `metadata_file`, tempting callers to pass `AF-<ID>-F1-metadata.json`. Doing so fails because the script actually expects the schema of `AF-<ID>-F1_summary.json`.
  * Moreover, `analyze_plddt.py` reports only a single whole-protein average pLDDT, which obscures high-confidence structured domains (`pLDDT > 85–90`) when a protein also contains long intrinsically disordered loops (`pLDDT < 50`).
* **Root Cause:**
  * Argument naming mismatch between `fetch_alphafold.py` (which outputs both `-metadata.json` and `_summary.json`) and `analyze_plddt.py`, plus lack of per-residue B-factor parsing in `analyze_plddt.py`.
* **Agnostic Solution Pattern:**
  1. Pass `AF-<ID>-F1_summary.json` to `analyze_plddt.py` for global metrics.
  2. Compute domain-by-domain mean pLDDT directly from the `B-factor` column of `AF-<ID>-F1-model_v6.cif` in Python/PyMOL using the exact domain coordinates retrieved from `uniprot_tools.py`.
* **What to Improve in Skills:**
  * Rename the positional argument in `analyze_plddt.py` to `summary_or_cif_file` and add support for computing per-domain pLDDT statistics from `.cif`/`.pdb` files given residue ranges.

---

### 6. PDB Construct Verification & Multi-Assembly / Altloc Failures in Headless PyMOL
* **Component:** `pdb-database` & `pymol`
* **The Complication:**
  1. **Mutant/engineered structures in PDB search results:** Searching RCSB PDB by protein name and ligand class (`search_pdb.py`) can return engineered constructs (e.g., point-mutated "salt-bridge rescue" pockets or chimeric fusion proteins) alongside wild-type complexes.
  2. **`cmd.get_distance` and `cmd.label` failures on `.cif` files:** Many experimental mmCIF structures contain either **alternate side-chain conformations (`alt A`/`alt B`)** or **multiple non-crystallographic symmetry copies** in the asymmetric unit. Calling `cmd.get_distance(atom_sel_1, atom_sel_2)` raises `CmdException: Error:get_distance: selections must each contain a single atom`, and `cmd.label()` renders overlapping duplicate labels.
* **Root Cause:**
  * PyMOL's `cmd.get_distance` strictly requires each selection string to resolve to exactly 1 atom (`len == 1`). When an atom has `alt A` and `alt B` records (or identical chain/residue identifiers across segments), a standard `chain X and resi Y and name Z` selection matches $\ge 2$ atoms.
* **Agnostic Solution Pattern:**
  1. **Inspect before rendering:** Run a quick inspection pass on candidate `.cif` files to print chain IDs, bound ligand `resn` codes, and active-site residue identities, verifying wild-type pocket architecture and discarding engineered rescue mutants.
  2. **Strip altlocs immediately after loading:**
     ```python
     cmd.load(cif_path, "complex")
     cmd.remove("solvent")
     cmd.remove("not alt ''+A")
     cmd.alter("all", "alt=''")
     ```
  3. **Use `first (...)` for labels and `math.dist` on atom coordinates for distance measurements:**
     ```python
     # Safe single-atom labeling:
     cmd.label(f"first (complex and chain {ch} and resi {res_id} and name CA)", f'"{label_text}"')

     # Safe interatomic distance calculation without cmd.get_distance exceptions:
     import math
     atoms_a = cmd.get_model(selection_a).atom
     atoms_b = cmd.get_model(selection_b).atom
     for a in atoms_a:
         for b in atoms_b:
             d = math.dist(a.coord, b.coord)
             if d <= 3.6:
                 print(f"{a.resn}{a.resi}:{a.name} -- {b.resn}{b.resi}:{b.name} = {d:.2f} A")
     ```
* **What to Improve in Skills:**
  * Add this exact altloc-stripping, `first (...)` labeling, and `cmd.get_model()` distance measurement pattern to `pymol/SKILL.md`.

---

### 7. ChEMBL CLI Subcommand Flag Mismatches & Fuzzy vs. Exact Molecule Search
* **Component:** `chembl-database` (`scripts/chembl_tools.py`)
* **The Complication:**
  1. Subcommands in `chembl_tools.py` use inconsistent flag names for the same ChEMBL molecule ID: `get-molecule`, `mechanisms`, and `drug-warnings` require `--chembl-id <ID>`, whereas `drug-indications` and `activities` require `--molecule <ID>` (and `activities` uses `--target <ID>` instead of `--target-id`), causing `exit code 2: unrecognized arguments` when flags are assumed uniform.
  2. `chembl_tools.py search-molecule --query "<Drug Name>"` performs a broad substring search across synonyms and mixture names, often returning multi-ingredient combinations, veterinary salts, or analogues before the canonical parent drug.
* **Root Cause:**
  * Separate `argparse` subparsers in `chembl_tools.py` were authored with different option names, and the ChEMBL REST `/molecule/search.json` endpoint ranks by text-indexing score rather than exact `pref_name` equality.
* **Agnostic Solution Pattern:**
  1. Respect the exact subcommand flag map:
     * `get-molecule`, `mechanisms`, `drug-warnings` $\rightarrow$ `--chembl-id <CHEMBL_ID>`
     * `drug-indications` $\rightarrow$ `--molecule <CHEMBL_ID>`
     * `activities` $\rightarrow$ `--target <TARGET_CHEMBL_ID>` and/or `--molecule <MOL_CHEMBL_ID>`
  2. After running `search-molecule`, filter the returned `molecules` list in Python by case-insensitive exact match on `pref_name` (`m.get("pref_name", "").upper() == query.upper()`) and verify `max_phase`, `molecule_type`, and `molecule_properties` (`mw_freebase`, `alogp`, `psa`).
* **What to Improve in Skills:**
  * Alias `--chembl-id` and `--molecule` across all molecule-accepting subcommands in `chembl_tools.py`, and add an `--exact` flag to `search-molecule` that queries `/molecule.json?pref_name__iexact=<query>`.

---

### 8. PubChem CLI Comma-Separated `--properties` Rejection & Nested `pug-view` JSON Trees
* **Component:** `pubchem-database` (`scripts/pubchem_S.py`)
* **The Complication:**
  1. Running `pubchem_S.py properties --cid <CID> --properties "MolecularFormula,MolecularWeight,XLogP,TPSA"` fails with `exit code 2: error: argument --properties: invalid choice` because `--properties` uses `nargs="+"` with `choices=[...]` and expects space-separated arguments.
  2. `pubchem_S.py pug-view --cid <CID> --heading "Pharmacology and Biochemistry"` returns a `60–150 KB` deeply nested JSON tree (`Record -> Section -> Section -> Information -> Value -> StringWithMarkup`) where text is fragmented across dozens of nested arrays.
* **Root Cause:**
  * `pubchem_S.py` joins space-separated `nargs="+"` tokens into a comma-separated string internally for the PUG-REST URL, so passing a pre-joined comma string fails `argparse` validation.
* **Agnostic Solution Pattern:**
  1. Always pass space-separated property tokens to `pubchem_S.py properties`:
     ```bash
     /home/sergiobermudez/.local/bin/uv run .../pubchem_S.py properties --cid <CID> \
       --properties MolecularFormula MolecularWeight CanonicalSMILES XLogP TPSA HBondDonorCount HBondAcceptorCount RotatableBondCount \
       --output scratch/pubchem_props.json
     ```
  2. Extract `pug-view` text using a recursive Python walker that visits every dict/list node and prints `(TOCHeading, StringWithMarkup[].String)`.
* **What to Improve in Skills:**
  * Allow `pubchem_S.py properties` to accept both comma-separated and space-separated property lists, and add a `--summary` text-flattening mode to `pubchem_S.py pug-view`.

---

### 9. Open Targets Entity-Type Dispatch & Clinical Drug Deduplication
* **Component:** `opentargets-database` (`scripts/query_opentargets.py`)
* **The Complication:**
  * `query_opentargets.py --disease <MONDO_or_EFO_ID> --drugs` returns `data.disease.knownDrugs.rows`, which contains one row *per clinical trial / indication record* rather than one row per unique drug—resulting in dozens of duplicate entries for well-studied drugs across phases and disease subtypes.
* **Root Cause:**
  * The Open Targets GraphQL `knownDrugs` connection is indexed at the `(drug, target, disease, clinicalTrial)` evidence level rather than aggregated by `drug.id`.
* **Agnostic Solution Pattern:**
  * Post-process `knownDrugs.rows` in Python by grouping on `drug.id` (`CHEMBL*`), retaining the maximum `phase`, collecting unique `mechanismOfAction` strings, and mapping target `approvedSymbol` / `ENSG` IDs into a deduplicated summary table.
* **What to Improve in Skills:**
  * Add a `--unique-drugs` flag to `query_opentargets.py --disease <id> --drugs` that aggregates `knownDrugs.rows` by `drug.id`.

---

### 10. Cross-Skill CLI Output & Compression Standardization
* **Component:** `uniprot-database`, `pdb-database`, `clinvar-database`, `dbsnp-database`, `gnomad-database`, `clinical-trials-database`
* **The Complication:**
  * Across skills, output flags and file formats vary:
    * `uniprot_tools.py get` and `search_pdb.py` write to `stdout` and reject `-o`/`--output`.
    * `fetch_pdb_metadata.py`, `clinvar_api.py`, `dbsnp_cli.py`, and `get_variant_frequency.py` require `--output <path>`.
    * `pdb_database/scripts/download.py` downloads gzip-compressed `.cif.gz` files (`pdb_0000xxxx.cif.gz`) rather than uncompressed `.cif` files.
* **Agnostic Solution Pattern:**
  * Check `SKILL.md` or `--help` before invoking an unfamiliar subcommand, decompress downloaded PDB archives with `gunzip -f`, and store all intermediate JSON responses in `scratch/`.
* **What to Improve in Skills:**
  * Standardize all skill CLI scripts to support optional `-o / --output <file>` (defaulting to `stdout` when omitted) and add an `--uncompress` flag to `pdb_database/scripts/download.py`.

---

### 11. Imprecise Gene-Range Coordinates (`None>None`) in ClinVar XML Records
* **Component:** `clinvar-database` (`scripts/clinvar_api.py`)
* **The Complication:**
  * Running `clinvar_api.py evidence` on many multi-submitter ClinVar Variation IDs returns gene-wide interval coordinates with null alleles (`"position_start": "<gene_start>", "position_stop": "<gene_end>", "reference_allele": null, "alternate_allele": null`) instead of the exact single-nucleotide VCF position and alleles.
* **Root Cause:**
  * ClinVar `VariationArchive` XML records frequently include a `<SequenceLocation>` element inside the `<Gene>` block (representing the full gene span) ahead of the allele-specific `<SequenceLocation>` element, and `clinvar_api.py` captures the first matching tag.
* **Agnostic Solution Pattern:**
  * Extract `"dbsnp_rsid"` from `allele_info` in the ClinVar evidence JSON and pass it to `dbsnp_database/scripts/dbsnp_cli.py` (`resolve-rsid` / `get-variant`) to recover exact GRCh38 (`NC_0000xx.xx`) VCF coordinates and alleles.
* **What to Improve in Skills:**
  * Restrict `<SequenceLocation>` extraction in `clinvar_api.py` to `<SimpleAllele>` / `<Measure>` nodes that possess non-empty `positionVCF`, `referenceAlleleVCF`, and `alternateAlleleVCF` attributes.

---

### 12. The 0-Based SPDI vs. 1-Based VCF Coordinate Off-by-One Trap & Minus-Strand Orientation
* **Component:** `dbsnp-database` (`scripts/dbsnp_cli.py`) & `gnomad-database` (`scripts/get_variant_frequency.py`)
* **The Complication:**
  * `dbsnp_cli.py get-variant <rsID>` returns genomic positions in NCBI **SPDI** format, which is **0-based**. Passing that position directly to 1-based VCF tools (`gnomad_database/scripts/get_variant_frequency.py --variant_id <chr>-<pos>-<ref>-<alt>`) fails with `"Variant not found"`.
  * For genes encoded on the **minus (`-`) strand**, coding HGVS substitutions (`c.`) are reverse-complemented relative to plus-strand GRCh38 genomic coordinates (`g.`).
* **Root Cause:**
  * Coordinate system mismatch between 0-based interbase SPDI coordinates and 1-based VCF/HGVS coordinates.
* **Agnostic Solution Pattern:**
  1. Run `dbsnp_cli.py resolve-rsid <rsID>`, which outputs both the 0-based SPDI coordinate and the 1-based genomic HGVS string (`g.<pos_1based><ref>><alt>`).
  2. Always compute `pos_1based_vcf = pos_0based_spdi + 1` and use plus-strand alleles when querying `gnomAD`, `ClinVar`, or `AlphaGenome`.
* **What to Improve in Skills:**
  * Rename the field in `dbsnp_cli.py get-variant` to `"position_0based_spdi"` and automatically emit `"position_1based_vcf"` and `"vcf_id_grch38": "<chr>-<pos+1>-<ref>-<alt>"`.

---

### 13. Transient gnomAD GraphQL `"Service overloaded"` Errors with Exit Code `0`
* **Component:** `gnomad-database` (`scripts/get_variant_frequency.py`)
* **The Complication:**
  * Launching $\ge 3$ concurrent queries against the public gnomAD GraphQL API frequently produces `{"errors": [{"message": "Service overloaded"}], "data": {"variant": null}}` while the Python script still exits with return code `0`.
* **Root Cause:**
  * GraphQL returns HTTP `200 OK` even when the backend rejects the query due to concurrency/rate limits, and `get_variant_frequency.py` writes the raw response without checking for `"errors"`.
* **Agnostic Solution Pattern:**
  * Always inspect the saved gnomAD JSON files for `"errors"` keys rather than trusting `exit code 0`, and limit parallel gnomAD invocations to $\le 2$ at a time.
* **What to Improve in Skills:**
  * Add automatic retry with exponential backoff in `gnomad_database` scripts whenever `"errors"` is present in the GraphQL JSON payload, and exit non-zero if all retries fail.

---

### 14. Overly Restrictive Entrez Property Combinations in ClinVar Search
* **Component:** `clinvar-database` (`scripts/clinvar_api.py search`)
* **The Complication:**
  * Combining multiple quoted Entrez filter clauses (such as `<GENE>[gene] AND "clinsig pathogenic"[Properties] AND "nonsense"[Molecular consequence] AND "criteria provided, multiple submitters, no conflicts"[Properties]`) often returns `0` matching variants even when hundreds exist.
* **Root Cause:**
  * NCBI Entrez `esearch` indexes molecular consequences and review statuses under specific internal filter names that do not always intersect cleanly when multiple `[Properties]` strings are combined with `AND`.
* **Agnostic Solution Pattern:**
  * Issue broader Entrez queries (e.g., `<GENE>[gene] AND "clinsig pathogenic"[Properties]`) and filter the resulting records locally in Python by inspecting `review_status`, `molecular_consequence_list`, and `clinical_significance` in the `clinvar_api.py summary` JSON output.
* **What to Improve in Skills:**
  * Add client-side post-filtering flags (e.g., `--min-review-stars`, `--consequence`) to `clinvar_api.py search` / `summary`.
