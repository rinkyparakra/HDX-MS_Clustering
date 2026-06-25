# HDX-MS Structural Mapping with PyMOL

This project provides a template for mapping peptide-level HDX-MS differences onto protein structures.

## Goal

Convert HDX-MS peptide-level differences into structure-level visualization using PyMOL.

## Workflow

1. Prepare peptide-level HDX difference table.
2. Assign each residue a value based on peptide coverage.
3. Write a PyMOL `.pml` script.
4. Color residues by protection, deprotection, or no major change.

## Skills Demonstrated

- Structural interpretation of HDX-MS
- PyMOL scripting
- Protein visualization
- Integrative structural biology

## Files

- `make_pymol_hdx_script.py` — creates a PyMOL coloring script
- `example_residue_scores.csv` — mock residue-level HDX scores
- `example_hdx_coloring.pml` — example PyMOL script
