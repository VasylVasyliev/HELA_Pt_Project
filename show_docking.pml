# PyMOL Script для проекта DNA-Data-Science
reinitialize
load ~/Documents/HELA_Pt_Project/data/1M17.pdb
load ~/Documents/HELA_Pt_Project/results/PtNP_complex.pdb

# Настройка вида
hide everything
show cartoon, 1M17
color slate, 1M17
show spheres, PtNP_complex
color silver, PtNP_complex

# Настройка мишени
show sticks, resi 794
color yellow, resi 794
label resi 794 and name CA, "CYS794 (Target)"
set label_size, 20
set label_outline_color, black

# Финальный ракурс
orient resi 794
zoom resi 794, 20
# Измерение и стиль / Measurement and style
distance dist1, (PtNP_complex and symbol Pt), (resi 794 and name SG)
set label_size, 50
set label_color, yellow
set label_position, [2, 2, 2]
set sphere_transparency, 0.5, PtNP_complex
