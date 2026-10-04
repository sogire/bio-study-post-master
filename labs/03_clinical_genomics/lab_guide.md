# Lab Guide 3: Population Genetics & Clinical Variant Curation

**Focus**: Natural Selection, gnomAD Constraint, and ACMG/AMP Pathogenicity  
**Primary Skills**: `gnomad-database`, `clinvar-database`, `dbsnp-database`, `ensembl-database`

---

## 🧬 Biological Context & Intuition

When sequencing a patient's genome, you find ~4 to 5 million variants compared to the reference human genome. How do clinical geneticists pinpoint the single causal mutation?
1. **The Allele Frequency Filter**:
   - If a disease is a severe childhood Mendelian condition with early lethality, natural selection rapidly purges causative variants from the population. Therefore, causative alleles must be **extremely rare** ($MAF < 0.01\%$ or absent in gnomAD).
   - If a variant has a frequency of $2\%$ in healthy gnomAD adults, it can immediately be ruled out as the primary cause of a severe high-penetrance pediatric disease (**BA1 criterion**).
2. **Gene Constraint (Intolerance to Mutation)**:
   - **pLI (Probability of Loss-of-function Intolerance)**: $\ge 0.90$ means the gene is **haploinsufficient**; losing one functional allele causes severe disease.
   - **LOEUF (Loss-of-function Observed/Expected Upper Bound Fraction)**: Continuous metric ranking genes from most constrained (low LOEUF, e.g., $<0.30$) to most tolerant (high LOEUF $>1.0$).
3. **The ACMG/AMP Pathogenicity Framework**:
   - Classifies variants into: *Pathogenic*, *Likely Pathogenic*, *VUS (Variant of Uncertain Significance)*, *Likely Benign*, *Benign*.
   - Uses weighted evidence rules: **PVS1** (null variant in LoF gene), **PS1-4** (strong clinical/functional evidence), **PM1-6** (moderate), **PP1-5** (supporting in silico/phenotype), **BA1/BS1-4** (benign).

---

## 🧪 Interactive Prompts for the Agent

### Exercise 3.1: Comparing Gene Constraints in gnomAD
Copy and paste this prompt to the agent:
> *"Query gnomAD for gene constraint metrics for SCN1A (sodium channel linked to Dravet syndrome) and compare them with OR2T1 (olfactory receptor). Extract pLI, LOEUF, and missense constraint scores. Explain what these numbers tell us about the evolutionary tolerance of each gene."*

### Exercise 3.2: Allele Frequency Spectrum Across Populations
Copy and paste this prompt to the agent:
> *"Look up the sickle cell anemia variant in the HBB gene (rs334, Glu6Val) using dbSNP and gnomAD. What are its allele frequencies across African, European, East Asian, and Latino populations in gnomAD? Explain why this pathogenic variant is maintained at high frequency in African ancestry populations (heterozygote advantage against malaria)."*

### Exercise 3.3: ClinVar Pathogenicity & VUS Resolution
Copy and paste this prompt to the agent:
> *"Query ClinVar for variants in the LDLR gene (Familial Hypercholesterolemia). Pick a reported Variant of Uncertain Significance (VUS), check its submission evidence, and run Ensembl VEP to predict its molecular consequence. Does the evidence lean toward pathogenic or benign?"*

---

## 💡 Biological Discussion Questions
1. Why does a nonsense mutation located in the last 50 nucleotides of the penultimate exon or in the last exon often fail to trigger Nonsense-Mediated Decay (NMD)?
2. What is the biological difference between a *haploinsufficient* mutation and a *dominant-negative* mutation?
