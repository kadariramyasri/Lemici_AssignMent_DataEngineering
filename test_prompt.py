from rag.prompt import build_prompt



if __name__ == "__main__":
        

    query = "I was charged twice for my subscription"
    retrieved = ["Poor charge also quality month"]

    prompt = build_prompt(query, retrieved)

    print(prompt)
