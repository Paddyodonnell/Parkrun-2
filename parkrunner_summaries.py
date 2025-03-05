import pandas as pd
from functions import ms2s, s2ms

df = pd.read_csv('cleaned_irish_parkruns.csv')
df['Time in Seconds'] = df['Time'].apply(ms2s)

# print(df.head())

# print(df.columns)

print(df['Parkrunner ID'].nunique())

# 5 or more runs?
runners_5_plus = df[df['Runs'] >= 5]['Parkrunner ID'].nunique()
print(f"Number of runners with at least 5 parkruns: {runners_5_plus}")

# 5 or more locations?
runners_location_counts = df.groupby('Parkrunner ID')['Location'].nunique()
runners_5_locations = (runners_location_counts >= 5).sum()
print(f"Number of runners who have completed at least 5 different parkrun locations: {runners_5_locations}")

# 10 or more runs?
runners_10_plus = df[df['Runs'] >= 10]['Parkrunner ID'].nunique()
print(f"Number of runners with at least 10 parkruns: {runners_10_plus}")

# 5 or more locations?
runners_location_counts = df.groupby('Parkrunner ID')['Location'].nunique()
runners_10_locations = (runners_location_counts >= 10).sum()
print(f"Number of runners who have completed at least 10 different parkrun locations: {runners_10_locations}")

# Define aggregation rules
aggregations = {
    'Name': 'first',  # Assuming name remains consistent for each runner
    'Age Group': 'last',  # Most recent Age Group (assuming sorted by date)
    'club': 'first',  # Taking the first recorded club (or 'last' if preferred)
    'Gender': 'first',  # Gender should remain constant
    'Position': 'mean',  # Average finishing position
    'Runs': 'last',  # Most recent number of runs
    'Volunteers': 'last',  # Most recent volunteer count
    'Age Grade': 'mean',  # Average Age Grade
    'Time in Seconds': 'mean',  # Average Time in Seconds
}

# Ensure data is sorted by Date so that 'last' works correctly
df = df.sort_values(by=['Parkrunner ID', 'Date'])

location_aggregations = df.groupby('Parkrunner ID')['Location'].agg(
    Last_Location='last',
    Unique_Locations='nunique'
)

# Group by Parkrunner ID and apply the aggregations
df_summary = df.groupby('Parkrunner ID').agg(aggregations).reset_index()

df_summary = pd.merge(location_aggregations, df_summary, on='Parkrunner ID').reset_index(drop=True)

# Rename columns for clarity
df_summary.rename(columns={
    'Age Group': 'Most Recent Age Group',
    'Position': 'Average Position',
    'Runs': 'Most Recent No. of Runs',
    'Volunteers': 'Most recent Volunteers',
    'Age Grade': 'Average Age Grade',
    'Time in Seconds': 'Average Time in Seconds',
    'Unique_Locations': 'Most Recent Number of Locations',
    'Last_Location': 'Location'
}, inplace=True)

df_summary['Average Time'] = df_summary['Average Time in Seconds'].apply(s2ms)

# Save to CSV
df_summary.to_csv("parkrun_summary.csv", index=False)

print("CSV file created: parkrun_summary.csv")

