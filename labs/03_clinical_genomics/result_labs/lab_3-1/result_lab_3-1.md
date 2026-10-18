# Exercise 3.1: Comparing Gene Constraints in gnomAD — *SCN1A* vs. *OR2T1*

> [!IMPORTANT]
> **gnomAD Data Usage & Policies Notification:** This analysis uses the `gnomad-database` skill to query the Genome Aggregation Database (gnomAD). Please review the gnomAD data usage terms and policies at [https://gnomad.broadinstitute.org/policies](https://gnomad.broadinstitute.org/policies) and the API documentation at [https://gnomad.broadinstitute.org/data#api](https://gnomad.broadinstitute.org/data#api). A record of this notice is stored in [.licenses/gnomad_database_LICENSE.txt](../../../../.licenses/gnomad_database_LICENSE.txt).

---

## 1. gnomAD Gene Constraint Metrics (GRCh38)

| Metric | Field in gnomAD | **SCN1A** (`ENSG00000144285`) | **OR2T1** (`ENSG00000175143`) | Reference Threshold / Interpretation |
| :--- | :--- | :--- | :--- | :--- |
| **pLI** (Probability of LoF Intolerance) | `pli` | **`1.0`** | `null` *(not calculated / flagged)* | $\ge 0.9$ indicates extreme LoF intolerance (haploinsufficient) |
| **pLoF O/E** (Observed / Expected ratio) | `oe_lof` | **`0.067`** (`0.0671`) | `null` *(not calculated / flagged)* | $0$ = complete depletion; $1$ = neutral expectation |
| **pLoF O/E 90% CI** | `oe_lof_lower` – `oe_lof_upper` | **`0.044 – 0.107`** | `null` | Confidence interval around pLoF O/E |
| **LOEUF** (LoF O/E Upper Bound Fraction) | `oe_lof_upper` | **`0.107`** (`0.1067`) | `null` *(not calculated / flagged)* | $< 0.35$ (or $< 0.6$ in v4) indicates strong LoF constraint |
| **Missense O/E** (Observed / Expected ratio) | `oe_mis` | **`0.584`** (`0.5842`) | **`1.128`** (`1.1275`) | $< 1.0$ indicates missense depletion; $\approx 1.0+$ indicates tolerance |
| **Missense O/E 90% CI (MOEUF = upper)** | `oe_mis_lower` – `oe_mis_upper` | **`0.559 – 0.610`** | **`1.043 – 1.220`** | Upper bound $< 0.6$–$0.7$ indicates strong missense constraint |

### Raw JSON Responses

#### *SCN1A* (`ENSG00000144285`)
```json
{
  "data": {
    "gene": {
      "gene_id": "ENSG00000144285",
      "symbol": "SCN1A",
      "gnomad_constraint": {
        "pli": 1,
        "oe_lof": 0.06710094439714273,
        "oe_lof_lower": 0.04368755392759899,
        "oe_lof_upper": 0.10668311571676678,
        "oe_mis": 0.5842214348461244,
        "oe_mis_lower": 0.5594604676649736,
        "oe_mis_upper": 0.6102622166183026
      }
    }
  }
}
```

#### *OR2T1* (`ENSG00000175143`)
```json
{
  "data": {
    "gene": {
      "gene_id": "ENSG00000175143",
      "symbol": "OR2T1",
      "gnomad_constraint": {
        "pli": null,
        "oe_lof": null,
        "oe_lof_lower": null,
        "oe_lof_upper": null,
        "oe_mis": 1.1275090772540621,
        "oe_mis_lower": 1.0430377901129975,
        "oe_mis_upper": 1.220018708282886
      }
    }
  }
}
```

---

## 2. Overview of Constraint Metrics

1. **pLI (`pli`) — Probability of Being Loss-of-Function Intolerant:**
   - Derived from a three-class mixture model classifying genes as null (complete tolerance), autosomal recessive, or haploinsufficient (heterozygous pLoF intolerance).
   - Values near $1.0$ ($\ge 0.9$) indicate extreme intolerance to losing a single copy of the gene in human populations.
2. **LOEUF (`oe_lof_upper`) — Loss-of-Function Observed/Expected Upper Bound Fraction:**
   - The upper bound of the 90% confidence interval of the observed-to-expected ($\text{O/E}$) ratio for predicted loss-of-function (pLoF) variants (nonsense, essential splice site, and frameshift variants).
   - Because small genes can exhibit a low point estimate (`oe_lof`) by chance due to small sample sizes, **LOEUF** incorporates gene length and statistical uncertainty. Lower LOEUF values indicate stronger purifying selection against truncating variants.
3. **Missense Constraint (`oe_mis` and 90% CI):**
   - Compares the observed count of missense (amino-acid-changing) variants in the population against the expected count under a neutral background mutation model.
   - An $\text{O/E} < 1$ means missense variants are depleted by purifying selection; $\text{O/E} \ge 1$ indicates that amino-acid substitutions accumulate freely without measurable fitness cost.

---

## 3. Evolutionary Tolerance Comparison

### *SCN1A* (Sodium Voltage-Gated Channel Alpha Subunit 1, $\text{Na}_\text{V}1.1$)
- **Extreme Loss-of-Function Intolerance (`pLI = 1.0`, `oe_lof = 0.067`, `LOEUF = 0.107`):**
  - Only **6.7%** of expected pLoF variants are observed in gnomAD, and the conservative 90% upper bound (**LOEUF = 0.107**) places *SCN1A* in the top decile of the most constrained genes in the human genome.
  - Evolutionarily, *SCN1A* is strictly **haploinsufficient**: losing one functional copy impairs action potential initiation in GABAergic inhibitory interneurons in the central nervous system, leading to severe early-onset developmental and epileptic encephalopathy (**Dravet syndrome**). Because Dravet syndrome severely reduces reproductive fitness, natural selection rapidly purges pLoF alleles from the population.
- **Strong Missense Constraint (`oe_mis = 0.584`, 90% CI: `0.559 – 0.610`):**
  - Over **41%** of expected missense variants are absent from the general population. Even single amino-acid substitutions—particularly in the pore-forming loops and voltage-sensing transmembrane segments—are subject to strong purifying selection and frequently cause Dravet syndrome or Generalized Epilepsy with Febrile Seizures Plus (GEFS+).

### *OR2T1* (Olfactory Receptor Family 2 Subfamily T Member 1)
- **Complete Missense Tolerance / Relaxed Purifying Selection (`oe_mis = 1.128`, 90% CI: `1.043 – 1.220`):**
  - *OR2T1* exhibits **~12.8% more missense variants than expected** under a neutral mutation model, with its entire 90% confidence interval exceeding $1.0$ (`1.043 – 1.220`).
  - Olfactory receptors belong to a massive, highly redundant multigene superfamily (~400 functional genes and >400 pseudogenes in humans) that recognizes odorants combinatorially. Because primates evolved reduced reliance on olfaction and high receptor redundancy buffers individual gene changes, amino-acid changes in *OR2T1* carry virtually no reproductive fitness penalty.
- **Why `pLI` and `LOEUF` are `null` for *OR2T1*:**
  - In gnomAD's constraint pipeline, genes that deviate strongly from neutral baseline expectations (e.g., excess synonymous/missense polymorphism, low expected pLoF counts in short ~1 kb single-exon transcripts, or paralogous alignment flags typical of olfactory receptors) have their pLoF constraint scores masked (`null`) to avoid unreliable estimates. Biologically, olfactory receptors are among the most LoF-tolerant genes in the human genome and frequently segregate common loss-of-function variants (segregating pseudogenes) in healthy populations.

