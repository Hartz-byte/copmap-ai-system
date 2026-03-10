# CopMap AI – Smart Surveillance Analysis System

## Overview

CopMap AI is an AI-powered surveillance analysis platform designed to assist police and city authorities in monitoring crowded public spaces, identifying potential risks, and generating patrol intelligence summaries.

The system combines computer vision, automated risk detection, and retrieval-augmented generation (RAG) to analyze surveillance images and provide actionable insights.

It performs the following tasks:

- Detects people, vehicles, and objects from surveillance images
- Analyzes crowd density in public areas
- Identifies suspicious objects such as unattended bags
- Generates automated alerts
- Calculates a location risk score
- Stores incident events in a vector database
- Produces AI-generated patrol summaries using a Large Language Model

The system exposes REST APIs through a FastAPI backend and includes a lightweight Streamlit dashboard for interactive testing.

---

## Task Requirements (Provided Problem Statement)

The objective was to design a backend system capable of processing surveillance images and generating structured intelligence outputs.

### Requirements

1. Accept surveillance images as input.
2. Use object detection to identify people, vehicles, and suspicious objects.
3. Perform crowd analysis and determine crowd density levels.
4. Generate alerts when suspicious conditions are detected.
5. Produce structured outputs such as:
   - Crowd statistics
   - Suspicious object detection
   - Risk indicators
6. Store historical events for later analysis.
7. Generate natural-language summaries for patrol planning.

---

## System Architecture

The system follows a modular AI pipeline architecture.

```
Surveillance Image
|
v
Object Detection (YOLOv8)
|
v
Crowd Analysis
|
v
Alert Engine
|
v
Risk Scoring Engine
|
v
Event Storage (Vector Database)
|
v
RAG Retrieval
|
v
LLM Patrol Intelligence Summary
```

---

## Key Features

### 1. Object Detection

The system uses YOLOv8 for detecting objects in surveillance images.

Detected classes include:
- Person
- Car
- Motorcycle
- Backpack
- Suitcase
- Handbag
- Other common urban objects

Object detection enables further analysis such as crowd density and suspicious object identification.

---

### 2. Crowd Density Analysis

Crowd density is determined using the number of detected people.

Density classification:

| Person Count | Density |
|--------------|--------|
| 0 – 10 | LOW |
| 11 – 20 | MEDIUM |
| 21+ | HIGH |

This helps identify potentially overcrowded public areas.

---

### 3. Suspicious Object Detection

The system flags possible unattended objects such as:

- Backpacks
- Suitcases

If such objects appear in crowded areas, alerts are generated.

---

### 4. Automated Alert Engine

Alerts are generated when specific conditions occur:

- High crowd density
- Suspicious objects
- Weapon detection (if detected)
- Vehicle congestion

Example alerts:

- High crowd density detected
- Unattended bags detected
- Vehicle congestion detected

---

### 5. Risk Scoring Engine

Each analyzed scene receives a risk score.

The score considers:

- Crowd density
- Suspicious objects
- Weapons (if detected)
- Vehicle congestion

Example output:

```
risk_score: 5
risk_level: MEDIUM
```

Risk levels:

| Score | Level |
|------|------|
| 0 – 2 | LOW |
| 3 – 5 | MEDIUM |
| 6+ | HIGH |

---

### 6. Event Storage with Vector Database

All analyzed scenes are stored in a FAISS vector database.

Stored information includes:

- location
- timestamp
- detections
- crowd data
- alerts
- risk score

This allows historical retrieval and contextual analysis.

---

### 7. AI Patrol Intelligence Summaries

The system uses a RAG pipeline to generate patrol recommendations.

Components used:

- Sentence Transformers for embeddings
- FAISS for vector search
- Groq API (LLaMA 3.1 8B) for language generation

Example summary output:

```
Crowd situation: High density with 21 people detected.

Vehicle activity: Limited vehicle movement observed.

Security risks: Four unattended bags detected in a crowded area.

Patrol recommendation: Increase patrol presence and investigate unattended objects.
```

---

## Technology Stack

### Backend
- Python
- FastAPI
- Uvicorn

### Computer Vision
- YOLOv8 (Ultralytics)
- OpenCV

### AI / ML
- Sentence Transformers
- FAISS
- Groq API (LLM inference)

### Frontend
- Streamlit

---

## Project Structure

```
copmap-ai-system/
├── backend/
│   ├── main.py
│   └── config.py
├── cv_pipeline/
│   ├── detector.py
│   └── crowd_analysis.py
├── alerts/
│   ├── alert_engine.py
│   └── risk_engine.py
├── rag/
│   ├── embeddings.py
│   ├── vector_store.py
│   └── rag_pipeline.py
├── utils/
│   └── schemas.py
├── frontend/
│   └── app.py
├── data/
│   ├── images/
│   └── faiss.index
├── download_models.py
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone Repository

```bash
git clone <repository_url>
cd copmap-ai-system
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Download Models

```bash
python download_models.py
```

This downloads:

- YOLOv8 model
- Sentence Transformer embedding model

---

## Running the Application

### Start Backend API

```bash
uvicorn backend.main:app --reload
```

API will run at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

### Start Frontend Dashboard

```bash
streamlit run frontend/app.py
```

Dashboard URL:

```
http://localhost:8501
```

---

## API Endpoints

### Analyze Surveillance Image

**POST** `/analyze`

Request

```json
{
  "image_path": "data/pic4.jpg",
  "location": "Sector D Market",
  "timestamp": "2026-03-10 18:20"
}
```

Response

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

### Generate Patrol Summary

**POST** `/summary`

Request

```json
{
  "query": "Provide patrol summary for Sector D"
}
```

Response

```json
{
  "summary": "High crowd density detected with unattended bags present..."
}
```

---

## Development Challenges

### 1. Detection Accuracy

Crowded scenes often contain occluded individuals and overlapping objects. This reduces object detection accuracy and requires careful threshold tuning.

### 2. LLM Hallucination

Language models sometimes generate incorrect counts or information. Prompt constraints and structured event data were used to reduce hallucination.

### 3. Resource Constraints

The system was designed to run on a local machine with:

- 16 GB RAM
- RTX 3050 GPU (4 GB VRAM)

Lightweight models such as YOLOv8n and YOLOv8s were selected to ensure compatibility.

### 4. Real-Time Performance

Maintaining acceptable inference speed while performing detection, alert generation, and vector storage required careful pipeline design.

---

## Possible Improvements

Future enhancements could include:

- Multi-camera video stream support
- Real-time event dashboards
- Face recognition integration
- Advanced anomaly detection models
- Temporal crowd tracking
- Heatmap visualization for high-risk zones

---

## Conclusion

CopMap AI demonstrates how modern AI technologies can assist law enforcement and city authorities in analyzing surveillance environments. By combining computer vision, automated alerts, vector databases, and language models, the system provides structured intelligence that can support patrol planning and public safety monitoring.

The modular architecture allows future expansion into larger surveillance and smart city monitoring platforms.