# Lab Guide 1: Structural Biology & Protein Biophysics

**Focus**: Dissecting Protein Order, Intrinsic Disorder, and 3D Fold Homology  
**Primary Skills**: `alphafold-database-fetch-and-analyze`, `foldseek-structural-search`, `pdb-database`, `pymol`

---

## 🧬 Biological Context & Intuition

When a ribosome translates an mRNA transcript, a linear chain of amino acids emerges. How does it know how to fold?
1. **The Hydrophobic Drive**: Hydrophobic side chains (Leu, Ile, Val, Phe) disrupt the hydrogen-bonding network of surrounding water. To minimize the system's Gibbs free energy ($\Delta G = \Delta H - T\Delta S$), the protein collapses, burying non-polar residues in an anhydrous core while exposing polar and charged residues to the solvent.
2. **Intrinsic Disorder (IDRs)**: Regions lacking bulky hydrophobic residues cannot drive hydrophobic collapse. They remain intrinsically disordered in solution (like boiled spaghetti). These IDRs are crucial for biological signaling because they can bind multiple different partners with high specificity but low affinity, allowing rapid on/off switching.
3. **Deciphering AlphaFold Metrics**:
   - **pLDDT**:
     - $>90$: Extremely high confidence. Side-chain conformations and pocket shapes are accurate.
     - $70-90$: Well-modeled backbone fold.
     - $50-70$: Low confidence; often flexible loops.
     - $<50$: **Hallmark of an Intrinsically Disordered Region (IDR)**. It is physical disorder in the test tube, not a failure of AlphaFold!
   - **PAE (Predicted Aligned Error)**:
     - Measures distance error between residue $x$ and residue $y$.
     - When residue $x$ is in Domain 1 and residue $y$ is in Domain 2, low PAE means Domain 1 and Domain 2 are locked in a rigid relative orientation. High PAE means they tumble independently around a flexible linker.

---

## 🧪 Interactive Prompts for the Agent

### Exercise 1.1: Analyzing Tumor Suppressor p53
Copy and paste this prompt to the agent:
> *"Using the AlphaFold skill, fetch the structure and PAE matrix for human Tumor Suppressor p53 (UniProt ID: P04637). Analyze its pLDDT distribution and PAE domain boundaries. Explain how the results reflect its known biology: the disordered transactivation domain (TAD) versus the rigid DNA-binding domain (DBD)."*

### Exercise 1.2: 3D Homology Search with Foldseek
Copy and paste this prompt to the agent:
> *"Take the AlphaFold model for human BRAF kinase (UniProt: P15056). Run a Foldseek structural search against PDB100. What are the top structural hits, and what experimental ligands/inhibitors are bound in those PDB entries?"*

### Exercise 1.3: Visualizing Active Sites with PyMOL
Copy and paste this prompt to the agent:
> *"Use PyMOL to generate a high-resolution cartoon rendering of the BRAF kinase domain. Highlight the ATP-binding pocket and residue Val600 in red sticks. Save both a PNG image and a PyMOL .pse session file."*

---

## 💡 Biological Discussion Questions
1. Why do oncogenic "hotspot" mutations in TP53 (e.g., R175H, R248Q, R273H) cluster in the DNA-binding domain (high pLDDT) rather than in the disordered termini (low pLDDT)?
2. If two proteins share only 15% sequence identity according to BLAST, but Foldseek aligns them with a TM-score of 0.85, what does this tell you about their evolutionary relationship and catalytic function?
