import os
import numpy as np
import matplotlib.pyplot as plt

# Define range of k_point values
k_point_values = np.arange(12 , 50 , 2)
energies = []

# Loop over each folder and extract energy
for k_point in k_point_values:
    folder_name = f"k_point_{k_point}"
    output_file = os.path.join(folder_name, "aims.out")

    if os.path.exists(output_file):
        with open(output_file, "r") as f:
            for line in f:
                if "| Total energy of the DFT / Hartree-Fock s.c.f. calculation      :" in line:  # Search for total energy line
                    energy = float(line.split()[-2])  # Extract energy value
                    energies.append(energy)
                    print(f"k_points = {k_point}, Energy = {energy:.6f} eV")
                    break  # Stop after finding first energy
    else:
        print(f"Skipping {folder_name}: system.out not found.")
        energies.append(None)  # Append None for missing files

# Convert to numpy arrays for plotting
k_point_values = np.array(k_point_values)
energies = np.array(energies, dtype=np.float64)

# Filter out None values
valid_indices = np.where(energies != None)
k_point_values = k_point_values[valid_indices]
energies = energies[valid_indices]

# Plotting Energy vs. k_points
plt.figure(figsize=(8, 6))
plt.plot(k_point_values, -energies, marker="o", linestyle="-", color="b")
plt.xlabel("k_points")
plt.ylabel("Total Energy (eV)")
plt.title("Energy Convergence with k_points")
plt.grid(True)
plt.savefig("basis_optimization.png")
plt.show()
