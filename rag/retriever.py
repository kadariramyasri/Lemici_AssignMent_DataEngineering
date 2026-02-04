class Retriever:
    def __init__(self, vector_store, score_threshold: float = 0.35):
        self.vector_store = vector_store
        self.score_threshold = score_threshold

    def retrieve(self, query_embedding, top_k: int = 5):
        results = self.vector_store.search(query_embedding, top_k)

        filtered = [
            r for r in results
            if r["score"] >= self.score_threshold
        ]

        return filtered

