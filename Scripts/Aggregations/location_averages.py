import pandas as pd

df = pd.read_csv('Data/cleaned_irish_parkruns.csv')

print(df.columns)

aggregations = {
    'Time in Seconds': 'mean',
    'Age Grade': 'mean',
}

df_summary = df.groupby('Location').agg(aggregations).reset_index()

df_summary.to_csv('Data/location_averages.csv', index=False)


# print(df[df['Most Recent Number of Locations']>=5].shape[0])

# # subset data, only parkrunners who have done 10 locations or more

# df_2 = df[df['Most Recent Number of Locations']>=10]

# # Summary of locations




