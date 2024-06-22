## Introduction
We are releasing Multimodal Clinical Monitoring in the Emergency Department (MC-MED), which is a comprehensive, multimodal, and de-identified clinical and physiological dataset. MC-MED includes 118,385 adult ED visits to an academic medical center from 2020 to 2022. The data includes continuously monitored vital signs, physiologic waveforms (electrocardiogram, photoplethysmogram, respiration), patient demographics, medical histories, orders, medication administrations, laboratory and imaging results, and visit outcomes. MC-MED is the first dataset to combine detailed physiologic monitoring with clinical events and outcomes for a large, diverse ED population. 

## Notebook

The included notebook demonstrates how to read and link the MCMED data to a given ED visit (specified by the corresponding CSN). 

To run the notebook, please make sure you have the following packages installed:

- plotly 5.19.0
- wfdb 4.1.2
- pandas 2.2.1

## Interact with our sample 

We have run this notebook on a data sample. You can interact with the cached output by downloading the notebook without rerunning it (so it doesn't wipe out the plots).