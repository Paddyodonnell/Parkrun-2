import pandas as pd
import sys
import os
# Ensure the parent directory is in sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.functions import ms2s, s2ms

df = pd.read_csv('Data/cleaned_irish_parkruns.csv')

print(df.columns)

aggregations = {
    'Time in Seconds': 'mean',
    'Age Grade': 'mean',
}

df_summary = df.groupby('Location').agg(aggregations).reset_index()

df_summary['Time'] = df_summary['Time in Seconds'].apply(s2ms)
df_summary["Time in Seconds"] = df_summary["Time in Seconds"].round(2)
df_summary["Age Grade"] = df_summary["Age Grade"].round(2)

df_summary.to_csv('Data/location_averages.csv', index=False)


# print(df[df['Most Recent Number of Locations']>=5].shape[0])

# # subset data, only parkrunners who have done 10 locations or more

# df_2 = df[df['Most Recent Number of Locations']>=10]

# # Summary of locations




