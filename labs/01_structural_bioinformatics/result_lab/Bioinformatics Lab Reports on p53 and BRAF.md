# **Bioinformatics Lab Reports on p53 and BRAF**

[https\://gemini.google.com/app/4feaed4140018b5a](https://gemini.google.com/app/4feaed4140018b5a)

*User prompt: Explain me those texts*

Response: Welcome, students\! Let's examine these three bioinformatics laboratory reports step-by-step. They cover two fundamental cancer biology targets—**p53** and **BRAF**—and demonstrate how computational tools like **AlphaFold**, **Foldseek**, and **PyMOL** help translate molecular structures into clinical and biological insights.

## **1\. Laboratory Report 1: Structural Confidence & Architecture of Tumor Suppressor p53**

### **Biological Context & Medicine**

**p53** (coded by *TP53*) is known as the "guardian of the genome". It is a tumor suppressor protein that senses cellular stress (such as DNA damage or hypoxia) and triggers repair mechanisms, cell cycle arrest, or apoptosis. Over 50% of human cancers harbor somatic mutations in *TP53*.

### **Key Bioinformatics Insights**

> * **Intrinsic Disorder vs. Rigid Domains**: AlphaFold uses the **pLDDT score** (0–100 scale measuring local accuracy) and the **PAE (Predicted Aligned Error)** matrix (measuring relative spatial orientation between residues).  
> * **The Bimodal Profile of p53**:  
  1. **Transactivation Domain (TAD, residues 1–61)**: Shows very low pLDDT (\~47.6) and high PAE relative to the rest of the protein (\~30.9 Å). This reflects an **Intrinsically Disordered Region (IDR)**. It does not adopt a fixed 3D shape until it engages binding partners (such as the negative regulator MDM2) via a process called *coupled folding-upon-binding*.  
  2. **DNA-Binding Domain (DBD / Core Domain, residues 99–293)**: Shows very high pLDDT (\~95.3) and a low intra-domain PAE (\~3.56 Å). This is the rigid, immunoglobulin-like *β*\-sandwich domain that binds directly to DNA. Most oncogenic "hotspot" mutations (e.g., R175, R248, R273) occur here, either destabilizing the fold or disrupting DNA binding.  
> * **Methodological Takeaway**: Because \~40% of p53 is flexible, whole-protein rigid docking or structural alignment with full-length p53 will cause steric artifacts. Molecular modeling must be restricted to the structured DBD (residues 99–293).

## **2\. Laboratory Report 2: Foldseek Structural Search of BRAF Kinase**

### **Biological Context & Medicine**

**BRAF** is a serine/threonine protein kinase component of the **MAPK/ERK signaling pathway** (RAS–RAF–MEK–ERK), which promotes cell proliferation, survival, and differentiation. Hyperactivation of this pathway—often via mutated BRAF—drives many malignancies, notably cutaneous melanoma, colorectal cancer, and non-small cell lung cancer (NSCLC).

### **Key Bioinformatics Insights**

> * **Foldseek Search & Alignment Classes**: Foldseek compares 3D tertiary shapes rather than just linear amino acid sequences. The structural alignment of full-length BRAF (UniProt: P15056) yielded two distinct hit categories:  
  1. **Multi-domain Complexes (Query Coverage \~76%)**: Include large Cryo-EM structures of BRAF bound to RAS, MEK, and 14-3-3 scaffold proteins (e.g., PDB IDs: 8DGS, 7MFD).  
  2. **Kinase Domain Co-crystals (Query Coverage \~35–36%)**: Align specifically to the \~274-residue catalytic core (residues 457–717).  
> * **Pharmacological & Kinome Landscape**:  
  * **Clinically Approved & Investigational BRAF Inhibitors**: The structures in the hit list contain key targeted drugs, including **Vemurafenib** (3OG7), **Dabrafenib** (5HIE), **Naporafenib** (6N0P), and **Tovorafenib** (8F7O).  
  * **Kinome Homologues**: The structural search revealed high structural similarity (Prob \= 1.0) with paralogs like C-RAF/KSR1/KSR2, as well as distinct kinase families like Src-family kinases (c-Src), Receptor Tyrosine Kinases (EGFR, RET, Eph receptors), and Tec-family kinases (BTK).

## **3\. Laboratory Report 3: Molecular Rendering of the BRAF Kinase Domain in PyMOL**

### **Biological Context & Structural Medicine**

To understand drug binding and oncogenic activation, we look at the structural machinery of the BRAF kinase domain:

        N-Lobe (Teal, β-sheets & αC-helix)  
                 \\  
                  \[  ATP-Binding Pocket (Cyan)  \]  
                 /                               \\  
\[ Hinge (Cys532) \]                             \[ DFG Motif (594-596) \]  
                                                          |  
                                               \[ Val600 (Red Sticks) \]  
                                                          |  
                 \\                             \[ Activation Loop (Pink) \]  
                  \[ Catalytic Cleft / HRD Loop (Asp576) \]  
                 /  
        C-Lobe (Slate, α-helical bundle)

### **Key Functional Regions & Vocabulary**

> 1. **N-Lobe & C-Lobe**: The catalytic domain is split into an N-terminal lobe (mostly *β*\-sheets) and a C-terminal lobe (mostly *α*\-helices).  
> 2. **ATP-Binding Pocket & Hinge Region**:  
   * **Glycine-rich loop (P-loop)**: Positioned to cover the phosphate groups of ATP.  
   * **Catalytic Salt Bridge (Lys483 – Glu501)**: Coordinates ATP in a productive active conformation.  
   * **Hinge (Cys532) & Gatekeeper (Thr529)**: The hinge connects the two lobes. Standard small-molecule ATP-competitive inhibitors form key hydrogen bonds with backbone atoms in this hinge region.  
> 3. **The DFG Motif & Activation Segment**:  
   * **DFG Motif (Asp594–Gly596)**: Functions as a conformational switch. In the **DFG-in** state, Asp594 points into the ATP pocket to coordinate a magnesium ion necessary for catalysis. In the **DFG-out** state, the switch flips, rendering the kinase inactive.  
> 4. **The V600E Oncogenic Driver Mutation**:  
   * **Wild-type (Val600)**: The non-polar valine sidechain packs into a hydrophobic autoinhibitory pocket, keeping the kinase in an inactive state until upstream signals arrive.  
   * **Mutation (V600E)**: Valine (Val) is replaced by Glutamic acid (Glu). Glutamate carries a negative charge. This acts as a **phosphomimetic**—it mimics an activating phosphorylation event, destabilizes the inactive conformation, and keeps the kinase constitutively active as a monomer, driving downstream oncogenic signaling.

### **Medical & Bioinformatics Glossary for Reference**

> * **pLDDT (Predicted Local Distance Difference Test)**: A per-residue confidence metric ranging from 0 to 100 used by AlphaFold.  
> * **PAE (Predicted Aligned Error)**: A matrix measuring distance error between pairs of residues to assess domain rigidity and inter-domain flexibility.  
> * **Kinase**: An enzyme that transfers a phosphate group from ATP to a specific substrate (phosphorylation).  
> * **Phosphomimetic**: An amino acid substitution (e.g., to Glutamate or Aspartate) whose negative charge mimics a phosphorylated residue.  
> * **Co-crystal Structure**: An X-ray or Cryo-EM structure of a protein bound simultaneously with its small-molecule drug or cofactor.

---

*User prompt: Why do oncogenic "hotspot" mutations in TP53 (e.g., R175H, R248Q, R273H) cluster in the DNA-binding domain (high pLDDT) rather than in the disordered termini (low pLDDT)?*

Response: Welcome, class\! That is a fundamental question in cancer genomics and structural biology. To understand why **tumor suppressor p53** (*TP53*) hotspot mutations cluster almost exclusively in the **DNA-Binding Domain (DBD)** rather than in its intrinsically disordered terminal regions, we must look at both the **protein's structural biochemistry** and the **evolutionary pressure of oncogenesis**.

### **1\. Structural Architecture & AlphaFold Metrics**

As seen in structural predictions, p53 exhibits a distinct modular architecture:

        TAD (1-61)         PRD (62-93)         DBD / Core Domain (99-293)           TD (325-356)  CTD (357-393)  
\[== Disordered (TAD1/2) \==\]\[= Flexible \=\]\[======= Rigid DNA-Binding Domain \========\]\[= Linker \=\]\[= Helix \=\]\[= Disordered \=\]  
  pLDDT: \~47.6 (Low)        pLDDT: \~50.1             pLDDT: \~95.3 (Very High)                     pLDDT: \~90.9  pLDDT: \~43.4

> * **The Disordered N- and C-Termini (Low pLDDT \< 50\)**: The **Transactivation Domain (TAD)** and **C-Terminal Domain (CTD)** are **Intrinsically Disordered Regions (IDRs)**. They lack a fixed 3D tertiary structure in isolation and undergo *coupled folding-upon-binding* when interacting with dynamic binding partners (such as MDM2, p300/CBP, or modification enzymes).  
> * **The Core DNA-Binding Domain (High pLDDT \> 90\)**: Residues 99–293 form a rigid, highly defined *β*\-sandwich fold scaffolded by a structural zinc ion (Zn2+) and specific loop-sheet-helix motifs that insert directly into DNA consensus sequences.

### **2\. Functional Impact: Tolerant vs. Vulnerable Structures**

The biological consequence of a missense mutation depends heavily on the target region's structure:

#### **A. Mutations in Disordered Regions (Low pLDDT) Are Mostly Non-Pathogenic**

> * **Structural Plasticity**: Because IDRs lack tight sidechain packing or precise atomic coordinates, substituting a single amino acid rarely destroys the region's overall function.  
> * **Redundant Linear Motifs**: Short Linear Motifs (SLiMs) within IDRs often have loose sequence requirements. A single point mutation typically alters binding affinity incrementally rather than completely abolishing protein function.  
> * **Lack of Selection Pressure in Cancer**: A mutation that does not compromise p53's ability to bind DNA and induce cell cycle arrest/apoptosis will not offer a clonal growth advantage to a precancerous cell.

#### **B. Mutations in the Rigid Core Domain (High pLDDT) Are Destructive**

The rigid immunoglobulin-like *β*\-sandwich requires exact atomic positioning. Point mutations in the DBD fall into two functional categories:

> 1. **Contact Mutations (e.g., R248Q, R273H)**:  
   * **Mechanism**: These residues extend sidechains directly into the major or minor grooves of DNA to form electrostatic and hydrogen bonds with target promoters (e.g., *CDKN1A/p21*, *BAX*).  
   * **Impact**: Mutating an arginine (R) to a glutamine (Q) or histidine (H) removes key positive charges, immediately abolishing DNA binding without altering the global protein fold.  
> 2. **Conformational / Structural Mutations (e.g., R175H, G245S, R249S, R282W)**:  
   * **Mechanism**: These residues stabilize the hydrophobic core, pack the *β*\-sandwich, or coordinate the essential Zn2+ ion (which holds loops L2 and L3 in place).  
   * **Impact**: Replacing arginine 175 destabilizes Zn2+ coordination, causing local or global protein unfolding at physiological temperature (37∘C).

### **3\. The Evolutionary Mechanics of "Hotspot" Clustering**

In oncology, a **"hotspot"** is not merely a locus prone to DNA damage; it is a position where specific mutations provide a strong **selective advantage** during somatic evolution:

> 1. **Loss of Function (LOF)**: Complete inactivation of p53's transcriptional activity prevents apoptosis or senescence in response to oncogenic stress.  
> 2. **Dominant-Negative Effect (DNE)**: Mutant p53 monomers can heterotetramerize with wild-type (WT) p53 monomers produced from the remaining intact allele, poisoning the tetramer and inhibiting WT function.  
> 3. **Gain of Function (GOF)**: Unfolded or structurally altered DBD mutants (like R175H) often aggregate or misbind other transcription factors (e.g., p63, p73), actively promoting invasion, metastasis, and drug resistance.

### **Key Technical Vocabulary Summary**

| Technical Term | Spanish Equivalent | Medical / Biological Definition |
| :---- | :---- | :---- |
| **Hotspot Mutation** | *Mutación punto caliente* | A recurrent mutation site observed at high frequency across tumor samples due to positive clonal selection. |
| **DNA-Binding Domain (DBD)** | *Dominio de unión al ADN* | The rigid core domain of p53 responsible for sequence-specific promoter binding. |
| **Intrinsically Disordered Region (IDR)** | *Región intrínsecamente desordenada* | A protein segment lacking a fixed 3D structure under physiological conditions. |
| **Dominant-Negative Effect** | *Efecto dominante negativo* | When a mutated protein subunit impairs the function of the co-expressed wild-type subunit within a multimeric complex. |
| **Gain of Function (GOF)** | *Ganancia de función* | A novel, often oncogenic property acquired by a mutant protein that is absent in the wild-type form. |

Does the distinction between structural/conformational mutations and direct contact mutations make sense, or would you like to explore how drug developers attempt to small-molecule re-activate mutant p53 like R175H?

---

*User prompt: If two proteins share only 15% sequence identity according to BLAST, but Foldseek aligns them with a TM-score of 0.85, what does this tell you about their evolutionary relationship and catalytic function?*

Response: This scenario illustrates a classic and crucial principle in structural bioinformatics and evolutionary biology: **structure is far more conserved during evolution than primary amino acid sequence**.

### **1\. Evolutionary Relationship: Distant Homology (Divergent Evolution)**

> * **The "Twilight Zone" of Sequence Alignment**: A **15% sequence identity** reported by BLAST falls deep within the bioinformatics **"twilight zone"** (typically \<20–35% identity). At this level, standard sequence-based search tools like BLAST fail to distinguish true evolutionary ancestry from random statistical noise.  
> * **High Structural Similarity (TM-score)**: The **TM-score (Template Modeling score)** evaluates global structural topology on a scale from 0 to 1\. A TM-score above **0.5** indicates that the two proteins share the same global fold, while a score of **0.85** from Foldseek indicates near-identical 3D backbone topology.  
> * **Evolutionary Verdict**: These two proteins are **homologous** (they share a common evolutionary ancestor). This is a clear case of **divergent evolution**. Over millions of years, selective pressures conserved the overall 3D structural scaffold—which is essential for physical stability—while the primary amino acid sequence accumulated extensive mutations.

### **2\. Catalytic Function & Active Site Dynamics**

While a TM-score of 0.85 proves they share the same structural fold, **it does not guarantee identical enzymatic substrates or identical catalytic activity**:

> * **Conserved Reaction Mechanism (Superfamily Level)**: Proteins with the same structural fold often belong to the same enzyme superfamily and perform similar chemistry (e.g., nucleophilic attack, ATP hydrolysis, or electron transfer).  
> * **Substrate Divergence**: Because 85% of the sequence has mutated, residues lining the **binding pocket** or **substrate-binding cleft** may have changed significantly. This allows homologous proteins to adapt to entirely different biological substrates or metabolic pathways while using the same fundamental 3D scaffold.  
> * **Active Site Conservation**: To verify if the exact catalytic function is preserved, you must inspect whether the specific **catalytic triad** or **coordinating residues** within the active site are spatially conserved, regardless of low global sequence identity.

### **Summary Table & Technical Vocabulary**

| Bioinformatics / Medical Term | Spanish Equivalent | Definition & Interpretation |
| :---- | :---- | :---- |
| **Twilight Zone** | *Zona de penumbra* | The sequence identity range (\<20–35%) where sequence aligners cannot reliably infer homology. |
| **TM-score** | *Puntuación TM* | A metric (0–1) for measuring 3D structural similarity independent of protein length (\>0.5 indicates identical fold). |
| **Homology** | *Homología* | Evolutionary divergence from a common ancestral gene or protein structure. |
| **Divergent Evolution** | *Evolución divergente* | Accumulation of sequence mutations over time while maintaining structural architecture. |
| **Foldseek** | *Foldseek* | A fast structural aligner that converts 3D tertiary interactions into 3Di sequences to identify deep homology. |

Would you like to examine how we can superimpose these two structures in PyMOL to check whether their catalytic residues are conserved?

---

