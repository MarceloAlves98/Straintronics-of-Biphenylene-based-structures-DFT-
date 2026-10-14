# Straintronics-of-Biphenylene-based-structures-DFT-
This repository serves to gather the current workflow of my research. The Thesis is centered in ab-initio electronic structure studies of strained 1 and 2 dimensional variations of the Biphneylene Network carbon material. The main goal of the project is to perform DFT calculations with the FHI-aims software for geometry optimization using the PBE-GGA functional, and then perform electronic band structure calculations using the HSE06 hybrid funcitonal. The project also contains a notebook workflow for plotting the data using the aims-tools python package.

## 📁 Project Structure
For context: since the 2D sheet calculations were performed in an earlier stage, the folder configuration and organization differs from the nanotube and nanoribbon versions. For the 2D sheets, the axis of deformation is used for the name of the folder:

-Strain/Compression-x: The x axis is increased/decreased;

-Strain/Compression-y: The y axis is increased/decreased;

In the context of carbon material science, a deformation in the x x-axis means a deformation in the zigzag direction, while a deformation in the y-axis means a deformation in the armchair direction.

```bash
.
├── AIMS-run/                 #Main directory: contains the main research workflow with the calculations made with FHI-aims and figures used in the thesis
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
       └──Strain-x            #Directory for 2D-sheet Strain in the zigzag (x-axis) direction
       └──Strain-y            #Directory for 2D-sheet Strain in the armchair (y-axis) direction
├──Qualificação               #Main folder containing every file necessary to generate the current state of the Thesis text
   └──figuras-vmd             #Figures generated using VMD
   └──Qualificação.zip        #Self-contained LaTeX project, ready for direct implementation in Overleaf
   └──text and presentations  #Directory containing finished text and presentation for Qaulification exam
└── README.md                   # This file/
```

---

## 🔁 Strain and Compression Workflow

The main focus of the research workflow is to run the aims-strain.py or aims-compress.py python scripts. These scripts are built to:

1-Run a geometry optimization for the undeformed material in the PBE-GGA level of theory;

2-Run one more geometry optimization step in the HSE06 level of theory;

3-Perform band structure calculations in the HSE06 level of theory;

4-Update the lattice parameter that is being deformed:

    -If strain: Lattice parameter is increased by 1% of its original value;
    
    -If compression: Lattice parameter is decreased by 1% of its original value;

5-Restart the loop with new lattice parameter fixed (so the material does not return tu original size).

## ⚛️ FHI-aims Calculation protocol

The workflow is projected to perform calculations using the FHI-aims software in increasing levels of accuracy. Input folders were generated using FHI-aims GIMS graphical interface for the generation of atomic defaults for carbon and, in the case of nanoribbons, hydrogen atoms. Input structures consist of increasing degrees of accuracy as instructed in FHI-aims GIMS "Simple calculation" and "Band Structure" apps. 

Python script follows the following steps for calculations:

1- Geomtery optimization in the light setting for species defaults (PBE-GGA);

2- Geomtery optimization in the intermediate setting for species defaults (PBE-GGA);

3- Geomtery optimization in the tight setting for species defaults (PBE-GGA);

4- Geomtery optimization in the really_tight setting for species defaults (PBE-GGA);

5- Geomtery optimization in the light setting for species defaults (HSE06);

    *For every new geometry optimization step, the geometry obtained from the previous step is copied and used as the strating configuration for the current calculation;

6- Band structure and DOS calculation in the intermediate setting for species defaults (HSE06);

    *In the case of the 2D BPN sheet, electronic structure is calculated in the tight setting (HSE06 functional) due to low system size.

7- Lattice parameter is increased/decreased and set to fixed (argument constrain_relaxation .true. is used in the lattice parameter that is being deformed)

8- Workflow starts again from item 1.

<p align="center">
  <img src="./Qualificação/text%20and%20presentations/workflow.png" width="900">
</p>

