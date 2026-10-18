# Module 2: Regulatory Genomics & In Silico Mutagenesis — Biological Discussion Questions

## Question 1: Cis-Regulatory Reactivation of *TERT* in Cancer

> *"Why does the C>T mutation in the TERT promoter reactivate telomerase in adult cancer cells, while having no effect on the amino acid sequence of the protein?"*

### Mechanistic Explanation

1. **Strict Spatial Separation of Coding and Cis-Regulatory Domains**:
   - The human *TERT* translation start site (ATG) is located at `chr5:1,295,352` on the negative strand. The `chr5:1,295,228 C>T` mutation is situated **124 base pairs upstream** of this initiation codon in non-coding DNA.
   - Because it resides completely upstream of the 5' untranslated region (5' UTR) and the open reading frame (ORF), the transcribed pre-mRNA does not alter any codon triplets in the resulting 1,132-amino acid catalytic subunit of the telomerase enzyme. The protein primary, secondary, and tertiary structures remain identical to wild-type TERT.

2. **The Hayflick Limit and the Epigenetic Barrier in Adult Tissues**:
   - In normal human somatic cells, *TERT* transcription is strictly repressed upon embryonic differentiation. This silencing is maintained by compact, closed chromatin (DNase-inaccessible), repressive histone modifications (H3K27me3 / H3K9me3), and DNA methylation across the CpG-dense promoter.
   - With each round of DNA replication, DNA polymerases fail to replicate the extreme ends of linear chromosomes due to the "end-replication problem," leading to progressive telomere attrition (50–100 bp lost per cell division). When telomeres reach a critical threshold, DNA damage response pathways (ATM/ATR $\rightarrow$ p53/p21) are triggered, driving the cell into irreversible replicative senescence (the **Hayflick limit**) or apoptotic crisis.

3. **Cis-Regulatory Gain-of-Function Overcomes the Epigenetic Barrier**:
   - Malignant cells require telomere maintenance to achieve **replicative immortality** (one of the classical Hallmarks of Cancer).
   - The `C228T` transition creates a de novo consensus binding site (`5'-TTCCGG-3'`) recognized specifically by the ETS-family transcription factor **GABPA** (GA-binding protein alpha).
   - GABPA recruits its obligate partner **GABPB1** (a $\beta\gamma$ tetramerization subunit). Unlike monomeric ETS factors, the heterotetrameric $\text{GABP}\alpha_2\beta_2$ complex acts as a potent transcriptional activator capable of binding inaccessible, compacted chromatin and recruiting histone acetyltransferases (HATs, such as p300/CBP) and chromatin remodeling complexes.
   - This chromatin opening is clearly demonstrated by AlphaGenome's quantitative predictions in [Exercise 2.3](lab_2-3/result_lab_2-3.md): sharp focal DNase hypersensitivity, marked induction of **H3K4me3** (quantile $> 0.999$), recruitment of **RNA Polymerase II** (**POLR2A**, quantile $> 0.997$), and de-repression of *TERT* mRNA synthesis (quantile $> 0.9999$).
   - Thus, the mutation acts as a pure **cis-regulatory gain-of-function**: the protein structure is entirely wild-type, but the gene's expression control switch is permanently locked in the "ON" state.

---

## Question 2: Evolutionary Conservation (UCSC phyloP) in Non-Coding DNA

> *"If a non-coding variant has a very high UCSC phyloP conservation score across 100 vertebrates, what does that imply about its regulatory necessity?"*

### Evolutionary & Biophysical Implications

1. **Evolutionary Purifying Selection**:
   - The UCSC **phyloP** (phylogenetic p-value) score measures evolutionary conservation or acceleration across multi-species alignments (such as the 100-vertebrate alignment). Positive phyloP scores indicate **evolutionary constraint** (purifying selection)—the observed substitution rate across vertebrate lineages is significantly slower than what would be expected under neutral genetic drift ($H_0$).
   - In non-coding genomic regions (which constitute $>98\%$ of the genome and generally evolve at near-neutral rates), a site exhibiting a very high positive phyloP score (e.g., phyloP $\ge 3.0$ or $> 5.0$) signifies that across hundreds of millions of years of vertebrate divergence, mutations at that exact base pair were systematically weeded out by natural selection because they impaired organismal fitness.

2. **Regulatory Grammar and Biophysical Binding Constraints**:
   - High non-coding conservation typically marks the invariant core residues of vital cis-regulatory elements:
     - **Transcription Factor Binding Cores**: The invariant 3–4 nucleotide "hotspots" within TF motifs (e.g., the `GATA` in GATA-binding sites in [Exercise 2.2](lab_2-2/result_lab_2-2.md), the `CACGTG` in E-boxes, or the `GGA(A/T)` in ETS motifs) where direct hydrogen bonding and van der Waals contacts occur between amino acid side chains and the DNA major groove.
     - **Spliceosome Anchors**: The canonical `GU` (donor) and `AG` (acceptor) splice junctions, polypyrimidine tracts, and branch point adenosines.
     - **Core Structural Insulators**: Invariant base pairs within the 20-bp CTCF binding sequence required to maintain topologically associating domain (TAD) boundaries and prevent aberrant enhancer-promoter rewiring (such as `EH38E1516900` in [Exercise 2.1](lab_2-1/result_lab_2-1.md)).

3. **Contrast with Gain-of-Function Mutations like *TERT* C228T**:
   - Interestingly, the wild-type cytidine at `chr5:1,295,228` does **not** have an extremely high vertebrate phyloP score because the *unmutated* sequence was not an active ETS binding site; in fact, the somatic mutation *creates* an ectopic binding motif that never existed in the normal vertebrate germline.
   - This highlights a fundamental principle of regulatory genomics: while high phyloP conservation reliably detects **loss-of-function** disruptions of ancient, essential cis-regulatory elements, **gain-of-function** oncogenic mutations (such as `TERT C228T`) frequently occur at positions that appear neutrally evolving, precisely because their pathogenicity arises from de novo motif creation rather than disruption of conserved ancestral function.

