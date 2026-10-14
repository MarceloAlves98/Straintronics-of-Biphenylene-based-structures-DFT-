import os
import shutil
import numpy as np
from genericpath import exists

c = 3.7532274515249466

step = float(1.0)
lim_sup = float(20.0)
num_iteracoes = np.arange(round(step , 1) , round((lim_sup + step) , 1) , round(step , 1))

#for item in num_iteracoes:
#    i = str(round(item , 1))
#    path_name = (f"/home/users/malvesf/BPN/AIMS-run/nanotubes/armchair/strain/{i}%")
#    if os.path.isdir(path_name):
#        shutil.rmtree(path_name)
#        print(f"Apagando pasta {i}%")
#    else:
#        print(f"{i}% nao tem broder")
#

os.chdir(f"/home/users/malvesf/BPN/AIMS-run/nanotubes/armchair/strain/0.0%/input_files_pbe_light/input_files/")
print(f"Running for PBE light for 0.0%")
os.system("mpirun -np 44 /home/users/woellner/softwares/FHIaims/build_coaraci/aims.220429.scalapack.mpi.x > aims.out")
os.chdir("../../input_files_pbe_inter/input_files/")
os.system("cp ../../input_files_pbe_light/input_files/geometry.in.next_step geometry.in")
os.system("cp ../../input_files_pbe_light/input_files/hessian.aims .")
print(f"Running for PBE intermediate for 0.0%")
os.system("mpirun -np 44 /home/users/woellner/softwares/FHIaims/build_coaraci/aims.220429.scalapack.mpi.x > aims.out")
os.chdir("../../input_files_pbe_tight/input_files/")
os.system("cp ../../input_files_pbe_inter/input_files/geometry.in.next_step geometry.in")
os.system("cp ../../input_files_pbe_inter/input_files/hessian.aims .")
print(f"Running for PBE tight for 0.0%")
os.system("mpirun -np 44 /home/users/woellner/softwares/FHIaims/build_coaraci/aims.220429.scalapack.mpi.x > aims.out")
os.chdir("../../input_files_pbe_really_tight/input_files/")
os.system("cp ../../input_files_pbe_tight/input_files/geometry.in.next_step geometry.in")
os.system("cp ../../input_files_pbe_tight/input_files/hessian.aims .")
print(f"Running for PBE really tight for 0.0%")
os.system("mpirun -np 44 /home/users/woellner/softwares/FHIaims/build_coaraci/aims.220429.scalapack.mpi.x > aims.out")
os.chdir("../../input_files_HSE06_light/input_files/")
os.system("cp ../../input_files_pbe_really_tight/input_files/geometry.in.next_step geometry.in")
os.system("cp ../../input_files_pbe_really_tight/input_files/hessian.aims .")
print(f"Running for HSE06 light for 0.0%")
os.system("mpirun -np 44 /home/users/woellner/softwares/FHIaims/build_coaraci/aims.220429.scalapack.mpi.x > aims.out")
os.chdir("../../input_files_HSE06_inter/input_files/")
os.system("cp ../../input_files_pbe_light/input_files/geometry.in.next_step geometry.in")
os.system("cp ../../input_files_pbe_light/input_files/hessian.aims .")
print(f"Running for HSE06 intermediate for 0.0%")