<p align="center">
  <em>Figure 1. Illustrative diagram of the computational workflow.</em>
</p>

Species settings (light --> really_tight) differ in the deffinition of the basis function. In the light settings, the first tier set of basis function is used. With increased level of accuracy in the intermediate, tight and really_tight settings, more basis functions are added to the minimal set.

Inside each of the main folders (strain and compress, which are made for the 2D sheet material, nanotube and ribbons), the deformation direction folders contain the two different deformation directions:

    -x and y for the 2D sheet because there is only one two dimensaional geometry which is used for both;
    -Armchair and zigzag for tubes and ribbons, since each chirality is a different geometry of 1D material that was generated from one of the two axes of the 2D version.

For each of the deformation direction folders, a simple python3 call will run the aims-strain.py or the aims-compress.py, or, for short, aims-deform-direction.py, where:

    -Deform is either strain or compression;
    -Direction is either x, y, zigzag or armchair;

When the script is called, it creates folders for each deformation step with a Z% name, in which Z is the percentage of deformation. The 0% folder is the initial stage, and therefore must already be in the directory when aims-deform-direction.py. After being called, the script will start performing the loop present in Figure 1 for 0%. It will then copy 0% into a folder called 1%, therefore finishing the first loop. The current deformation is made until 20% is reached, even though results in the thesis are presented only until 14% deformation, which were the most "Interesting" results obtained so far.

## 📊 Results
After simulations are concluded, the figures containing the electronic structure analysis can be generated in the jupyter notebook called bands_turbo.ipynb, which is located in the AIMS-run/figures/figuras_quali/ folder.

This notebook generates the following Figures:

1-Band structure + DOS for the relaxed geometry of 2D sheet:

<p align="center">
  <img src="./AIMS-run/figures/figuras_quali/sheet/bands_0_unitcell.png" width="900">
</p>

<p align="center">
  <em>Figure 1. Band structure and DOS of 2D sheet.</em>
</p>

2-Band structure + DOS for the relaxed geometries of Armchair and Zigzag Nanotubes:

<p align="center">
  <img src="./AIMS-run/figures/figuras_quali/tube/armchair/bands_0_tube_armchair.png" width="900">
</p>

<p align="center">
  <em>Figure 1. Band structure and DOS of armchair nanotube.</em>
</p>

<p align="center">
  <img src="./AIMS-run/figures/figuras_quali/tube/zigzag/bands_0_tube_zigzag.png" width="900">
</p>

<p align="center">
  <em>Figure 1. Band structure and DOS of zigzag nanotube.</em>
</p>

3-Band structure + DOS for the relaxed geometries of Armchair and Zigzag Nanoribbons:

<p align="center">
  <img src="./AIMS-run/figures/figuras_quali/ribbon/armchair/bands_0_ribbon_armchair.png" width="900">
</p>

<p align="center">
  <em>Figure 1. Band structure and DOS of armchair nanoribbon.</em>
</p>

<p align="center">
  <img src="./AIMS-run/figures/figuras_quali/ribbon/zigzag/bands_0_ribbon_zigzag.png" width="900">
</p>

<p align="center">
  <em>Figure 1. Band structure and DOS of zigzag nanoribbon.</em>
</p>

4-Band structure from 0% until 14% deformation for:

4.1-Armchair and zigzag strain for the 2D sheet:
<p align="center">
  <img src="./AIMS-run/figures/figuras_quali/sheet/bands_strain_armchair.png" width="900">
</p>

<p align="center">
  <em>Figure 1. Armchair strain for 2D sheet.</em>
</p>

<p align="center">
  <img src="./AIMS-run/figures/figuras_quali/sheet/bands_strain_zigzag.png" width="900">
</p>

<p align="center">
  <em>Figure 1. Zigzag strain for the 2D sheet.</em>
</p>

4.2-Armchair and zigzag compression for the 2D sheet:
<p align="center">
  <img src="./AIMS-run/figures/figuras_quali/sheet/bands_compress_armchair.png" width="900">
