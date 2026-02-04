from rag.pipeline import RAGPipeline




if __name__ == "__main__":
        

    CSV_PATH = "data/raw/customer_support_tickets.csv"
    RESPONSE_COLUMN = "Resolution"

    rag = RAGPipeline(CSV_PATH, RESPONSE_COLUMN)

    query = "I was charged twice for my subscription"
    result = rag.run(query)

    print("User Query:")
    print(result["query"])

    print("\nRetrieved Context:")
    for ctx in result["retrieved_context"]:
        print("-", ctx)

    print("\nFinal Suggested Response:")
    print(result["response"])
