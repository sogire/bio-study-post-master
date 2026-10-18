# Exercise 2.1: Dissecting an Enhancer Landscape with ENCODE

## 1. Executive Summary

This report documents the candidate cis-regulatory elements (cCREs) identified around the human beta-globin (*HBB*) locus on chromosome 11 within the window **`chr11:5,200,000-5,225,000`** (human genome assembly **GRCh38**), queried via the **ENCODE SCREEN API** (Registry of Candidate cis-Regulatory Elements).

A total of **20 cCREs** reside within this 25 kb interval. The primary regulatory elements classified as **Promoters (PLS)**, **Proximal Enhancers (pELS)**, and **Distal Enhancers (dELS)** are:

* **Promoter-like Signature (PLS)**: **1 element** (`EH38E2941857`)
* **Proximal Enhancer-like Signatures (pELS)**: **2 elements** (`EH38E2941856`, `EH38E2941850`)
* **Distal Enhancer-like Signatures (dELS)**: **2 elements** (`EH38E1516902`, `EH38E4028464`)

The remaining 15 elements represent chromatin-accessible structural/boundary elements (**6 CA-CTCF**), open chromatin alone (**6 CA**), chromatin accessibility with promoter-like histone modifications (**2 CA-H3K4me3**), and transcription factor binding sites (**1 CA-TF**).

---

## 2. Genomic & Biological Context

* **Gene Locus**: *HBB* (hemoglobin subunit beta, Ensembl ID: `ENSG00000244734`) is located at **`chr11:5,225,464-5,229,395`** on the reverse strand.
* **Target Region**: **`chr11:5,200,000-5,225,000`** (25,001 bp). This region lies directly upstream of the *HBB* transcription start site (TSS) and spans the proximal promoter region and downstream portions of the beta-globin Locus Control Region (LCR) regulatory domain.
* **Nearest Flanking Genes**:
  * *HBB* (`chr11:5,225,464-5,229,395`)
  * *HBD* (`chr11:5,232,678-5,243,657`)
  * *OR51V1* (`chr11:5,198,393-5,202,304`)
  * Long non-coding transcripts / pseudogene features (e.g., `ENSG00000224091`, `ENSG00000221031`)

---

## 3. Detailed Breakdown of Target Regulatory Elements

### A. Promoter-like Signatures (PLS) — 1 Element

Promoter-like elements are defined by high chromatin accessibility (DNase $Z \ge 1.64$) accompanied by high trimethylation of histone H3 lysine 4 (H3K4me3 $Z \ge 1.64$), typically situated within 200 bp of an annotated TSS.

#### `EH38E2941857`
* **Coordinates (GRCh38)**: `chr11:5,224,606-5,224,887`
* **Length**: 281 bp
* **Max Epigenetic Z-Scores**:
  * **DNase (Accessibility)**: `6.03`
  * **H3K4me3 (Promoter mark)**: `4.80`
  * **H3K27ac (Enhancer mark)**: `2.70`
  * **CTCF (Insulator mark)**: `1.89`
* **Nearest Gene**: `ENSG00000221031` (0 bp) / *HBB* (~577 bp downstream at `5,225,464`)
* **Biological Relevance**: Shows exceptionally strong DNase accessibility and H3K4me3 enrichment, matching the primary core promoter driving beta-globin cluster transcription.

---

### B. Proximal Enhancer-like Signatures (pELS) — 2 Elements

Proximal enhancer-like elements display high chromatin accessibility (DNase $Z \ge 1.64$) and high acetylation of histone H3 lysine 27 (H3K27ac $Z \ge 1.64$) located within 2 kb of an annotated TSS, or with intermediate H3K4me3 levels.

#### 1. `EH38E2941856`
* **Coordinates (GRCh38)**: `chr11:5,224,200-5,224,360`
* **Length**: 160 bp
* **Max Epigenetic Z-Scores**:
  * **DNase**: `5.67`
  * **H3K4me3**: `1.39`
  * **H3K27ac**: `1.97`
  * **CTCF**: `1.89`
* **Nearest Gene**: `ENSG00000221031` (279 bp) / *HBB* (~1,104 bp upstream)
* **Biological Relevance**: Proximal upstream enhancer element acting in concert with the *HBB* promoter (`EH38E2941857`).

#### 2. `EH38E2941850`
* **Coordinates (GRCh38)**: `chr11:5,205,904-5,206,175`
* **Length**: 271 bp
* **Max Epigenetic Z-Scores**:
  * **DNase**: `2.39`
  * **H3K4me3**: `1.07`
  * **H3K27ac**: `1.66`
  * **CTCF**: `1.43`
