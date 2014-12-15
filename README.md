Open Healthcare Data Hack
=========================

Code produced at [Open Healthcare Data Hack](http://healthcaredatascience.com/) 13/14 December 2014.

The Python script preprocesses [MIMIC II Physionet dataset](http://physionet.org/challenge/2012/). Each patient is represented as one row of CSV file with the following features:

* __Survival - OUTPUT VARIABLE__ (0: survived, or 1: not survived)
* __Age__ (years) 
* __Gender__ (0: female, or 1: male) 
* __Height__ (cm) 
* __ICUType__ (1: Coronary Care Unit, 2: Cardiac Surgery Recovery Unit, 3: Medical ICU, or 4: Surgical ICU) 
* __Weight__ (kg) 

There are 36 temporal attributes in the dataset for which some measurements are taken during 48 hours:
  * Albumin (g/dL) 
  * ALP [Alkaline phosphatase (IU/L)] 
  * ALT [Alanine transaminase (IU/L)] 
  * AST [Aspartate transaminase (IU/L)] 
  * Bilirubin (mg/dL) 
  * BUN [Blood urea nitrogen (mg/dL)] 
  * Cholesterol (mg/dL) 
  * Creatinine [Serum creatinine (mg/dL)] 
  * DiasABP [Invasive diastolic arterial blood pressure (mmHg)] 
  * FiO2 [Fractional inspired O2 (0-1)] 
  * GCS [Glasgow Coma Score (3-15)] 
  * Glucose [Serum glucose (mg/dL)] 
  * HCO3 [Serum bicarbonate (mmol/L)] 	•	HCT [Hematocrit (%)] 
  * HR [Heart rate (bpm)] 
  * K [Serum potassium (mEq/L)] 
  * Lactate (mmol/L) 
  * Mg [Serum magnesium (mmol/L)] 
  * MAP [Invasive mean arterial blood pressure (mmHg)] 
  * MechVent [Mechanical ventilation respiration (0:false, or 1:true)] 
  * Na [Serum sodium (mEq/L)] 
  * NIDiasABP [Non-invasive diastolic arterial blood pressure (mmHg)] 
  * NIMAP [Non-invasive mean arterial blood pressure (mmHg)] 
  * NISysABP [Non-invasive systolic arterial blood pressure (mmHg)] 	•	PaCO2 [partial pressure of arterial CO2 (mmHg)] 
  * PaO2 [Partial pressure of arterial O2 (mmHg)] 
  * pH [Arterial pH (0-14)] 
  * Platelets (cells/nL) 
  * RespRate [Respiration rate (bpm)] 
  * SaO2 [O2 saturation in hemoglobin (%)] 
  * SysABP [Invasive systolic arterial blood pressure (mmHg)] 
  * Temp [Temperature (°C)] 
  * TropI [Troponin-I (μg/L)] 
  * TropT [Troponin-T (μg/L)] 
  * Urine [Urine output (mL)] 
  * WBC [White blood cell count (cells/nL)] 
  * Weight (kg)* 


