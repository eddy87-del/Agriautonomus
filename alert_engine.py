ALERTS = []

def trigger_alert(level, message):
    ALERTS.append({
        "level": level,
        "message": message
    })

    print(f"[{level}] {message}")
