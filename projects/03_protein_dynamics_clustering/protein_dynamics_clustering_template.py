import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

INPUT = "example_cluster_input.csv"
OUTPUT = "example_cluster_output.csv"

def main():
    df = pd.read_csv(INPUT)
    features = df[["t0_5_min", "t5_min", "t30_min"]]

    scaled = StandardScaler().fit_transform(features)

    model = KMeans(n_clusters=2, random_state=42, n_init=10)
    df["cluster"] = model.fit_predict(scaled)

    df.to_csv(OUTPUT, index=False)
    print(f"Saved: {OUTPUT}")

if __name__ == "__main__":
    main()
