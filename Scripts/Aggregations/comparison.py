import pandas as pd
import ast 

events = pd.read_csv('Data/location_averages.csv')
parkrunners = pd.read_csv('Data/over_5.csv')

print(events.head())
print(parkrunners.head())

# Convert string representation of lists into actual lists
parkrunners["Location Names"] = parkrunners["Location Names"].apply(ast.literal_eval)

# Explode so that each location gets its own row
parkrunners_exploded = parkrunners.explode("Location Names").rename(columns={"Location Names": "Location"})

df_merged = parkrunners_exploded.merge(events, on="Location", suffixes=("_runner", "_location"))

df_merged.to_csv('df_merged.csv', index=False)

print(df_merged.columns)

# df_merged["Time Difference"] = df_merged["Average Time in Seconds_runner"] - df_merged["Time in Seconds_location"]

# location_speed = df_merged.groupby("Location")["Time Difference"].mean().reset_index()
# location_speed = location_speed.sort_values(by="Time Difference")  # Sort ascending

# print(location_speed.head(10))  # 10 fastest locations

# print(location_speed.tail(10))  # 10 slowest locations

# df_merged["Relative Rank"] = df_merged.groupby("Location")["Time Difference"].rank()

