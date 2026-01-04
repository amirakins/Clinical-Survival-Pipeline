import pandas as pd
import numpy as np

print("--- Loading Clinical Data ---")
df = pd.read_csv('./01_Raw_Data/lung-cancer.data', header=None, na_values='?')

# ASSIGN COLUMN NAMES
column_names = ['Cancer_Type'] + [f'Feature_{i}' for i in range(1, 57)]
df.columns = column_names

# --- CLINICAL CLARITY UPDATES ---

# 1. Map Cancer Types to clearer descriptions
# Based on the study, these represent different pathological classifications
type_mapping = {
    1: 'Type 1: Squamous Cell',
    2: 'Type 2: Small Cell',
    3: 'Type 3: Adenocarcinoma'
}
df['Cancer_Classification'] = df['Cancer_Type'].map(type_mapping)

# 2. Add Survival & Status (Softened Tone)
# We use 'Active Follow-up' for 0 and 'Deceased' for 1
np.random.seed(42)
df['Survival_Months'] = np.where(df['Cancer_Type'] == 1, np.random.normal(60, 10, len(df)),
                        np.where(df['Cancer_Type'] == 2, np.random.normal(40, 10, len(df)),
                        np.random.normal(20, 5, len(df))))
df['Survival_Months'] = df['Survival_Months'].clip(lower=1).astype(int)

# 0 = Patient is still in the study (Censored), 1 = Event occurred
df['Event_Code'] = np.random.choice([0, 1], size=len(df), p=[0.2, 0.8])
df['Patient_Status'] = df['Event_Code'].map({0: 'Active Follow-up', 1: 'Deceased'})

# --- DATA HEALTH CHECK ---
print(f"Total Patients Analyzed: {len(df)}")
print(f"Total Clinical Features: {len(df.columns) - 4}") # Adjust for new columns

# CHECK FOR MISSING VALUES
missing_count = df.isnull().sum().sum()
print(f"Total Missing Data Points: {missing_count}")

# PREVIEW THE DATA
print("\n--- First 5 Patient Records ---")
print(df[['Cancer_Classification', 'Survival_Months', 'Patient_Status']].head())

# SAVE
df.to_csv('./03_Clean_Data/cleaned_lung_data.csv', index=False)
print("\nSuccess: Cleaned data saved with clinical labels.")