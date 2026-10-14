#!/bin/bash

#SBATCH -n 1
#SBATCH --job-name submit_jobs
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
module load python

/opt/anaconda3/2023.07/bin/python3 -u submit_jobs.py
