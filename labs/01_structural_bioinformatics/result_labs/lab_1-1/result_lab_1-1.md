# Exercise 1.1: Analyzing Tumor Suppressor p53 with AlphaFold

> [!IMPORTANT]
> **AlphaFold Database Terms Notice**: AlphaFold predictions are subject to the terms and conditions of the AlphaFold Protein Structure Database. Please check the terms of use at [https://alphafold.ebi.ac.uk/](https://alphafold.ebi.ac.uk/). A record of this notice has been saved to [.licenses/alphafold_database_fetch_and_analyze_LICENSE.txt](../../../../.licenses/alphafold_database_fetch_and_analyze_LICENSE.txt).

Using the **AlphaFold Database Fetch and Analyze** skill, the structure, API metadata, and Predicted Aligned Error (PAE) matrix for human Tumor Suppressor p53 (**UniProt ID: P04637**, 393 amino acids) were retrieved and analyzed.

---

### Downloaded Assets
- **Structure (mmCIF)**: [AF-P04637-F1-model_v6.cif](output/AF-P04637-F1-model_v6.cif) *(per-residue pLDDT values are stored in the B-factor column)*
- **PAE Matrix**: [AF-P04637-F1-predicted_aligned_error_v6.json](output/AF-P04637-F1-predicted_aligned_error_v6.json)
- **API Metadata**: [AF-P04637-F1-metadata.json](output/AF-P04637-F1-metadata.json)

---

### 1. Structural Confidence & pLDDT Distribution

| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **Overall Global pLDDT** | **75.06** | Moderate overall prediction confidence |
| **Very High (>90)** | **52.7%** | High-accuracy backbone and sidechain placement |
| **Confident (70–90)** | **7.1%** | Well-predicted backbone |
| **Low (50–70)** | **10.4%** | Flexible or low confidence backbone |
| **Very Low (<50)** | **29.8%** | Hallmark signature of intrinsic disorder |

* **pLDDT Conclusion**: The protein exhibits moderate global prediction confidence. It displays a bimodal confidence distribution: over half the protein is predicted with very high confidence (>90), while roughly 40% has low or very low confidence (<70), pointing to prominent flexible/disordered regions flanking a folded core.

---

### 2. Predicted Aligned Error (PAE) & Domain Boundaries

| PAE Metric | Value |
| :--- | :--- |
| **Matrix Dimensions** | 393 × 393 |
| **Mean Error** | 20.59 Å |
| **Max Error** | 32.00 Å *(maximum positional uncertainty)* |
| **Confident Residue Pairs (<5 Å)** | 21.8% |
| **Distinct Global Domains Detected** | **1 domain**: **residues 99 – 293** (Length: 195 AAs) |

* **PAE Structural Conclusion**: The protein consists of a single well-folded, rigid composite domain (residues 99–293, intra-domain mean PAE ~3.56 Å), flanked by unstructured, highly mobile regions that show no fixed spatial orientation relative to the core domain (TAD-to-DBD mean PAE ~30.88 Å).

---

> [!WARNING]
> **Explicit Structural Disorder Warning**:
> Approximately **40.2%** of full-length p53 has low or very low pLDDT (<70, with nearly 30% below 50), and the PAE matrix identifies only **one single rigid domain** across the entire 393-amino-acid chain.
> 
> **Downstream Analysis Guidance**:
> - **Do not** use the full-length monomer structure for whole-protein structural alignments (e.g., Foldseek) or rigid molecular docking, as the flexible terminal tails will produce arbitrary orientations and steric artifacts.
> - **Restrict downstream structural analyses strictly to the rigid DNA-binding domain boundaries: residues 99–293**.

---

### 3. Biological Reflection: TAD vs. DBD

The AlphaFold confidence and error metrics mirror the modular functional architecture of p53:

```
        TAD (1-61)         PRD (62-93)         DBD / Core Domain (99-293)           TD (325-356)  CTD (357-393)
[== Disordered (TAD1/2) ==][= Flexible =][======= Rigid DNA-Binding Domain ========][= Linker =][= Helix =][= Disordered =]
  pLDDT: ~47.6 (Very Low)    pLDDT: ~50.1             pLDDT: ~95.3 (Very High)                     pLDDT: ~90.9  pLDDT: ~43.4
  PAE vs DBD: ~30.9 Å                                 Intra-DBD PAE: ~3.56 Å
```

#### Transactivation Domain (TAD, residues 1–61)
* **Biological Function**: The N-terminal TAD (subdivided into TAD1 and TAD2) recruits basal transcriptional machinery (e.g., TFIID, TFIIH) and transcriptional co-activators (e.g., p300/CBP), while also mediating binding to negative regulators like MDM2. To interact promiscuously with distinct multimeric protein complexes, it relies on being an **intrinsically disordered region (IDR)** that can undergo coupled folding-upon-binding (e.g., forming an amphipathic α-helix only when engaging the hydrophobic cleft of MDM2).
* **AlphaFold Manifestation**: 
  - **pLDDT**: Low to very low (mean ~47.56, reaching down to 34.25). AlphaFold accurately recognizes that TAD lacks a fixed tertiary fold in isolation.
  - **PAE**: Dispersed intra-TAD error (~19.2 Å) and maximal inter-domain error relative to the DBD (~30.9 Å, close to the 32 Å limit). This confirms the absence of a defined tertiary position or packing interface against the core domain.

#### DNA-Binding Domain (DBD, residues 99–293)
* **Biological Function**: The central core domain is the sequence-specific DNA-binding module. It adopts an immunoglobulin-like β-sandwich architecture with two loop clusters (L2 and L3) that coordinate a structural $\text{Zn}^{2+}$ ion, as well as a loop-sheet-helix motif (L1 and H2) that inserts directly into the DNA major and minor grooves. Over 80% of cancer-associated somatic missense mutations in p53 (such as R175, G245, R248, R249, R273, R282) destabilize this folded core or disrupt its direct DNA contacts.
* **AlphaFold Manifestation**:
  - **pLDDT**: Exceptionally high (mean ~95.29, peaking at 98.69), reflecting a rigid, well-defined tertiary structure.
  - **PAE**: Dense cluster of confident residue pairs (intra-DBD mean PAE ~3.56 Å), causing the domain heuristic to delineate it as the **sole rigid global domain (residues 99–293)**.

#### Flanking Regulatory Regions (PRD, TD, and CTD)
* **Proline-Rich Domain (62–93)**: Acts as a flexible spacer regulating apoptosis; predicted with low confidence (pLDDT ~50.1).
* **Tetramerization Domain (325–356)**: Forms a short, confident α-helix (pLDDT ~90.9), but lacks fixed spatial orientation relative to the DBD (PAE ~20.9 Å) because in native conditions it assembles as a dimer-of-dimers (tetramer), which is not captured in this isolated monomer prediction.
* **C-Terminal Domain (357–393)**: Intrinsically disordered regulatory segment (pLDDT ~43.4) subject to extensive post-translational modifications (acetylation, ubiquitination, methylation, phosphorylation).