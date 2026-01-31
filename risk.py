def spot_targets(entry):
    return {
        "tp1": round(entry * 1.004, 6),
        "sl": round(entry * 0.996, 6)
    }
