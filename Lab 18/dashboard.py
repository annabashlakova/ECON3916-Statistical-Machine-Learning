"""
Lab 18 — Interactive Fraud Detection Dashboard
================================================
Run with:  streamlit run dashboard.py

This dashboard extends the Lab 18 notebook with:
  Panel 1: Threshold slider → confusion matrix, Precision, Recall, F1, dollar cost
  Panel 2: Logistic Regression vs. Random Forest (ROC-AUC & PR-AUC side by side)
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    confusion_matrix, roc_curve, roc_auc_score,
    precision_recall_curve, auc,
    precision_score, recall_score, f1_score,
    ConfusionMatrixDisplay,
)

# ---------------------------------------------------------------------------
# Page configuration
# ---------------------------------------------------------------------------
st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")
st.title("Lab 18 — Fraud Detection: Threshold & Model Comparison Dashboard")

# ---------------------------------------------------------------------------
# Data loading and model training (cached so slider changes don't retrain)
# ---------------------------------------------------------------------------

@st.cache_resource(show_spinner="Loading data and training models (one-time)…")
def load_and_train():
    """
    Load the credit-card fraud dataset, split, scale, and train both a
    Logistic Regression and a Random Forest.  Results are cached via
    @st.cache_resource so they persist across Streamlit reruns triggered
    by slider/widget changes — only the first page load pays the cost.
    """
    # --- data -----------------------------------------------------------
    import kagglehub
    path = kagglehub.dataset_download("mlg-ulb/creditcardfraud")
    df = pd.read_csv(f"{path}/creditcard.csv")

    X = df.drop(columns=["Class", "Time"])
    y = df["Class"]

    scaler = StandardScaler()
    X["Amount"] = scaler.fit_transform(X[["Amount"]])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # --- Logistic Regression (same as notebook) -------------------------
    log_reg = LogisticRegression(max_iter=1000, random_state=42)
    log_reg.fit(X_train, y_train)
    y_prob_lr = log_reg.predict_proba(X_test)[:, 1]

    # --- Random Forest --------------------------------------------------
    rf = RandomForestClassifier(
        n_estimators=100, max_depth=12, random_state=42, n_jobs=-1
    )
    rf.fit(X_train, y_train)
    y_prob_rf = rf.predict_proba(X_test)[:, 1]

    return X_train, X_test, y_train, y_test, y_prob_lr, y_prob_rf, log_reg, rf


X_train, X_test, y_train, y_test, y_prob_lr, y_prob_rf, log_reg, rf = load_and_train()

# =========================================================================
# PANEL 1 — Threshold Explorer
# =========================================================================
st.header("Panel 1 — Threshold Explorer (Logistic Regression)")

st.markdown(
    """
    Drag the slider to change the classification threshold **τ**.
    Every widget change triggers a full Streamlit rerun, but because the
    models are cached the only work repeated is the lightweight metric
    computation below — so updates feel instant.
    """
)

# --- Sidebar controls ----------------------------------------------------
tau = st.slider(
    "Classification threshold (τ)",
    min_value=0.01, max_value=0.99, value=0.50, step=0.01,
    help="Transactions with P(fraud) ≥ τ are flagged as fraud.",
)

# Cost parameters — users can tweak these in the sidebar
st.sidebar.header("Cost Parameters")
st.sidebar.markdown(
    "Set the dollar cost of each error type. These drive the "
    "**Total Dollar Cost** metric."
)
cost_fn = st.sidebar.number_input(
    "Cost per missed fraud (FN)", value=500, min_value=0, step=50,
    help="Average loss when a fraud is NOT caught (chargeback + investigation).",
)
cost_fp = st.sidebar.number_input(
    "Cost per false alarm (FP)", value=25, min_value=0, step=5,
    help="Average cost of investigating a legitimate transaction flagged as fraud.",
)

# --- Compute metrics at chosen threshold ---------------------------------
y_pred_tau = (y_prob_lr >= tau).astype(int)
cm = confusion_matrix(y_test, y_pred_tau)
tn, fp, fn, tp = cm.ravel()

prec = precision_score(y_test, y_pred_tau, zero_division=0)
rec  = recall_score(y_test, y_pred_tau)
f1   = f1_score(y_test, y_pred_tau, zero_division=0)

# --- Dollar-cost metric --------------------------------------------------
# Total Cost = (number of missed frauds × cost per missed fraud)
#            + (number of false alarms × cost per false alarm)
#
# FN * cost_fn: each missed fraud costs the bank a chargeback / loss.
# FP * cost_fp: each false alarm costs manual investigation effort.
# The sum is the total expected cost at this operating point.
total_cost = fn * cost_fn + fp * cost_fp

# --- Display metrics in columns ------------------------------------------
c1, c2, c3, c4 = st.columns(4)
c1.metric("Precision", f"{prec:.2%}")
c2.metric("Recall", f"{rec:.2%}")
c3.metric("F1-Score", f"{f1:.3f}")
c4.metric("Total Dollar Cost", f"${total_cost:,.0f}")

st.markdown(f"**Flagged transactions:** {fp + tp:,}  |  "
            f"**Frauds caught:** {tp} / {tp + fn}  |  "
            f"**False alarms:** {fp:,}")

# --- Confusion matrix plot -----------------------------------------------
fig_cm, ax_cm = plt.subplots(figsize=(5, 4))
ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Legit", "Fraud"]).plot(
    ax=ax_cm, cmap="Blues", values_format=","
)
ax_cm.set_title(f"Confusion Matrix at τ = {tau:.2f}")
st.pyplot(fig_cm)

# --- Cost curve across all thresholds ------------------------------------
st.subheader("Dollar Cost & F1 vs. Threshold")

thresholds = np.arange(0.01, 0.99, 0.01)
costs, f1s = [], []
for t in thresholds:
    yp = (y_prob_lr >= t).astype(int)
    tn_t, fp_t, fn_t, tp_t = confusion_matrix(y_test, yp).ravel()
    # Same cost formula: FN * cost_fn + FP * cost_fp
    costs.append(fn_t * cost_fn + fp_t * cost_fp)
    f1s.append(f1_score(y_test, yp, zero_division=0))

fig_cost, ax1 = plt.subplots(figsize=(10, 5))

color_cost = "#dc2626"
color_f1   = "#16a34a"

ax1.plot(thresholds, costs, color=color_cost, linewidth=2, label="Total Dollar Cost")
ax1.set_xlabel("Threshold (τ)")
ax1.set_ylabel("Dollar Cost ($)", color=color_cost)
ax1.tick_params(axis="y", labelcolor=color_cost)

# Mark cost-minimizing threshold
best_cost_idx = int(np.argmin(costs))
best_cost_tau = thresholds[best_cost_idx]
ax1.axvline(best_cost_tau, color=color_cost, linestyle=":", alpha=0.7)
ax1.annotate(
    f"Min cost τ={best_cost_tau:.2f}\n${costs[best_cost_idx]:,.0f}",
    xy=(best_cost_tau, costs[best_cost_idx]),
    xytext=(best_cost_tau + 0.12, max(costs) * 0.7),
    arrowprops=dict(arrowstyle="->", color=color_cost),
    color=color_cost, fontsize=10,
)

# F1 on secondary axis
ax2 = ax1.twinx()
ax2.plot(thresholds, f1s, color=color_f1, linewidth=2, linestyle="--", label="F1-Score")
ax2.set_ylabel("F1-Score", color=color_f1)
ax2.tick_params(axis="y", labelcolor=color_f1)

best_f1_idx = int(np.argmax(f1s))
best_f1_tau = thresholds[best_f1_idx]
ax2.axvline(best_f1_tau, color=color_f1, linestyle=":", alpha=0.7)
ax2.annotate(
    f"Best F1 τ={best_f1_tau:.2f}\nF1={f1s[best_f1_idx]:.3f}",
    xy=(best_f1_tau, f1s[best_f1_idx]),
    xytext=(best_f1_tau + 0.12, f1s[best_f1_idx] - 0.15),
    arrowprops=dict(arrowstyle="->", color=color_f1),
    color=color_f1, fontsize=10,
)

# Mark currently selected threshold
ax1.axvline(tau, color="#2563eb", linewidth=2, alpha=0.5, label=f"Current τ = {tau:.2f}")

fig_cost.legend(loc="upper center", ncol=3, fontsize=10, bbox_to_anchor=(0.5, 1.02))
fig_cost.tight_layout()
st.pyplot(fig_cost)

# =========================================================================
# PANEL 2 — Model Comparison: Logistic Regression vs. Random Forest
# =========================================================================
st.header("Panel 2 — Model Comparison (Logistic Reg. vs. Random Forest)")

# --- ROC curves ----------------------------------------------------------
fpr_lr, tpr_lr, _ = roc_curve(y_test, y_prob_lr)
fpr_rf, tpr_rf, _ = roc_curve(y_test, y_prob_rf)
auc_lr = roc_auc_score(y_test, y_prob_lr)
auc_rf = roc_auc_score(y_test, y_prob_rf)

# --- PR curves -----------------------------------------------------------
prec_lr, rec_lr, _ = precision_recall_curve(y_test, y_prob_lr)
prec_rf, rec_rf, _ = precision_recall_curve(y_test, y_prob_rf)
pr_auc_lr = auc(rec_lr, prec_lr)
pr_auc_rf = auc(rec_rf, prec_rf)

col_left, col_right = st.columns(2)

# ROC plot
with col_left:
    fig_roc, ax_roc = plt.subplots(figsize=(6, 6))
    ax_roc.plot(fpr_lr, tpr_lr, linewidth=2, label=f"LogReg  (AUC={auc_lr:.4f})")
    ax_roc.plot(fpr_rf, tpr_rf, linewidth=2, label=f"RF       (AUC={auc_rf:.4f})")
    ax_roc.plot([0, 1], [0, 1], "k--", linewidth=1, label="Random (AUC=0.5)")
    ax_roc.set_xlabel("False Positive Rate")
    ax_roc.set_ylabel("True Positive Rate (Recall)")
    ax_roc.set_title("ROC Curve Comparison")
    ax_roc.legend(loc="lower right")
    st.pyplot(fig_roc)

# PR plot
with col_right:
    fig_pr, ax_pr = plt.subplots(figsize=(6, 6))
    ax_pr.plot(rec_lr, prec_lr, linewidth=2, label=f"LogReg  (PR-AUC={pr_auc_lr:.4f})")
    ax_pr.plot(rec_rf, prec_rf, linewidth=2, label=f"RF       (PR-AUC={pr_auc_rf:.4f})")
    baseline = y_test.mean()
    ax_pr.axhline(baseline, color="k", linestyle="--", linewidth=1,
                  label=f"Random (Prec={baseline:.4f})")
    ax_pr.set_xlabel("Recall")
    ax_pr.set_ylabel("Precision")
    ax_pr.set_title("Precision-Recall Curve Comparison")
    ax_pr.legend(loc="upper right")
    st.pyplot(fig_pr)

# --- Why PR-AUC matters more here ----------------------------------------
# For highly imbalanced data (0.17% fraud), ROC-AUC can look deceptively
# high because the x-axis (FPR) denominator is huge (284k negatives).
# A model that creates 1,000 false positives only moves FPR by 0.35%.
# PR-AUC does NOT use TN at all — it focuses entirely on how well the
# model performs on the minority class, making it a stricter and more
# informative metric when the positive class is rare.

st.markdown(
    """
    **Why PR-AUC is more informative than ROC-AUC for imbalanced data:**
    ROC-AUC can appear deceptively high because the FPR denominator
    (≈284k negatives) is enormous — even 1,000 false alarms barely move
    the FPR. PR-AUC ignores True Negatives entirely and focuses on how
    well the model performs *on the fraud class*, making it a stricter
    and more honest metric when positives are rare (0.17%).
    """
)

# --- AUC summary table ---------------------------------------------------
st.subheader("AUC Summary")
auc_df = pd.DataFrame({
    "Model": ["Logistic Regression", "Random Forest"],
    "ROC-AUC": [f"{auc_lr:.4f}", f"{auc_rf:.4f}"],
    "PR-AUC":  [f"{pr_auc_lr:.4f}", f"{pr_auc_rf:.4f}"],
})
st.table(auc_df)
