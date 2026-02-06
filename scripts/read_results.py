import csv
import os

# Define path to the results
# Определить путь к результатам
file_path = os.path.expanduser('~/Documents/HELA_Pt_Project/results/docking_data.csv')

if os.path.exists(file_path):
    # Use a dictionary to store unique results
    # Использовать словарь для хранения уникальных результатов
    unique_results = {}

    with open(file_path, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            key = (row['Protein'], row['Mutation_Site'])
            # Store the latest distance for each mutation
            # Сохранить последнюю дистанцию для каждой мутации
            unique_results[key] = row['Distance_Angstrom']

    print(f"{'PROTEIN':<15} | {'MUTATION':<10} | {'DISTANCE (A)':<12}")
    print("-" * 45)
    
    for (prot, mut), dist in unique_results.items():
        print(f"{prot:<15} | {mut:<10} | {dist:<12}")
else:
    print("Database not found.")
    # База данных не найдена.