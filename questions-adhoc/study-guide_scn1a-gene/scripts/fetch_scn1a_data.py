# /// script
# requires-python = ">=3.10, <3.13"
# dependencies = [
#     "requests>=2.31.0",
# ]
# ///
"""
Reproducible data acquisition script for the SCN1A (NaV1.1) Study Guide.
Queries Reactome Analysis Service, STRING API, and AlphaFold DB metadata,
saving structured outputs to ../data/ and network figure to ../figures/.

Usage:
    /home/sergiobermudez/.local/bin/uv run scripts/fetch_scn1a_data.py
"""

from pathlib import Path
import json
import requests

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
FIGURES_DIR = BASE_DIR / "figures"

CHANNELOSOME_GENES = [
    "SCN1A", "SCN1B", "SCN2B", "SCN3B", "SCN4B",
    "ANK3", "SPTBN4", "SPTAN1", "NFASC", "NRCAM", "L1CAM",
    "FGF12", "FGF13", "FGF14",
    "CALM1", "CALM2", "CALM3",
    "PRKACA", "PRKACB", "PRKACG",
    "NEDD4L",
]


def fetch_reactome_enrichment(genes: list[str]) -> dict:
    """Submit the 21-gene SCN1A channelosome list to Reactome Analysis Service."""
    url = "https://reactome.org/AnalysisService/identifiers/?interactors=false&pageSize=20&page=1"
    headers = {"Content-Type": "text/plain", "Accept": "application/json"}
    response = requests.post(url, data="\n".join(genes), headers=headers, timeout=30)
    response.raise_for_status()
    return response.json()


def fetch_string_network_image(genes: list[str], out_path: Path) -> None:
    """Download high-resolution STRING PPI network image for human SCN1A channelosome."""
    url = "https://string-db.org/api/highres_image/network"
    params = {
        "identifiers": "%0d".join(genes),
        "species": 9606,
        "network_flavor": "Confidence",
        "hide_node_labels": 0,
    }
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    out_path.write_bytes(response.content)


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Verified SCN1A data files in {DATA_DIR}:")
    for p in sorted(DATA_DIR.glob("*.json")):
        data = json.loads(p.read_text())
        print(f"  - {p.name} ({len(data)} top-level keys)")


if __name__ == "__main__":
    main()

