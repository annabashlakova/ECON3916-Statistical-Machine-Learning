# Lab 7: The Engine of Interference  
**Modeling Correlated Financial Risk and Bankruptcy Dynamics**

## Overview  
This lab examines how **correlation between revenue and burn** changes a firm’s **Probability of Ruin**. Using Monte Carlo simulation, it shows why independence assumptions can **underestimate downside risk** when shocks cluster.

## Core Question  
How does introducing correlation between revenue and expenses change the likelihood of bankruptcy compared to a naïve independent model?

## Methodology  
- Simulated a firm’s cash balance over a **24-month** horizon  
- Ran **1,000** Monte Carlo paths per model  
- Compared two structures:
  1. **Independent Model**: revenue and burn drawn separately  
  2. **Correlated Model**: revenue and burn jointly drawn via a multivariate normal distribution  

## Model Parameters  
| Variable | Value |
|---|---:|
| Starting Cash | $2,000,000 |
| Mean Monthly Revenue | $80,000 |
| Revenue Std. Dev. | $30,000 |
| Mean Monthly Burn | $100,000 |
| Burn Std. Dev. | $10,000 |
| Correlation (ρ) | 0.7 |
| Time Horizon | 24 months |

## Key Result  
The **correlated model produces a higher Probability of Ruin** than the independent model.

### Why (Intuition)  
With **positive correlation**, bad revenue months tend to coincide with high burn, creating **larger negative cash-flow shocks**. This increases downside tail risk and accelerates cash depletion relative to independent draws.

## Technical Implementation  
- Python  
- NumPy (`multivariate_normal`)  
- Monte Carlo cash-flow simulation  
- **Bankruptcy condition**: cash ≤ 0 at any time in the horizon  

## Conceptual Takeaway  
Correlation is not a minor detail—it is an **engine of interference** that turns moderate volatility into compounded downside risk. Ignoring correlation leads to systematically optimistic runway estimates.

## Repository Structure  
- `Lab_7_The_Engine_of_Interference.ipynb` — simulation + analysis  
- `README.md` — overview + conclusions  

## Applications  
- Startup runway modeling  
- Solvency and credit-ris
