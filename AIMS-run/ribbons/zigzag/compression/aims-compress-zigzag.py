import os
import shutil
import numpy as np
from genericpath import exists

b = 4.4512976200000001

step = float(1.0)
lim_sup = float(20.0)
first = float(14.0)
num_iteracoes = np.arange(round(step , 1) , round((lim_sup + step) , 1) , round(step , 1))

#for item in num_iteracoes:
#    i = str(round(item , 1))
#    path_name = (f"/home/users/malvesf/BPN/AIMS-run/ribbons/zigzag/compression/{i}%")
#    if os.path.isdir(path_name):
#        shutil.rmtree(path_name)
#        print(f"Apagando pasta {i}%")
#    else:
#        print(f"{i}% nao tem broder")
#

os.chdir(f"/home/users/malvesf/BPN/AIMS-run/ribbons/zigzag/compression/0.0%/input_files_pbe_light/input_files/")
print(f"Running for PBE light for 0.0%")
os.system("mpirun -np 90 /home/users/woellner/softwares/FHIaims/build_coaraci/aims.220429.scalapack.mpi.x > aims.out")
os.chdir("../../input_files_pbe_inter/input_files/")
os.system("cp ../../input_files_pbe_light/input_files/geometry.in.next_step geometry.in")
os.system("cp ../../input_files_pbe_light/input_files/hessian.aims .")
print(f"Running for PBE intermediate for 0.0%")
os.system("mpirun -np 90 /home/users/woellner/softwares/FHIaims/build_coaraci/aims.220429.scalapack.mpi.x > aims.out")

os.chdir("../../input_files_pbe_tight/input_files/")
os.system("cp ../../input_files_pbe_inter/input_files/geometry.in.next_step geometry.in")
os.system("cp ../../input_files_pbe_inter/input_files/hessian.aims .")
print(f"Running for PBE tight for 0.0%")
os.system("mpirun -np 90 /home/users/woellner/softwares/FHIaims/build_coaraci/aims.220429.scalapack.mpi.x > aims.out")

os.chdir("../../input_files_pbe_really_tight/input_files/")
os.system("cp ../../input_files_pbe_tight/input_files/geometry.in.next_step geometry.in")
os.system("cp ../../input_files_pbe_tight/input_files/hessian.aims .")
print(f"Running for PBE really tight for 0.0%")
os.system("mpirun -np 90 /home/users/woellner/softwares/FHIaims/build_coaraci/aims.220429.scalapack.mpi.x > aims.out")

os.chdir("../../input_files_HSE06_light/input_files/")
os.system("cp ../../input_files_pbe_really_tight/input_files/geometry.in.next_step geometry.in")
os.system("cp ../../input_files_pbe_really_tight/input_files/hessian.aims .")
print(f"Running for HSE06 light for 0.0%")
os.system("mpirun -np 90 /home/users/woellner/softwares/FHIaims/build_coaraci/aims.220429.scalapack.mpi.x > aims.out")

os.chdir("../../input_files_HSE06_inter/input_files/")
os.system("cp ../../input_files_pbe_light/input_files/geometry.in.next_step geometry.in")
os.system("cp ../../input_files_pbe_light/input_files/hessian.aims .")
print(f"Running for HSE06 intermediate for 0.0%")
os.system("mpirun -np 90 /home/users/woellner/softwares/FHIaims/build_coaraci/aims.220429.scalapack.mpi.x > aims.out")

#os.chdir("../../input_files_HSE06_tight/input_files/")
#os.system("cp ../../input_files_HSE06_inter/input_files/geometry.in.next_step geometry.in")
#os.system("cp ../../input_files_HSE06_inter/input_files/hessian.aims .")
#print(f"Running for HSE06 tight for 0.0%")
#os.system("mpirun -np 90 /home/users/woellner/softwares/FHIaims/build_coaraci/aims.220429.scalapack.mpi.x > aims.out")
#
#os.chdir("../../input_files_HSE06_really_tight/input_files/")
#os.system("cp ../../input_files_HSE06_tight/input_files/geometry.in.next_step geometry.in")
#os.system("cp ../../input_files_HSE06_tight/input_files/hessian.aims .")
#print(f"Running for HSE06 really tight for 0.0%")
#os.system("mpirun -np 90 /home/users/woellner/softwares/FHIaims/build_coaraci/aims.220429.scalapack.mpi.x > aims.out")

def read_geometry(file_path):
    lattice_vectors = []
    atoms = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            if line.startswith('lattice_vector'):
                lattice_vectors.append(line.split())
            elif line.startswith('atom_frac'):
                atoms.append(line.split())
    
    return lattice_vectors, atoms

def write_geometry(file_path, lattice_vectors, atoms):
    with open(file_path, 'w') as file:
        file.write(f"{' '.join(map(str,lattice_vectors[0]))}\n")
        file.write("constrain_relaxation .true.\n")
        file.write(f"{' '.join(map(str,lattice_vectors[1]))}\n")
        file.write("constrain_relaxation .true.\n")
        file.write(f"{' '.join(map(str,lattice_vectors[2]))}\n")
        file.write("constrain_relaxation .true.\n")
        for atom in atoms:
            file.write(f"{' '.join(map(str,atom))}\n")

