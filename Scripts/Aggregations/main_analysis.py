import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("Data/exploded.csv")

# Finishing Time Analysis

# Compute deviation (Actual - Expected)
df["Time Deviation"] = df["Times"] - df["Average Time in Seconds"]

# Compute average deviation per location
location_performance_time = df.groupby("Location Names")["Time Deviation"].mean().rename("Avg Time Deviation")

# Rank locations from fastest to slowest
location_performance_time = location_performance_time.sort_values()

location_performance_time.to_csv('Data/location_difficulty_time', index=False)


#####################################################

# visualisations

plt.figure(figsize=(10, 6))
sns.histplot(location_performance_time, bins=30, kde=True)
plt.title("Distribution of Average Time Deviations by Location")
plt.xlabel("Avg Time Deviation (Seconds)")
plt.ylabel("Number of Locations")
plt.tight_layout()
plt.savefig("Data/Graphs/Distribution_Time_deviations.png")
plt.show()

location_performance_time.plot(kind='barh', figsize=(10, 15), color='red')
plt.xlabel("Avg Time Deviation (Seconds)")
plt.title("Relative Difficulty of Irish Parkruns (Time)")
plt.tight_layout()
plt.savefig("Data/Graphs/relative_difficulty(Time).png", dpi=300)
plt.show()


################################################################################

# Age Grade Analysis

# Compute deviation (Actual - Expected)
df["Age Grade Deviation"] = df["Age_Grades"] - df["Average Age Grade"]

# Compute average deviation per location
location_performance_age_grade = df.groupby("Location Names")["Age Grade Deviation"].mean().rename("Avg Age Grade Deviation")

# Rank locations from fastest to slowest
location_performance_age_grade = location_performance_age_grade.sort_values()

location_performance_age_grade.to_csv('Data/location_difficulty_age_grade', index=False)

#####################################################

# visualisations

plt.figure(figsize=(10, 6))
sns.histplot(location_performance_age_grade, bins=30, kde=True)
plt.title("Distribution of Average Age Grade Deviations by Location")
plt.xlabel("Avg Age Grade Deviation (Percent)")
plt.ylabel("Number of Locations")
plt.tight_layout()
plt.savefig("Data/Graphs/Distribution_Age_Grade_deviations.png")
plt.show()

location_performance_age_grade.plot(kind='barh', figsize=(10, 15), color='red')
plt.gca().invert_yaxis()
plt.gca().invert_xaxis()
plt.xlabel("Avg Age Grade Deviation (Percent)")
plt.title("Relative Difficulty of Irish Parkruns (Age Grade)")
plt.tight_layout()
plt.savefig("Data/Graphs/relative_difficulty(Age Grade).png", dpi=300)
plt.show()

