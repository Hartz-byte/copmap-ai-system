def calculate_risk(detections, crowd_data):

    score = 0

    vehicle_count = detections.count("car") + detections.count("truck")
    bag_count = detections.count("backpack") + detections.count("suitcase")

    if crowd_data["crowd_density"] == "HIGH":
        score += 3
    elif crowd_data["crowd_density"] == "MEDIUM":
        score += 1

    if bag_count > 0:
        score += 2

    if "knife" in detections or "gun" in detections:
        score += 5

    if vehicle_count > 10:
        score += 1

    if score <= 2:
        level = "LOW"
    elif score <= 5:
        level = "MEDIUM"
    else:
        level = "HIGH"

    return {
        "risk_score": score,
        "risk_level": level
    }
