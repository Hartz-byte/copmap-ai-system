import os
from pathlib import Path
from ultralytics import YOLO
from sentence_transformers import SentenceTransformer

def create_directories():
    """
    Create required model directories
    """
    base_dir = Path("models")
    yolo_dir = base_dir / "yolo"
    embed_dir = base_dir / "embeddings"

    yolo_dir.mkdir(parents=True, exist_ok=True)
    embed_dir.mkdir(parents=True, exist_ok=True)

    return yolo_dir, embed_dir


def download_yolo_models(yolo_dir):
    """
    Download YOLOv8n and YOLOv8s models
    """
    model_variants = ["yolov8n.pt", "yolov8s.pt"]
    
    for variant in model_variants:
        print(f"Checking/Downloading YOLO {variant}...")
        target_path = yolo_dir / variant

        model = YOLO(str(target_path)) 
        print(f"YOLO {variant} ready at: {target_path}")

def download_embedding_model(embed_dir):
    """
    Download SentenceTransformer embedding model
    """
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    save_path = embed_dir / "all-MiniLM-L6-v2"
    
    print(f"\nDownloading embedding model to {save_path}...")

    model = SentenceTransformer(model_name)

    model.save(str(save_path))

    print(f"Embedding model saved to: {save_path}")

def main():
    print("\nStarting model download process...\n")

    yolo_dir, embed_dir = create_directories()

    # Download YOLO models
    download_yolo_models(yolo_dir)

    # Download the embedding model
    download_embedding_model(embed_dir)

    print("\nAll models (YOLOv8n, YOLOv8s, and MiniLM) downloaded successfully!\n")

if __name__ == "__main__":
    main()
