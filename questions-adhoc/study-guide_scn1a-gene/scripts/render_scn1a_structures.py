# /// script
# requires-python = ">=3.10, <3.13"
# dependencies = [
#     "pymol-open-source-whl",
# ]
# ///
"""
Reproducible PyMOL 3D structural analysis and ray-tracing script for the
SCN1A (NaV1.1) Study Guide.

Loads structures from ../structures/ and generates publication-grade figures
(.png) paired with interactive PyMOL session files (.pse) in ../figures/:
  - fig1_alphafold_plddt.{png,pse} (AF-P35498-F1-model_v6.cif)
  - fig2_cryoem_7dtd_domains.{png,pse} (7DTD.cif)
  - fig3_functional_and_disease_hotspots.{png,pse} (7DTD.cif)

Usage:
    PYOPENGL_PLATFORM=osmesa /home/sergiobermudez/.local/bin/uv run scripts/render_scn1a_structures.py
"""

import os
from pathlib import Path

os.environ.setdefault("PYOPENGL_PLATFORM", "osmesa")

import pymol
from pymol import cmd

BASE_DIR = Path(__file__).resolve().parent.parent
STRUCTURES_DIR = BASE_DIR / "structures"
FIGURES_DIR = BASE_DIR / "figures"


def apply_base_publication_style() -> None:
    """Apply clean publication rendering parameters in headless PyMOL."""
    cmd.bg_color("white")
    cmd.set("ray_opaque_background", 1)
    cmd.set("orthoscopic", 1)
    cmd.set("depth_cue", 0)
    cmd.set("antialias", 2)
    cmd.set("ray_trace_mode", 1)
    cmd.set("ray_shadows", 0)
    cmd.set("specular", 0.25)
    cmd.set("cartoon_fancy_helices", 1)


def render_fig1_alphafold_plddt() -> None:
    """Render Figure 1: AlphaFold 2 structure of human NaV1.1 (P35498) colored by pLDDT."""
    cmd.reinitialize()
    apply_base_publication_style()
    cmd.load(str(STRUCTURES_DIR / "AF-P35498-F1-model_v6.cif"), "nav11_af")
    cmd.hide("everything", "all")
    cmd.show("cartoon", "nav11_af")

    cmd.set_color("plddt_vh", [0.0, 0.325, 0.843])
    cmd.set_color("plddt_conf", [0.396, 0.796, 0.953])
    cmd.set_color("plddt_low", [1.0, 0.859, 0.075])
    cmd.set_color("plddt_vlow", [1.0, 0.490, 0.271])

    cmd.color("plddt_vh", "nav11_af and b > 89.99")
    cmd.color("plddt_conf", "nav11_af and b < 90.0 and b > 69.99")
    cmd.color("plddt_low", "nav11_af and b < 70.0 and b > 49.99")
    cmd.color("plddt_vlow", "nav11_af and b < 50.0")

    cmd.orient("nav11_af and resi 110-454+750-1022+1200-1483+1542-1788")
    cmd.zoom("nav11_af", buffer=4.0)

    cmd.save(str(FIGURES_DIR / "fig1_alphafold_plddt.pse"))
    cmd.png(str(FIGURES_DIR / "fig1_alphafold_plddt.png"), width=1800, height=1400, dpi=300, ray=1)


def render_fig2_cryoem_7dtd_domains() -> None:
    """Render Figure 2: Experimental Cryo-EM structure of NaV1.1 + Beta-4 (PDB: 7DTD)."""
    cmd.reinitialize()
    apply_base_publication_style()
    cmd.load(str(STRUCTURES_DIR / "7DTD.cif"), "nav11_em")
    cmd.hide("everything", "all")
    cmd.show("cartoon", "nav11_em and polymer.protein")

    cmd.color("deepteal", "chain A and resi 110-454")
    cmd.color("forest", "chain A and resi 750-1022")
    cmd.color("tv_orange", "chain A and resi 1200-1483")
    cmd.color("tv_red", "chain A and resi 1484-1541")
    cmd.color("marine", "chain A and resi 1542-1788")
    cmd.color("magenta", "chain B")

    cmd.select("ifm_motif", "chain A and resi 1498-1500")
    cmd.show("spheres", "ifm_motif")
    cmd.color("red", "ifm_motif")

    cmd.orient("nav11_em and polymer.protein")
    cmd.zoom("nav11_em and polymer.protein", buffer=3.0)

    cmd.save(str(FIGURES_DIR / "fig2_cryoem_7dtd_domains.pse"))
    cmd.png(str(FIGURES_DIR / "fig2_cryoem_7dtd_domains.png"), width=1800, height=1400, dpi=300, ray=1)


def render_fig3_functional_and_disease_hotspots() -> None:
    """Render Figure 3: Top-down pore view of DEKA selectivity filter, S4 sensors, and IFM latch."""
    cmd.reinitialize()
    apply_base_publication_style()
    cmd.load(str(STRUCTURES_DIR / "7DTD.cif"), "nav11_em")
    cmd.hide("everything", "all")
    cmd.show("cartoon", "chain A")
    cmd.color("gray85", "chain A")

    # Pore module (S5-S6)
    cmd.color("lightblue", "chain A and resi 246-423+892-992+1346-1483+1666-1788")
    # Voltage-sensing S4 helices
    cmd.color("tv_yellow", "chain A and resi 214-235+855-874+1314-1332+1637-1655")
    # DIII-DIV inactivation gate + IFM latch
    cmd.color("tv_red", "chain A and resi 1484-1541")
    cmd.show("spheres", "chain A and resi 1498-1500 and name CA+CB")
    cmd.color("red", "chain A and resi 1498-1500")

    # DEKA selectivity filter (Asp382, Glu951, Lys1432, Ala1724)
    cmd.select("deka_filter", "chain A and resi 382+951+1432+1724")
    cmd.show("spheres", "deka_filter")
    cmd.color("marine", "deka_filter")

    # GoF S4 mutation hotspots (Thr226, Leu1649)
    cmd.select("gof_hotspots", "chain A and resi 226+1649")
    cmd.show("spheres", "gof_hotspots")
    cmd.color("magenta", "gof_hotspots")

    cmd.orient("deka_filter")
    cmd.zoom("chain A", buffer=2.0)

    cmd.save(str(FIGURES_DIR / "fig3_functional_and_disease_hotspots.pse"))
    cmd.png(str(FIGURES_DIR / "fig3_functional_and_disease_hotspots.png"), width=1800, height=1400, dpi=300, ray=1)


def main() -> None:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    pymol.finish_launching(["pymol", "-cq"])
    render_fig1_alphafold_plddt()
    render_fig2_cryoem_7dtd_domains()
    render_fig3_functional_and_disease_hotspots()
    print(f"Rendered figures and PyMOL sessions in {FIGURES_DIR}")


if __name__ == "__main__":
    main()

