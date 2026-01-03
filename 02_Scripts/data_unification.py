import pandas as pd
import numpy as np

df = pd.read_csv('./03_Clean_Data/final_clinical_dataset.csv')

#SIMULATE CLINICAL OUTCOMES 
np.random.seed(42)
df['Survival_Months'] = np.where(df['Cancer_Type'] == 1, np.random.normal(60, 10, len(df)),
                        np.where(df['Cancer_Type'] == 2, np.random.normal(40, 10, len(df)),
                        np.random.normal(20, 5, len(df))))

#Ensure we don't have negative months and make them integers
df['Survival_Months'] = df['Survival_Months'].clip(lower=1).astype(int)

#ADD THE 'EVENT' COLUMN 
df['Event_Occurred'] = np.random.choice([0, 1], size=len(df), p=[0.2, 0.8])

#SAVE
df.to_csv('./03_Clean_Data/final_clinical_dataset_with_survival.csv', index=False)

print("Success! File 'final_clinical_dataset_with_survival.csv' created with survival columns.")
print(df[['Cancer_Type', 'Survival_Months', 'Event_Occurred']].head())