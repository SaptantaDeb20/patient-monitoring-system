import os
import sys

sys.path.append(os.path.dirname(__file__))

from ml_model import train_model, apply_model

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data", "raw", "simulated_patient_data_v2.csv")
OUT = os.path.join(BASE, "data", "processed", "ml_predictions.csv")

# Train model
model, scaler, feature_cols = train_model(DATA)

# Apply model
df = apply_model(model, scaler, feature_cols, DATA)

# Save results
os.makedirs(os.path.dirname(OUT), exist_ok=True)
df.to_csv(OUT, index=False)

print("ML predictions saved:", OUT)
