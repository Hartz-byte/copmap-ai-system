import os
from dotenv import load_dotenv

load_dotenv()

YOLO_MODEL_PATH = "models/yolo/yolov8s.pt"
EMBEDDING_MODEL_PATH = "models/embeddings/all-MiniLM-L6-v2"
VECTOR_DB_PATH = "data/faiss_index"
EVENT_LOG_PATH = "data/events.json"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
