# /// script
# requires-python = ">=3.10, <3.13"
# dependencies = [
#     "pymol-open-source-whl",
# ]
# ///
"""Reproducible PyMOL 3.2 structural analysis and rendering script for Non-Infectious Anterior Uveitis.

Loads experimental structures from `../structures/`:
  1. 1M2Z.cif — Human Glucocorticoid Receptor (NR3C1) LBD + corticosteroid agonist + TIF2 peptide
  2. 4U15.cif — Muscarinic Acetylcholine Receptor M3 (CHRM3) + orthosteric antimuscarinic antagonist
  3. 3WD5.cif — Human TNF-alpha + Adalimumab Fab fragment

Computes key polar contact distances and saves ray-traced figures (.png) and PyMOL sessions (.pse)
into `../figures/`.
"""

import os
from pathlib import Path

os.environ.setdefault("PYOPENGL_PLATFORM", "osmesa")

import pymol
from pymol import cmd

BASE_DIR = Path(__file__).resolve().parent.parent
STRUCTURES_DIR = BASE_DIR / "structures"
FIGURES_DIR = BASE_DIR / "figures"


def setup_pymol() -> None:
    pymol.finish_launching(["pymol", "-cq"])
    cmd.set("bg_rgb", [1.0, 1.0, 1.0])
    cmd.set("ray_opaque_background", 1)
    cmd.set("orthoscopic", 1)
    cmd.set("antialias", 2)
    cmd.set("ray_trace_mode", 1)
    cmd.set("ray_shadows", 0)
    cmd.set("specular", 0.25)


def render_fig1_nr3c1() -> None:
    """Render Figure 1: NR3C1 LBD + Corticosteroid Pocket (PDB 1M2Z)."""
    cmd.reinitialize()
    setup_pymol()
    cmd.load(str(STRUCTURES_DIR / "1M2Z.cif"), "nr3c1")
    cmd.remove("solvent")

    cmd.hide("everything")
    cmd.show("cartoon", "chain A and polymer.protein")
    cmd.color("marine", "chain A and polymer.protein")
    cmd.show("cartoon", "chain B and polymer.protein")
    cmd.color("brightorange", "chain B and polymer.protein")

    cmd.select("steroid", "chain A and resn DEX")
    cmd.show("sticks", "steroid")
    cmd.util.cbag("steroid")
    cmd.color("tv_yellow", "steroid and elem C")

    pocket_res = "chain A and resi 564+570+611+642+739"
    cmd.show("sticks", pocket_res)
    cmd.util.cbac(pocket_res)

    cmd.distance("hbonds_nr3c1", "steroid", pocket_res, mode=2, cutoff=3.5)
    cmd.color("red", "hbonds_nr3c1")
    cmd.hide("labels", "hbonds_nr3c1")

    cmd.orient("steroid or (" + pocket_res + ")")
    cmd.zoom("steroid or (" + pocket_res + ")", buffer=4.0)

    cmd.save(str(FIGURES_DIR / "fig1_nr3c1_corticosteroid_pocket.pse"))
    cmd.ray(1800, 1400)
    cmd.png(str(FIGURES_DIR / "fig1_nr3c1_corticosteroid_pocket.png"), dpi=300)
    print("Saved Figure 1: fig1_nr3c1_corticosteroid_pocket.{png,pse}")


def render_fig2_chrm3() -> None:
    """Render Figure 2: CHRM3 Orthosteric Antimuscarinic Pocket (PDB 4U15)."""
    cmd.reinitialize()
    setup_pymol()
    cmd.load(str(STRUCTURES_DIR / "4U15.cif"), "chrm3")
    cmd.remove("solvent")

    cmd.hide("everything")
    cmd.show("cartoon", "chain A and polymer.protein")
    cmd.color("deepteal", "chain A and polymer.protein")

    cmd.select("antag", "chain A and resn 0HK")
    cmd.show("sticks", "antag")
    cmd.util.cbao("antag")

    pocket_res = "chain A and resi 147+148+503+506+507+529+533"
    cmd.show("sticks", pocket_res)
    cmd.util.cbaw(pocket_res)

    cmd.distance("hbonds_chrm3", "antag", pocket_res, mode=2, cutoff=3.5)
    cmd.color("red", "hbonds_chrm3")
    cmd.hide("labels", "hbonds_chrm3")

    cmd.orient("antag or (" + pocket_res + ")")
    cmd.zoom("antag or (" + pocket_res + ")", buffer=4.0)

    cmd.save(str(FIGURES_DIR / "fig2_chrm3_antimuscarinic_pocket.pse"))
    cmd.ray(1800, 1400)
    cmd.png(str(FIGURES_DIR / "fig2_chrm3_antimuscarinic_pocket.png"), dpi=300)
    print("Saved Figure 2: fig2_chrm3_antimuscarinic_pocket.{png,pse}")


def render_fig3_tnf_adalimumab() -> None:
    """Render Figure 3: TNF-alpha + Adalimumab Fab Complex (PDB 3WD5)."""
    cmd.reinitialize()
    setup_pymol()
    cmd.load(str(STRUCTURES_DIR / "3WD5.cif"), "tnf_ada")
    cmd.remove("solvent")

    cmd.hide("everything")
    cmd.show("cartoon", "chain A+H+L and polymer.protein")
    cmd.color("salmon", "chain A")
    cmd.color("marine", "chain H")
    cmd.color("skyblue", "chain L")

    epitope = "chain A and resi 20+21+65+67+145+146+147"
    paratope = "(chain H and resi 57+103+104) or (chain L and resi 1+30+31+91+92+93)"
    cmd.show("sticks", epitope)
    cmd.color("firebrick", epitope + " and elem C")
    cmd.show("sticks", paratope)
    cmd.color("deepblue", paratope + " and elem C")

    cmd.distance("hbonds_tnf", epitope, paratope, mode=2, cutoff=3.5)
    cmd.color("red", "hbonds_tnf")
    cmd.hide("labels", "hbonds_tnf")

    cmd.orient("(" + epitope + ") or (" + paratope + ")")
    cmd.zoom("(" + epitope + ") or (" + paratope + ")", buffer=5.0)

    cmd.save(str(FIGURES_DIR / "fig3_tnf_adalimumab_complex.pse"))
    cmd.ray(1800, 1400)
    cmd.png(str(FIGURES_DIR / "fig3_tnf_adalimumab_complex.png"), dpi=300)
    print("Saved Figure 3: fig3_tnf_adalimumab_complex.{png,pse}")


if __name__ == "__main__":
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    render_fig1_nr3c1()
    render_fig2_chrm3()
    render_fig3_tnf_adalimumab()

