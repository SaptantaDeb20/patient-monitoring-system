import time

def generate_alert(row):
    return {
        "patient_id": row["patient_id"],
        "time_step": row["time_step"],
        "alert_time": time.time(),
        "scenario": row["scenario"]
    }
