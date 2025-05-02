import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Data/location_averages.csv')

df_sorted_time = df.sort_values(by='Time in Seconds', ascending=True)
df_sorted_age_grade = df.sort_values(by='Age Grade', ascending=True)

df_sorted_time = df_sorted_time.set_index('Location')
df_sorted_time = df_sorted_time['Time in Seconds']

df_sorted_time.plot(kind='barh', figsize=(10, 15), color='red')
plt.title('Location Average Times Ranked')
plt.xlabel('Time in Seconds')
plt.ylabel('Location Names')
plt.tight_layout()
plt.savefig('Data/Graphs/Location_Average_Times_ranked.png')
plt.show()

df_sorted_age_grade = df_sorted_age_grade.set_index('Location')
df_sorted_age_grade = df_sorted_age_grade['Age Grade']

df_sorted_age_grade.plot(kind='barh', figsize=(10, 15), color='red')
plt.gca().invert_yaxis()
plt.title('Location Average Age Grades Ranked')
plt.xlabel('Age Grade Percent')
plt.ylabel('Location Names')
plt.tight_layout()
plt.savefig('Data/Graphs/Location_Average_Age_Grades_ranked.png')
plt.show()

