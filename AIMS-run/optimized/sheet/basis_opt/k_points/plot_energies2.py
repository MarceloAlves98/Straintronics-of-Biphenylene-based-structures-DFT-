import os
import numpy as np
import matplotlib.pyplot as plt


# ==========================================================
# PARAMETERS
# ==========================================================

# Define range of k-point values
k_point_values = np.arange(8, 50, 2)

# Energy convergence threshold in eV
threshold = 0.001


# ==========================================================
# EXTRACT ENERGIES
# ==========================================================

energies = []

for k_point in k_point_values:

    folder_name = f"k_point_{k_point}"
    output_file = os.path.join(folder_name, "aims.out")

    if os.path.exists(output_file):

        with open(output_file, "r") as f:

            for line in f:

                if "| Total energy of the DFT / Hartree-Fock s.c.f. calculation      :" in line:

                    energy = float(line.split()[-2])

                    energies.append(energy)

                    print(
                        f"k_points = {k_point}, "
                        f"Energy = {energy:.6f} eV"
                    )

                    break

    else:

        print(
            f"Skipping {folder_name}: aims.out not found."
        )

        energies.append(None)


# ==========================================================
# CONVERT TO NUMPY ARRAYS
# ==========================================================

k_point_values = np.array(k_point_values)

energies = np.array(
    energies,
    dtype=np.float64
)


# ==========================================================
# REMOVE MISSING CALCULATIONS
# ==========================================================

valid_indices = np.where(energies != None)

k_point_values = k_point_values[valid_indices]

energies = energies[valid_indices]


# ==========================================================
# CALCULATE DELTA E
# ==========================================================

# Difference between neighboring k-point calculations
#
# np.diff calculates:
#
# E(10) - E(8)
# E(12) - E(10)
# E(14) - E(12)
# etc.
#
# np.abs() makes the difference positive.

delta_E = np.abs(np.diff(energies))


print("\n")
print("=" * 70)
print("K-POINT CONVERGENCE ANALYSIS")
print("=" * 70)

print(
    f"\nConvergence criterion: ΔE < {threshold:.6f} eV\n"
)

print(
    f"{'Previous k':>12} "
    f"{'Current k':>12} "
    f"{'ΔE (eV)':>15} "
    f"{'Converged?':>15}"
)

print("-" * 70)


# ==========================================================
# PRINT ALL DELTA E VALUES
# ==========================================================

for i in range(len(delta_E)):

    previous_k = k_point_values[i]

    current_k = k_point_values[i + 1]

    difference = delta_E[i]

    if difference < threshold:
        status = "YES"
    else:
        status = "NO"

    print(
        f"{previous_k:>12} "
        f"{current_k:>12} "
        f"{difference:>15.6f} "
        f"{status:>15}"
    )


# ==========================================================
# FIND STRICTLY CONVERGED K-POINT GRID
# ==========================================================

converged_k = None

#
# We start at each possible k-point grid and ask:
#
# "Are ALL ΔE values from this point onward
#  smaller than the threshold?"
#
# For example, for k = 18:
#
# ΔE(18→20)
# ΔE(20→22)
# ΔE(22→24)
# ...
#
# must ALL be < threshold.
#

for i in range(1, len(k_point_values)):

    # Delta E values starting from the current k-point
    remaining_delta_E = delta_E[i:]

    # Check whether ALL remaining differences
    # satisfy the convergence criterion
    if np.all(remaining_delta_E < threshold):

        converged_k = k_point_values[i]

        break


# ==========================================================
# REPORT RESULT
# ==========================================================

print("\n")
print("=" * 70)

if converged_k is not None:

    print("K-POINT CONVERGENCE ACHIEVED")
    print("=" * 70)

    print(
        f"\nLowest converged k-point grid: "
        f"{converged_k} x {converged_k} x 1"
    )

    print(
        f"\nCriterion:"
        f"\nAll subsequent ΔE values must be < "
        f"{threshold:.6f} eV."
    )

    # Find index of selected k-point
    selected_index = np.where(
        k_point_values == converged_k
    )[0][0]

    # Show the first ΔE associated with the selected k-point
    if selected_index < len(delta_E):

        print(
            f"\nΔE ({k_point_values[selected_index]} → "
            f"{k_point_values[selected_index + 1]}) = "
            f"{delta_E[selected_index]:.6f} eV"
        )

    print("\nThis is the lowest k-grid for which")
    print("all subsequent energy differences remain")
    print(f"below {threshold:.6f} eV.")

else:

    print("NO FULL CONVERGENCE FOUND")
    print("=" * 70)

    print(
        f"\nNo k-point grid was found for which "
        f"all subsequent ΔE values remain below "
        f"{threshold:.6f} eV."
    )


print("=" * 70)


# ==========================================================
# PLOT ENERGY CONVERGENCE
# ==========================================================

plt.figure(figsize=(8, 6))

plt.plot(
    k_point_values,
    -energies,
    marker="o",
    linestyle="-",
    label="Total Energy"
)


# Mark the selected converged k-point
if converged_k is not None:

    selected_energy = -energies[
        np.where(k_point_values == converged_k)[0][0]
    ]

    plt.axvline(
        converged_k,
        linestyle="--",
        label=f"Converged: {converged_k} × {converged_k} × 1"
    )

    plt.scatter(
        converged_k,
        selected_energy,
        s=100,
        zorder=5
    )


plt.xlabel("k_points")
plt.ylabel("Total Energy (eV)")

plt.title(
    "Energy Convergence with k_points"
)

plt.grid(True)

plt.legend()

plt.savefig(
    "basis_optimization.png",
    dpi=300
)

plt.show()
