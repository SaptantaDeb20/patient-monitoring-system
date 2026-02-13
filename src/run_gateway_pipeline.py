import os, sys, pandas as pd
sys.path.append(os.path.dirname(__file__))

from gateway_logic import rule_based_check
from alert_manager import generate_alert

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data", "raw", "simulated_patient_data_v2.csv")
OUT = os.path.join(BASE, "data", "processed", "rule_based_alerts.csv")

df = pd.read_csv(DATA)
alerts = []

for _, row in df.iterrows():
    if rule_based_check(row):
        alerts.append(generate_alert(row))

pd.DataFrame(alerts).to_csv(OUT, index=False)
print("Rule-based alerts:", len(alerts))
