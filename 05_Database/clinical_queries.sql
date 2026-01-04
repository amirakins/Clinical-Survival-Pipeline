SELECT 
    Cancer_Type,
    COUNT(*) AS Total_Patients,
    ROUND(AVG(Survival_Months), 1) AS Mean_Survival_Months,
    SUM(Event_Occurred) AS Total_Deaths
FROM lung_cancer_data
GROUP BY Cancer_Type
ORDER BY Mean_Survival_Months DESC;


DROP VIEW IF EXISTS high_risk_patients;
CREATE VIEW high_risk_patients AS
SELECT * FROM lung_cancer_data
WHERE Cancer_Type = 3 
  AND Survival_Months < 12 
  AND Event_Occurred = 1;


DROP VIEW IF EXISTS high_priority_followup;
CREATE VIEW high_priority_followup AS
SELECT 
    Cancer_Type,
    Survival_Months,
    Event_Occurred
FROM lung_cancer_data
WHERE Cancer_Type = 3 
  AND Survival_Months < 24
  AND Event_Occurred = 1;


SELECT 
    Feature_20, 
    COUNT(*) as frequency
FROM lung_cancer_data
WHERE Cancer_Type = 1
GROUP BY Feature_20
ORDER BY frequency DESC;