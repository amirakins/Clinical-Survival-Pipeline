import pandas as pd
import numpy as np

print("--- Loading Clinical Data ---")
df = pd.read_csv('./01_Raw_Data/lung-cancer.data', header=None, na_values='?')

#ASSIGN COLUMN NAMES
column_names = ['Cancer_Type'] + [f'Feature_{i}' for i in range(1, 57)]
df.columns = column_names

#DATA HEALTH CHECK 
print(f"Total Patients Analyzed: {len(df)}")
print(f"Total Clinical Features: {len(df.columns) - 1}")

# CHECK FOR MISSING VALUES
missing_count = df.isnull().sum().sum()
print(f"Total Missing Data Points: {missing_count}")

#PREVIEW THE DATA
print("\n--- First 5 Patient Records ---")
print(df.head())

#SAVE
df.to_csv('./03_Clean_Data/cleaned_lung_data.csv', index=False)
print("\nSuccess: Cleaned data saved as 'cleaned_lung_data.csv'")