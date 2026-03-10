# Analyze Surveillance Image

**POST** `/analyze`

**Request**

```json
{
  "image_path": "data/example.jpg",
  "location": "Sector D Market",
  "timestamp": "2026-03-10 18:20"
}
```

**Response**

```json
{
  "location": "Sector D Market",
  "crowd": {
    "person_count": 21,
    "crowd_density": "HIGH"
  },
  "alerts": [
    "High crowd density detected",
    "Unattended bags detected"
  ],
  "risk": {
    "risk_score": 5,
    "risk_level": "MEDIUM"
  }
}
```

---

# Generate Patrol Summary

**POST** `/summary`

**Request**

```json
{
  "query": "Provide patrol summary for Sector D"
}
```

**Response**

```json
{
  "summary": "Crowd situation: High crowd density (21 people) detected. Vehicle activity: 9 cars, 1 motorcycle, and 1 car detected. Security risks: Unattended bags: 4 detected (including 3 backpacks and 1 suitcase). Risk score: 5 (MEDIUM risk level). Patrol recommendation: Increase patrol presence in Sector D to manage high crowd density and address unattended bag risks."
}
```