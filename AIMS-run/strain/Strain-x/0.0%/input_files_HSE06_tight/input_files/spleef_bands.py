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

    all_rows = []
    k_shift = 0.0

    for idx, f in enumerate(files):
        k, e = read_band_file(f)
        k = k - k[0]      # reset segment start
        k += k_shift      # shift to continue
        k_shift = k[-1]

        for i in range(len(k)):
            row = [k[i]] + list(e[i]) + [1 if i == 0 or i == len(k)-1 else 0]
            all_rows.append(row)

        # add NaN row between segments (to prevent straight lines)
        if idx < len(files) - 1:
            nan_row = [np.nan] + [np.nan]*e.shape[1] + [0]
            all_rows.append(nan_row)

    # column names
    colnames = ["k"] + [f"band{i+1}" for i in range(e.shape[1])] + ["sym_point"]

    df = pd.DataFrame(all_rows, columns=colnames)
    df.to_csv(output_csv, index=False)
    print(f"Saved concatenated bands with symmetry markers to {output_csv}")

if __name__ == "__main__":
    concatenate_bands("bands.csv")
