#!/bin/bash

#SBATCH -n 90
#SBATCH --job-name BPN_NR_armchair-compression
#SBATCH --nodes 2
#SBATCH --partition par480-x
#SBATCH -o out.txt
#SBATCH -e err.txt

export OMP_NUM_THREADS=1

cd $SLURM_SUBMIT_DIR

#### Prepare o ambiente com os devidos módulos #########
# hwloc faz parte das variáveis de ambiente gerais do cluster
module purge
module load hwloc
module load intel
module load mpi
module load python

/opt/anaconda3/2023.07/bin/python3 -u aims-strain-armchair.py
