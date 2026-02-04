from rag.data_loader import load_agent_responses
from rag.embeddings import EmbeddingGenerator

if __name__ == "__main__":
    CSV_PATH = "data/raw/customer_support_tickets.csv"
    RESPONSE_COLUMN = "Resolution"

    kb = load_agent_responses(CSV_PATH, RESPONSE_COLUMN)

    texts = kb[RESPONSE_COLUMN].tolist()

    embedder = EmbeddingGenerator()
    embeddings = embedder.generate(texts)

    print("Total texts:", len(texts))
    print("Embeddings shape:", embeddings.shape)
    print("Sample embedding (first 5 values):", embeddings[0][:5])
