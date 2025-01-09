# MC-MED Dataset README

## Overview
The Multimodal Clinical Monitoring in the Emergency Department (MC-MED) dataset provides a comprehensive, multimodal collection of de-identified emergency department (ED) patient visits from an academic medical center between 2020 and 2022. MC-MED combines rich clinical data (e.g., patient demographics, lab results, medication administrations, radiology reports) with continuous physiological signals (electrocardiogram [ECG], photoplethysmogram [Pleth/PPG], respiration), enabling in-depth research on ED care, patient trajectories, physiologic monitoring, and the impact of interventions.

The dataset includes:

* Tabular clinical data: Demographics, visits data, past medical history, orders, labs, medications, radiology results, and numeric vitals.
* Physiological waveform data: High-frequency ECG (II lead), PPG (Pleth), and respiration (Resp) segments recorded from continuous patient monitors.

A total of 118,385 adult ED visits are included, representing 70,545 unique patients, with a diverse demographic mix and variable acuity levels. For a subset of 83,623 visits, physiologic waveforms are available.

## Directory Structure
The MC-MED dataset is organized into the following directory structure, with all data files stored under a primary dataset directory:

```
./
├── labs.csv
├── meds.csv
├── numerics.csv
├── orders.csv
├── pmh.csv
├── rads.csv
├── split_chrono_train.csv
├── split_chrono_val.csv
├── split_chrono_test.csv
├── split_random_train.csv
├── split_random_val.csv
├── split_random_test.csv
├── visits.csv
├── waveform_summary.csv
├── waveforms_0xx.zip
├── waveforms_1xx.zip
├── waveforms_2xx.zip
├── waveforms_3xx.zip
├── waveforms_4xx.zip
├── waveforms_5xx.zip
├── waveforms_6xx.zip
├── waveforms_7xx.zip
├── waveforms_8xx.zip
└── waveforms_9xx.zip
```

## Top-Level Files

* **visits.csv**: Contains high-level visit information (e.g., patient age, sex, arrival method, chief complaint, disposition, timing of events).
* **pmh.csv** (Past Medical History): Documents patients' historical diagnoses (ICD-9/ICD-10 codes and descriptions).
* **meds.csv** (Home Medications): Lists patient home medications along with start/end dates and coded medication identifiers.
* **orders.csv**: Contains orders placed during the ED visit, including labs, imaging, medications, and their associated timestamps.
* **labs.csv**: Includes laboratory test results, component values, abnormal flags, and normal ranges.
* **rads.csv** (Radiology): Provides imaging study names and summarized impressions.
* **numerics.csv**: Contains minute-level numeric vitals recorded during the ED stay (HR, RR, SpO2, SBP, DBP, MAP, Temp, Perf, Pain, LPM_O2, 1min_HRV, 5min_HRV).
* **waveform_summary.csv**: Overview of available waveform segments (ECG, Pleth, Resp) for each visit, including total duration and segment count.
* **split_ files**: Predefined training/validation/test splits. Two types of splits are provided:
  * **split_random_*.csv**: A random 80/10/10 split by patient.
  * **split_chrono_*.csv**: A chronological split, ensuring no patient overlap between sets and that validation/test visits occur after training visits.

## Waveform Data
The data are organized into compressed archives (waveforms_0xx.zip, waveforms_1xx.zip, etc.) based on the last three digits of each Visit ID (CSN). Each ZIP archive extracts to a nested folder structure:

```
    {CSN_suffix}/              # Folder named by last three digits of the CSN
        {Full_CSN}/            # Folder named by the full CSN (visit identifier)
            II/                # ECG waveform segments
                {Full_CSN}_{segment_number}.dat
                {Full_CSN}_{segment_number}.hea
            Pleth/             # PPG waveform segments
                {Full_CSN}_{segment_number}.dat
                {Full_CSN}_{segment_number}.hea
                ...
            Resp/              # Respiration waveform segments
                {Full_CSN}_{segment_number}.dat
                {Full_CSN}_{segment_number}.hea
```

* **.dat and .hea Files**: The waveforms are stored in WFDB (WaveForm DataBase) format. Each segment consists of a header file (.hea) and a binary data file (.dat).
* **Segmenting**: Waveforms may be split into multiple segments due to discontinuities or equipment disconnections.

## Getting Started

### Data Access
* The main CSV files (visits, labs, etc.) can be read directly with standard data analysis tools (e.g., pandas in Python).
* The waveform data are stored as compressed archives. You will need to unzip them before accessing the WFDB files.

### Unzipping Waveforms (Optional)
Run a command like `unzip waveforms_0xx.zip` within the waveforms directory to extract waveform files. Repeat for each required archive. Note that the waveform data is large, so ensure sufficient storage space.

### Data Linkages
The primary key to link tables is:

* **CSN** (Visit identifier): Uniquely identifies a patient's ED visit. Use CSN to join visits.csv with labs.csv, orders.csv, rads.csv, and numerics.csv.
* **MRN** (Patient identifier): Identifies unique patients and can be used to link meds.csv and pmh.csv to patient-level information (e.g., multiple visits from the same patient).

Note: To respect patient privacy and prevent re-identification, MRN and CSN are randomized and do not map to original patient identifiers.

### Timestamps and De-identification
Times have been randomly shifted, while preserving the temporal order. This ensures that relative timing (e.g., order placed after arrival) remains correct, but absolute calendar dates do not match original data.

Patients over 90 are binned to age 90, and continuous numeric values are masked or shifted if they potentially contained identifying information.

### Train/Validation/Test Splits
Use the provided split_*.csv files to ensure reproducible training and evaluation without data leakage. The chosen split depends on your research question:

* **Random split**: Generally used for broad generalization.
* **Chronological split**: More realistic for testing temporal generalizability, as it simulates prospective evaluation.

## Usage Suggestions

* **Clinical Prediction Tasks**: Use waveform data alongside numeric vitals, labs, and order information to develop models for predicting ED disposition, adverse events, or diagnosing acute conditions.
* **Physiological Signal Processing**: Leverage the continuous ECG, Pleth, and Resp signals for advanced physiological analyses (e.g., arrhythmia detection, respiratory instability prediction).
* **Health Services Research**: Analyze visit-level data to understand patient flow, triage acuity distributions, resource utilization, and outcomes.

## Data Quality and Limitations

* **Data Gaps**: Some waveform segments are missing where patients were disconnected from monitors. The waveform_summary.csv file helps identify the total available segment durations.
* **De-identification Measures**: PII has been removed and timestamps shifted, which may limit certain types of temporal or longitudinal analyses.

## Additional Resources

* **WFDB Tools**: For reading waveform data, consider using the WFDB Python Package or other WFDB-compatible libraries.
* **Data Dictionary**: Refer back to the provided variable descriptions for details on column meanings and data formats.
