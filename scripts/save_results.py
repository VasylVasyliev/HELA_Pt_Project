import csv
import os

# Base directory and file path
# Базовая директория и путь к файлу
base_dir = os.path.expanduser('~/Documents/HELA_Pt_Project')
file_path = os.path.join(base_dir, 'results', 'docking_data.csv')

# Current research data for a new mutation
# Текущие данные исследования для новой мутации
new_entry = ['EGFR (1M17)', 'L858R', '3.2']
header = ['Protein', 'Mutation_Site', 'Distance_Angstrom']

existing_data = []

# Read existing data to check for duplicates
# Прочитать существующие данные для проверки дубликатов
if os.path.exists(file_path):
    with open(file_path, mode='r', newline='') as f:
        reader = list(csv.reader(f))
        if len(reader) > 0:
            existing_data = reader[1:] # Skip header / Пропустить заголовок

# Check if the new entry is already in the file
# Проверить, есть ли уже такая запись в файле
if new_entry not in existing_data:
    with open(file_path, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not os.path.isfile(file_path) or os.stat(file_path).st_size == 0:
            writer.writerow(header)
        writer.writerow(new_entry)
    print(f"Entry {new_entry[1]} added.")
    # Запись {new_entry[1]} добавлена.
else:
    print(f"Entry {new_entry[1]} already exists. Skipping.")
    # Запись {new_entry[1]} уже существует. Пропуск.