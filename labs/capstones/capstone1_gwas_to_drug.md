# Capstone 1: End-to-End GWAS-to-Target Precision Medicine Pipeline

**Objective**: Take a statistical GWAS risk locus and perform an autonomous multi-omics biological investigation—from non-coding variant impact to target validation, 3D structural pocket analysis, and candidate drug identification.

---

## The Biological Scenario

A recent large-scale meta-analysis identified a genome-wide significant risk locus associated with **Coronary Artery Disease (CAD)** on chromosome 1p32.3. The lead SNP is located in a non-coding region near the *PCSK9* locus.

As the computational biology lead, your goal is to determine:
1. Does this non-coding variant alter an active regulatory element or transcription factor binding site?
2. Which gene in the locus is the true causal target according to eQTL and L2G evidence?
3. Where is this gene expressed in human tissues, and what is its subcellular destination?
4. What does the 3D structure look like, and does it contain a druggable pocket?
5. Are there known chemical leads, approved drugs, or active clinical trials targeting this mechanism?

---

## Step-by-Step Prompting Guide for the Agent

### Step 1: Variant Mapping & Conservation
> *"Map the lead variant rs11591147 to GRCh38 coordinates using dbSNP. Check its UCSC evolutionary conservation score (phyloP and phastCons) across 100 vertebrates."*

### Step 2: Regulatory & Epigenetic Context
> *"Query ENCODE for candidate cis-regulatory elements (cCREs) overlapping this genomic locus. Does it fall within an active enhancer or promoter? Check if JASPAR or UniBind identify any transcription factor binding peaks at this site."*

### Step 3: Deep Learning In Silico Mutagenesis (AlphaGenome)
> *"Evaluate the variant rs11591147 using AlphaGenome single variant analysis. What are the predicted effects on chromatin accessibility, histone modifications, and splicing?"*

### Step 4: Causal Gene Prioritization (GTEx & Open Targets L2G)
> *"Query GTEx Portal for significant cis-eQTLs associated with this variant in liver and artery tissues. Then, query Open Targets Platform to retrieve the Locus-to-Gene (L2G) prioritization score for this CAD locus. Does the evidence point to PCSK9 as the causal target?"*

### Step 5: Tissue Proteomics & Interactome
> *"Query the Human Protein Atlas (HPA) for PCSK9's protein abundance in human liver and its subcellular localization. Then construct a STRING protein-protein interaction network to map its functional partners in cholesterol clearance."*

### Step 6: 3D Protein Biophysics (AlphaFold & PyMOL)
> *"Fetch the 3D AlphaFold structure and PAE matrix for PCSK9 (UniProt: Q8NBP7). Analyze its rigid domain boundaries and render a PyMOL cartoon showing the catalytic domain and the LDL receptor binding surface."*

### Step 7: Drug Tractability, ChEMBL & Clinical Landscape
> *"Query Open Targets for PCSK9's tractability profile (small molecule vs antibody). Query ChEMBL for bioactivity profiles of known inhibitors, and query ClinicalTrials.gov for completed Phase 3 trials evaluating PCSK9 inhibitors (e.g., Evolocumab, Alirocumab)."*

---

## Final Deliverable & Report Structure
Synthesize your findings into a scientific brief in `labs/capstones/cad_pcsk9_report.md` addressing:
1. **Genetic & Regulatory Mechanism**: How the variant modulates target expression.
2. **Biological Function**: Role in hepatic LDL receptor degradation and circulating cholesterol.
3. **Structural & Pharmacological Translation**: Why monoclonal antibodies succeeded while small molecules proved challenging.
