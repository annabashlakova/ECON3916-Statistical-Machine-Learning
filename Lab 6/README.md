## Lab 6: The Architecture of Bias  
**Investigating Data Generating Processes, Sampling Bias, and Experimental Integrity**

---

### Overview  
This lab analyzes how bias enters empirical analysis *before* any machine learning model is trained—through flawed sampling, broken randomization, and distorted data-generating processes (DGPs). Using the Titanic dataset as a controlled case study, the project demonstrates how sampling error, covariate shift, and experimental failures invalidate inference in both machine learning and applied economics.

---

### Objectives  
- Examine how sampling design affects statistical validity  
- Demonstrate the instability of finite-sample Simple Random Sampling  
- Eliminate covariate shift through stratified sampling  
- Perform forensic audits of A/B tests using Sample Ratio Mismatch (SRM) detection  
- Connect empirical bias to real-world economic and startup datasets  

---

### Tech Stack  
- **Python**  
- **pandas, numpy** – data manipulation and simulation  
- **scipy** – Chi-Square hypothesis testing  
- **scikit-learn** – stratified sampling and experimental controls  

---

### Methodology  

#### 1. Simple Random Sampling (SRS) Simulation  
- Manually implemented simple random sampling on the full Titanic dataset  
- Demonstrated high variance and unstable subgroup representation across samples  
- Showed how repeated SRS draws yield materially different survival estimates  

**Key insight:**  
Even unbiased sampling procedures can produce unreliable estimates in finite samples when subgroup proportions are not preserved.

---

#### 2. Stratified Sampling to Eliminate Covariate Shift  
- Implemented stratified sampling using passenger class (`pclass`)  
- Preserved population-level class distributions across train/test splits  
- Eliminated covariate shift between training and evaluation datasets  

**Key insight:**  
Stratification directly targets representation bias and improves internal validity and model generalization.

---

#### 3. Sample Ratio Mismatch (SRM) Forensic Audit  
- Applied Chi-Square tests to compare expected vs. observed group allocations  
- Used SRM detection to identify experimental integrity failures such as:
  - broken randomization
  - logging or instrumentation errors
  - treatment assignment leakage  

**Key insight:**  
SRM is not a modeling issue—it is an engineering failure signal. Any downstream inference is invalid until SRM is resolved.

---

## Theoretical Extension: Survivorship Bias and Ghost Data  

### Question  
**Why does analyzing only successful Unicorn startups (e.g., TechCrunch datasets) lead to Survivorship Bias, and what Ghost Data is required to fix it using a Heckman Correction?**

### Answer  

Restricting analysis to Unicorn startups introduces **Survivorship Bias** because the dataset is conditioned on *success*. Firms that failed, stagnated, or exited before reaching Unicorn status are systematically excluded. As a result, estimated relationships between firm characteristics and success conflate true causal effects with selection effects.

This bias occurs because inclusion in the dataset is **non-random** and correlated with unobserved factors such as founder quality, access to capital, or early network effects.

To correct this bias using a **Heckman Selection Model**, the required *Ghost Data* consists of:

- A dataset of **non-Unicorn startups**, including failed and non-observed firms  
- A **selection equation** modeling the probability of being observed (e.g., appearing on TechCrunch)  
- At least one **exclusion restriction** that affects selection into observation but not post-selection outcomes (e.g., media exposure, geography, or accelerator access)  

By explicitly modeling the selection process and incorporating this missing counterfactual population, the Heckman correction adjusts outcome estimates for non-random sample selection, restoring causal interpretability.

---

### Core Takeaway  
Bias is often introduced upstream—through data collection, sampling, and experimental design. No amount of model complexity can recover causal truth from a broken Data Generating Process.
