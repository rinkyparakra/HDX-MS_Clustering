# Protein Dynamics Clustering

This project demonstrates how peptide-level dynamics can be grouped by uptake behavior across time points.

## Goal

Cluster HDX-MS peptide uptake profiles to identify regions with similar dynamic behavior.

## Workflow

1. Load peptide/timepoint uptake matrix.
2. Normalize uptake values.
3. Cluster peptides using k-means.
4. Export cluster assignments.
5. Interpret clusters in the context of protein domains or interaction interfaces.

## Skills Demonstrated

- Python
- pandas
- scikit-learn
- k-means clustering
- protein dynamics interpretation
