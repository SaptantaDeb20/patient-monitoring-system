import numpy as np
import pandas as pd

def generate_patient_data(
    patient_id,
    scenario,
    duration_minutes=60,
    interval_sec=5,
    noise_prob=0.02
):
    steps = int((duration_minutes * 60) / interval_sec)

    # Patient-specific baselines
    hr_base = np.random.normal(75, 7)
    spo2_base = np.random.normal(97, 1)
    temp_base = np.random.normal(36.8, 0.3)

    hr = np.random.normal(hr_base, 4, steps)
    spo2 = np.clip(np.random.normal(spo2_base, 1, steps), 85, 100)
    temp = np.random.normal(temp_base, 0.2, steps)

    label = np.zeros(steps)

    if scenario == "deterioration":
        start = int(steps * 0.5)
        for i in range(start, steps):
            hr[i] += np.random.uniform(0.2, 0.6) * (i - start)
            spo2[i] -= np.random.uniform(0.02, 0.06) * (i - start)
            temp[i] += np.random.uniform(0.005, 0.02) * (i - start)
            label[i] = 1

    elif scenario == "emergency":
        start = int(steps * 0.7)
        hr[start:] = np.random.normal(135, 8, steps - start)
        spo2[start:] = np.random.normal(86, 2, steps - start)
        temp[start:] = np.random.normal(39.3, 0.4, steps - start)
        label[start:] = 1

    # Sensor noise
    for i in range(steps):
        if np.random.rand() < noise_prob:
            hr[i] += np.random.normal(0, 15)
        if np.random.rand() < noise_prob:
            spo2[i] -= np.random.normal(0, 5)
        if np.random.rand() < noise_prob:
            temp[i] += np.random.normal(0, 1)

    return pd.DataFrame({
        "patient_id": patient_id,
        "time_step": range(steps),
        "heart_rate": hr,
        "spo2": spo2,
        "temperature": temp,
        "anomaly_label": label,
        "scenario": scenario
    })
