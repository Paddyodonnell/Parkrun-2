import pandas as pd
import ast

df = pd.read_csv('Data/over_5.csv')

df["Age_Grades"] = df["Age_Grades"].fillna("[]")

df = df['Age_Grades']

print(df.head())

print(df.dtype)

print(df.head(10))  # Show the first 10 rows
print(df.sample(5))  # Show 5 random rows

def safe_eval(x):
    try:
        return ast.literal_eval(x) if isinstance(x, str) else x
    except Exception as e:
        print(f"Error at row: {x} -> {e}")
        return None  # Return None to mark problematic rows

df = df.apply(safe_eval)

problematic_rows = df[df.isna()]  # Rows where conversion failed
print(problematic_rows)

invalid_rows = df[~df.astype(str).str.startswith('[') | ~df.astype(str).str.endswith(']')]
print(invalid_rows)
