# Lab Guide 4: Multi-Omics, Spatial Proteomics & Systems Biology

**Focus**: eQTL Mechanics, Spatial Protein Targeting, and Reaction Interactomes  
**Primary Skills**: `gtex-database`, `human-protein-atlas-database`, `reactome-database`, `string-database`, `quickgo-database`, `embl-ebi-ols`

---

## 🧬 Biological Context & Intuition

Genomics gives you the blueprint; multi-omics reveals the dynamic machinery.
1. **The Disconnect Between RNA and Protein**:
   - The Central Dogma is not linear. RNA expression (measured by RNA-seq in GTEx) tells you whether a gene is transcribed, but protein abundance (measured by IHC in the Human Protein Atlas) depends on translation rate, ribosomal stalling, and protein degradation by the ubiquitin-proteasome system.
2. **eQTL Mechanics (Expression Quantitative Trait Loci)**:
   - **cis-eQTLs**: SNPs within 1 Mb of a gene that alter promoter/enhancer binding, modulating steady-state mRNA levels in specific cell types.
   - **Tissue Specificity**: Most eQTLs are tissue-specific because chromatin is only accessible in tissues where the appropriate cell-type lineage transcription factors are expressed.
3. **Subcellular Localization**:
   - A protein must travel to its designated cellular address. Proteins with an N-terminal signal peptide enter the secretory pathway (ER $\to$ Golgi $\to$ plasma membrane / extracellular secretion). Proteins with a Nuclear Localization Signal (NLS) enter the nucleus via importins.
4. **Network Topology (STRING) & Biochemical Reactions (Reactome)**:
   - Biological interactomes are **scale-free**. "Hub" proteins have dozens of partners and high degree centrality. Disrupting a hub often causes systemic lethality, whereas peripheral nodes are well-tolerated.
   - Reactome tracks the exact chemical transformations: inputs, outputs, catalysts, and allosteric inhibitors.

---

## 🧪 Interactive Prompts for the Agent

### Exercise 4.1: RNA Abundance vs. Protein Localization for PCSK9
Copy and paste this prompt to the agent:
> *"Query GTEx Portal for PCSK9 median expression across all 54 human tissues. In which tissue is PCSK9 predominantly expressed? Then query the Human Protein Atlas (HPA) to verify its immunohistochemistry protein staining and subcellular localization. Does PCSK9 follow the secretory pathway?"*

### Exercise 4.2: Constructing the Cholesterol Clearance Interactome in STRING
Copy and paste this prompt to the agent:
> *"Build a protein-protein interaction network in STRING for human PCSK9, LDLR, APOB, LDLRAP1, and HMGCR (NCBI Taxon 9606). What are the interaction confidence scores? Identify the central hub protein in this subnetwork."*

### Exercise 4.3: Tracing Biochemical Reaction Mechanisms in Reactome
Copy and paste this prompt to the agent:
> *"Query the Reactome database for the pathway 'LDL clearance' or 'Receptor-mediated endocytosis of LDLR'. Extract the specific biochemical reactions, including the formation of the PCSK9:LDLR complex and its lysosomal fate."*

---

## 💡 Biological Discussion Questions
1. Why does therapeutic inhibition of PCSK9 in the blood plasma (via monoclonal antibodies like Evolocumab) cause liver cells to express *more* LDL receptors on their surface, dramatically lowering blood cholesterol?
2. If an eQTL variant increases PCSK9 mRNA expression in the liver by 40%, what effect do you expect on circulating LDL-cholesterol levels and risk of myocardial infarction?
