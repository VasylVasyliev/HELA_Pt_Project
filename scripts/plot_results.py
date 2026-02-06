import matplotlib.pyplot as plt
import pandas as pd
import os

# Load docking data for EGFR analysis
# Загрузка данных докинга для анализа EGFR
data_path = 'results/docking_data.csv'
df = pd.read_csv(data_path)

# Create a bar chart comparing HeLa, L858R, and T790M
# Создание диаграммы: HeLa, L858R и резистентная мутация T790M
plt.figure(figsize=(10, 6))
colors = ['#4CAF50', '#FF9800', '#FF5252']  # Green, Orange, Red
bars = plt.bar(df['Mutation'], df['Distance_Angstrom'], color=colors)

# Add a threshold line for stable binding at 3.0 Å
# Добавление пороговой линии стабильности на уровне 3.0 Å
plt.axhline(y=3.0, color='blue', linestyle='--', linewidth=2, label='Stability Threshold (3.0 Å)')

# Labeling the chart
# Настройка подписей и заголовков
plt.title('EGFR Binding Affinity: Wild Type vs Mutations', fontsize=14)
plt.xlabel('Protein Variant', fontsize=12)
plt.ylabel('Distance (Å)', fontsize=12)
plt.ylim(0, 5)  # Increased limit to accommodate T790M
plt.legend()

# Add distance values on top of bars
# Добавление значений дистанции над столбцами
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, yval, ha='center', va='bottom')

# Save the visualization
# Сохранение результата
plt.savefig('results/egfr_comparison_plot.png')
print("Analysis complete. Plot saved to results/egfr_comparison_plot.png")