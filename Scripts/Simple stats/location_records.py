import pandas as pd

df = pd.read_csv('Data/cleaned_irish_parkruns.csv')

# overall location record holders

course_record_holders = df.loc[df.groupby('Location')['Time in Seconds'].idxmin()]

print(course_record_holders)

##############################################

# Female location record holders

df_female = df[df['Gender'] == 'Female']

female_course_record_holders = df_female.loc[df_female.groupby('Location')['Time in Seconds'].idxmin()]

print(female_course_record_holders)

##############################################

# overall age grade record holders

age_grade_record_holders = df.loc[df.groupby('Location')['Age Grade'].idxmax()]

print(age_grade_record_holders)