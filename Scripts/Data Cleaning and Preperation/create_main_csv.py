import json
import pandas as pd
import os

jsons = 'Data/scraped_files'

all_data = []

for scraped_file in os.listdir(jsons):
    if scraped_file.endswith('.json'):
        file_path = os.path.join(jsons, scraped_file)

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if isinstance(data, list):
            all_data.extend(data)
        else:
            all_data.append(data)

df = pd.DataFrame(all_data)

df.to_csv('Data/irish_parkruns.csv', index=False)
