# Capstone 2: Autonomous ACMG/AMP Clinical Variant Curation Agent

**Objective**: Create and package a reusable AI agent skill using `workflow-skill-creator` that automatically gathers multi-modal evidence across gnomAD, ClinVar, AlphaGenome, AlphaFold, and PubMed to evaluate human genetic variants according to ACMG/AMP clinical guidelines.

---

## The Biological Scenario

In clinical molecular diagnostic laboratories, variant curation is the major bottleneck. When a patient with a suspected genetic disorder has an unclassified missense or non-coding variant reported as a **Variant of Uncertain Significance (VUS)**, human geneticists spend hours querying disparate databases to apply ACMG/AMP criteria.

Your mission is to formulate an automated evidence synthesis protocol that evaluates any variant across 6 pillars:
1. **Population Rarity**: gnomAD global and ancestral frequencies (**BA1** / **PM2**).
2. **Gene Constraint**: gnomAD LOEUF and pLI metrics.
3. **Clinical Precedence**: ClinVar assertion status, conflicting interpretations, and submitter reviews.
4. **In Silico Effect**: Ensembl VEP molecular consequence + AlphaGenome functional variant score (**PP3**).
5. **Structural Context**: AlphaFold pLDDT confidence (is the mutation in a rigid functional core or a flexible disordered loop?).
6. **Literature Mining**: PubMed and Europe PMC case reports (**PS4** / **PP4**).

---

## Interactive Protocol to Run with the Agent

### Step 1: Execute the Multi-Skill Manual Protocol
Pick a test variant (e.g., an unclassified missense mutation in *LDLR*, *BRCA1*, or *SCN1A*):
> *"Let's curate the variant BRCA1 c.5095C>T (p.Arg1699Trp, rs55770732):*
> *1. Check its population frequency in gnomAD.*
> *2. Fetch its clinical significance and submissions in ClinVar.*
> *3. Retrieve the gene constraint (LOEUF) for BRCA1.*
> *4. Evaluate its AlphaFold 3D structure: does residue 1699 fall in a high-confidence domain?*
> *5. Query PubMed for clinical case studies associating this variant with hereditary breast and ovarian cancer.*
> *6. Synthesize these findings into an ACMG/AMP classification table."*

### Step 2: Distill the Workflow into an Agent Skill
Once the workflow produces the desired clinical report, invoke `workflow-skill-creator`:
> *"Let's turn the clinical variant curation workflow we just executed into a new reusable skill called `acmg-variant-curator` using the workflow-skill-creator skill. Guide me through the brainstorming and packaging steps."*

---

## Final Deliverable & Validation
- A new, self-contained agent skill with:
  - `SKILL.md` defining triggers, guidelines, and output templates.
  - Test validation on a known Pathogenic variant and a known Benign control to verify accurate ACMG scoring.
