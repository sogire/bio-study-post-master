# Lab Guide 5: Translational Bioinformatics & AI Drug Discovery

**Focus**: GWAS Target Prioritization, L2G Scoring, Cheminformatics, and Clinical Trials  
**Primary Skills**: `opentargets-database`, `chembl-database`, `pubchem-database`, `openfda-database`, `clinical-trials-database`

---

## 🧬 Biological Context & Intuition

Drug development costs ~$2.6 billion per approved drug, and >90% of clinical candidates fail in clinical trials. The single factor that doubles the probability of Phase 3 success is **human genetic evidence** supporting the drug target.
1. **The GWAS Locus-to-Gene (L2G) Challenge**:
   - A GWAS signal only pinpoints a statistical genomic region (a "locus" containing variants in linkage disequilibrium).
   - In ~50% of loci, the nearest gene is **not** the true causal gene! The causal variant frequently loops through 3D space to activate a distant gene.
   - Open Targets Platform trains a machine-learning Locus-to-Gene (L2G) model integrating distance, molecular QTL colocalization (eQTL, sQTL), chromatin interactions (Capture Hi-C), and functional annotations.
2. **Target Tractability (Druggability)**:
   - **Small Molecules**: Target must have an accessible, concave hydrophobic pocket ($>300\text{ \AA}^3$).
   - **Monoclonal Antibodies**: Target must be exposed on the outer surface of the plasma membrane or secreted into extracellular fluid.
3. **Pharmacodynamics & Kinetics**:
   - **IC50**: Concentration required to inhibit 50% of enzyme activity in vitro.
   - **Ki**: True thermodynamic binding constant ($K_i = [E][I]/[EI]$), independent of substrate concentration.
   - **Off-Target Liability**: Many small-molecule kinase inhibitors cross-react with other kinases due to ATP pocket similarity, causing adverse events.

---

## 🧪 Interactive Prompts for the Agent

### Exercise 5.1: Causal Target Prioritization with Open Targets L2G
Copy and paste this prompt to the agent:
> *"Query the Open Targets Platform for Rheumatoid Arthritis (MONDO_0008383). Retrieve the top genetically supported target genes. For the top kinase target (e.g., JAK1), extract its tractability profile across small molecules and antibodies, and summarize its clinical safety precedence."*

### Exercise 5.2: Bioactivity Profiling & Chemical Structures in ChEMBL and PubChem
Copy and paste this prompt to the agent:
> *"Query ChEMBL for the approved drug Osimertinib (CHEMBL3353410) targeting EGFR. Retrieve its nanomolar IC50 values against wild-type EGFR versus EGFR T790M. Then, fetch its 2D chemical structure, SMILES string, and molecular weight from PubChem."*

### Exercise 5.3: Clinical Trials & Adverse Events Surveillance
Copy and paste this prompt to the agent:
> *"Query ClinicalTrials.gov for active Phase 3 clinical trials evaluating Osimertinib in Non-Small Cell Lung Cancer. Then, check openFDA for reported adverse drug events (FAERS) associated with Osimertinib."*

---

## 💡 Biological Discussion Questions
1. Why does targeting a cytokine like TNF require an injectable antibody (e.g., Adalimumab), while targeting an intracellular kinase like JAK1 requires an orally bioavailable small molecule (e.g., Tofacitinib)?
2. How does the T790M mutation in EGFR sterically clash with 1st-generation ATP-competitive inhibitors like Gefitinib, and how does the covalent acrylamide warhead in Osimertinib overcome this resistance?
