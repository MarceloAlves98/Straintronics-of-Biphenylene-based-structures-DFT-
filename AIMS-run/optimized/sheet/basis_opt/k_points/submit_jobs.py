import os
import numpy as np
import time

# Define range of K_points values (in Ry)
k_point_values = np.arange(2, 48, 2)  # Example: 100 to 600 Ry in steps of 50

# Loop over different K_points values
for k_point in k_point_values:
    folder_name = f"k_point_{k_point}"
    os.makedirs(folder_name, exist_ok=True)  # Create folder if not exists
    os.system(f"cp job.slurm {folder_name}")
    os.system(f"cp geometry.in {folder_name}")

    # Create input file with specific MeshCutoff
    input_file = os.path.join(folder_name, "control.in")
    with open(input_file, "w") as f:
        base_input_content = f"""\
#===============================================================================
# FHI-aims file: /tmp/tmpuwj4kims/tar/input_files/control.in
# Created using the Atomic Simulation Environment (ASE)
# Thu Sep 18 13:47:32 2025
#===============================================================================
xc                                 pbe
k_grid                             {k_point} {k_point} 1
#output dos                         -30 30 10000 0.05
#compute_dielectric                 50 10000
#output                             hirshfeld
#output                             mulliken
#relax_geometry trm                 0.005
#relax_unit_cell                    full
relativistic                       atomic_zora scalar
#===============================================================================

################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for C atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        C
#     global species definitions
    nucleus             6
    mass                12.0107
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         34 5.0
    radial_multiplier   1
    angular_grids specified
      division   0.3326   50
      division   0.5710  110
      division   0.7727  194
      division   0.8772  302
#      division   0.9334  434
#      division   0.9625  590
#      division   0.9924  770
#      division   1.0230  974
#      division   1.4589 1202
#     outer_grid  974
     outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      2  s   2.
    valence      2  p   2.
#     ion occupancy
    ion_occ      2  s   1.
    ion_occ      2  p   1.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.0 A, 1.25 A, 1.5 A, 2.0 A, 3.0 A
#
################################################################################
#  "First tier" - improvements: -1214.57 meV to -155.61 meV
     hydro 2 p 1.7
     hydro 3 d 6
     hydro 2 s 4.9
#  "Second tier" - improvements: -67.75 meV to -5.23 meV
#     hydro 4 f 9.8
#     hydro 3 p 5.2
#     hydro 3 s 4.3
#     hydro 5 g 14.4
#     hydro 3 d 6.2
#  "Third tier" - improvements: -2.43 meV to -0.60 meV
#     hydro 2 p 5.6
#     hydro 2 s 1.4
#     hydro 3 d 4.9
#     hydro 4 f 11.2
#  "Fourth tier" - improvements: -0.39 meV to -0.18 meV
#     hydro 2 p 2.1
#     hydro 5 g 16.4
#     hydro 4 d 13.2
#     hydro 3 s 13.6
#     hydro 4 f 17.6
#  Further basis functions - improvements: -0.08 meV and below
#     hydro 3 s 2
#     hydro 3 p 6
#     hydro 4 d 20
"""
        f.write(base_input_content)

    # Check if job.slurm exists and submit
    slurm_file = os.path.join(folder_name, "job.slurm")

    if os.path.exists(slurm_file):
        os.chdir(f"{folder_name}")
        time.sleep(2)
        os.system(f"sbatch job.slurm")
        print(f"Submitted job for k_point = {k_point}")
        time.sleep(2)
        os.chdir("..")
    else:
        print(f"Skipping {folder_name}: job.slurm not found.")
print("All available jobs have been submitted.")