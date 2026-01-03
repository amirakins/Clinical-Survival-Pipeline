import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./03_Clean_Data/final_clinical_dataset.csv')

#CREATE A SUMMARY TABLE
summary_table = df.groupby('Cancer_Type').mean()
print("--- Mean Feature Values by Cancer Type ---")
print(summary_table.head())

# VISUALIZATION: Heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(summary_table.iloc[:, :20], annot=True, cmap='YlGnBu')
plt.title('Clinical Feature Profile by Lung Cancer Type (First 20 Features)')
plt.ylabel('Cancer Type')
plt.xlabel('Clinical Attributes')
plt.savefig('./04_Reports/clinical_heatmap.png') # Saves the chart as a file
print("\nSuccess: Heatmap saved as 'clinical_heatmap.png'")

#FINDING THE "MOST DIFFERENT" FEATURE
variation = summary_table.std().sort_values(ascending=False)
print(f"\nTop 3 Distinguishing Features:\n{variation.head(3)}")