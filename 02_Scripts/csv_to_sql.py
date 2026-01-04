import pandas as pd
import sqlite3

df = pd.read_csv('./03_Clean_Data/final_clinical_dataset_with_survival.csv')

conn = sqlite3.connect('./03_Clean_Data/lung_cancer_research.db')

df.to_sql('lung_cancer_data', conn, if_exists='replace', index=False)

print("Check complete. Columns are now named properly")
conn.close()