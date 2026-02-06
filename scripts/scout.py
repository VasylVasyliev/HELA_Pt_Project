import os
from Bio.PDB import PDBParser

# Путь к файлу / Path to the file
data_path = os.path.expanduser("~/Documents/HELA_Pt_Project/data/1M17.pdb")

# Инициализация парсера / Initialize parser
parser = PDBParser(QUIET=True)
structure = parser.get_structure('EGFR', data_path)

print("\n--- FINAL COORDINATES FOR PLATINUM DOCKING ---")
print(f"{'Residue':<10} | {'Atom':<5} | {'Coordinates (x, y, z)':<25}")
print("-" * 60)

# Извлечение координат найденных атомов / Extract coordinates of found atoms
for model in structure:
    for chain in model:
        for residue in chain:
            res_num = residue.id[1]
            
            # Фокус на CYS 794 и ближайший THR / Focus on CYS 794 and nearest THR
            if (residue.get_resname() == 'CYS' and res_num == 794) or \
               (residue.get_resname() == 'THR' and res_num == 701):
                
                # Попытка достать активный атом / Try to get target atom
                atom_type = 'SG' if residue.get_resname() == 'CYS' else 'OG1'
                
                try:
                    atom = residue[atom_type]
                    print(f"{residue.get_resname()}{res_num:<4} | {atom_type:<5} | {atom.coord}")
                except KeyError:
                    # Если атома нет, берем Альфа-Углерод / If atom missing, take Alpha-Carbon
                    atom = residue['CA']
                    print(f"{residue.get_resname()}{res_num:<4} | CA    | {atom.coord}")

print("-" * 60)
print("[READY]: Coordinates extracted for simulation setup.")