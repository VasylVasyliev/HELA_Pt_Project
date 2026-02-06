##  Technical Specification: EGFR Inhibition by Pt 
Nanoparticles - MD & DFT Simulation Protocol

**Objective:** To quantitatively assess the interaction 
between a platinum nanoparticle (PtNP) and the epidermal 
growth factor receptor (EGFR) kinase domain (PDB: 1M17) 
using molecular dynamics (MD) and density functional 
theory (DFT) simulations. This study aims to determine 
the stability of PtNP binding, identify key interactions, 
and investigate potential allosteric effects.

**System Setup:**

* **Model System:** A 2-5 nm PtNP docked into the active 
site of EGFR kinase domain (PDB: 1M17), with Cys797 and 
Thr790 coordinating with the PtNP surface.
* **Force Field:**  CHARMM36 for protein residues, 
COMPASS force field for the PtNP, considering recent 
advancements in describing metal nanoparticles.

**Molecular Dynamics Simulations (MD):**

**Simulation Parameters:**
* **Time Scale:** 100 ns long MD simulations using 
explicit solvent (TIP3P water) and periodic boundary 
conditions.
* **Temperature:** 300 K, Pressure: 1 atm.
* **Integration Time Step:** 2 fs.


**Quantifiable Parameters:**

1. **Coordination Bond Lengths (Pt-S):**  
    * Track the Pt-S bond lengths between the PtNP and 
Cys797 over the entire simulation duration (every 50 ps). 
Calculate average, standard deviation, and potential 
fluctuations in bond length.
2. **Binding Free Energy Components (MM-PBSA):**
    * Analyze binding free energy contributions from:
        * Electrostatic interactions
        * Van der Waals forces
        * Polar solvation effects (using MM-PBSA method) 
at various simulation time points (every 20 ns).

3. **RMSF of P-loop and Activation Loop:**  
    * Calculate root mean square fluctuations (RMSF) for 
the P-loop and activation loop residues throughout the 
simulation to assess conformational changes induced by 
PtNP binding. Analyze RMSF changes at different time 
intervals (every 10 ns).

**DFT Calculations:**

**Objective:** To gain insights into electronic structure 
and bonding interactions between PtNP and EGFR residues.

* **Geometry Optimization:** Optimize the geometry of the 
PtNP-EGFR complex using DFT methods with appropriate 
exchange-correlation functionals (e.g., PBE, B3LYP). 
* **Electronic Density Transfer Values:**  Analyze 
electron density difference maps between the isolated 
PtNP and the PtNP-EGFR complex to quantify electron 
transfer between the PtNP and EGFR residues (specifically 
Cys797 and Thr790).

**Data Analysis & Interpretation:**

* Correlate MD simulation results with DFT findings to 
understand the interplay between structural dynamics and 
electronic interactions.
* Identify potential allosteric pockets through analysis 
of RMSF changes in regions distant from the primary 
binding site. 


**Deliverables:**

1. A detailed report summarizing the MD and DFT 
simulation results, including figures and tables 
showcasing the analyzed parameters.
2. Jupyter notebooks containing the full code for the 
simulations and data analysis pipeline.



This technical specification provides a framework for 
conducting rigorous simulations to investigate the 
complex interactions between Pt nanoparticles and the 
EGFR kinase domain. The defined quantitative parameters 
will enable a comprehensive understanding of the binding 
mechanism, stability, and potential allosteric effects, 
ultimately contributing to the development of novel 
Pt-based therapeutic strategies.
