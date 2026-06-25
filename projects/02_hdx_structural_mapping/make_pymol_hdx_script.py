import pandas as pd

INPUT = "example_residue_scores.csv"
OUTPUT = "example_hdx_coloring.pml"

def color_for_delta(delta):
    if delta <= -0.15:
        return "blue"      # protected
    if delta >= 0.15:
        return "red"       # deprotected
    return "white"         # unchanged

def main():
    df = pd.read_csv(INPUT)

    lines = [
        "hide everything",
        "show cartoon",
        "color grey80",
        "bg_color white"
    ]

    for _, row in df.iterrows():
        residue = int(row["residue"])
        color = color_for_delta(row["delta"])
        lines.append(f"color {color}, resi {residue}")

    lines.extend([
        "set cartoon_transparency, 0.05",
        "zoom"
    ])

    with open(OUTPUT, "w") as f:
        f.write("\n".join(lines))

    print(f"Saved: {OUTPUT}")

if __name__ == "__main__":
    main()
