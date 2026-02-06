import matplotlib.pyplot as plt
import pandas as pd
import os

# Load docking data for EGFR analysis
# Загрузка данных докинга для анализа EGFR
data_path = 'results/docking_data.csv'
df = pd.read_csv(data_path)

# Create a bar chart comparing HeLa vs Lung Cancer mutation
# Создание столбчатой диаграммы: HeLa против мутации рака легких
plt.figure(figsize=(8, 6))
bars = plt.bar(df['Mutation'], df['Distance_Angstrom'], color=['#4CAF50', '#FF5252'])

# Add a threshold line for stable binding (2.8 Å)
# Добавление пороговой линии для стабильной связи (2.8 Å)
plt.axhline(y=2.8, color='blue', linestyle='--', label='Optimal Binding (2.8 Å)')

# Labeling the chart
# Настройка подписей графика
plt.title('EGFR Binding Affinity: Wild Type vs L858R Mutation')
plt.xlabel('Protein Type')
plt.ylabel('Distance (Å)')
plt.ylim(0, 4)
plt.legend()

# Save the professional visualization
# Сохранение профессиональной визуализации
plt.savefig('results/egfr_comparison_plot.png')
print("Analysis complete. Visualization saved to results/egfr_comparison_plot.png")