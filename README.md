# Post-Master's Bioinformatics Study Program
### 12-Week Interactive Curriculum: Biological Mechanisms & AI Skill Mastery

[![GitHub Repo](https://img.shields.io/badge/GitHub-bio--study--post--master-blue?logo=github)](https://github.com/sogire/bio-study-post-master)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Welcome to the **Post-Master's Bioinformatics Study Program**.

This workspace contains an advanced, 12-week computational biology and bioinformatics curriculum designed for a **Bioinformatics Master's graduate** with strong quantitative and analytical skills who wants to build **deep intuitive biological understanding** across structural biology, epigenetics, clinical genetics, systems biology, and AI drug discovery.

---

## 🔬 The Scientific Investigator Paradigm

In this curriculum, you do **not** write or debug Python scripts, manage virtual environments, or deal with API boilerplates. 

The workspace AI agent handles 100% of the software engineering, tool execution, and database parsing. Your role is that of the **Lead Scientific Investigator**:
1. **Formulate Hypotheses**: Frame biomedical inquiries (e.g., causal mechanisms of a GWAS hit).
2. **Direct AI Skills**: Prompt the agent to interrogate authoritative biological databases (AlphaFold, gnomAD, ENCODE, ChEMBL).
3. **Interpret Biological Evidence**: Analyze returned metrics (pLDDT, LOEUF, eQTL NES, IC50/Ki) in a physiological context.
4. **Synthesize Discoveries**: Chain cross-omics evidence into target validation and clinical curation dossiers.

---

## 🗺️ 12-Week Curriculum Roadmap

| Phase | Weeks | Focus Area | Core Biological Mechanisms | Primary Skills Mastered |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 1** | **Weeks 1–2** | **Structural Biology & Protein Biophysics** | Hydrophobic collapse, Ramachandran limits, intrinsic disorder (IDRs), domain modularity, fold conservation, catalytic clefts. | `alphafold-database`, `foldseek`, `pdb`, `pymol`, `uniprot`, `interpro` |
| **Phase 2** | **Weeks 3–4** | **Regulatory Genomics & Deep Learning** | Nucleosome compaction, histone marks (H3K4me3, H3K27ac), CTCF insulation (TADs), TF binding thermodynamics, splicing grammar. | `encode-ccres`, `jaspar`, `unibind`, `ucsc-conservation`, `alphagenome` |
| **Phase 3** | **Weeks 5–6** | **Population Genetics & Clinical Curation** | Purifying selection, neutral drift, allele frequency spectrum, haploinsufficiency, ACMG/AMP clinical variant interpretation framework. | `gnomad`, `clinvar`, `dbsnp`, `ensembl` (VEP) |
| **Phase 4** | **Weeks 7–8** | **Multi-Omics & Systems Biology** | Central dogma dynamics (RNA $\ne$ protein abundance), cis/trans-eQTLs, subcellular protein sorting, scale-free interactome topology. | `gtex`, `human-protein-atlas`, `reactome`, `string`, `quickgo` |
| **Phase 5** | **Weeks 9–10** | **AI Target Discovery & Pharmacology** | GWAS fine-mapping, linkage disequilibrium, Locus-to-Gene (L2G) ML, target tractability, binding kinetics (IC50, Ki), Lipinski rules. | `opentargets`, `chembl`, `pubchem`, `openfda`, `clinical-trials` |
| **Phase 6** | **Weeks 11–12** | **Literature Mining & Agentic Workflows** | Evidence hierarchies, tracking resistance mutations, packaging multi-tool protocols into reusable AI agent skills, capstone projects. | `pubmed`, `literature-search-europepmc`, `literature-search-biorxiv`, `workflow-skill-creator` |

👉 **Complete Syllabus**: Read [plan.md](plan.md) for full biological mechanism explainers and investigative protocols.

---

## 📂 Repository Layout

```
.
├── README.md                            # Workspace overview & setup
├── plan.md                              # 12-Week Master Curriculum & Biological Syllabus
├── .gitignore                           # Git ignore rules for data and environments
├── .agents/
│   └── skills.json                      # Workspace scientific skills configuration
└── labs/
    ├── README.md                        # Laboratory suite guide
    ├── 01_structural_bioinformatics/    # AlphaFold confidence, Foldseek homology, PyMOL
    │   └── lab_guide.md
    ├── 02_regulatory_genomics/          # ENCODE cCREs, JASPAR motifs, AlphaGenome
    │   └── lab_guide.md
    ├── 03_clinical_genomics/            # gnomAD constraint, ClinVar, ACMG rules
    │   └── lab_guide.md
    ├── 04_systems_biology/              # GTEx eQTLs, Human Protein Atlas, Reactome, STRING
    │   └── lab_guide.md
    ├── 05_drug_discovery/               # Open Targets L2G, ChEMBL bioactivity, ClinicalTrials
    │   └── lab_guide.md
    ├── 06_agentic_workflows/            # Scientific literature surveillance & skill creation
    │   └── lab_guide.md
    └── capstones/
        ├── capstone1_gwas_to_drug.md    # End-to-end CAD/PCSK9 precision medicine pipeline
        └── capstone2_variant_curation.md# Autonomous ACMG clinical variant curation agent
```

---

## 🚀 How to Conduct a Study Session

1. Open this repository in your AI coding assistant or workspace.
2. Direct the agent using prompts from the weekly modules or lab guides:
   > *"Let's begin Week 1 of the study plan. Explain the biophysics of protein folding and let's run Exercise 1.1 on TP53 using AlphaFold."*
3. The agent will fetch the biological data, present the analysis, and discuss the biological implications with you.

---

## 📜 License

This study repository and its curriculum materials are released under the [MIT License](LICENSE).
