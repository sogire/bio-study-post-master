import os
import sys
import json
import dotenv
import pandas as pd
import numpy as np

# Load environment variables
dotenv.load_dotenv(os.path.expanduser('~/.env'))

from alphagenome.models import dna_client
from alphagenome.models import variant_scorers
from alphagenome.data import genome

api_key = os.environ.get('ALPHAGENOME_API_KEY')
if not api_key:
    print("Error: ALPHAGENOME_API_KEY not found in ~/.env", file=sys.stderr)
    sys.exit(1)

print("Connecting to AlphaGenome API...")
dna_model = dna_client.create(api_key=api_key, address='dns:///gdmscience.googleapis.com:443')

variant_str = "chr5:1295228:C>T"
chrom = "chr5"
pos = 1295228
ref = "C"
alt = "T"

SEQ_LENGTH = 2**20  # 1,048,576 bp
interval = genome.Interval(chrom, pos - SEQ_LENGTH // 2, pos + SEQ_LENGTH // 2)
variant = genome.Variant(chrom, pos, ref, alt)

print(f"Scoring variant {variant_str} across recommended differential scorers...")
scorers = [
    variant_scorers.RECOMMENDED_VARIANT_SCORERS[m]
    for m in variant_scorers.RECOMMENDED_VARIANT_SCORERS
    if "ACTIVE" not in m and "CAGE" not in m and "PROCAP" not in m
]

scores_list = dna_model.score_variant(interval=interval, variant=variant, variant_scorers=scorers)

all_dfs = []
for score_adata in scores_list:
    df = variant_scorers.tidy_scores([score_adata], match_gene_strand=True)
    if df is not None:
        all_dfs.append(df)

if all_dfs:
    df = pd.concat(all_dfs, ignore_index=True)
    print(f"Total scored tracks: {len(df)}")
    print(f"Columns: {list(df.columns)}")
    
    # Save full results to TSV
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(base_dir, "output")
    os.makedirs(out_dir, exist_ok=True)
    df.to_csv(os.path.join(out_dir, "tert_c228t_all_scores.tsv"), sep="\t", index=False)
    
    # Significant hits
    if 'quantile_score' in df.columns:
        sig = df[df['quantile_score'].abs() > 0.99]
        ranked = sig.sort_values('raw_score', key=abs, ascending=False)
        print("\n=== TOP 25 SIGNIFICANT HITS (|quantile| > 0.99) ===")
        print(ranked[['biosample_name', 'gene_name', 'output_type', 'raw_score', 'quantile_score']].head(25).to_string())
        
        # Specifically filter for TERT
        tert_df = df[df['gene_name'] == 'TERT'].sort_values('raw_score', key=abs, ascending=False)
        print("\n=== TOP TERT HITS ===")
        print(tert_df[['biosample_name', 'gene_name', 'output_type', 'raw_score', 'quantile_score']].head(25).to_string())
        
        # Group by output_type for TERT
        print("\n=== TERT SCORES BY OUTPUT TYPE ===")
        for otype, group in tert_df.groupby('output_type'):
            print(f"\n--- {otype} (top 5) ---")
            print(group[['biosample_name', 'raw_score', 'quantile_score']].head(5).to_string())
            
        # Cancer and disease-relevant keywords
        keywords = ["melanoma", "skin", "glioma", "glioblastoma", "brain", "bladder", "liver", "hep", "urothelial", "fibroblast"]
        mask = df['biosample_name'].str.contains('|'.join(keywords), case=False, na=False)
        cancer_df = df[mask].sort_values('raw_score', key=abs, ascending=False)
        print(f"\n=== CANCER & RELEVANT TISSUES HITS ({keywords}) ===")
        print(cancer_df[['biosample_name', 'gene_name', 'output_type', 'raw_score', 'quantile_score']].head(25).to_string())
else:
    print("No scores returned.")

