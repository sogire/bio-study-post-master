# Lab Guide 2: Regulatory Genomics & In Silico Mutagenesis

**Focus**: Cis-Regulatory Elements, Transcription Factor Dynamics, and Splicing  
**Primary Skills**: `encode-ccres-database`, `jaspar-database`, `unibind-database`, `ucsc-conservation-and-tfbs`, `alphagenome-single-variant-analysis`

---

## 🧬 Biological Context & Intuition

Over 98% of the human genome does not code for proteins, yet >90% of disease-associated variants discovered in GWAS fall in non-coding DNA. How do non-coding mutations cause disease?
1. **The Cis-Regulatory Grammar**:
   - **Promoters**: Located directly upstream of Transcription Start Sites (TSS). Characterized by open chromatin and **H3K4me3**.
   - **Enhancers**: Can be located 500 bp to 1,000,000 bp away. They loop physically across 3D nuclear space to touch promoters. Characterized by **H3K27ac** (acetylation neutralizes lysine positive charge, loosening histone grip on DNA).
   - **Insulators (CTCF)**: Form the anchor points of chromatin loops, creating insulated neighborhoods (TADs) so enhancers don't accidentally fire the wrong gene.
2. **Pre-mRNA Splicing Rules**:
   - Splicing removes introns using conserved dinucleotide anchors: `GU` at the 5' donor site and `AG` at the 3' acceptor site, plus an upstream branch point adenosine.
   - Non-coding variants can create **cryptic splice sites** or disrupt exonic splicing enhancers (ESEs), causing exon skipping or intron retention, which triggers nonsense-mediated decay (NMD).
3. **In Silico Saturation Mutagenesis (ISM)**:
   - Deep learning architectures (AlphaGenome) predict chromatin accessibility, histone marks, and gene expression changes for any variant directly from sequence ab initio.

---

## 🧪 Interactive Prompts for the Agent

### Exercise 2.1: Dissecting an Enhancer Landscape with ENCODE
Copy and paste this prompt to the agent:
> *"Query the ENCODE database for candidate cis-regulatory elements (cCREs) around the beta-globin (HBB) locus on chromosome 11 (chr11:5,200,000-5,225,000). Identify which elements are classified as Promoters (PLS), Proximal Enhancers (pELS), or Distal Enhancers (dELS)."*

### Exercise 2.2: Cross-Referencing TF Motifs with Direct ChIP-seq Binding
Copy and paste this prompt to the agent:
> *"Fetch the JASPAR binding matrix for the erythroid master regulator GATA1 (Matrix ID: MA0035.4). Then, query UniBind to see if experimental ChIP-seq binding peaks for GATA1 are documented in erythroid cell lines at the HBB locus."*

### Exercise 2.3: Non-Coding Variant Analysis with AlphaGenome
Copy and paste this prompt to the agent:
> *"Analyze the functional consequences of the classic oncogenic TERT promoter mutation (chr5:1,295,228 C>T). Use AlphaGenome single variant analysis to inspect predicted changes in chromatin accessibility, transcription factor binding, and gene expression. Generate the AlphaGenome Atlas interactive links."*

---

## 💡 Biological Discussion Questions
1. Why does the C>T mutation in the TERT promoter reactivate telomerase in adult cancer cells, while having no effect on the amino acid sequence of the protein?
2. If a non-coding variant has a very high UCSC phyloP conservation score across 100 vertebrates, what does that imply about its regulatory necessity?
