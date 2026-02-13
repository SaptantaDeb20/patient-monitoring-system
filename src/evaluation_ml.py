import os
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(BASE, "data", "processed", "ml_predictions.csv")

df = pd.read_csv(PATH)

y_true = df["anomaly_label"].astype(int)
y_pred = df["ml_anomaly"].astype(int)

precision = precision_score(y_true, y_pred, zero_division=0)
recall = recall_score(y_true, y_pred, zero_division=0)
f1 = f1_score(y_true, y_pred, zero_division=0)

print("ML Evaluation Metrics")
print("---------------------")
print(f"Precision : {precision:.3f}")
print(f"Recall    : {recall:.3f}")
print(f"F1-score  : {f1:.3f}")

print("\nCounts")
print("------")
print("True anomalies      :", int(y_true.sum()))
print("Predicted anomalies :", int(y_pred.sum()))
print("Correct detections  :", int(((y_true == 1) & (y_pred == 1)).sum()))
