import pandas as pd

df = pd.read_csv('irish_parkruns.csv')
data = df[df['Name'] != 'Unknown']

print(df['parkrunner_id'].nunique)

# Count races per individual
races_per_runner = df['parkrunner_id'].value_counts().reset_index()
races_per_runner.columns = ['parkrunner_id', 'num_races']

print(races_per_runner.head())  # Check the output

# Count unique locations per runner
locations_per_runner = df.groupby('parkrunner_id')['event_name'].nunique().reset_index()
locations_per_runner.columns = ['parkrunner_id', 'num_unique_locations']

print(locations_per_runner.head())  # Check the output

# Merge the two datasets
runner_summary = races_per_runner.merge(locations_per_runner, on='runner_id')

print(runner_summary.head())  # View the summary


