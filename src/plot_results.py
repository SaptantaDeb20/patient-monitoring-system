import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score, recall_score, f1_score

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ML_PATH = os.path.join(BASE, "data", "processed", "ml_predictions.csv")
HYBRID_PATH = os.path.join(BASE, "data", "processed", "hybrid_alerts.csv")
DATA_PATH = os.path.join(BASE, "data", "raw", "simulated_patient_data_v2.csv")

# Load data
ml = pd.read_csv(ML_PATH)
hybrid = pd.read_csv(HYBRID_PATH)
raw = pd.read_csv(DATA_PATH)

# --- ML metrics ---
y_true_ml = ml["anomaly_label"]
y_pred_ml = ml["ml_anomaly"]

ml_precision = precision_score(y_true_ml, y_pred_ml)
ml_recall = recall_score(y_true_ml, y_pred_ml)
ml_f1 = f1_score(y_true_ml, y_pred_ml)

# --- Hybrid metrics ---
raw["predicted"] = 0
raw.loc[
    raw.set_index(["patient_id", "time_step", "scenario"]).index.isin(
        hybrid.set_index(["patient_id", "time_step", "scenario"]).index
    ),
    "predicted"
] = 1

y_true_h = raw["anomaly_label"]
y_pred_h = raw["predicted"]

hy_precision = precision_score(y_true_h, y_pred_h)
hy_recall = recall_score(y_true_h, y_pred_h)
hy_f1 = f1_score(y_true_h, y_pred_h)

# --- Plot 1: Metric comparison ---
labels = ["Precision", "Recall", "F1-score"]
ml_scores = [ml_precision, ml_recall, ml_f1]
hy_scores = [hy_precision, hy_recall, hy_f1]

x = range(len(labels))

plt.figure()
plt.bar(x, ml_scores)
plt.bar(x, hy_scores)
plt.xticks(x, labels)
plt.ylim(0, 1)
plt.title("ML vs Hybrid Performance Comparison")
plt.ylabel("Score")
plt.legend(["ML", "Hybrid"])
plt.show()

# --- Plot 2: Alert count comparison ---
ml_alerts = int(y_pred_ml.sum())
hy_alerts = int(y_pred_h.sum())

plt.figure()
plt.bar(["ML Alerts", "Hybrid Alerts"], [ml_alerts, hy_alerts])
plt.title("Alert Count Comparison")
plt.ylabel("Number of Alerts")
plt.show()
