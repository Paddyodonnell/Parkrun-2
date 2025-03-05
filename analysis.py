import pandas as pd

df = pd.read_csv('parkrun_summary.csv')

print(df.columns)

print(df[df['Most Recent Number of Locations']>=5].shape[0])

# subset data, only parkrunners who have done 10 locations or more

df_2 = df[df['Most Recent Number of Locations']>=10]

print(df_2.head())