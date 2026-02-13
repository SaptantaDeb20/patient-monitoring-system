import os
import pandas as pd

# Base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths
RULE_ALERTS_PATH = os.path.join(BASE_DIR, "data", "processed", "rule_based_alerts.csv")
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "simulated_patient_data_v2.csv")

# Load data
alerts = pd.read_csv(RULE_ALERTS_PATH)
data = pd.read_csv(RAW_DATA_PATH)

# Merge alerts with ground-truth labels
merged = alerts.merge(
    data,
    on=["patient_id", "time_step", "scenario"],
    how="left"
)

# Compute metrics
true_alerts = merged["anomaly_label"].sum()
false_alerts = len(merged) - true_alerts

print("Rule-Based Evaluation:")
print(f"True alerts (correct detections): {int(true_alerts)}")
print(f"False alerts (normal flagged): {int(false_alerts)}")
