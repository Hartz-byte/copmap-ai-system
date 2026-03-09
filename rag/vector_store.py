import faiss
import numpy as np
import json
import os
from pathlib import Path

class VectorStore:
    def __init__(self, dimension=384, index_path="data/faiss.index", meta_path="data/metadata.json"):
        self.index_path = index_path
        self.meta_path = meta_path
        self.dimension = dimension
        
        # Ensure the data directory exists
        os.makedirs(os.path.dirname(self.index_path), exist_ok=True)

        # Load existing index if it exists, otherwise create new
        if os.path.exists(self.index_path) and os.path.exists(self.meta_path):
            print(f"Loading existing index from {self.index_path}...")
            self.index = faiss.read_index(self.index_path)
            with open(self.meta_path, 'r') as f:
                self.metadata = json.load(f)
        else:
            print("Creating new FAISS index...")
            self.index = faiss.IndexFlatL2(self.dimension)
            self.metadata = []

    def add(self, vector, meta):
        self.index.add(np.array([vector]).astype("float32"))
        self.metadata.append(meta)
        self.save()

    def search(self, vector, k=3):
        D, I = self.index.search(np.array([vector]).astype("float32"), k)
        results = []

        for idx in I[0]:
            if idx != -1 and idx < len(self.metadata):
                results.append(self.metadata[idx])

        return results

    def save(self):
        """
        Persist the index and metadata to disk
        """
        # Save FAISS index
        faiss.write_index(self.index, self.index_path)
        
        # Save Metadata as JSON
        with open(self.meta_path, 'w') as f:
            json.dump(self.metadata, f)
            
        print(f"Index and Metadata successfully saved to {os.path.dirname(self.index_path)}")
