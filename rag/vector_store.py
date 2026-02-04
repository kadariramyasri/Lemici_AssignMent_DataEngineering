import faiss
import numpy as np

class VectorStore:
    def __init__(self, embedding_dim: int):
        self.index = faiss.IndexFlatIP(embedding_dim)
        self.texts = []

    def add(self, embeddings: np.ndarray, texts: list[str]):
        if len(embeddings) != len(texts):
            raise ValueError("Embeddings and texts length mismatch")

        self.index.add(embeddings)
        self.texts.extend(texts)

    def search(self, query_embedding: np.ndarray, top_k: int = 5):
        scores, indices = self.index.search(query_embedding, top_k)
        results = []

        for idx, score in zip(indices[0], scores[0]):
            results.append({
                "text": self.texts[idx],
                "score": float(score)
            })

        return results

