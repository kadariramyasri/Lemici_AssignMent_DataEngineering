from rag.prompt import build_prompt

query = "I was charged twice for my subscription"
retrieved = ["Poor charge also quality month"]

prompt = build_prompt(query, retrieved)

print(prompt)
