from rag.data_loader import load_agent_responses
from rag.embeddings import EmbeddingGenerator
from rag.vector_store import VectorStore
import numpy as np



if __name__ == "__main__":
        

    CSV_PATH = "data/raw/customer_support_tickets.csv"
    RESPONSE_COLUMN = "Resolution"

    # Load KB
    kb = load_agent_responses(CSV_PATH, RESPONSE_COLUMN)
    texts = kb[RESPONSE_COLUMN].tolist()

    # Generate embeddings
    embedder = EmbeddingGenerator()
    embeddings = embedder.generate(texts)

    # Create vector store
    store = VectorStore(embedding_dim=embeddings.shape[1])
    store.add(embeddings, texts)

    # Test search
    query = "I was charged twice for my subscription"
    query_embedding = embedder.generate([query])

    results = store.search(query_embedding, top_k=3)

    print("Query:", query)
    for r in results:
        print(f"Score: {r['score']:.4f} | Text: {r['text']}")


