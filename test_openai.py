from rag.generator import generate_response

prompt = """
User Query:
I was charged twice for my subscription.

Provide a helpful response.
"""

response = generate_response(prompt)

print("LLM Response:")
print(response)
