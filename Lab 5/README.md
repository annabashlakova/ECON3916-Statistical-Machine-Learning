# Lab 5: The Architecture of Bias  
**Sampling Error, Covariate Shift, and Forensic Detection in Machine Learning**

## Overview  
This lab investigates how **data sampling choices distort inference** in machine learning and causal analysis. Using the Titanic dataset as a controlled environment, the project demonstrates how naïve sampling introduces bias, how stratification corrects it, and how **Sample Ratio Mismatch (SRM)** can be detected as an engineering failure in experimental pipelines.

The lab emphasizes that bias is not accidental — it is structural.

## Core Questions  
- Why does Simple Random Sampling generate unstable and misleading estimates?  
- How does Stratified Sampling correct Covariate Shift?  
- How can SRM reveal silent failures in A/B testing systems?

## Methodology  

### 1. Data Generating Process (DGP) Inspection  
- Loaded the full Titanic dataset as the population  
- Measured baseline survival rates and class distributions  
- Treated the full dataset as ground truth  

### 2. Simple Random Sampling (SRS) Simulation  
- Manually shuffled indices using NumPy  
- Drew samples without stratification  
- Observed high variance and unstable class proportions  
- Demonstrated sampling error as a function of randomness, not noise  

### 3. Stratified Sampling  
- Used `train_test_split` with stratification on passenger class (`pclass`)  
- Enforced stable class proportions across train/test splits  
- Eliminated Covariate Shift introduced by naïve sampling  

### 4. Sample Ratio Mismatch (SRM) Detection  
- Applied Chi-Square tests to compare expected vs. observed group ratios  
- Used SRM as a **forensic tool** to detect pipeline or assignment failures  
- Framed SRM as a diagnostic, not a statistical curiosity  

## Key Findings  
- Simple Random Sampling produces **high-variance estimates** even with large samples  
- Stratified Sampling stabilizes inference by preserving population structure  
- SRM reliably flags silent experimental failures that invalidate conclusions  

## Technical Stack  
- **Python**  
- **pandas**, **numpy**  
- **scipy.stats** (Chi-Square tests)  
- **scikit-learn** (Stratified Sampling)  
- **seaborn** (dataset access)  

## Conceptual Takeaway  
Bias enters systems **before models are trained**. Sampling is a design decision, and poor design produces confident but incorrect conclusions. Robust inference requires aligning samples with the true data-generating process.

## File Structure  
- `Lab_5 (1).ipynb` — full analysis, simulations, and diagnostics  
- `README.md` — conceptual framing and results  

## Applications  
- A/B testing integrity checks  
- ML pipeline validation  
- Causal inference under real-world data constraints  
- Diagnosing survivorship and selection bias  

