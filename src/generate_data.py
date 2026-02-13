import os
import pandas as pd
from sensor_simulator import generate_patient_data

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "data", "raw", "simulated_patient_data_v2.csv")

patients = []
pid = 1

# Normal patients
for _ in range(10):
    patients.append(generate_patient_data(pid, "normal"))
    pid += 1

# Deterioration patients
for _ in range(3):
    patients.append(generate_patient_data(pid, "deterioration"))
    pid += 1

# Emergency patients
for _ in range(2):
    patients.append(generate_patient_data(pid, "emergency"))
    pid += 1

df = pd.concat(patients, ignore_index=True)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
df.to_csv(OUT, index=False)

print("✅ simulated_patient_data_v2.csv regenerated")
print("Rows:", len(df))
