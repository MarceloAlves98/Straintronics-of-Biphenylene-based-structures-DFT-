# Straintronics-of-Biphenylene-based-structures-DFT-
This repository serves to gather the current workflow of my research. The Thesis is centered in ab-initio electronic structure studies of strained 1 and 2 dimensional variations of the Biphneylene Network carbon material. The main goal of the project is to perform DFT calculations with the FHI-aims software for geometry optimization using the PBE-GGA functional, and then perform electronic band structure calculations using the HSE06 hybrid funcitonal. The project also contains a notebook workflow for plotting the data using the aims-tools python package.

## 📁 Project Structure
For context: since the 2D sheet calculations were performed in an earlier stage, the folder configuration and organization differs from the nanotube and nanoribbon versions. For the 2D sheets, the axis of deformation is used for the name of the folder:

-Strain/Compression-x: The x axis is increased/decreased;

-Strain/Compression-y: The y axis is increased/decreased;

In the context of carbon material science, a deformation in the x x-axis means a deformation in the zigzag direction, while a deformation in the y-axis means a deformation in the armchair direction.

```bash
.
├── AIMS-run/                 #Main directory: contains the calculations made with FHI-aims and figures used in the thesis
    └──compress               #Directory for 2D sheet compression
       └──Compress-x          #Directory for 2D-sheet compression in the zigzag (x-axis) direction
       └──Compress-y          #Directory for 2D-sheet compression in the armchair (y-axis) direction
    └──figures                #Figures generated from the analysis notebook
    └──nanotubes              #Directory for nanotube strain and compressions
       └──armchair            #Directory for deformations of armchair-chiral nanotubes
          └──compress         #Directory for nanotube compressions
          └──strain           #Directory for nanotube strain
       └──zigzag              #Directory for deformations of zigzag-chiral nanotubes
          └──compress         #Directory for nanotube compressions
          └──strain           #Directory for nanotube strain
    └──ribbons                #Directory for nanoribbon strain and compression
       └──armchair            #Directory for deformations of armchair-chiral nanoribbons
          └──compress         #Directory for nanoribbon compressions
          └──strain           #Directory for nanoribbon strain
       └──zigzag              #Directory for deformations of zigzag-chiral nanoribbon
          └──compress         #Directory for nanoribbon compressions
          └──strain           #Directory for nanoribbon strain
    └──strain                 #Directory for 2D sheet strain
       └──Strain-x          #Directory for 2D-sheet Strain in the zigzag (x-axis) direction
       └──Strain-y          #Directory for 2D-sheet Strain in the armchair (y-axis) direction
└── README.md                   # This file/
```

---

