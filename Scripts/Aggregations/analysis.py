import pandas as pd
import sys
import os
# Ensure the parent directory is in sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.functions import ms2s, s2ms

df = pd.read_csv('Data/cleaned_irish_parkruns.csv')
df['Time in Seconds'] = df['Time'].apply(ms2s)

print(df.columns)

aggregations = {
    'Time in Seconds': 'mean',
    'Age Grade': 'mean'
}

df_summary = df.groupby('Location').agg(aggregations).reset_index()

df_summary.to_csv('Data/location_averages.csv', index=False)

df = pd.read_csv('Data/location_averages.csv')

df_summary_over_5 = df[df['Number of Locations']>=5]

df_summary_over_5.to_csv('over_5.csv', index=False)







