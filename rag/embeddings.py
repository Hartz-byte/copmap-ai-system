from sentence_transformers import SentenceTransformer

class EmbeddingModel:

    def __init__(self, model_path):
        self.model = SentenceTransformer(model_path)

    def embed(self, text):
        return self.model.encode([text])[0]
