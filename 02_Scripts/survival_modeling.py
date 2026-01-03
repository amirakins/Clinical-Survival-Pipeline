import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test

df = pd.read_csv('./03_Clean_Data/final_clinical_dataset_with_survival.csv')

#INITIALIZE THE MODEL
kmf = KaplanMeierFitter()
plt.figure(figsize=(10, 6))

#PLOT CURVES FOR EACH CANCER TYPE
for name, grouped_df in df.groupby('Cancer_Type'):
    kmf.fit(grouped_df['Survival_Months'], 
            event_observed=grouped_df['Event_Occurred'], 
            label=f'Cancer Type {name}')
    kmf.plot_survival_function()

#FORMATTING
plt.title('Kaplan-Meier Survival Curves by Lung Cancer Type')
plt.xlabel('Timeline (Months)')
plt.ylabel('Survival Probability')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
plt.savefig('./04_Reports/survival_curve.png')
print("--- Survival Curve Generated: survival_curve.png ---")

#STATISTICAL SIGNIFICANCE 
type1 = df[df['Cancer_Type'] == 1]
type3 = df[df['Cancer_Type'] == 3]
results = logrank_test(type1['Survival_Months'], type3['Survival_Months'], 
                       type1['Event_Occurred'], type3['Event_Occurred'])

print(f"\nLog-Rank Test (Type 1 vs Type 3):")
print(f"P-value: {results.p_value:.4f}")

if results.p_value < 0.05:
    print("Conclusion: There is a statistically significant difference in survival.")