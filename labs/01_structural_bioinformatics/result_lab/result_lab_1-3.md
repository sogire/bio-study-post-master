> [!IMPORTANT]
> **PyMOL License Notice**: PyMOL visualizations are subject to the terms and licensing conditions of PyMOL (Schrödinger, Inc.). For details, visit [https://www.pymol.org/](https://www.pymol.org/). A record of this notice has been saved to [.licenses/pymol_LICENSE.txt](file:///home/sergiobermudez/local_projects/study-bio/.licenses/pymol_LICENSE.txt).

Using the **PyMOL** skill, a high-resolution cartoon rendering of the human **BRAF kinase domain** was generated from the AlphaFold model ([AF-P15056-F1-model_v6.cif](file:///home/sergiobermudez/local_projects/study-bio/data/alphafold_braf/AF-P15056-F1-model_v6.cif)).

---

### Generated Assets
- **High-Resolution PNG (300 DPI)**: [braf_kinase_domain.png](file:///home/sergiobermudez/local_projects/study-bio/output/braf_kinase_domain.png)
- **PyMOL Session File**: [braf_kinase_domain.pse](file:///home/sergiobermudez/local_projects/study-bio/output/braf_kinase_domain.pse)
- **Automated Render Script**: [render_braf.py](file:///home/sergiobermudez/local_projects/study-bio/scripts/render_braf.py)

---

### Visualization Preview

![BRAF Kinase Domain Rendering](file:///home/sergiobermudez/.gemini/antigravity-cli/brain/e5f8f09a-142d-496e-a6f1-403fb23e2c16/braf_kinase_domain.png)

---

### Structural Annotations

```
        N-Lobe (Teal, β-sheets & αC-helix)
                 \
                  [  ATP-Binding Pocket (Cyan Sticks)  ]
                 /                                      \
[ Hinge (Cys532) ]                                    [ DFG Motif (594-596) ]
                                                                 |
                                                      [ Val600 (Red Sticks) ]
                                                                 |
                 \                                    [ Activation Loop (Pink) ]
                  [  Catalytic Cleft / HRD Loop (Asp576)  ]
                 /
        C-Lobe (Slate, α-helical bundle)
```

1. **Domain Scaffold & Orientation**:
   - Oriented in the standard kinase perspective: the **N-terminal lobe** (residues 457–535, light teal) with its five-stranded antiparallel $\beta$-sheet and regulatory $\alpha$C-helix sits at the top.
   - The larger, primarily $\alpha$-helical **C-terminal lobe** (residues 536–717, slate) sits at the bottom.
2. **The ATP-Binding Pocket (Cyan Sticks)**:
   - **Glycine-rich loop (P-loop, 464–471)**: Caps the nucleotide phosphate-binding site.
   - **Catalytic Lys483 & $\alpha$C Glu501**: Form the conserved electrostatic salt bridge required for productive ATP coordination.
   - **Gatekeeper Thr529 & Hinge (530–535, Cys532)**: Govern deep pocket accessibility and provide hydrogen-bonding partners for kinase inhibitor hinge-binders.
   - **Catalytic Loop (574–578)**: Houses the invariant catalytic base Asp576.
   - **DFG Motif (Asp594–Gly596, wheat)**: The regulatory switch controlling the active ($\text{DFG-in}$) versus inactive ($\text{DFG-out}$) conformations.
3. **Residue Val600 (Prominent Red Sticks)**:
   - Positioned at residue 600 at the base of the activation segment (pink, residues 597–620), immediately downstream of the DFG motif.
   - **Biological & Oncogenic Context**: In wild-type BRAF, the hydrophobic Val600 sidechain packs into an autoinhibitory pocket between the $\alpha$C-helix and the activation segment, stabilizing the inactive state in the absence of upstream activation. The somatic **V600E** driver mutation introduces a bulky negative glutamate charge that acts as a phosphomimetic, creating an electrostatic repulsion that destabilizes the inactive conformation and constitutively flips the activation loop into an active, dimer-independent state.

---

### Interactive PyMOL Exploration
To inspect, rotate, and interact with the molecular model:
```bash
pymol output/braf_kinase_domain.pse
```
All named selections (`braf_kd`, `atp_pocket`, and `val600`) are preserved in the session.