#!/bin/bash

#SBATCH -n 90
#SBATCH --job-name BPN_NR_zigzag
#SBATCH --nodes 2
#SBATCH --partition par480-x
#SBATCH -o out.txt
#SBATCH -e err.txt

export OMP_NUM_THREADS=1

cd $SLURM_SUBMIT_DIR

module purge
module load hwloc
module load intel
module load mpi

mpirun /home/users/woellner/softwares/FHIaims/build_coaraci/aims.220429.scalapack.mpi.x > aims.out
