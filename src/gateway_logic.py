from config import HR_MAX, HR_MIN, SPO2_MIN, TEMP_MAX
import numpy as np

# Per-patient rolling history
_patient_history = {}


def rule_based_check(row, window=10, z_thresh=3.0):
    """
    Adaptive rule-based alerting using patient-specific baselines.
    Falls back to hard thresholds for safety.
    """

    pid = row["patient_id"]
    hr = row["heart_rate"]
    spo2 = row["spo2"]
    temp = row["temperature"]

    # Initialize history
    hist = _patient_history.setdefault(pid, {
        "hr": [],
        "spo2": [],
        "temp": []
    })

    # Always enforce hard safety limits
    if hr > HR_MAX or hr < HR_MIN:
        return True
    if spo2 < SPO2_MIN:
        return True
    if temp > TEMP_MAX:
        return True

    # Update history
    hist["hr"].append(hr)
    hist["spo2"].append(spo2)
    hist["temp"].append(temp)

    if len(hist["hr"]) > window:
        hist["hr"].pop(0)
        hist["spo2"].pop(0)
        hist["temp"].pop(0)

    # Not enough data yet
    if len(hist["hr"]) < window:
        return False

    # Adaptive z-score checks
    hr_z = abs((hr - np.mean(hist["hr"])) / (np.std(hist["hr"]) + 1e-6))
    spo2_z = abs((spo2 - np.mean(hist["spo2"])) / (np.std(hist["spo2"]) + 1e-6))
    temp_z = abs((temp - np.mean(hist["temp"])) / (np.std(hist["temp"]) + 1e-6))

    if hr_z > z_thresh or spo2_z > z_thresh or temp_z > z_thresh:
        return True

    return False
