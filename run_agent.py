from agent.agent_controller import SupportAgent
from rag.pipeline import RAGPipeline

if __name__ == "__main__":
    # Instantiate RAG pipeline EXACTLY once
    rag_pipeline = RAGPipeline(
        response_column="response"   # this matches your dataset design
    )

    agent = SupportAgent(rag_pipeline=rag_pipeline)

    test_query = "I was charged twice for my subscription"
    result = agent.decide_and_respond(test_query)

    print("\n[Agent Response]")
    print(result)
