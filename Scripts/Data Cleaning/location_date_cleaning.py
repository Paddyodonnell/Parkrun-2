import pandas as pd

df = pd.read_csv('Data/irish_parkruns.csv')
df = df[df['Name']!='Unknown']

## Mistakes with paricular names

# Hmmm… can't reach t
# Glengarrif, 11/4/17

event_update = {
    90: ('Glengarrif', '11/4/17')
}

mask = (df['Location'] == "Hmmm… can't reach t") & (df['Date'] == 'unknown date')

for event_num, (location, date) in event_update.items():
    df.loc[mask & (df['Event Number'] == event_num), ['Location', 'Date']] = location, date

# Royal Canal parkrun,
# Royal Canal, Kilcock

df['Location'] = df['Location'].str.replace("Royal Canal parkrun,", "Royal Canal, Kilcock")

# The Grand Canal Way parkrun, T
# The Grand Canal Way, Tullamore

df['Location'] = df['Location'].str.replace("The Grand Canal Way parkrun, T", "The Grand Canal Way, Tullamore")

# Tramore parkrun, W
# Tramore, Waterford

df['Location'] = df['Location'].str.replace("Tramore parkrun, W", "Tramore, Waterford")

# Tramore Valley parkr
# Tramore Valley, Cork

df['Location'] = df['Location'].str.replace("Tramore Valley parkr", "Tramore Valley, Cork")

# Deerpark parkrun, Car
# Deerpark, Carlanstown

df['Location'] = df['Location'].str.replace("Deerpark parkrun, Car", "Deerpark, Carlanstown")

# Deerpark Forest parkrun, 
# Deerpark Forest, Virginia

df['Location'] = df['Location'].str.replace("Deerpark Forest parkrun,", "Deerpark Forest, Virginia")

## unknown location

# Ballincollig, 260, 1/21/23

# Brickfields, 22, 6/9/18

# Newcastle West, 55, 5/13/17

# Tramore Valley parkr, 97, 3/16/24

event_updates = {
    260: ('Ballincollig', '1/21/23'),
    22: ('Brickfields', '6/9/18'),
    55: ('Newcastle West', '5/13/17'),
    97: ('Tramore Valley parkr', '3/16/24')
}

# Apply updates only where Location and Date are 'Unknown'
mask = (df['Location'] == 'unknown location') & (df['Date'] == 'unknown date')

# Update DataFrame using .loc for efficient assignment
for event_num, (location, date) in event_updates.items():
    df.loc[mask & (df['Event Number'] == event_num), ['Location', 'Date']] = location, date

print((df['Location']=='unknown location').sum())

df.to_csv('Data/cleaned_irish_parkruns.csv', index=False)

print(df['Location'].unique())


