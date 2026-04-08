# Fraud Detection Model Evaluation — Metrics that Matter

## Objective

Evaluate a logistic regression fraud detector using decision-theoretic metrics — confusion matrices, Precision-Recall analysis, ROC curves, and threshold optimization — to expose the accuracy paradox and identify a business-relevant operating point on a severely imbalanced dataset.

## Methodology

- Loaded the Kaggle Credit Card Fraud Detection dataset (284,807 European transactions; 0.172% fraud prevalence) with PCA-anonymized features V1–V28 and transaction Amount
- Established a naive baseline classifier to demonstrate the accuracy paradox: 99.83% accuracy with zero fraud recall
- Trained a logistic regression model using scikit-learn and generated confusion matrices, classification reports, ROC curves, and Precision-Recall curves
- Computed ROC-AUC and PR-AUC to assess discriminative performance, with particular attention to PR-AUC as the more informative metric under extreme class imbalance
- Swept classification thresholds to identify the F1-optimal cutoff, showing that the default 0.5 boundary is suboptimal for rare-event detection
- Applied a capacity constraint (maximum 500 daily investigations) to translate model output into an actionable, resource-aware decision rule

## Key Findings

- **Accuracy paradox confirmed:** A trivial "predict no fraud" baseline achieves near-perfect accuracy yet catches zero fraudulent transactions, underscoring why accuracy alone is misleading under class imbalance.
- **Strong discriminative power:** Logistic regression produced a high ROC-AUC and meaningful PR-AUC on the minority class, indicating reliable separation between fraud and legitimate transactions despite the 580:1 class ratio.
- **Threshold sensitivity:** The F1-optimal threshold fell well below the default 0.5, reflecting the asymmetric cost structure inherent in fraud detection — false negatives carry far greater economic consequence than false positives.
- **Operationalized decision rule:** Imposing a 500-investigation daily cap yielded a principled operating point that balances fraud capture against investigative capacity, bridging the gap between statistical output and business deployment.

## Tech Stack

Python · scikit-learn · matplotlib · seaborn · pandas · NumPy
