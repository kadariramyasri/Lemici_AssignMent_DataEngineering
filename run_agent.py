from agent.agent_controller import SupportAgent
from rag.pipeline import RAGPipeline

if __name__ == "__main__":
    # Instantiate RAG pipeline EXACTLY once
    rag_pipeline = RAGPipeline(
        csv_path = "data/raw/customer_support_tickets.csv",
        response_column="Resolution"   # this matches your dataset design
    )

    agent = SupportAgent(rag_pipeline=rag_pipeline)

    test_query = """I'm facing a problem with my GoPro Hero. The GoPro Hero is not turning on. It was working fine until yesterday, 
                    but now it doesn't respond.
                    1.8.3 I really I'm using the original charger that came with my GoPro Hero, but it's not charging properly.
                    """
    result = agent.decide_and_respond(test_query)

    print("\n[Agent Response]")
    print(result)
