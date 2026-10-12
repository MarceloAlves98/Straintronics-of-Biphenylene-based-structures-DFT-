import glob
import numpy as np
import pandas as pd

def read_band_file(filename):
    k_points = []
    energies = []
    with open(filename, "r") as f:
        for line in f:
            if line.strip() == "" or line.startswith("#"):
                continue
            parts = line.split()
            k = float(parts[0])
            vals = list(map(float, parts[1:]))
            k_points.append(k)
            energies.append(vals)
    return np.array(k_points), np.array(energies)

def concatenate_bands(output_csv="bands.csv"):
    files = sorted(glob.glob("band*.out"))
    if not files:
        raise FileNotFoundError("No band*.out files found!")

    all_k = []
    all_e = []

    k_shift = 0.0
    for f in files:
        k, e = read_band_file(f)
        k = k - k[0]          # reset segment start to 0
        k += k_shift          # shift for continuity
        k_shift = k[-1]

        all_k.extend(k)
        all_e.extend(e)

    all_k = np.array(all_k)
    all_e = np.array(all_e)

    # Build DataFrame
    df = pd.DataFrame(all_e, columns=[f"band{i+1}" for i in range(all_e.shape[1])])
    df.insert(0, "k", all_k)  # insert k as first column

    # Write CSV
    df.to_csv(output_csv, index=False)
    print(f"Saved concatenated bands to {output_csv}")

if __name__ == "__main__":
    concatenate_bands("bands.csv")
