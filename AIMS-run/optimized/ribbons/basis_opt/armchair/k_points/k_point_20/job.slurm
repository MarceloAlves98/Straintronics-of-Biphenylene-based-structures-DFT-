#!/bin/bash

#SBATCH -n 32
#SBATCH --job-name BPN-ribbon_arm
#SBATCH --nodes 1
#SBATCH --partition par48-x
#SBATCH -o out.txt
#SBATCH -e err.txt

export OMP_NUM_THREADS=1

cd $SLURM_SUBMIT_DIR

module purge
module load hwloc
module load intel
module load mpi

mpirun /home/users/woellner/softwares/FHIaims/build_coaraci/aims.220429.scalapack.mpi.x > aims.out