* **Nearest Gene**: `ENSG00000224091` (863 bp) / *OR51V1* (5,222 bp)
* **Biological Relevance**: Enhancer element located ~19.3 kb upstream of the *HBB* TSS, situated near upstream non-coding transcript anchors.

---

### C. Distal Enhancer-like Signatures (dELS) — 2 Elements

Distal enhancer-like elements exhibit high DNase accessibility and high H3K27ac ($Z \ge 1.64$), low H3K4me3, and are situated greater than 2 kb away from the nearest annotated TSS.

#### 1. `EH38E1516902`
* **Coordinates (GRCh38)**: `chr11:5,210,486-5,210,830`
* **Length**: 344 bp
* **Max Epigenetic Z-Scores**:
  * **DNase**: `2.90`
  * **H3K4me3**: `1.31`
  * **H3K27ac**: `2.74`
  * **CTCF**: `1.94`
* **Nearest Gene**: `ENSG00000224091` (5,445 bp) / *HBB* (~14.6 kb upstream)
* **Biological Relevance**: Strong distal enhancer element with prominent H3K27ac enrichment (max $Z = 2.74$), characteristic of active looping enhancers in the beta-globin regulatory landscape.

#### 2. `EH38E4028464`
* **Coordinates (GRCh38)**: `chr11:5,209,470-5,209,685`
* **Length**: 215 bp
* **Max Epigenetic Z-Scores**:
  * **DNase**: `2.71`
  * **H3K4me3**: `1.36`
  * **H3K27ac**: `1.82`
  * **CTCF**: `1.44`
* **Nearest Gene**: `ENSG00000224091` (4,429 bp) / *HBB* (~15.8 kb upstream)
* **Biological Relevance**: Distal enhancer element located ~15.8 kb upstream of *HBB*, contributing to long-range transcriptional activation.

---

## 4. Summary Table of PLS, pELS, and dELS Elements

| Accession | Classification | Genomic Coordinates (GRCh38) | Size | DNase Max-Z | H3K4me3 Max-Z | H3K27ac Max-Z | CTCF Max-Z | Relative Position |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **`EH38E2941857`** | **PLS** (Promoter) | `chr11:5,224,606-5,224,887` | 281 bp | **6.03** | **4.80** | **2.70** | 1.89 | ~0.6 kb upstream of *HBB* TSS |
| **`EH38E2941856`** | **pELS** (Proximal Enhancer) | `chr11:5,224,200-5,224,360` | 160 bp | **5.67** | 1.39 | **1.97** | 1.89 | ~1.2 kb upstream of *HBB* TSS |
| **`EH38E2941850`** | **pELS** (Proximal Enhancer) | `chr11:5,205,904-5,206,175` | 271 bp | **2.39** | 1.07 | **1.66** | 1.43 | ~19.3 kb upstream of *HBB* TSS |
| **`EH38E4028464`** | **dELS** (Distal Enhancer) | `chr11:5,209,470-5,209,685` | 215 bp | **2.71** | 1.36 | **1.82** | 1.44 | ~15.8 kb upstream of *HBB* TSS |
| **`EH38E1516902`** | **dELS** (Distal Enhancer) | `chr11:5,210,486-5,210,830` | 344 bp | **2.90** | 1.31 | **2.74** | 1.94 | ~14.6 kb upstream of *HBB* TSS |

---

## 5. Complete Catalog of All 20 cCREs in `chr11:5,200,000-5,225,000`

In addition to the 5 promoter and enhancer elements, the remaining 15 cCREs establish chromatin boundaries, loops, and uncharacterized accessible regions:

