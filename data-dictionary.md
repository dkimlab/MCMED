# Data Dictionary

## Visits

| Column Name | Description | Data Type | Sample Data |
|------------|-------------|------------|-------------|
| MRN | Patient identifier (Random ID mapped to original MRN) | int | 99940664 |
| CSN | Visit identifier (Random ID mapped to original CSN) | int | 98874959 |
| Visit_no | The visit number for this patient in the dataset | int | 1 |
| Visits | Total number of visits for this patient in the dataset | int | 1 |
| Age | Patient age in years at time of visit (Random perturbation of age +/- 2 years, Ages greater than 90 set to 90) | int | 90 |
| Gender | Patient gender | string | F |
| Race | Patient race | string | White |
| Ethnicity | Patient hispanic ethnicity | string | Non-Hispanic/Non-Latino |
| Means_of_arrival | Means of arrival to the ED | string | Self |
| Triage_Temp | Temperature at triage (C) | float | 36.7 |
| Triage_HR | Heart rate at triage (bpm) | float | 80.0 |
| Triage_RR | Respiratory rate at triage (breaths per min.) | float | 18.0 |
| Triage_SpO2 | Oxygen saturation at triage (%) | float | 100.0 |
| Triage_SBP | Systolic blood pressure at triage (mmHg) | float | 128.0 |
| Triage_DBP | Diastolic blood pressure at triage (mmHg) | float | 78.0 |
| Triage_acuity | Emergency Severity Index (ESI) at triage (1-5) | string | 3-Urgent |
| CC | Chief complaint(s) at triage | string | ABDOMINAL PAIN |
| ED_dispo | Disposition of patient from the ED | string | Discharge |
| Hours_to_next_visit | For patients with a subsequent visit, number of hours from departure of current visit to arrival of next visit | float | 40.0 |
| Dispo_class_next_visit | Dispo_class for next visit | string | Discharge |
| ED_LOS | Length of ED stay, hours | float | 4.82 |
| Hosp_LOS | Length of hospital stay (including post-ED admission), days | float | 1.0 |
| DC_dispo | Final disposition of patient from the hospital | string | Home/Work (includes foster care) |
| Payor_class | Class of primary visit payor | string | Medicare |
| Admit_service | For admitted patients, service admitting the patient from the ED | string | Emergency Medicine |
| Dx_ICD9 | Primary visit diagnosis, ICD9 code | string | 786.50 |
| Dx_ICD10 | Primary visit diagnosis, ICD10 code | string | R07.9 |
| Dx_name | Name of ICD10 code | string | Chest pain, unspecified type |
| Arrival_time | Time of arrival to ED (Random-shift date, keeping season constant) | datetime | 2262-01-09T03:16:07Z |
| Roomed_time | Time of patient rooming (Random-shift date, keeping season constant) | datetime | 2283-03-02T07:36:59Z |
| Dispo_time | Time of disposition decision (Random-shift date, keeping season constant) | datetime | 2247-09-22T10:54:42Z |
| Admit_time | For admitted patients, time of admission order (Random-shift date, keeping season constant) | datetime | 2283-03-02T12:29:59Z |
| Departure_time | Time of departure from ED (Random-shift date, keeping season constant) | datetime | 2209-08-12T11:31:38Z |

## Orders

| Column Name | Description | Data Type | Sample Data |
|------------|-------------|------------|-------------|
| CSN | Visit identifier (Random ID mapped to original CSN) | int | 99139687 |
| Order_time | Time of order (Random-shift date, keeping season constant) | datetime | 2226-01-15T15:39:22Z |
| Order_type | Type of order (lab, imaging, medication, etc) | string | Lab |
| Procedure_name | Name of order | string | CBC WITH DIFFERENTIAL |
| Procedure_ID | Identifier for order (Mapped to CPT codes) | string | LABMETC |
| First_admin_time | For medications, time of first administration (Random-shift date, keeping season constant) | datetime | 2212-11-03T16:51:00Z |
| Result_time | For lab and imaging tests, time of result (Random-shift date, keeping season constant) | datetime | 2295-08-25T16:55:28Z |

## Meds (Home medications)

| Column Name | Description | Data Type | Sample Data |
|------------|-------------|------------|-------------|
| MRN | Patient identifier (Random ID mapped to original MRN) | int | 99721983 |
| Med_ID | Medication identifier (mapped to NDC id) | int | 14113 |
| NDC | National Drug Code identifier | string | 69618-066-10 |
| Name | Medication name | string | ASPIRIN 81 MG PO TBEC |
| Generic_name | Generic name | string | aspirin 81 mg tablet,delayed release |
| Med_class | High-level classification of the medication | string | VITAMIN D PREPARATIONS |
| Med_subclass | A more detailed classification | string | Vitamins - D Derivatives |
| Active | Indicates whether a patient was thought to be using the medication at the time of the visit | string | Y |
| Entry_date | Medication entry date (Random-shift date, keeping season constant) | date | 2270-07-20T00:00:00Z |
| Start_date | Medication start date (Random-shift date, keeping season constant) | date | 2275-08-31T00:00:00Z |
| End_date | Medication end date (Random-shift date, keeping season constant) | date | 2241-08-06T00:00:00Z |

