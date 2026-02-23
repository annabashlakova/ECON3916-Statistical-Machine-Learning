# Hypothesis Testing & Causal Evidence Architecture  
**The Epistemology of Falsification: Hypothesis Testing on the Lalonde Dataset**

## Overview
This project operationalizes the scientific method within a data science workflow by shifting the focus from *estimation* to *falsification*. Using the Lalonde (1986) job training dataset, the analysis adjudicates between competing causal narratives by systematically testing whether proposed effects can survive rigorous statistical refutation.

Rather than optimizing for model fit or predictive accuracy, the project prioritizes inferential discipline, robustness, and epistemic clarity.

---

## Objective
The primary objective is to demonstrate how causal claims should be evaluated through hypothesis testing rather than accepted through point estimates alone. The analysis pivots from “How large is the effect?” to the more fundamental question:

**Can the null hypothesis plausibly explain the observed data?**

This approach treats statistical inference as a tool for rejecting false explanations, not confirming convenient ones.

---

## Technical Approach
- Estimated the Average Treatment Effect (ATE) using **Welch’s T-Test**, explicitly accounting for unequal variances and heterogeneous earnings distributions.
- Evaluated the **signal-to-noise ratio** of the treatment effect to separate meaningful causal signal from sampling variability.
- Performed a **non-parametric permutation test** with 10,000 resamples to validate inference under minimal distributional assumptions.
- Cross-validated parametric and non-parametric results to guard against model-driven artifacts.
- Enforced strict hypothesis testing discipline, including explicit control of **Type I error**, to prevent false discoveries arising from data dredging or researcher degrees of freedom.
- Used SciPy’s statistical testing framework as an inference engine rather than a black-box estimator.

---

## Key Findings
The analysis identifies a statistically significant increase in post-training real earnings of approximately **$1,795**.  
The null hypothesis of no treatment effect is rejected via **statistical contradiction**, with consistent evidence across both parametric and non-parametric testing regimes.

This convergence strengthens causal credibility by demonstrating robustness to distributional assumptions.

---

## Business Insight
In modern data-driven organizations, hypothesis testing functions as the **safety valve of the algorithmic economy**.

Rigorous falsification:
- Prevents spurious correlations from being operationalized as business logic.
- Constrains data grubbing and post-hoc storytelling.
- Reduces model risk in high-stakes decision systems.
- Improves trust, auditability, and accountability in analytics pipelines.

By embedding falsification at the core of causal analysis, teams ensure that deployed insights reflect genuine structure in the data rather than retrospective pattern fitting.

---

## Takeaway
This project demonstrates how disciplined hypothesis testing transforms data science from pattern detection into **causal reasoning under uncertainty**—a prerequisite for responsible deployment in production environments.
