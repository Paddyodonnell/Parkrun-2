import pandas as pd
import ast  # To safely convert string lists to actual lists

# Sample DataFrame (Replace this with your actual CSV reading step)
df = pd.read_csv("Data/over_5.csv")

# replace nans from Age_Grades with 0s. (Remember to remove if averaging)
df["Age_Grades"] = df["Age_Grades"].str.replace('nan', '0', regex=False)

# Convert string lists into actual lists
list_columns = ["Location Names", "Times", "Age_Grades"]
for col in list_columns:
    df[col] = df[col].apply(ast.literal_eval)

# Explode the three columns simultaneously
df_exploded = df.explode(list_columns, ignore_index=True)

# Display the new structure
print(df_exploded.head())

df_exploded.to_csv('Data/exploded.csv', index=False)
