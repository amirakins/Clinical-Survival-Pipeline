import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD DATA
# Ensure this matches the file name from your cleaning script
df = pd.read_csv('./03_Clean_Data/final_clinical_dataset.csv')


# 3. STATISTICAL AGGREGATION
# We group by the numeric 'Cancer_Type' but tell pandas to ignore the string columns
summary_table = df.groupby('Cancer_Type').mean(numeric_only=True)

print("--- Mean Feature Values by Cancer Type (Numeric Summary) ---")
print(summary_table.iloc[:, :5]) # Print first 5 features for brevity

# 4. VISUALIZATION: Heatmap
plt.figure(figsize=(14, 7))

# We plot the first 20 features to keep the heatmap readable
# Using 'YlGnBu' (Yellow-Green-Blue) is a standard professional color palette
sns.heatmap(summary_table.iloc[:, :20], annot=True, cmap='YlGnBu', fmt='.1f')

plt.title('Clinical Feature Profile by Pathological Lung Cancer Type', fontsize=15)
plt.ylabel('Numeric Cancer Type (1, 2, 3)', fontsize=12)
plt.xlabel('Clinical Attributes (Feature 1 - 20)', fontsize=12)

# Save high-resolution version for the portfolio
plt.savefig('./04_Reports/clinical_heatmap.png', dpi=300, bbox_inches='tight')
print("\nSuccess: Heatmap saved to 04_Reports/clinical_heatmap.png")

# 5. RESEARCH INSIGHT: Finding the "Most Different" Feature
# This helps you answer "Which feature actually matters?" in an interview
variation = summary_table.std().sort_values(ascending=False)
print("\n--- Top 3 Distinguishing Features ---")
print(variation.head(3))