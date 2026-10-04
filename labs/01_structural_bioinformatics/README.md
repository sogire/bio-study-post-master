# Module 1: AI & Modern Structural Bioinformatics

**Weeks 1–2 | Protein Biophysics, AlphaFold, Foldseek & PyMOL**

---

## 🔬 Biological Foundations

1. **Thermodynamics of Folding**:
   - Polypeptide chains collapse into tertiary structures driven by the **hydrophobic effect**: minimizing the exposure of non-polar side chains (Val, Leu, Ile, Phe) to surrounding aqueous solvent.
   - Polar and charged residues form exterior electrostatic networks (salt bridges, hydrogen bonds) that stabilize the fold and mediate protein-protein and protein-ligand interactions.
2. **Order vs. Intrinsic Disorder (IDRs)**:
   - Not all functional proteins adopt fixed 3D structures. Intrinsically Disordered Regions (IDRs) remain flexible, allowing multivalent binding (e.g., linear motifs), rapid post-translational modifications (phosphorylation), and biomolecular condensation (liquid-liquid phase separation).
3. **AlphaFold Confidence Interpretation**:
   - **pLDDT < 50**: Physical signature of intrinsic disorder, not an algorithm defect.
   - **pLDDT > 70–90**: High confidence; backbone conformation is reliable.
   - **pLDDT > 90**: Extremely high accuracy; side-chain rotamers are suitable for drug docking and pocket analysis.
   - **PAE (Predicted Aligned Error)**: Discloses inter-domain orientation. Low PAE across two domains indicates a rigid multi-domain unit; high PAE indicates domains connected by flexible linkers.

---

## 🛠️ Skills & Utility Scripts

- `alphafold-database-fetch-and-analyze`:
  - `fetch_structure.py P04637 -o data/`
  - `analyze_plddt.py data/AF-P04637-F1-metadata.json`
  - `analyze_pae.py data/AF-P04637-F1-predicted_aligned_error_v6.json`
- `foldseek-structural-search`:
  - `search.py data/AF-P15056-F1-model_v4.cif --database pdb100 --output data/braf_foldseek.json`
- `pymol`:
  - Headless OSMesa rendering to generate high-resolution PNGs and interactive `.pse` sessions.

---

## 💻 Executable Labs

### Week 1 Lab: AlphaFold Confidence & Domain Analysis (TP53)
Run the automated lab script:
```bash
uv run run_week1_alphafold.py
```
This fetches the human tumor suppressor TP53 (`P04637`), extracts pLDDT confidence statistics, and analyzes the PAE matrix to delineate the rigid DNA-binding domain from flexible transactivation and regulatory loops.
