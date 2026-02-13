import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

FEATURES = ["heart_rate", "spo2", "temperature"]

def add_temporal_features(df, window=10):
    df = df.copy()

    for col in FEATURES:
        df[f"{col}_diff"] = df[col].diff().fillna(0)
        df[f"{col}_roll_mean"] = df[col].rolling(window).mean().fillna(df[col])
        df[f"{col}_roll_std"] = df[col].rolling(window).std().fillna(0)

    return df


def train_model(csv_path):
    df = pd.read_csv(csv_path)

    # Train ONLY on normal behavior
    normal = df[df["scenario"] == "normal"]

    normal = add_temporal_features(normal)

    feature_cols = [c for c in normal.columns if any(f in c for f in FEATURES)]
    X = normal[feature_cols]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = IsolationForest(
        n_estimators=200,
        contamination="auto",
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_scaled)

    return model, scaler, feature_cols


def apply_model(model, scaler, feature_cols, csv_path):
    df = pd.read_csv(csv_path)
    df = add_temporal_features(df)

    X = df[feature_cols]
    X_scaled = scaler.transform(X)

    preds = model.predict(X_scaled)
    df["ml_anomaly"] = (preds == -1).astype(int)

    return df

def apply_model_df(model, scaler, feature_cols, df):
    df = add_temporal_features(df)
    X = scaler.transform(df[feature_cols])
    df["ml_anomaly"] = (model.predict(X) == -1).astype(int)
    return df

