def hybrid_alert_decision(
    rule_alert,
    ml_anomaly,
    history,
    window=6,
    ml_ratio_threshold=0.7
):
    """
    rule_alert: bool
    ml_anomaly: 0 or 1
    history: list storing recent ml_anomaly values
    """

    # Always respect rule-based alerts
    if rule_alert:
        history.clear()
        return True

    # Update ML history
    history.append(int(ml_anomaly))
    if len(history) > window:
        history.pop(0)

    # Not enough data yet
    if len(history) < window:
        return False

    anomaly_ratio = sum(history) / window

    # Trigger alert if ML confidence is high
    if anomaly_ratio >= ml_ratio_threshold:
        history.clear()  # reset after alert
        return True

    return False
