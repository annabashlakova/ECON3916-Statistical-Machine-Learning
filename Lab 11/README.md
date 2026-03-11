# Data Wrangling & Engineering Pipeline

## Objective
Engineer structural features and impute missing values in a chaotic HR economics dataset to produce a clean, regression-ready data pipeline for econometric modeling.

## Data
- **Source:** `messy_hr_economics.csv`
- **Tech Stack:** Python, pandas, statsmodels, missingno, category_encoders

## Methodology
- Conducted a full missing-value audit using `missingno` to visually map missingness patterns and classify them as Missing at Random (MAR) vs. Missing Completely at Random (MCAR)
- Implemented targeted imputation strategies based on missingness structure rather than blindly dropping rows
- Created dummy variables for categorical features and diagnosed perfect multicollinearity (the Dummy Variable Trap) by identifying that dummy columns summed to the constant
- Resolved multicollinearity by dropping a reference category using `drop_first=True`, restoring valid OLS estimation
- Compressed high-cardinality geographic data using Target Encoding via `category_encoders`, reducing dimensionality while preserving predictive signal
- Validated the cleaned pipeline by running OLS regression through `statsmodels` and confirming coefficient stability and valid inference tables

## Key Findings
- Missingness in the dataset was structurally driven (MAR), not random — blind listwise deletion would have introduced selection bias
- Retaining all dummy categories alongside a constant produced NaN coefficients, confirming the Dummy Variable Trap in practice
- Target Encoding successfully compressed geographic categories into a single continuous feature without significant information loss
- Final cleaned dataset passed all diagnostic checks and was ready for downstream econometric analysis
