import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# Load DOS data
# -------------------------
# Expected format (dos.dat): Energy(eV)   DOS
# Adjust filename if necessary
#dos_file = "dos.BPN.dat"
#dos_df = pd.read_csv(dos_file, sep='\s+' , comment = '#', header = None, names=["Energy", "DOS" , "int DOS"])

# -------------------------
# Load Band Structure data
# -------------------------
# Expected format (bands.dat.gnu): k-point   Energy(eV)
# with blank lines separating bands
bands_file = "bands.dat"

bands_data = []
current_band = []
with open(bands_file, "r") as f:
    for line in f:
        if line.strip() == "":  # new band
            if current_band:
                bands_data.append(pd.DataFrame(current_band, columns=["k", "Energy"]))
                current_band = []
        else:
            k, e = map(float, line.split())
            current_band.append([k, e])
if current_band:
    bands_data.append(pd.DataFrame(current_band, columns=["k", "Energy"]))


# -------------------------
# Plot Band Structure
# -------------------------
plt.figure(figsize=(6,5))
for band in bands_data:
    plt.plot(band["k"], band["Energy"], color="red")

plt.axhline(0, color="k", linestyle="--", linewidth=0.8)
plt.xlabel("k-path")
plt.ylabel("Energy (eV)")
plt.title("Band Structure")
plt.show()
plt.savefig("Bands.png")
