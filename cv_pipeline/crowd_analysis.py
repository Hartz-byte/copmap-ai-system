def analyze_crowd(detections):

    person_count = detections.count("person")

    if person_count <= 10:
        density = "LOW"
    elif 10 < person_count <= 20:
        density = "MEDIUM"
    else:
        density = "HIGH"

    return {
        "person_count": person_count,
        "crowd_density": density
    }
