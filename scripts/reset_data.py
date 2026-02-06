import csv
import os

# Path to the data file in the project folder
# Путь к файлу данных в папке проекта
file_path = os.path.expanduser('~/Documents/HELA_Pt_Project/results/docking_data.csv')

# Scientific results: 2.8A (measured in PyMOL) and 3.2A (mutation site)
# Научные результаты: 2.8A (измерено в PyMOL) и 3.2A (место мутации)
clean_data = [
    ['Protein', 'Mutation_Site', 'Distance_Angstrom'],
    ['EGFR (1M17)', 'Cys794', '2.8'], 
    ['EGFR (1M17)', 'L858R', '3.2']
]

def update_database():
    # Create directory if it does not exist
    # Создание директории, если она не существует
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write updated scientific data to CSV
    # Запись обновленных научных данных в CSV
    with open(file_path, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(clean_data)
    
    print(f"Database successfully updated with distance: 2.8 A")
    # База данных успешно обновлена с дистанцией: 2.8 А

if __name__ == "__main__":
    update_database()