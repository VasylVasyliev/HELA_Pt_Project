import matplotlib.pyplot as plt
import pandas as pd
import json

# Load the traffic data
# Загрузка данных о трафике
log_file = 'results/global_traffic_stats.json'
data = []

with open(log_file, 'r') as f:
    for line in f:
        data.append(json.loads(line))

df = pd.DataFrame(data)

# Process data: get the latest entry for each repository
# Обработка данных: берем последнюю запись для каждого репозитория
latest_stats = df.sort_values('timestamp').groupby('repository').last().reset_index()

# Plotting
# Построение графика
plt.figure(figsize=(10, 6))
bars = plt.bar(latest_stats['repository'], latest_stats['views'], color=['#3498db', '#9b59b6'])

# Add labels
# Добавление подписей
plt.title('GitHub Repository Popularity (Total Views)', fontsize=14)
plt.ylabel('Number of Views')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add values on top of bars
# Добавление значений над столбцами
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5, int(yval), ha='center', va='bottom', fontweight='bold')

# Save the plot
# Сохранение графика
plt.savefig('results/traffic_comparison.png')
print("Traffic plot saved to results/traffic_comparison.png")