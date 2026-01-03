import pandas as pd

df = pd.read_csv('./03_Clean_Data/cleaned_lung_data.csv')

#IDENTIFY THE GAPS
print("--- Missing Values Per Column (Before Imputation) ---")
print(df.isnull().sum()[df.isnull().sum() > 0])

#APPLY CLINICAL MODE IMPUTATION
for col in df.columns:
    if df[col].isnull().sum() > 0:
        column_mode = df[col].mode()[0]
        df[col] = df[col].fillna(column_mode)
        print(f"Filled missing values in {col} with mode: {column_mode}")

#FINAL VALIDATION 
print("\n--- Final Integrity Check ---")
remaining_missing = df.isnull().sum().sum()
if remaining_missing == 0:
    print("Success: Dataset is now complete and analysis-ready.")
else:
    print(f"Warning: {remaining_missing} missing values still remain.")

#SAVE
df.to_csv('./03_Clean_Data/final_clinical_dataset.csv', index=False)