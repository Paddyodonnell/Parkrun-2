import pandas as pd
import ast 

events = pd.read_csv('Data/location_averages.csv')
parkrunners = pd.read_csv('Data/over_5.csv')

print(events.head())
print(parkrunners.head())

# Convert string representation of lists into actual lists
parkrunners["Location Names"] = parkrunners["Location Names"].apply(ast.literal_eval)
parkrunners["Times"] = parkrunners["Times"].apply(ast.literal_eval)
parkrunners["Age_Grades"] = parkrunners["Age_Grades"].apply(ast.literal_eval)

# Convert to DataFrame and explode all three lists together
parkrunners_exploded = parkrunners.explode(["Location Names", "Times", "Age_Grades"])

# Rename columns
parkrunners_exploded = parkrunners_exploded.rename(columns={"Location Names": "Location"})

# Merge with events data
df_merged = parkrunners_exploded.merge(events, on="Location", suffixes=("_runner", "_location"))

# Save to CSV
df_merged.to_csv('Data/df_merged.csv', index=False)

