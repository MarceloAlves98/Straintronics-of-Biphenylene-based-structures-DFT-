import pandas as pd
import matplotlib.pyplot as plt

def plot_bands(csv_file="bands.csv", fermi_level=0.0):
    df = pd.read_csv(csv_file)

    k = df["k"]
    bands = df.drop(columns=["k", "sym_point"])

    plt.figure(figsize=(6, 8))

    # Plot each band (NaNs break the lines automatically)
    for col in bands.columns:
        plt.plot(k, bands[col] - fermi_level, color="black", linewidth=1)

    # Add vertical lines at symmetry points
    sym_kpoints = df.loc[df["sym_point"] == 1, "k"].dropna().unique()
    for sp in sym_kpoints:
        plt.axvline(x=sp, color="gray", linestyle="--", linewidth=0.8)

    plt.axhline(y=0.0, color="red", linestyle="--", linewidth=0.8, label="Fermi level")
    plt.ylabel("Energy (eV)")
    plt.xlabel("k-path")
    plt.xticks([])  # can later be replaced with labels like Γ, M, K
    plt.title("Band structure from FHI-aims")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_bands("bands.csv", fermi_level=0.0)
