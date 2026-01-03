# Clinical Survival Analysis: Pathological Lung Cancer Classification
## 🏥 Project Overview
This project focuses on the end-to-end processing and statistical analysis of a high-dimensional lung cancer dataset. The primary goal was to transform raw, undocumented clinical attributes into a structured format suitable for survival modeling—a key requirement for clinical research roles at institutions like **Emory University**.

### Key Deliverables:
* **Automated Data Pipeline:** 5 Python scripts for ingestion, cleaning, and modeling.
* **Statistical Validation:** Kaplan-Meier survival analysis and Log-Rank testing.
* **Data Governance:** Professional Metadata and Data Dictionary documentation.

---

## 🛠️ Tech Stack
* **Language:** Python 3.11
* **Data Handling:** Pandas, NumPy
* **Statistical Analysis:** Lifelines (Survival Analysis)
* **Visualization:** Matplotlib, Seaborn
* **Environment:** OS-agnostic directory automation

---
## Heatmap
![heatmap](https://github.com/amirakins/Clinical-Survival-Pipeline/blob/main/04_Reports/clinical_heatmap.png)
## Survival
![survival](https://github.com/amirakins/Clinical-Survival-Pipeline/blob/main/04_Reports/survival_curve.png)

## 📂 Project Structure
```text
Lung_Cancer_Project/
├── 01_Raw_Data/           # Original .data and .names files
├── 02_Scripts/            # Python automation scripts
├── 03_Clean_Data/         # Imputed and unified datasets
└── 04_Report/             # Visualizations (Heatmaps, Survival Curves)