for item in num_iteracoes:
    current_i = str(round(item , 1))
    previous_i = str(round((item - step) , 1))
    stretch_val = float(round(item , 1))

    os.system(f"cp -rf /home/users/malvesf/BPN/AIMS-run/ribbons/zigzag/compression/{previous_i}%/ /home/users/malvesf/BPN/AIMS-run/ribbons/zigzag/compression/{current_i}%")

    previous_path_HSE06_light = (f"/home/users/malvesf/BPN/AIMS-run/ribbons/zigzag/compression/{previous_i}%/input_files_HSE06_light/input_files/geometry.in.next_step") # Directory of previous run
    current_path_pbe_light = (f"/home/users/malvesf/BPN/AIMS-run/ribbons/zigzag/compression/{current_i}%/input_files_pbe_light/input_files/geometry.in") # Directory of current run
    
    lattice_vectors = read_geometry(previous_path_HSE06_light)[0] # put lattice vectors in a list
    atoms = read_geometry(previous_path_HSE06_light)[1] # put atom positions in a list
    lattice_vectors[1][2] = b - ((stretch_val / 100) * b) # increase lattice vector for x direction

    write_geometry(current_path_pbe_light, lattice_vectors, atoms) # write new geometry file

    # Run stuff again

    os.chdir(f"/home/users/malvesf/BPN/AIMS-run/ribbons/zigzag/compression/{current_i}%/input_files_pbe_light/input_files/")
    print(f"Running for PBE light for {current_i}%")
    os.system("mpirun -np 90 /home/users/woellner/softwares/FHIaims/build_coaraci/aims.220429.scalapack.mpi.x > aims.out")

    os.chdir("../../input_files_pbe_inter/input_files/")
    os.system("cp ../../input_files_pbe_light/input_files/geometry.in.next_step geometry.in")
    os.system("cp ../../input_files_pbe_light/input_files/hessian.aims .")
    print(f"Running for PBE intermediate for {current_i}%")
    os.system("mpirun -np 90 /home/users/woellner/softwares/FHIaims/build_coaraci/aims.220429.scalapack.mpi.x > aims.out")
    
    os.chdir("../../input_files_pbe_tight/input_files/")
    os.system("cp ../../input_files_pbe_inter/input_files/geometry.in.next_step geometry.in")
    os.system("cp ../../input_files_pbe_inter/input_files/hessian.aims .")
    print(f"Running for PBE tight for {current_i}%")
    os.system("mpirun -np 90 /home/users/woellner/softwares/FHIaims/build_coaraci/aims.220429.scalapack.mpi.x > aims.out")

    os.chdir("../../input_files_pbe_really_tight/input_files/")
    os.system("cp ../../input_files_pbe_tight/input_files/geometry.in.next_step geometry.in")
    os.system("cp ../../input_files_pbe_tight/input_files/hessian.aims .")
    print(f"Running for PBE really tight for {current_i}%")
    os.system("mpirun -np 90 /home/users/woellner/softwares/FHIaims/build_coaraci/aims.220429.scalapack.mpi.x > aims.out")

    os.chdir("../../input_files_HSE06_light/input_files/")
    os.system("cp ../../input_files_pbe_really_tight/input_files/geometry.in.next_step geometry.in")
    os.system("cp ../../input_files_pbe_really_tight/input_files/hessian.aims .")
    print(f"Running for HSE06 light for {current_i}%")
    os.system("mpirun -np 90 /home/users/woellner/softwares/FHIaims/build_coaraci/aims.220429.scalapack.mpi.x > aims.out")

    os.chdir("../../input_files_HSE06_inter/input_files/")
    os.system("cp ../../input_files_pbe_light/input_files/geometry.in.next_step geometry.in")
    os.system("cp ../../input_files_pbe_light/input_files/hessian.aims .")
    print(f"Running for HSE06 intermediate for {current_i}%")
    os.system("mpirun -np 90 /home/users/woellner/softwares/FHIaims/build_coaraci/aims.220429.scalapack.mpi.x > aims.out")

    #os.chdir("../../input_files_HSE06_tight/input_files/")
    #os.system("cp ../../input_files_HSE06_inter/input_files/geometry.in.next_step geometry.in")
    #os.system("cp ../../input_files_HSE06_inter/input_files/hessian.aims .")
    #print(f"Running for HSE06 tight for {current_i}%")
    #os.system("mpirun -np 90 /home/users/woellner/softwares/FHIaims/build_coaraci/aims.220429.scalapack.mpi.x > aims.out")
#
    #os.chdir("../../input_files_HSE06_really_tight/input_files/")
    #os.system("cp ../../input_files_HSE06_tight/input_files/geometry.in.next_step geometry.in")
    #os.system("cp ../../input_files_HSE06_tight/input_files/hessian.aims .")
    #print(f"Running for HSE06 really tight for {current_i}%")
    #os.system("mpirun -np 90 /home/users/woellner/softwares/FHIaims/build_coaraci/aims.220429.scalapack.mpi.x > aims.out")