</p>

<p align="center">
  <em>Figure 1. Armchair compression for 2D sheet.</em>
</p>

<p align="center">
  <img src="./AIMS-run/figures/figuras_quali/sheet/bands_compress_zigzag.png" width="900">
</p>

<p align="center">
  <em>Figure 1. Zigzag compression for the 2D sheet.</em>
</p>

4.3-Strain and compression for Armchair nanotube:
<p align="center">
  <img src="./AIMS-run/figures/figuras_quali/tube/armchair/bands_tube_strain_armchair.png" width="900">
</p>

<p align="center">
  <em>Figure 1. Strain on armchair nanotube, with band gap opening.</em>
</p>

<p align="center">
  <img src="./AIMS-run/figures/figuras_quali/tube/armchair/bands_tube_compress_armchair.png" width="900">
</p>

<p align="center">
  <em>Figure 1. Compression on armchair nanotube.</em>
</p>

4.4-Strain and compression for Zigzag nanotube:
<p align="center">
  <img src="./AIMS-run/figures/figuras_quali/tube/zigzag/bands_tube_strain_zigzag.png" width="900">
</p>

<p align="center">
  <em>Figure 1. Strain on zigzag nanotube.</em>
</p>

<p align="center">
  <img src="./AIMS-run/figures/figuras_quali/tube/zigzag/bands_tube_compress_zigzag.png" width="900">
</p>

<p align="center">
  <em>Figure 1. Compression on zigzag nanotube, with observed possible transition into semimetal.</em>
</p>

4.5-Strain and compression for Armchair ribbon:
<p align="center">
  <img src="./AIMS-run/figures/figuras_quali/ribbon/armchair/bands_ribbon_strain_armchair.png" width="900">
</p>

<p align="center">
  <em>Figure 1. Strain on armchair nanoribbon, with observed band gap opening.</em>
</p>

<p align="center">
  <img src="./AIMS-run/figures/figuras_quali/ribbon/armchair/bands_ribbon_compress_armchair.png" width="900">
</p>

<p align="center">
  <em>Figure 1. Compression on armchair nanoribbon.</em>
</p>

4.6-Strain and compression for Zigzag nanoribbon:
<p align="center">
  <img src="./AIMS-run/figures/figuras_quali/ribbon/zigzag/bands_ribbon_strain_zigzag.png" width="900">
</p>

<p align="center">
  <em>Figure 1. Strain on zigzag ribbon.</em>
</p>

<p align="center">
  <img src="./AIMS-run/figures/figuras_quali/ribbon/zigzag/bands_ribbon_compress_zigzag.png" width="900">
</p>

<p align="center">
  <em>Figure 1. Compression on zigzag ribbon, with observed band gap opening.</em>
</p>

5-Dimensionality reduction effects (Comparisson):

5.1-Armchair chirality:

<p align="center">
  <img src="./AIMS-run/figures/figuras_quali/bands_dimension_reduction_armchair.png" width="900">
</p>

<p align="center">
  <em>Figure 1. Dimensionality reduction for the armchair materials.</em>
</p>

5.2-Zigzag chirality:

<p align="center">
  <img src="./AIMS-run/figures/figuras_quali/bands_dimension_reduction_zigzag.png" width="900">
</p>

<p align="center">
  <em>Figure 1. Dimensionality reduction for the zigzag materials.</em>
</p>

6-Some specific cases of interest that are specified in the Results section in the thesis, for example:
<p align="center">
  <img src="./AIMS-run/figures/figuras_quali/tube/zigzag/bands_12_tube_zigzag.png" width="900">
</p>

<p align="center">
  <em>Figure 1. Possible transition into semimetal observed for 12% compression on zigzag nanotube.</em>
</p>

## 🔜 Future Steps
Some calculations are still to be made:

1- Strain vs. Stress curves;

2- Youngs modulus;

3- Electronic Localization function;

4- Atomic forces;
