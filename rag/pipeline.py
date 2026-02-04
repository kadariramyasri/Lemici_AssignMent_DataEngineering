from rag.data_loader import load_agent_responses
from rag.embeddings import EmbeddingGenerator
from rag.vector_store import VectorStore
from rag.retriever import Retriever
from rag.prompt import build_prompt
from rag.generator import generate_response


class RAGPipeline:
    def __init__(self, csv_path: str, response_column: str):
        # Load knowledge base
        self.kb = load_agent_responses(csv_path, response_column)
        self.texts = self.kb[response_column].tolist()

        # Initialize components
        self.embedder = EmbeddingGenerator()
        self.embeddings = self.embedder.generate(self.texts)

        self.vector_store = VectorStore(
            embedding_dim=self.embeddings.shape[1]
        )
        self.vector_store.add(self.embeddings, self.texts)

        self.retriever = Retriever(self.vector_store)

    def run(self, user_query: str) -> dict:
        # Embed query
        query_embedding = self.embedder.generate([user_query])

        # Retrieve context
        retrieved = self.retriever.retrieve(query_embedding)
        retrieved_texts = [r["text"] for r in retrieved]

        # Build prompt
        prompt = build_prompt(user_query, retrieved_texts)

        # Generate response
        response = generate_response(prompt)

        return {
            "query": user_query,
            "retrieved_context": retrieved_texts,
            "response": response
        }
