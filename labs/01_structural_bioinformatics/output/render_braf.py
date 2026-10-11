# /// script
# requires-python = ">=3.10, <3.13"
# dependencies = [
#     "pymol-open-source-whl",
# ]
# ///

"""Generates a high-resolution cartoon rendering of the BRAF kinase domain,

highlighting the ATP-binding pocket and residue Val600 in PyMOL.
"""

import os
import sys

# Headless OSMesa configuration
os.environ["PYOPENGL_PLATFORM"] = "osmesa"

import pymol
pymol.pymol_argv = ["pymol", "-cq"]
pymol.finish_launching()

from pymol import cmd

# 1. Pre-flight file check
cif_path = "output/AF-P15056-F1-model_v6.cif"
if not os.path.exists(cif_path):
    print(f"Error: Structure file {cif_path} does not exist.")
    cmd.quit()
    sys.exit(1)

# 2. Load structure and verify atoms
cmd.load(cif_path, "braf_full")
if cmd.count_atoms("braf_full") == 0:
    print("Error: 0 atoms loaded from structure.")
    cmd.quit()
    sys.exit(1)

# 3. Create isolated kinase domain object (residues 448-723)
cmd.create("braf_kd", "braf_full and resi 448-723")
cmd.disable("braf_full")

# 4. Orient: standard kinase orientation (N-lobe top, C-lobe bottom, cleft facing viewer)
cmd.orient("braf_kd")
cmd.rotate("z", -90)
cmd.rotate("y", -20)
cmd.rotate("x", 15)
cmd.center("braf_kd")
cmd.zoom("braf_kd", buffer=1.5)

# 5. Visual settings
cmd.bg_color("white")
cmd.set("ray_opaque_background", 1)
cmd.set("ambient", 0.25)
cmd.set("specular", 0.35)
cmd.set("shininess", 50)
cmd.set("cartoon_transparency", 0.15)
cmd.set("cartoon_fancy_helices", 1)
cmd.set("stick_radius", 0.20)

# Kinase cartoon coloring
cmd.show("cartoon", "braf_kd")
cmd.color("gray85", "braf_kd")
cmd.color("slate", "braf_kd and ss h")
cmd.color("lightblue", "braf_kd and ss s")

# 6. Define ATP-binding pocket and Val600 selections
cmd.select("atp_pocket", "braf_kd and resi 464-471+483+501+529-535+574-576+594-596")
cmd.select("val600", "braf_kd and resi 600")

# Show ATP pocket residues as sticks (warm gold/orange with heteroatom coloring)
cmd.show("sticks", "atp_pocket")
cmd.color("brightorange", "atp_pocket and elem c")
cmd.color("oxygen", "atp_pocket and elem o")
cmd.color("nitrogen", "atp_pocket and elem n")
cmd.color("sulfur", "atp_pocket and elem s")

# Highlight Val600 in prominent red sticks
cmd.show("sticks", "val600")
cmd.set("stick_radius", 0.32, "val600")
cmd.color("red", "val600 and elem c")
cmd.color("oxygen", "val600 and elem o")
cmd.color("nitrogen", "val600 and elem n")

# Label Val600
cmd.set("label_color", "firebrick")
cmd.set("label_size", 22)
cmd.set("label_font_id", 7)
cmd.set("label_position", [-1.5, 0.5, 3.0])
cmd.label("val600 and name CA", '"Val600"')

# Render high-resolution PNG (300 DPI, 2000x1500)
cmd.png("output/braf_kinase_distinct.png", width=2000, height=1500, dpi=300)

# Variation with all pocket residues in red sticks
cmd.color("firebrick", "atp_pocket and elem c")
cmd.color("red", "val600 and elem c")
cmd.set("label_color", "red")
cmd.png("output/braf_kinase_all_red.png", width=2000, height=1500, dpi=300)

# 7. Save PyMOL session file (.pse)
cmd.save("output/braf_kinase_domain.pse")

print("Rendering and session export completed successfully.")
cmd.quit()

