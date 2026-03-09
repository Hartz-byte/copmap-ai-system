def generate_alerts(detections, crowd_data):

    alerts = []
    vehicle_count = detections.count("car") + detections.count("truck")

    if crowd_data["crowd_density"] == "HIGH":
        alerts.append("High crowd density detected")

    if "knife" in detections or "gun" in detections:
        alerts.append("Possible weapon detected")

    if vehicle_count > 20:
        alerts.append("Vehicle congestion detected")

    return alerts
