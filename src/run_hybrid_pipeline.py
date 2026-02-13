import os, sys, pandas as pd
import time

start_time = time.time()
sys.path.append(os.path.dirname(__file__))

from gateway_logic import rule_based_check
from hybrid_alert_manager import hybrid_alert_decision

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data", "processed", "ml_predictions.csv")
OUT = os.path.join(BASE, "data", "processed", "hybrid_alerts.csv")

df = pd.read_csv(DATA)
alerts = []
history = {}

for _, row in df.iterrows():
    pid = row["patient_id"]
    history.setdefault(pid, [])

    final = hybrid_alert_decision(
        rule_based_check(row),
        row["ml_anomaly"],
        history[pid]
    )

    if final:
        alerts.append({
            "patient_id": pid,
            "time_step": row["time_step"],
            "scenario": row["scenario"]
        })

pd.DataFrame(alerts).to_csv(OUT, index=False)
print("Hybrid alerts:", len(alerts))
end_time = time.time()
latency = end_time - start_time
print(f"Hybrid alert processing latency: {latency:.4f} seconds")