def generate_alerts(detections, crowd_data):

    alerts = []
    vehicle_count = detections.count("car") + detections.count("truck")
    bag_count = detections.count("backpack") + detections.count("suitcase")

    if crowd_data["crowd_density"] == "HIGH":
        alerts.append("High crowd density detected")

    if "knife" in detections or "gun" in detections:
        alerts.append("Possible weapon detected")

    if bag_count > 0:
        alerts.append("Unattended bags detected")

    if vehicle_count > 20:
        alerts.append("Vehicle congestion detected")

    return alerts
