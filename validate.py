import pandas as pd
df = pd.read_csv("simulated_patient_data_v2.csv")

print(df.groupby("scenario")["anomaly_label"].mean())
print(df.describe())