| Accession | Class | Coordinates (GRCh38) | Size | DNase Z | H3K4me3 Z | H3K27ac Z | CTCF Z | Primary Feature |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `EH38E4028460` | **CA** | `chr11:5,201,493-5,201,825` | 332 bp | 2.18 | 1.10 | 0.95 | 1.53 | Open chromatin |
| `EH38E4028461` | **CA** | `chr11:5,203,401-5,203,735` | 334 bp | 2.86 | 1.03 | 1.36 | 1.64 | Open chromatin |
| `EH38E2941849` | **CA-CTCF** | `chr11:5,204,387-5,204,699` | 312 bp | 1.93 | 1.16 | 1.26 | 2.80 | Insulator/boundary |
| `EH38E1516900` | **CA-CTCF** | `chr11:5,204,840-5,205,189` | 349 bp | **5.57** | 0.85 | 1.39 | **5.04** | Major CTCF loop anchor |
| `EH38E4028462` | **CA-TF** | `chr11:5,205,471-5,205,800` | 329 bp | 2.87 | 1.06 | 1.62 | 1.43 | TF-bound open chromatin |
| `EH38E2941850` | **pELS** | `chr11:5,205,904-5,206,175` | 271 bp | 2.39 | 1.07 | 1.66 | 1.43 | Proximal enhancer |
| `EH38E2941851` | **CA-CTCF** | `chr11:5,206,974-5,207,153` | 179 bp | 1.88 | 0.99 | 1.08 | 1.75 | Insulator/boundary |
| `EH38E4028463` | **CA** | `chr11:5,208,235-5,208,561` | 326 bp | 2.07 | 1.13 | 0.91 | 1.47 | Open chromatin |
| `EH38E1516901` | **CA-CTCF** | `chr11:5,208,972-5,209,131` | 159 bp | 2.16 | 1.44 | 1.25 | 2.44 | Insulator/boundary |
| `EH38E4028464` | **dELS** | `chr11:5,209,470-5,209,685` | 215 bp | 2.71 | 1.36 | 1.82 | 1.44 | Distal enhancer |
| `EH38E1516902` | **dELS** | `chr11:5,210,486-5,210,830` | 344 bp | 2.90 | 1.31 | 2.74 | 1.94 | Distal enhancer |
| `EH38E2941852` | **CA-H3K4me3** | `chr11:5,213,651-5,213,994` | 343 bp | 2.38 | 1.66 | 0.90 | 1.42 | Open chromatin + H3K4me3 |
| `EH38E2941853` | **CA-H3K4me3** | `chr11:5,214,120-5,214,407` | 287 bp | 1.89 | 2.33 | 0.88 | 1.47 | Open chromatin + H3K4me3 |
| `EH38E2941854` | **CA-CTCF** | `chr11:5,215,377-5,215,702` | 325 bp | 1.86 | 1.30 | 1.29 | 1.77 | Insulator/boundary |
| `EH38E4028465` | **CA** | `chr11:5,221,441-5,221,771` | 330 bp | 1.72 | 1.01 | 0.95 | 1.42 | Open chromatin |
| `EH38E2941855` | **CA-CTCF** | `chr11:5,222,325-5,222,555` | 230 bp | 3.15 | 1.16 | 0.68 | 1.94 | Insulator/boundary |
| `EH38E4028466` | **CA** | `chr11:5,223,181-5,223,527` | 346 bp | 4.10 | 1.14 | 1.22 | 1.25 | Open chromatin |
| `EH38E4028467` | **CA** | `chr11:5,223,724-5,224,006` | 282 bp | 5.50 | 0.98 | 1.12 | 1.45 | High-accessibility region |
| `EH38E2941856` | **pELS** | `chr11:5,224,200-5,224,360` | 160 bp | 5.67 | 1.39 | 1.97 | 1.89 | Proximal enhancer |
| `EH38E2941857` | **PLS** | `chr11:5,224,606-5,224,887` | 281 bp | 6.03 | 4.80 | 2.70 | 1.89 | Core promoter |

> **Key Observation on Insulation**: Element `EH38E1516900` displays an exceptionally strong CTCF signal ($Z = 5.04$) and high DNase accessibility ($Z = 5.57$). In erythroid development, strong CTCF binding sites in the beta-globin upstream locus function as critical loop anchors (insulators) demarcating the active beta-globin regulatory domain from flanking heterochromatin and olfactory receptor gene clusters.

---

## 6. ENCODE Classification Logic Reference

ENCODE classifies candidate cis-regulatory elements using standardized thresholds on normalized epigenetic assay Z-scores:

```
                          ┌────────────────────────┐
                          │ DNase Z >= 1.64 or     │
                          │ H3K4me3/H3K27ac/CTCF   │
                          │      Z >= 1.64         │
                          └───────────┬────────────┘
                                      │
              ┌───────────────────────┴───────────────────────┐
              ▼                                               ▼
       H3K4me3 Z >= 1.64                               H3K4me3 Z < 1.64
              │                                               │
      ┌───────┴───────┐                               ┌───────┴───────┐
      ▼               ▼                               ▼               ▼
TSS <= 200 bp   TSS > 200 bp                    H3K27ac >= 1.64  H3K27ac < 1.64
     │               │                                │               │
    PLS             dELS                      ┌───────┴───────┐       ▼
(Promoter)   (if H3K27ac >= 1.64)             ▼               ▼    CTCF >= 1.64?
                      or                 TSS <= 2000 bp  TSS > 2000 bp   ├── Yes -> CA-CTCF
                  CA-H3K4me3                  │               │          └── No  -> CA
                                             pELS            dELS
                                         (Proximal)        (Distal)
```

---

## 7. Data Attribution & Compliance

Data was obtained through the **ENCODE Project Consortium / SCREEN Registry of cCREs** via the SCREEN GraphQL API endpoint (`https://factorbook.api.wenglab.org/graphql`). For information on data citation and usage guidelines, see the [ENCODE REST API & Usage Policy](https://www.encodeproject.org/help/rest-api/).

