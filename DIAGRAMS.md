# DIAGRAMS.md

## Overview

This document contains the architectural and system diagrams used in the CopMap AI project. These diagrams explain how the system processes surveillance images, performs AI analysis, stores event data, and generates patrol intelligence summaries.

The goal is to clearly demonstrate the system design, data flow, and integration between computer vision, backend services, vector databases, and language models.

---

# 1. High-Level System Architecture

This diagram shows the major components of the CopMap AI system.

```
            Surveillance Image
                    |
                    v
          Object Detection Model
               (YOLOv8)
                    |
                    v
            Detection Results
     (persons, vehicles, objects)
                    |
                    v
           Crowd Analysis Module
                    |
                    v
             Alert Engine
                    |
                    v
             Risk Scoring Engine
                    |
                    v
             Structured Event
                    |
                    v
            Vector Embedding Model
      (Sentence Transformers - MiniLM)
                    |
                    v
              Vector Database
                    |
                    v
           RAG Retrieval Pipeline
                    |
                    v
             Large Language Model
              (LLaMA via Groq)
                    |
                    v
        Patrol Intelligence Summary
                    |
                    v
          Frontend Dashboard (Streamlit)
```

This architecture ensures modularity where each component can be upgraded independently.

---

# 2. Computer Vision Processing Pipeline

This diagram focuses on the AI processing performed on surveillance images.

```
         Input Image
              |
              v
      YOLOv8 Object Detector
              |
              v
       Detected Objects
--------------------------------
| Person | Car | Backpack | etc |
--------------------------------
              |
              v
        Crowd Analyzer
    (person counting logic)
              |
              v
       Crowd Density Label
    LOW / MEDIUM / HIGH
              |
              v
       Suspicious Object Check
     (bags / weapons detection)
              |
              v
            Alerts
```

Outputs produced by this stage:

- detected objects
- crowd statistics
- suspicious object indicators
- alerts

---

# 3. Alert Generation Logic

The alert engine analyzes detection results and crowd conditions.

```
    Detection Results
          |
          v
    Crowd Density Check
          |
  ----------------------
  |                    |

HIGH DENSITY NORMAL
| |
v v
Add Crowd Alert Continue
|
v
Suspicious Object Check
(backpack / suitcase)
|
----------------------
| |
Suspicious No Risk
| |
v v
Add Security Alert Continue
|
v
Final Alert List
```

Example alerts:


High crowd density detected
Unattended bags detected
Vehicle congestion detected


---

# 4. Risk Scoring Architecture

The risk scoring engine calculates a risk score based on scene conditions.

```
     Detection Results
            |
            v
    Crowd Density Score
  LOW = 0
  MEDIUM = 1
  HIGH = 3
            |
            v
    Suspicious Object Score
  Bag Detected = +2
            |
            v
     Weapon Detection Score
  Weapon Found = +5
            |
            v
     Vehicle Congestion Score
  High Vehicles = +1
            |
            v
         Total Score
            |
            v
    Risk Level Classification

   02  -> LOW
   32  -> MEDIUM
   6+   -> HIGH
```

Example output:

```
risk_score: 5
risk_level: MEDIUM
```

---

# 5. Event Storage and Vector Database

This diagram shows how analyzed events are stored and indexed for retrieval.

```
    Structured Event

(location, timestamp, detections)
|
v
Convert to JSON Text
|
v
Sentence Transformer Model
(MiniLM)
|
v
Vector Embedding
|
v
FAISS Index
|
v
Stored Event Metadata
```

Benefits:

- fast similarity search
- contextual retrieval
- scalable storage of historical events

---

# 6. Retrieval Augmented Generation (RAG)

The system uses a RAG pipeline to generate patrol intelligence summaries.

```
     User Query

"Summarize patrol risks"
|
v
Query Embedding
|
v
Vector Search
(FAISS)
|
v
Retrieve Relevant Events
|
v
LLM Prompt
(Events + Query Context)
|
v
Large Language Model
(LLaMA via Groq)
|
v
Patrol Intelligence Summary
```

The RAG system ensures summaries are grounded in real event data.

---

# 7. Backend API Architecture

The FastAPI backend exposes two main endpoints.

```
          Client
            |
    -------------------
    |                 |
    v                 v
  /analyze          /summary
    |                 |
    v                 v

CV Processing RAG Pipeline
| |
v v
Event JSON AI Summary
| |
-------------------
|
v
Response
```

API responsibilities:

- image analysis
- alert generation
- risk scoring
- vector storage
- patrol intelligence generation

---

# 8. Frontend Interaction Flow

The Streamlit dashboard provides an interface for testing the system.

```
    User Uploads Image
            |
            v
       Streamlit UI
            |
            v
    Analyze Scene Button
            |
            v
       /analyze API
            |
            v
  Detection + Risk Results
            |
            v
     Display on Dashboard
            |
            v
 Generate Patrol Summary Button
            |
            v
       /summary API
            |
            v
  AI Patrol Intelligence Output
```

---

# 9. Full End-to-End Data Flow

This diagram shows the complete data flow from image input to intelligence summary.

```
    Surveillance Image
            |
            v
     YOLOv8 Detection
            |
            v
    Crowd Density Analysis
            |
            v
    Alert Generation Engine
            |
            v
      Risk Score Engine
            |
            v
      Event JSON Record
            |
            v
    Vector Embedding Model
            |
            v
         FAISS DB
            |
            v
        RAG Retrieval
            |
            v
     Large Language Model
            |
            v

Patrol Intelligence Summary
|
v
Streamlit Dashboard
```

---

# Conclusion

These diagrams illustrate the modular architecture and AI pipeline used in the CopMap AI system.

The design emphasizes:

- modular AI components
- scalable event storage
- explainable risk indicators
- AI-assisted patrol intelligence

This architecture allows the system to evolve into a larger real-time surveillance intelligence platform for smart city and law enforcement applications.