# /// script
# requires-python = ">=3.10, <3.13"
# dependencies = [
#     "pymol-open-source-whl",
# ]
# ///

import os
import sys

# Set environment variable for headless rendering before importing anything else
os.environ["PYOPENGL_PLATFORM"] = "osmesa"

import pymol
pymol.pymol_argv = ["pymol", "-cq"]
pymol.finish_launching()

from pymol import cmd, util

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(base_dir, "output")
    structure_path = os.path.join(output_dir, "AF-P15056-F1-model_v6.cif")
    os.makedirs(output_dir, exist_ok=True)
    
    png_path = os.path.join(output_dir, "braf_kinase_domain.png")
    pse_path = os.path.join(output_dir, "braf_kinase_domain.pse")
    
    if not os.path.exists(structure_path):
        print(f"[!] Error: Structure file '{structure_path}' does not exist.")
        cmd.quit()
        sys.exit(1)
        
    print(f"[*] Loading structure: {structure_path}")
    cmd.load(structure_path, "braf_full")
    
    total_atoms = cmd.count_atoms("braf_full")
    if total_atoms == 0:
        print("[!] Error: 0 atoms loaded from structure.")
        cmd.quit()
        sys.exit(1)
    print(f"[*] Successfully loaded {total_atoms} atoms.")
    
    # Check if CA-only trace
    ca_atoms = cmd.count_atoms("braf_full and name CA")
    is_ca_trace = (ca_atoms == total_atoms)
    if is_ca_trace:
        print("[*] Detected C-alpha only trace.")
        cmd.set("cartoon_trace_atoms", 1)
        
    # Isolate kinase domain (canonical residues ~448-723)
    # This removes long disordered N- and C-terminal tails to provide an uncluttered, clear focus on the kinase
    print("[*] Extracting kinase domain (residues 448-723)...")
    cmd.create("braf_kd", "braf_full and resi 448-723")
    cmd.delete("braf_full")
    
    # Configure global visual settings
    cmd.bg_color("white")
    cmd.set("ray_opaque_background", 1)
    cmd.set("cartoon_fancy_helices", 1)
    cmd.set("cartoon_smooth_loops", 1)
    cmd.set("cartoon_flat_sheets", 1)
    cmd.set("stick_radius", 0.22)
    cmd.set("ambient", 0.35)
    cmd.set("direct", 0.65)
    cmd.set("reflect", 0.45)
    cmd.set("shininess", 40)
    cmd.set("specular", 0.4)
    cmd.set("depth_cue", 1)
    
    # Overall cartoon representation
    cmd.show("cartoon", "braf_kd")
    cmd.color("gray85", "braf_kd")
    
    # N-lobe (residues 457-535) and C-lobe (536-717) subtle coloring
    cmd.color("lightteal", "braf_kd and resi 457-535")
    cmd.color("slate", "braf_kd and resi 536-717")
    
    # 1. Define and highlight ATP-binding pocket
    # P-loop (464-471), catalytic Lys483, alphaC Glu501, gatekeeper Thr529, hinge (530-535), catalytic loop (574-578), DFG motif (594-596)
    pocket_sel = "braf_kd and (resi 464-471 or resi 483 or resi 501 or resi 529-535 or resi 574-578 or resi 594-596)"
    cmd.select("atp_pocket", pocket_sel)
    
    # Cartoon highlight for pocket
    cmd.color("palecyan", "atp_pocket and resi 464-471")   # P-loop
    cmd.color("aquamarine", "atp_pocket and resi 529-535") # Hinge
    cmd.color("wheat", "atp_pocket and resi 594-596")      # DFG motif
    
    # Pocket key sidechains as sticks
    pocket_sidechains = "atp_pocket and (resi 468 or resi 483 or resi 501 or resi 529 or resi 532 or resi 576 or resi 594 or resi 595)"
    cmd.show("sticks", pocket_sidechains)
    cmd.color("cyan", f"{pocket_sidechains} and elem C")
    util.cnc(pocket_sidechains)
    
    # Highlight activation segment containing Val600
    cmd.color("lightpink", "braf_kd and resi 597-620")

    # 2. Highlight Val600 in prominent red sticks
    print("[*] Highlighting residue Val600 in red sticks...")
    cmd.select("val600", "braf_kd and resi 600")
    cmd.show("sticks", "val600")
    cmd.color("red", "val600")
    cmd.set("stick_radius", 0.42, "val600")

    # Setup camera view: classic kinase orientation (N-lobe top, C-lobe bottom)
    cmd.orient("braf_kd")
    cmd.turn("z", -90)
    cmd.turn("y", 15)
    cmd.turn("x", 10)
    cmd.zoom("braf_kd", buffer=2.0)
    
    # Deselect all to remove dashed pink selection box
    cmd.deselect()
    
    print(f"[*] Rendering high-resolution PNG: {png_path}")
    cmd.png(png_path, width=1920, height=1440, dpi=300)
    
    print(f"[*] Saving PyMOL session file: {pse_path}")
    cmd.save(pse_path)
    
    print("[*] PyMOL script finished successfully.")
    cmd.quit()

if __name__ == "__main__":
    main()
