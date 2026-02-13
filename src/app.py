from flask import Flask, request, jsonify,render_template
import pandas as pd
import os, sys

sys.path.append(os.path.dirname(__file__))

from ml_model import train_model, apply_model_df
from gateway_logic import rule_based_check
from hybrid_alert_manager import hybrid_alert_decision

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)


BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data", "raw", "simulated_patient_data_v2.csv")

# -----------------------------
# Load model ONCE at startup
# -----------------------------
model, scaler, feature_cols = train_model(DATA)

# Per-patient ML history
history = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/predict", methods=["POST"])
def predict():
    payload = request.json

    # Convert JSON to DataFrame
    df = pd.DataFrame([payload])

    # ML prediction
    df = apply_model_df(model, scaler, feature_cols, df)

    pid = payload["patient_id"]
    history.setdefault(pid, [])

    rule_alert = rule_based_check(df.iloc[0])
    hybrid_alert = hybrid_alert_decision(
        rule_alert,
        int(df.iloc[0]["ml_anomaly"]),
        history[pid]
    )

    return jsonify({
        "patient_id": pid,
        "rule_alert": rule_alert,
        "ml_anomaly": int(df.iloc[0]["ml_anomaly"]),
        "hybrid_alert": hybrid_alert
    })




if __name__ == "__main__":
    app.run(debug=True)
