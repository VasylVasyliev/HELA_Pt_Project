import requests
import json
import datetime
import os

# Configuration
# Конфигурация
TOKEN = os.getenv('GITHUB_TOKEN')
REPOS = [
    'VasylVasyliev/HELA_Pt_Project',
    'VasylVasyliev/DNA-Data-Science'
]
LOG_FILE = 'results/global_traffic_stats.json'

def fetch_all_traffic():
    headers = {'Authorization': f'token {TOKEN}'}
    all_data = []

    for repo_name in REPOS:
        print(f"Fetching data for {repo_name}...")
        url = f'https://api.github.com/repos/{repo_name}/traffic/views'
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            
            # Record which repo this data belongs to
            # Указываем, к какому репозиторию относятся данные
            entry = {
                'repository': repo_name,
                'timestamp': datetime.datetime.now().isoformat(),
                'views': data.get('count', 0),
                'uniques': data.get('uniques', 0)
            }
            all_data.append(entry)
            
        except Exception as e:
            print(f"Error fetching {repo_name}: {e}")

    # Save to history
    # Сохранение в историю
    if not os.path.exists('results'):
        os.makedirs('results')
        
    with open(LOG_FILE, 'a') as f:
        for entry in all_data:
            json.dump(entry, f)
            f.write('\n')
    
    print(f"\nSuccess! Statistics for {len(all_data)} repos saved to {LOG_FILE}")

if __name__ == "__main__":
    fetch_all_traffic()