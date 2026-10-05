> [!IMPORTANT]
> **Foldseek & RCSB PDB Terms of Use**: Structural searches and metadata retrieval were conducted in accordance with the terms of service of [Foldseek](https://search.foldseek.com/search) and the [RCSB Protein Data Bank](https://www.rcsb.org/pages/usage-policy). License acknowledgments are recorded in [.licenses/foldseek_structural_search_LICENSE.txt](file:///home/sergiobermudez/local_projects/study-bio/.licenses/foldseek_structural_search_LICENSE.txt) and [.licenses/pdb_database_LICENSE.txt](file:///home/sergiobermudez/local_projects/study-bio/.licenses/pdb_database_LICENSE.txt).

The AlphaFold structure for human **Serine/threonine-protein kinase B-raf** (**UniProt: P15056**, 766 amino acids) was fetched and submitted to a 3D structural alignment search against the **PDB100** database using the **Foldseek Structural Search** and **RCSB PDB Database** skills.

---

### Output Files Generated
- **AlphaFold Structure**: [AF-P15056-F1-model_v6.cif](file:///home/sergiobermudez/local_projects/study-bio/data/alphafold_braf/AF-P15056-F1-model_v6.cif)
- **Foldseek Markdown Summary**: [braf_foldseek_pdb100.md](file:///home/sergiobermudez/local_projects/study-bio/data/braf_foldseek_pdb100.md)
- **Foldseek Raw JSON Payload**: [braf_foldseek_pdb100.json](file:///home/sergiobermudez/local_projects/study-bio/data/braf_foldseek_pdb100.json)
- **PDB Ligand Metadata**: [pdb_ligands_top10.json](file:///home/sergiobermudez/local_projects/study-bio/data/pdb_ligands_top10.json) and [pdb_ligands_prominent.json](file:///home/sergiobermudez/local_projects/study-bio/data/pdb_ligands_prominent.json)

---

### 1. Top Structural Hits from Foldseek against PDB100

Foldseek results partition into two structural classes based on query coverage:
1. **Multi-domain Cryo-EM Complexes (Q-Cov ~76%)**: Align across both the regulatory Ras-binding/cysteine-rich domains (RBD/CRD) and the kinase domain.
2. **High-Resolution Kinase Domain Co-crystals (Q-Cov ~35–36%)**: Align specifically to the ~274-residue catalytic core (residues 457–717).

| Rank | PDB Target ID | Description / State | Q-Cov | Prob | E-value | Seq Identity | Aligned Length |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **1** | **[8DGS](https://www.rcsb.org/structure/8DGS)** (Chain A) | Cryo-EM structure of a RAS/RAF complex (state 1) | **76.2%** | **1.000** | $1.72 \times 10^{-64}$ | 72.7% | 584 AAs |
| **2** | **[7MFD](https://www.rcsb.org/structure/7MFD)** (Chain A) | Autoinhibited BRAF:(14-3-3)$_2$:MEK complex with RBD | **76.1%** | **1.000** | $1.66 \times 10^{-55}$ | 70.1% | 583 AAs |
| **3** | **[7MFE](https://www.rcsb.org/structure/7MFE)** (Chain A) | Autoinhibited BRAF:(14-3-3)$_2$ complex with RBD | **76.1%** | **1.000** | $3.84 \times 10^{-52}$ | 69.9% | 583 AAs |
| **4** | **[6NYB](https://www.rcsb.org/structure/6NYB)** (Chain A) | Structure of a MAPK pathway complex (BRAF:MEK1:14-3-3) | **66.1%** | **1.000** | $9.17 \times 10^{-50}$ | 68.9% | 506 AAs |
| **5** | **[5FD2](https://www.rcsb.org/structure/5FD2)** (Chain A) | BRAF WT kinase domain + purinylpyridinylamino inhibitor | **35.4%** | **1.000** | $4.88 \times 10^{-43}$ | 96.6% | 271 AAs |
| **6** | **[4EHG](https://www.rcsb.org/structure/4EHG)** (Chain A) | BRAF kinase domain + aminopyrimidine-based inhibitor | **35.8%** | **1.000** | $5.16 \times 10^{-43}$ | 94.5% | 274 AAs |
| **7** | **[4EHE](https://www.rcsb.org/structure/4EHE)** (Chain A) | BRAF kinase domain + aminothienopyrimidine-based inhibitor | **35.8%** | **1.000** | $5.16 \times 10^{-43}$ | 96.3% | 274 AAs |
| **8** | **[4PP7](https://www.rcsb.org/structure/4PP7)** (Chain A) | BRAF(V600E) kinase domain + 3-N-methylquinazoline-4(3H)-one | **35.5%** | **1.000** | $6.09 \times 10^{-43}$ | 97.4% | 272 AAs |
| **9** | **[6N0P](https://www.rcsb.org/structure/6N0P)** (Chain A) | BRAF kinase domain + LXH254 (naporafenib) | **35.6%** | **1.000** | $1.00 \times 10^{-42}$ | 98.1% | 273 AAs |
| **10** | **[4FC0](https://www.rcsb.org/structure/4FC0)** (Chain B) | BRAF kinase domain + DFG-out inhibitor | **35.4%** | **1.000** | $1.32 \times 10^{-42}$ | 96.3% | 271 AAs |

*All top 10 hits have a structural probability score of **1.000 (100%)**, indicating unequivocal structural alignment with negligible E-values ($10^{-42}$ to $10^{-64}$).*

---

### 2. Experimental Ligands and Bound Inhibitors

GraphQL queries to the RCSB PDB Data API identified the bound chemical components across the top structural entries:

#### A. Multi-Protein Signaling Complexes
* **[8DGS](https://www.rcsb.org/structure/8DGS)**: 
  - **LCJ** (trametinib analogue / allosteric MEK inhibitor): Imidazo[1,5-a]pyridine-6-carboxamide.
  - **GNP** (GppNHp): Non-hydrolyzable GTP analogue bound to KRAS.
  - **AGS**: ATP-$\gamma$-S in the active kinase cleft.
  - **ZN**: Structural zinc ions coordinated within the BRAF C1/cysteine-rich domain (CRD).
* **[7MFD](https://www.rcsb.org/structure/7MFD)**:
  - **CHU**: Chromen-2-one derivative stabilizing the autoinhibited BRAF:MEK interface.
  - **ZN**: Structural zinc ions in the CRD.
* **[6NYB](https://www.rcsb.org/structure/6NYB)**:
  - **LCJ**: Imidazo[1,5-a]pyridine allosteric MEK inhibitor.
  - **AGS** / **ADP** / **MG**: Nucleotide cofactors.
  - **ZN**: Structural zinc ions.

#### B. Top BRAF Kinase Domain Small-Molecule Inhibitors
* **[5FD2](https://www.rcsb.org/structure/5FD2)**: Bound to **5XJ** (purinylpyridinylamino-based ATP-competitive inhibitor).
* **[4EHG](https://www.rcsb.org/structure/4EHG)**: Bound to **RI9** (aminopyrimidine-based sulfonamide inhibitor).
* **[4EHE](https://www.rcsb.org/structure/4EHE)**: Bound to **RI8** (aminothienopyrimidine-7-carboxamide sulfonamide inhibitor).
* **[4PP7](https://www.rcsb.org/structure/4PP7)**: Bound to **2VX** (3-N-methylquinazoline-4(3H)-one sulfonamide targeting BRAF$^{V600E}$).
* **[6N0P](https://www.rcsb.org/structure/6N0P)** / **[8F7P](https://www.rcsb.org/structure/8F7P)**: Bound to **K81** (**LXH254 / naporafenib**), a clinical pan-RAF dimer inhibitor.
* **[4FC0](https://www.rcsb.org/structure/4FC0)**: Bound to **0T2** (Type II DFG-out thiazolopyridine inhibitor).

#### C. Clinically Prominent BRAF Inhibitors in the Hit List
Querying corresponding hits deeper in the ranking identifies standard-of-care and investigational therapeutics:
* **[5HIE](https://www.rcsb.org/structure/5HIE)** / **[5CSW](https://www.rcsb.org/structure/5CSW)**: **Dabrafenib** (Comp ID: `P06`, FDA-approved Type 1.5 $\alpha\text{C-in}/\text{DFG-in}$ inhibitor).
* **[3OG7](https://www.rcsb.org/structure/3OG7)**: **Vemurafenib / PLX4032** (Comp ID: `032`, FDA-approved Type 1.5 inhibitor).
* **[8F7O](https://www.rcsb.org/structure/8F7O)**: **Tovorafenib / TAK580** (Comp ID: `QOP`, Type II dimer-breaker pan-RAF inhibitor).
* **[4KSP](https://www.rcsb.org/structure/4KSP)**: **TAK-632** (Comp ID: `1SU`, potent DFG-out pan-RAF inhibitor).
* **[5HI2](https://www.rcsb.org/structure/5HI2)**: **Sorafenib** (Comp ID: `BAX`, multikinase/Type II DFG-out inhibitor).
* **[5C9C](https://www.rcsb.org/structure/5C9C)**: **LY3009120** (Comp ID: `4Z5`, pan-RAF dimer inhibitor).

---

### 3. Kinome-Wide Structural Homologues & Functional Diversity

Beyond BRAF itself, Foldseek matched a broad spectrum of structural homologues across the human kinome (Prob = 1.000, Seq Identity 25–35%, E-values $10^{-18}$ to $10^{-34}$):

1. **Paralogous RAF Kinases & Pseudokinases**:
   - **C-RAF / RAF-1** ([3OMV](https://www.rcsb.org/structure/3OMV), [8GFT](https://www.rcsb.org/structure/8GFT)): Closest structural homologue (Seq ID ~75.5%).
   - **KSR1 & KSR2** ([7JUS](https://www.rcsb.org/structure/7JUS), [7JUZ](https://www.rcsb.org/structure/7JUZ), [5KKR](https://www.rcsb.org/structure/5KKR)): MAPK pathway scaffold pseudokinases bound to MEK1 and cobimetinib/selumetinib.
2. **Src-Family Non-Receptor Tyrosine Kinases**:
   - Extensive matches to **c-Src** ([7NG7](https://www.rcsb.org/structure/7NG7), [4K11](https://www.rcsb.org/structure/4K11), [6F3F](https://www.rcsb.org/structure/6F3F), [1FMK](https://www.rcsb.org/structure/1FMK)), **LCK** ([3MPM](https://www.rcsb.org/structure/3MPM)), **HCK** ([5H09](https://www.rcsb.org/structure/5H09)), and **FYN** ([2DQ7](https://www.rcsb.org/structure/2DQ7)) in complex with bosutinib, dasatinib, and imatinib.
3. **Receptor Tyrosine Kinases (RTKs)**:
   - **Ephrin Receptors** (**EphA2**, **EphB4**, **EphB1**; e.g. [8BK0](https://www.rcsb.org/structure/8BK0), [5NK4](https://www.rcsb.org/structure/5NK4), [6HES](https://www.rcsb.org/structure/6HES)): Over 30 co-crystals representing one of the largest structural clusters.
   - **RET** ([5FM3](https://www.rcsb.org/structure/5FM3), [6I82](https://www.rcsb.org/structure/6I82)), **FGFR1** ([6C1O](https://www.rcsb.org/structure/6C1O)), **EGFR** ([5GNK](https://www.rcsb.org/structure/5GNK), [6DUK](https://www.rcsb.org/structure/6DUK)), and **c-MET** ([3A4P](https://www.rcsb.org/structure/3A4P)).
4. **Tec-Family Kinases**:
   - **BTK** ([5BQ0](https://www.rcsb.org/structure/5BQ0), [7N4Q](https://www.rcsb.org/structure/7N4Q), [5P9J](https://www.rcsb.org/structure/5P9J), [8FLN](https://www.rcsb.org/structure/8FLN)): Bound to ibrutinib, tirabrutinib, and pirtobrutinib.
5. **Necroptosis Regulators**:
   - **RIPK1** ([4NEU](https://www.rcsb.org/structure/4NEU), [6HHO](https://www.rcsb.org/structure/6HHO), [7FCZ](https://www.rcsb.org/structure/7FCZ)): Bound to necrostatin analogues.