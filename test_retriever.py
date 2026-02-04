from rag.data_loader import load_agent_responses
from rag.embeddings import EmbeddingGenerator
from rag.vector_store import VectorStore
from rag.retriever import Retriever






if __name__ == "__main__":
        

    CSV_PATH = "data/raw/customer_support_tickets.csv"
    RESPONSE_COLUMN = "Resolution"

    # Load KB
    kb = load_agent_responses(CSV_PATH, RESPONSE_COLUMN)
    texts = kb[RESPONSE_COLUMN].tolist()

    # Embeddings
    embedder = EmbeddingGenerator()
    embeddings = embedder.generate(texts)

    # Vector store
    store = VectorStore(embedding_dim=embeddings.shape[1])
    store.add(embeddings, texts)

    # Retriever
    retriever = Retriever(store, score_threshold=0.35)

    query = "I was charged twice for my subscription"
    query_embedding = embedder.generate([query])

    results = retriever.retrieve(query_embedding, top_k=5)

    print("Filtered Results:")
    for r in results:
        print(f"Score: {r['score']:.4f} | Text: {r['text']}")