## PMH (Prior diagnoses)

| Column Name | Description | Data Type | Sample Data |
|------------|-------------|------------|-------------|
| MRN | Patient identifier (Random ID mapped to original MRN) | int | 99084665 |
| Noted_date | Date when the diagnosis was recorded (Random-shift date, keeping season constant) | date | 2219-08-10T00:00:00Z |
| CodeType | Whether code is ICD9 or ICD10 | string | Dx10 |
| Code | Diagnosis code | string | I10 |
| Desc10 | Text description of the code | string | Essential (primary) hypertension |
| CCS | Clinical Classification Software category of the diagnosis | float | 259.0 |
| DescCCS | Text description of the CCS category | string | Residual codes; unclassified |

## Labs (Lab results from the ED visit)

| Column Name | Description | Data Type | Sample Data |
|------------|-------------|------------|-------------|
| CSN | Visit identifier (Random ID mapped to original CSN) | int | 99880957 |
| Order_time | Time of lab order (Random-shift date, keeping season constant) | datetime | 2221-07-03T18:37:12Z |
| Result_time | Time of lab result (Random-shift date, keeping season constant) | datetime | 2233-07-07T04:37:14Z |
| Display_name | Name of order | string | CBC with Differential (CBCD) |
| Abnormal | Flag for abnormal or critical result | string | Abnormal |
| Component_name | Name of lab component | string | SODIUM |
| Component_result | Lab result (Removed results containing dates or names) | string | Negative |
| Component_value | Lab value (Sometimes identical to result, sometimes different, e.g. result may be categorical and value numeric. Removed results containing dates or names) | string | 1 |
| Component_units | Units of component_value, where applicable | string | % |
| Component_abnormal | Flag for abnormal component_value | string | Normal |
| Component_nml_low | Low end of normal range for component | float | 0.0 |
| Component_nml_high | High end of normal range for component | float | 5.2 |

## Rads (Imaging result from the ED visit)

| Column Name | Description | Data Type | Sample Data |
|------------|-------------|------------|-------------|
| CSN | Visit identifier (Random ID mapped to original CSN) | int | 99002166 |
| Order_time | Time of imaging order (Random-shift date, keeping season constant) | datetime | 2205-07-07T11:11:36Z |
| Result_time | Time of imaging result (Random-shift date, keeping season constant) | datetime | 2291-10-02T05:06:13Z |
| Study | Imaging study name | string | XR CHEST 1 VIEW |
| Impression | Imaging result impression (Used the Stanford AIMI De-identification tool JAMIA, HuggingFace) | string | "1. No acute cardiopulmonary disease." |
## Continuous Vital Signs & Other Numeric Features

| Column Name | Description | Data Type | Sample Data |
|------------|-------------|------------|-------------|
| CSN | Visit identifier (Random ID mapped to original CSN) | int | 99833461 |
| Source | Indicates whether a value was recorded by nursing (Chart) or derived directly from the monitoring database (Monitor) | string | Monitor |
| Measure | One of 12 measurements:<br>- `HR` Heart rate, heartbeats per minute<br>- `RR` Respiratory rate, breaths per minute<br>- `SpO2` Oxygen saturation by pulse oximetry, %<br>- `SBP` Systolic blood pressure, mmHg<br>- `DBP` Diastolic blood pressure, mmHg<br>- `MAP` Mean arterial pressure, mmHg<br>- `Temp` Body temperature, degrees Fahrenheit<br>- `Perf` Mean last-minute perfusion index derived from the PPG waveform<br>- `Pain` Self-reported pain rating, 0 (no pain) to 10 (worst pain)<br>- `LPM_O2` Flow rate of supplemental oxygen, liters per minute<br>- `1min_HRV` or `5min_HRV` Heart rate variability over the last 1 minute or 5 minutes, calculated as the standard deviation of the beat-to-beat RR interval of the ECG waveform over this period. | string | SpO2 |
| Value | Observation value | float | 100.0 |
| Time | Timestamp of the measurement. When underlying observations are made more frequently than once per minute, they are aggregated to the mean value over the 60 seconds preceding the timestamp. | string | 2247-05-09T06:40:42Z |

## Waveform Summary File
| Column Name | Description | Data Type | Sample Data |
|------------|-------------|------------|-------------|
| CSN | Visit identifier (Random ID mapped to original CSN) | int | 99633476 |
| Type | One of 3 waveforms:<br>- `II` Electrocardiogram<br>- `Pleth` Photoplethysmogram<br>- `Resp` Respiration | string | Pleth |
| Segments | The number of waveform segments | int | 1 |
| Duration | The total duration for all segments for the waveform type, in seconds | float | 119.984 |

## Waveforms

| Type | Description | Common Uses |
|------|-------------|-------------|
| Electrocardiogram (ECG) | Records the voltage and timing of the heart's electrical activity | Diagnosis of myocardial injury, arrhythmias, electrolyte derangements; assessment of medication responses |
| Photoplethysmogram (Pleth/PPG) | Records changes in blood volume over time at the site of the sensor | Estimation of heart rate, respiratory rate, blood pressure, blood oxygen saturation |
| Respiration (Resp) | Estimates chest wall expansion and contraction | Estimation of respiratory rate, tidal volume, respiratory function |
