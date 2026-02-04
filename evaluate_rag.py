from rag.pipeline import RAGPipeline

CSV_PATH = "data/raw/customer_support_tickets.csv"
RESPONSE_COLUMN = "Resolution"

rag = RAGPipeline(CSV_PATH, RESPONSE_COLUMN)

test_queries = [
    "I was charged twice for my subscription",
    "My internet is not working",
    "I want to cancel my account",
    "Payment failed but money was deducted"
]

hit_count = 0
total_score = 0
total_retrieved = 0

for query in test_queries:
    result = rag.run(query)
    retrieved = result["retrieved_context"]

    if retrieved:
        hit_count += 1
        total_retrieved += len(retrieved)

print("Total test queries:", len(test_queries))
print("Queries with retrieved context:", hit_count)
print("Hit Rate:", hit_count / len(test_queries))
