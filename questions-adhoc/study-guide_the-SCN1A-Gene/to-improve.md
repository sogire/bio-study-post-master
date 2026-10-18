# 🛠️ Technical Issues, Complications & Solutions Log (`to-improve.md`)

**Study Context:** Comprehensive Multi-Modal Study Guide on the ***SCN1A* Gene ($\text{Na}_\text{V}1.1$)**  
**Study Guide Location:** [`questions-adhoc/study-guide_the-SCN1A-Gene/study-guide_the-SCN1A-Gene.md`](file:///home/sergiobermudez/local_projects/study-bio/questions-adhoc/study-guide_the-SCN1A-Gene/study-guide_the-SCN1A-Gene.md)  
**Skills Exercised:** `uv`, `literature-search-europepmc`, `uniprot-database`, `alphafold-database-fetch-and-analyze`, `pdb-database`, `pymol`, `gnomad-database`, `clinvar-database`, `dbsnp-database`, `credentials`

---

## Executive Summary

During the construction of the *SCN1A* study guide across three phases—**(1) Scientific Literature**, **(2) 3D Protein Structure & PyMOL Rendering**, and **(3) Clinical & Population Genetics**—we encountered **9 distinct technical complications** spanning sandbox filesystem isolation, external API security headers, coordinate system indexing (`0-based SPDI` vs. `1-based VCF`), incomplete clinical XML records, and inconsistent CLI flag conventions across skills.

Every issue was resolved during the study without losing data integrity. This document records each technical complication, its root cause, the exact approach used to solve it, and actionable recommendations to improve the skills and workflow in future studies.

---

## Summary Matrix of Issues & Solutions

| # | Phase | Skill / Component | Technical Issue / Complication | Approach Used to Solve It |
| :-: | :--- | :--- | :--- | :--- |
| **1** | Setup & Env | `uv` / Terminal Sandbox | `uv` (`~/.local/bin/uv`) is invisible inside the default terminal sandbox (`BypassSandbox: false`), causing `No such file or directory` (`exit 127`) and triggering unnecessary reinstallation attempts (`curl ... \| sh`). | Verified `/home/sergiobermudez/.local/bin/uv` with `BypassSandbox: true` and codified workspace rules in [`GEMINI.md`](file:///home/sergiobermudez/local_projects/study-bio/GEMINI.md) to never reinstall `uv` or `pymol` and always invoke `uv` with `BypassSandbox: true`. |
| **2** | Phase 1: Literature | `literature-search-europepmc` | Large JSON search outputs (`365 KB` / `10,678` lines) combined with `jq: command not found` (`exit 127`) in the Linux environment and `view_file` truncation limits (`46 KB`). | Replaced `jq` with targeted `grep -n` field extraction and Python one-liners, and used `ContentOffset` pagination in `view_file` to read `74 KB` full-text articles (`PMC10779156`). |
| **3** | Phase 2: Structure | `alphafold-database-fetch-and-analyze` | `fetch_alphafold.py P35498` failed with `HTTP Error 403 Forbidden` because EBI blocks requests when `POLITE_HTTP_USER_AGENT` defaults to an empty string `""`. | Passed `POLITE_HTTP_USER_AGENT="Mozilla/5.0 (X11; Linux x86_64) StudyBio/1.0"` in the environment when calling `fetch_alphafold.py`. |
| **4** | Phase 2: Structure | `alphafold-database-fetch-and-analyze` | `analyze_plddt.py` rejected `AF-P35498-F1-metadata.json` (`Expecting value: line 1 column 1` / wrong schema) because its positional argument `metadata_file` actually expects `AF-P35498-F1_summary.json`, and it only reports a single global mean pLDDT (`68.50`). | Passed `AF-P35498-F1_summary.json` to `analyze_plddt.py` and wrote a custom PyMOL/Python parser (`render_scn1a_structures.py`) to compute per-domain pLDDT directly from the `.cif` B-factors (`88.6–91.0` in transmembrane domains vs. `42.1–51.5` in linkers). |
| **5** | Phase 2 & 3 | `uniprot`, `pdb`, `clinvar`, `gnomad` | Inconsistent CLI script names and output flags (`stdout` vs. `-o` vs. `--output`, `--ids` vs. `--variant_ids`, `download.py` vs. `download_pdb.py`, `clinvar_api.py` vs. `dbsnp_cli.py`). | Checked `--help` / `SKILL.md` per script, decompressed `.cif.gz` files with `gunzip -f`, and standardized outputs to `scratch/`. |
| **6** | Phase 3: Genetics | `clinvar-database` | `clinvar_api.py evidence` returned gene-wide interval coordinates with null alleles (`chr2:165957418:None>None`) instead of exact VCF coordinates for several classic variants (`12902`, `68578`, `189913`, `189921`). | Extracted `dbsnp_rsid` from each ClinVar evidence JSON and queried `dbsnp_database/scripts/dbsnp_cli.py` (`get-variant` & `resolve-rsid`) to recover exact `NC_000002.12` (GRCh38) coordinates and alleles. |
| **7** | Phase 3: Genetics | `dbsnp-database` & `gnomad-database` | **0-based SPDI vs. 1-based VCF off-by-one trap:** `dbsnp_cli.py get-variant` returns 0-based SPDI positions (e.g., `165992419`), which fail with `"Variant not found"` in gnomAD (`get_variant_frequency.py`) unless converted to 1-based VCF (`165992420`) and reverse-complemented for the minus (`-`) strand. | Used `dbsnp_cli.py resolve-rsid` to verify 1-based HGVS coordinates (`g.165992420T>C`), applied `pos_1based = pos_spdi + 1` across all 8 variants, and successfully retrieved gnomAD v4 frequencies. |
| **8** | Phase 3: Genetics | `gnomad-database` | Running 3 concurrent `get_variant_frequency.py` requests against the public gnomAD GraphQL API triggered `"Service overloaded"` errors inside the JSON response while still exiting with `code 0`. | Inspected every output JSON file to catch silent GraphQL errors, reduced concurrency to $\le 2$ parallel requests, and retried the affected variant cleanly. |
| **9** | Phase 3: Genetics | `clinvar-database` | Combining multiple strict Entrez property filters (e.g., `"nonsense"[Molecular consequence] AND "criteria provided, multiple submitters, no conflicts"[Properties]`) returned `0` results in `clinvar_api.py search`. | Queried ClinVar with broader molecular consequence or protein-level terms and filtered by `review_status` locally in the output `summary` JSON. |

---

## Detailed Analysis of Each Technical Issue & Solution

### 1. Terminal Sandbox Isolation Hiding `~/.local/bin/uv` & Pre-Cached Packages
* **Phase & Skill:** Initial Setup (`uv` & `pymol` skills)
* **The Complication:**
  * When checking for `uv` via `uv --version` and `/home/sergiobermudez/.local/bin/uv --version` in the default sandboxed terminal (`BypassSandbox: false`), bash returned `exit code 127: No such file or directory`.
  * Following the standard fallback in `uv/SKILL.md` (`curl -LsSf https://astral.sh/uv/install.sh | sh`) failed in the sandbox due to lack of network access (`Could not resolve host: astral.sh`) and prompted an unnecessary unsandboxed install request that the user declined.
* **Root Cause:**
  * The default sandbox (`BypassSandbox: false`) isolates the filesystem to the active workspace (`/home/sergiobermudez/local_projects/study-bio`), `/tmp`, and standard system directories (`/usr/bin`, `/bin`). User-level directories outside the workspace—specifically `/home/sergiobermudez/.local/bin/uv`, `~/.cache/uv`, and `~/.local/share/uv`—are not mounted inside the sandbox, making `uv` appear missing when it is already installed (`uv 0.13.1`).
* **Approach Used to Solve It:**
  1. Verified `/home/sergiobermudez/.local/bin/uv --version` with `BypassSandbox: true`, confirming `uv 0.13.1` and pre-cached `pymol-open-source-whl` were already installed.
  2. Documented persistent workspace rules in [`GEMINI.md`](file:///home/sergiobermudez/local_projects/study-bio/GEMINI.md) stating that `uv` and `pymol` are pre-installed, must never be reinstalled, and must be invoked with `BypassSandbox: true`.
* **What to Improve:**
  * Update `uv/SKILL.md` to note that in sandboxed agent environments, `No such file or directory` on `~/.local/bin/uv` can be caused by sandbox mount isolation rather than a missing installation, and agents should check `~/.local/bin/uv --version` with `BypassSandbox: true` before attempting to download and run `install.sh`.

---

### 2. Missing `jq` Utility & Large Literature Search Payloads
* **Phase & Skill:** Phase 1 — Literature Search (`literature-search-europepmc`)
* **The Complication:**
  * Searching Europe PMC for open-access reviews (`scn1a_reviews.json`) produced a `365 KB` (`10,678`-line) JSON file.
  * Running `jq` to summarize the JSON failed with `bash: line 1: jq: command not found` (`exit code 127`), and `view_file` is capped at `800` lines or `46,080` bytes per call.
* **Root Cause:**
  * The host Linux environment does not have `jq` installed in `/usr/bin`, and Europe PMC's `search` command includes full abstract texts and author lists for up to 25–50 records per file.
* **Approach Used to Solve It:**
  1. Used sandboxed `grep -n` commands (`grep -n '"title":\|"pmid":\|"pmcid":\|"doi":\|"pubYear":\|"citedByCount":'`) and lightweight `python3 -c "import json..."` one-liners (since `python3` stdlib `json` is always available inside the sandbox) to rank papers by citation count and publication year.
  2. When viewing `74 KB` full-text files (`PMC10779156_fulltext.txt`), used `view_file` with `ContentOffset: 46080` to read the second half of the manuscript seamlessly.
* **What to Improve:**
  * Add a `--summary` or `--fields pmid,pmcid,title,pubYear,citedByCount` option to `literature_search_europepmc` scripts, or recommend `python3 -m json.tool` / `python3 -c` instead of `jq` in skill documentation.

---

### 3. AlphaFold EBI API `HTTP 403 Forbidden` on Empty `User-Agent`
* **Phase & Skill:** Phase 2 — 3D Protein Structure (`alphafold-database-fetch-and-analyze`)
* **The Complication:**
  * Running `/home/sergiobermudez/.local/bin/uv run .../fetch_alphafold.py P35498` failed with:
    `[!] HTTP error fetching API data: HTTP Error 403 while fetching https://alphafold.ebi.ac.uk/api/prediction/P35498 (Hint: this may be caused by the User-Agent ''. Override it by setting the POLITE_HTTP_USER_AGENT environment variable.)`
* **Root Cause:**
  * `fetch_alphafold.py` reads `os.environ.get("POLITE_HTTP_USER_AGENT", "")` and sets the HTTP `User-Agent` header to `""` (empty string) when the environment variable is not set. EBI's firewall rejects requests with an empty `User-Agent` header with `HTTP 403 Forbidden`.
* **Approach Used to Solve It:**
  * Re-ran `fetch_alphafold.py` with an explicit user agent:
    `POLITE_HTTP_USER_AGENT="Mozilla/5.0 (X11; Linux x86_64) StudyBio/1.0"`
    which succeeded immediately and downloaded `AF-P35498-F1-model_v6.cif`, `AF-P35498-F1-model_v6.pdb`, `AF-P35498-F1-predicted_aligned_error_v6.json`, `AF-P35498-F1-metadata.json`, and `AF-P35498-F1_summary.json`.
* **What to Improve:**
  * In `alphafold_database_fetch_and_analyze/scripts/fetch_alphafold.py`, provide a sensible non-empty default fallback for `POLITE_HTTP_USER_AGENT` (e.g., `"DeepMind-Science-Skills/1.0 (python-urllib)"`) instead of `""`.

---

### 4. Misleading `metadata_file` Argument & Global-Only Metrics in `analyze_plddt.py`
* **Phase & Skill:** Phase 2 — 3D Protein Structure (`alphafold-database-fetch-and-analyze`)
* **The Complication:**
  * `analyze_plddt.py -h` shows `usage: analyze_plddt.py [-h] metadata_file`. However, passing `AF-P35498-F1-metadata.json` (which `fetch_alphafold.py` explicitly logs as `Saved API metadata to: .../AF-P35498-F1-metadata.json`) caused `analyze_plddt.py` to fail or misparse, because it actually expects `AF-P35498-F1_summary.json`.
  * Furthermore, `analyze_plddt.py` only prints the **overall global pLDDT (`68.50`)** and fraction of confident residues (`65.0%`), which is misleading for a multi-domain membrane channel like $\text{Na}_\text{V}1.1$ that has rigid transmembrane domains connected by long disordered intracellular loops.
* **Root Cause:**
  * `fetch_alphafold.py` saves two JSON files (`-metadata.json` and `_summary.json`), and `analyze_plddt.py` names its argument `metadata_file` even though it reads the schema of `_summary.json`. It also does not parse per-residue pLDDT values from the `.cif` structure file.
* **Approach Used to Solve It:**
  1. Passed `AF-P35498-F1_summary.json` to `analyze_plddt.py` to obtain the global metrics.
  2. Wrote a custom PyMOL/Python analysis script (`render_scn1a_structures.py`) that loaded `AF-P35498-F1-model_v6.cif` and calculated mean pLDDT (`b` factor) across exact UniProt domain boundaries—proving that the four transmembrane repeats (`DI–DIV`) have very high confidence (**`88.6–91.0` pLDDT**), whereas the intracellular linkers (`DI–DII` linker `42.1`, `DII–DIII` linker `51.5`) are intrinsically disordered (`< 50` pLDDT).
* **What to Improve:**
  * Rename the positional argument in `analyze_plddt.py` to `summary_or_cif_file` and support parsing `.cif`/`.pdb` B-factor columns directly to report per-region pLDDT statistics.

---

### 5. Inconsistent CLI Conventions Across Bio-Database Skills
* **Phase & Skill:** Phases 2 & 3 (`uniprot-database`, `pdb-database`, `clinvar-database`, `dbsnp-database`, `gnomad-database`)
* **The Complication:**
  * Several commands failed on the first invocation (`exit code 2`) due to subtle differences in CLI naming and argument conventions across skills:
    1. **Script filenames:** `clinvar_database` uses `scripts/clinvar_api.py`, `dbsnp_database` uses `scripts/dbsnp_cli.py`, `uniprot_database` uses `scripts/uniprot_tools.py`, and `pdb_database` uses `scripts/download.py` (while `search_pdb.py` and `fetch_pdb_metadata.py` include `_pdb` in the filename).
    2. **Output redirection vs. `-o`/`--output`:** `uniprot_tools.py get` and `search_pdb.py` print to `stdout` and fail if given `-o`/`--output`, whereas `fetch_pdb_metadata.py`, `clinvar_api.py`, `dbsnp_cli.py`, and `get_variant_frequency.py` *require* `--output` and fail if omitted.
    3. **List arguments:** `clinvar_api.py summary` requires `--variant_ids ID1 ID2 ...` (space-separated `nargs='+'`), whereas other tools accept comma-separated IDs.
    4. **Compressed PDB downloads:** `pdb_database/scripts/download.py` downloads `.cif.gz` archives (`pdb_00007dtd.cif.gz`) rather than uncompressed `.cif` files.
* **Approach Used to Solve It:**
  * Checked `SKILL.md` and `--help` outputs whenever a CLI flag mismatch occurred, ran `gunzip -f` on `pdb_00007dtd.cif.gz`, and copied clean `.cif` files into `questions-adhoc/study-guide_the-SCN1A-Gene/structures/`.
* **What to Improve:**
  * Standardize CLI arguments across all `deepmind-science` skills so every script supports `-o / --output <file>` (defaulting to `stdout` if omitted) and accepts both comma-separated and space-separated ID lists.

---

### 6. Imprecise Gene-Range Coordinates (`None>None`) in ClinVar XML Records
* **Phase & Skill:** Phase 3 — Clinical & Population Genetics (`clinvar-database` & `dbsnp-database`)
* **The Complication:**
  * A core rule of `clinvar-database` is to always report genomic coordinates in `<chrom>:<pos>:<ref>><alt>` format (GRCh38).
  * However, when we ran `clinvar_api.py evidence` on our key benchmark variants (`12902` / `p.Phe1499Leu`, `68578` / `p.Thr226Met`, `189913` / `p.Asp382Glu`, `189921` / `p.Arg1645Ter`, `12889` / `p.Arg222Ter`), the parsed JSON returned:
    * `"position_start": "165957418", "position_stop": "166036400", "reference_allele": null, "alternate_allele": null` (`chr2:165957418:None>None`).
* **Root Cause:**
  * In NCBI ClinVar's public XML (`VariationArchive`), many older or multi-submitter records store the `<SequenceLocation>` at the `<Gene>` element level (the start and stop coordinates of the entire *SCN1A* gene or transcript) before or instead of the allele-specific VCF attributes, causing `clinvar_api.py`'s XML parser to pick up the gene range without `reference_allele` / `alternate_allele`.
* **Approach Used to Solve It:**
  * Followed the fallback protocol in `clinvar-database/SKILL.md`: extracted `"dbsnp_rsid"` from `allele_info` in each ClinVar evidence JSON (`rs121918632`, `rs121917984`, `rs794726753`, `rs1553541206`, `rs1690583220`, `rs794726759`, `rs121918624`, `rs373967247`) and resolved each `rsID` via `dbsnp_database/scripts/dbsnp_cli.py` to obtain exact GRCh38 (`NC_000002.12`) single-nucleotide positions and alleles.
* **What to Improve:**
  * Update `clinvar_api.py`'s XML parser so it specifically scopes `<SequenceLocation>` lookup to `<SimpleAllele>` / `<Measure>` nodes that contain non-empty `positionVCF`, `referenceAlleleVCF`, and `alternateAlleleVCF` attributes, ignoring `<Gene>`-level `<SequenceLocation>` tags.

---

### 7. The 0-Based SPDI vs. 1-Based VCF Coordinate Off-by-One Trap & Minus-Strand Orientation
* **Phase & Skill:** Phase 3 — Clinical & Population Genetics (`dbsnp-database` & `gnomad-database`)
* **The Complication:**
  * After running `dbsnp_cli.py get-variant rs373967247` (for the common benign polymorphism `p.Met1619Val`), the output JSON reported:
    `"seq_id": "NC_000002.12", "deleted_sequence": "T", "inserted_sequence": "C", "position": 165992419`.
  * When we queried `gnomad_database/scripts/get_variant_frequency.py --variant_id 2-165992419-T-C`, gnomAD returned `"Variant not found"` (`variant: null`), even though `dbsnp_rs373967247.json` clearly showed `392` alleles in `GnomAD_exomes`!
* **Root Cause:**
  * NCBI's `get-variant` endpoint uses **SPDI (Sequence-Position-Deletion-Insertion)** notation, which is **0-based** (`165992419`), whereas **VCF, ClinVar, and gnomAD** use **1-based** genomic coordinates (`165992420`).
  * Additionally, because *SCN1A* is encoded on the **minus (`-`) strand** of Chromosome 2, coding cDNA substitutions (`NM_001165963.4:c.4855A>G`, `c.677C>T`) are reverse-complemented on the plus-strand GRCh38 reference assembly (`T>C`, `G>A`).
* **Approach Used to Solve It:**
  1. Ran `dbsnp_cli.py resolve-rsid rs373967247`, which outputs both the 0-based SPDI (`165992419`) and the 1-based HGVS string (`NC_000002.12:g.165992420T>C`), immediately exposing the 1-bp offset (`1-based VCF = 0-based SPDI + 1`).
  2. Converted all 8 benchmark variants to 1-based GRCh38 coordinates (`chr2:165992420:T>C`, `chr2:165996099:A>G`, `chr2:166052869:G>A`, `chr2:165992342:G>A`, etc.).
  3. Re-queried `get_variant_frequency.py` with `--variant_id 2-165992420-T-C`, which immediately returned the full gnomAD v4 dataset (`401 / 1,461,354` exome alleles, `7` healthy homozygotes in South Asia).
* **What to Improve:**
  * Update `dbsnp_cli.py get-variant` so that its output JSON explicitly labels `"position_0based_spdi": 165992419` and automatically includes `"position_1based_vcf": 165992420` (and `"vcf_id_grch38": "2-165992420-T-C"`), preventing off-by-one errors when piping dbSNP coordinates into gnomAD or AlphaGenome.

---

### 8. Transient gnomAD GraphQL `"Service overloaded"` Errors with Exit Code `0`
* **Phase & Skill:** Phase 3 — Clinical & Population Genetics (`gnomad-database`)
* **The Complication:**
  * When launching 3 parallel `get_variant_frequency.py` commands against the public gnomAD GraphQL API, one command returned:
    `{"errors": [{"message": "Service overloaded"}], "data": {"variant": null}}`
    while still exiting with return code `0` (looking identical at the shell level to a successful query).
* **Root Cause:**
  * The public gnomAD GraphQL endpoint (`https://gnomad.broadinstitute.org/api`) enforces strict rate/concurrency limits and returns HTTP 200 with a JSON `"errors"` field when overloaded.
* **Approach Used to Solve It:**
  * Always inspected the generated JSON files with `view_file` rather than trusting `exit code 0`, noticed `"message": "Service overloaded"`, and re-ran the queries sequentially / in pairs (`<= 2` at a time), which succeeded in ~5 seconds per query.
* **What to Improve:**
  * Enhance `gnomad_database/scripts/get_variant_frequency.py` (and other gnomAD scripts) to check if `"errors"` is present in the GraphQL JSON response: if `"Service overloaded"` or rate-limiting occurs, automatically retry with exponential backoff (e.g., 2s, 4s, 8s) and exit with a non-zero exit code if retries are exhausted.

---

### 9. Overly Restrictive Entrez Property Combinations in ClinVar Search
* **Phase & Skill:** Phase 3 — Clinical & Population Genetics (`clinvar-database`)
* **The Complication:**
  * Searching ClinVar with combined property filters like:
    `SCN1A[gene] AND "clinsig pathogenic"[Properties] AND "nonsense"[Molecular consequence] AND "criteria provided, multiple submitters, no conflicts"[Properties]`
    returned `Total matching variants: 0`, even though *SCN1A* has 554 pathogenic nonsense variants in ClinVar.
* **Root Cause:**
  * NCBI Entrez's `clinvar` database indexes review status strings and molecular consequences under specific filter/property aliases that do not always intersect as expected when multiple quoted `[Properties]` clauses are combined with `AND`.
* **Approach Used to Solve It:**
  * Simplified the Entrez search query (e.g., `SCN1A[gene] AND "clinsig pathogenic"[Properties] AND "nonsense"[Molecular consequence]` or searching specific well-characterized nonsense variants like `"p.Arg1645Ter" OR "p.Arg222Ter"`), fetched their summaries via `clinvar_api.py summary`, and verified `"review_status": "criteria provided, multiple submitters, no conflicts"` (`★★☆☆`) directly in the returned JSON.
* **What to Improve:**
  * Document tested Entrez filter combinations for star ratings in `clinvar_database/SKILL.md`, or add a client-side `--min-stars 2` filter flag to `clinvar_api.py summary`.

