import os
import json
from fastapi import FastAPI
from backend.config import *
from cv_pipeline.detector import ObjectDetector
from cv_pipeline.crowd_analysis import analyze_crowd
from alerts.alert_engine import generate_alerts
from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore
from rag.rag_pipeline import RAGPipeline
from utils.schemas import ImageRequest, SummaryRequest


app = FastAPI()
detector = ObjectDetector(YOLO_MODEL_PATH)
embedding_model = EmbeddingModel(EMBEDDING_MODEL_PATH)
vector_store = VectorStore()
rag = RAGPipeline(vector_store, embedding_model, GROQ_API_KEY)


@app.get("/")
def health():
    return {"status": "CopMap AI running"}


@app.post("/analyze")
def analyze_image(req: ImageRequest):
    detections = detector.detect(req.image_path)
    crowd = analyze_crowd(detections)
    alerts = generate_alerts(detections, crowd)

    event = {
        "location": req.location,
        "timestamp": req.timestamp,
        "detections": detections,
        "crowd": crowd,
        "alerts": alerts
    }

    text_event = json.dumps(event)
    vec = embedding_model.embed(text_event)
    vector_store.add(vec, text_event)

    return event


@app.post("/summary")
def summary(req: SummaryRequest):
    result = rag.generate_summary(req.query)

    return {"summary": result}
