import pandas as pd
import matplotlib.pyplot as plt
import os

# Path to the data and output
# Путь к данным и выходному файлу
data_path = os.path.expanduser('~/Documents/HELA_Pt_Project/results/docking_data.csv')
output_path = os.path.expanduser('~/Documents/HELA_Pt_Project/results/comparison_plot.png')

def create_visual():
    # Load docking results
    # Загрузка результатов докинга
    df = pd.read_csv(data_path)
    
    plt.figure(figsize=(10, 6))
    
    # Set different colors for different mutation sites
    # Установка разных цветов для разных сайтов мутаций
    bar_colors = ['#2E86C1', '#E67E22'] # Blue for Cys794, Orange for L858R
    
    bars = plt.bar(df['Mutation_Site'], df['Distance_Angstrom'], color=bar_colors)
    
    # Add a threshold line for biological activity (2.5 - 3.0 A)
    # Добавление линии порога биологической активности (2.5 - 3.0 А)
    plt.axhline(y=3.0, color='red', linestyle='--', label='Max Active Distance')
    
    plt.title('Platinum Docking Efficiency: Cys794 vs L858R', fontsize=14)
    plt.xlabel('Mutation Site', fontsize=12)
    plt.ylabel('Distance (Angstroms)', fontsize=12)
    plt.legend()
    
    # Save the professional plot
    # Сохранение профессионального графика
    plt.savefig(output_path)
    print(f"Professional plot saved at: {output_path}")
    # Профессиональный график сохранен по адресу: {output_path}

if __name__ == "__main__":
    if os.path.exists(data_path):
        create_visual()
    else:
        print("Data file not found. Run reset_data.py first.")
        # Файл данных не найден. Сначала запустите reset_data.py.