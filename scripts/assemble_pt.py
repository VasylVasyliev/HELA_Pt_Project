import os
import numpy as np

# Координаты мишени CYS794 / Coordinates of CYS794 target
target_coords = np.array([18.079, 15.523, 66.796])

# Параметры наночастицы / Nanoparticle parameters
pt_radius = 2.5  # Радиус в Ангстремах / Radius in Angstroms
atom_dist = 2.8  # Расстояние между атомами Pt / Distance between Pt atoms

def generate_pt_cluster(center, radius, spacing):
    """
    Генерация кластера атомов платины / Generation of Platinum atom cluster
    """
    atoms = []
    # Создание сетки координат / Creation of coordinate grid
    grid = np.arange(-radius, radius + spacing, spacing)
    for x in grid:
        for y in grid:
            for z in grid:
                pos = np.array([x, y, z])
                # Проверка нахождения внутри сферы / Sphere boundary check
                if np.linalg.norm(pos) <= radius:
                    atoms.append(pos + center)
    return atoms

# Путь к выходному файлу / Path to the output file
output_path = os.path.expanduser("~/Documents/HELA_Pt_Project/results/PtNP_complex.pdb")

# Проверка наличия папки результатов / Ensure results directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Генерация / Execution
pt_atoms = generate_pt_cluster(target_coords, pt_radius, atom_dist)

# Запись в формате PDB / Write in PDB format
with open(output_path, 'w') as f:
    f.write("REMARK   Platinum Nanoparticle Positioned at CYS794\n")
    for i, pos in enumerate(pt_atoms):
        # Форматирование строки ATOM / ATOM line formatting
        f.write(f"ATOM  {i+1:>5}  Pt  UNL     1    {pos[0]:>8.3f}{pos[1]:>8.3f}{pos[2]:>8.3f}  1.00  0.00          Pt\n")
    f.write("END\n")

print(f"--- Complex assembly complete ---")
print(f"Created PtNP with {len(pt_atoms)} atoms at target location.")
print(f"File saved to: {output_path}")