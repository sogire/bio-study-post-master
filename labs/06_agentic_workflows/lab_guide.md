# Lab Guide 6: Scientific Literature Mining & Agentic Workflows

**Focus**: Automated Knowledge Extraction, Preprint Tracking, and Workflow Distillation  
**Primary Skills**: `pubmed-database`, `literature-search-europepmc`, `literature-search-biorxiv`, `literature-search-openalex`, `workflow-skill-creator`

---

## 🧬 Biological Context & Intuition

The speed of biomedical discovery exceeds human reading capacity. Thousands of papers and preprints appear every month.
1. **Preprint Surveillance**:
   - In oncology and generative genomics, breakthroughs (e.g., new drug resistance mutations, AlphaFold updates, single-cell foundation models) appear on **bioRxiv** and **arXiv** months before peer review.
2. **Text Mining & Entity Co-Occurrence**:
   - Automated literature retrieval links variants to drugs, clinical phenotypes, and experimental validation in published papers.
3. **Packaging Workflows into Agent Skills (`workflow-skill-creator`)**:
   - Scientific reproducibility requires standardizing multi-step inquiries so that you (or an AI assistant) can run them systematically across any new gene or variant in seconds.

---

## 🧪 Interactive Prompts for the Agent

### Exercise 6.1: Tracking Oncogenic Resistance on Europe PMC & bioRxiv
Copy and paste this prompt to the agent:
> *"Search Europe PMC and bioRxiv for papers published in the last 12 months discussing resistance mutations to KRAS G12C inhibitors (such as Sotorasib or Adagrasib). Download the key abstracts and summarize the reported secondary mutations (e.g., Y96D, R68S)."*

### Exercise 6.2: Mapping Citation Networks with OpenAlex
Copy and paste this prompt to the agent:
> *"Query OpenAlex for the seminal AlphaFold 2 paper published in Nature (2021). Retrieve its citation count, top citing concepts, and identify 3 highly cited follow-up papers focusing on structural drug discovery."*

### Exercise 6.3: Packaging an Investigative Workflow into a New Skill
Copy and paste this prompt to the agent:
> *"I want to package the multi-step variant evaluation workflow we just performed into a reusable agent skill using workflow-skill-creator. Guide me through Phase 1 (Brainstorming) to define the skill's inputs, dependencies, and outputs."*

---

## 💡 Biological Discussion Questions
1. When tracking emerging drug resistance in cancer patients, why are preprints on bioRxiv/medRxiv critical compared to waiting for 12-month peer-review publication cycles?
2. How does combining programmatic PubMed queries with clinical databases like ClinVar prevent false-positive variant pathogenicity calls?
