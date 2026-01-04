import pandas as pd

df = pd.read_csv('./03_Clean_Data/final_clinical_dataset_with_survival.csv')

# Check: Do all features stay within the 0-3 range?
for i in range(1, 57):
    col = f'Feature_{i}'
    if not df[col].isin([0, 1, 2, 3]).all():
        print(f"Warning: {col} has values outside the 0-3 range!")

print("Schema Check Complete.")