import pandas as pd

df = pd.read_csv('Data/exploded.csv')
df2 = pd.read_csv('Data/location_averages.csv')

df2.rename(columns={
    'Location':'Location',
    'Time in Seconds':'Location Average Time in Seconds',
    'Age Grade':'Location Average Age Grade',
    'Time':'Location Average Time'
}, inplace=True )

merged_df = pd.merge(
    df, 
    df2, 
    left_on='Location Names', 
    right_on='Location', 
    how='left'
)

merged_df.drop(columns='Location', inplace=True)

merged_df.rename(columns={
    'Parkrunner ID':'Parkrunner ID',
    'Location Names':'Location',
    'Number of Locations':'Most Recent No. of locations',
    'Times':'Time',
    'Age_Grades':'Age Grade',
    'Name':'Parkruner Name',
    'Most Recent Age Group':'Most Recent Age Group',
    'club':'Club',
    'Gender':'Gender',
    'Average Position':'Average Position',
    'Most Recent No. of Runs':'Most Recent No. of Runs',
    'Most recent Volunteers':'Most Recent No. of Volunteers',
    'Average Age Grade': 'Parkrunner Average Age Grade',
    'Average Time in Seconds':'Parkrunner Average Time in Seconds',
    'Average Time':'Parkrunner Average Time',
    'Location Average Time in Seconds':'Location Average Time in Seconds',
    'Location Average Age Grade':'Location Average Age Grade',
    'Location Average Time':'Location Average Time'
}, inplace=True)

merged_df.to_csv('Data/everything.csv', index=False)