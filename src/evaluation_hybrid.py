import os
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RULE_PATH = os.path.join(BASE_DIR, "data", "processed", "rule_based_alerts.csv")
HYBRID_PATH = os.path.join(BASE_DIR, "data", "processed", "hybrid_alerts.csv")
DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "simulated_patient_data_v2.csv")

data = pd.read_csv(DATA_PATH)


def evaluate(alerts_df, name):
    merged = data.copy()
    merged["predicted"] = 0

    if not alerts_df.empty:
        merged = merged.merge(
            alerts_df.assign(predicted=1),
            on=["patient_id", "time_step", "scenario"],
            how="left"
        )
        merged["predicted"] = merged["predicted_y"].fillna(0).astype(int)

    y_true = merged["anomaly_label"].astype(int)
    y_pred = merged["predicted"]

    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)

    print(f"\n{name} Evaluation")
    print("-" * 25)
    print(f"Precision : {precision:.3f}")
    print(f"Recall    : {recall:.3f}")
    print(f"F1-score  : {f1:.3f}")
    print(f"Alerts    : {int(y_pred.sum())}")


rule_alerts = pd.read_csv(RULE_PATH)
hybrid_alerts = pd.read_csv(HYBRID_PATH)

evaluate(rule_alerts, "Rule-Based")
evaluate(hybrid_alerts, "Hybrid")
