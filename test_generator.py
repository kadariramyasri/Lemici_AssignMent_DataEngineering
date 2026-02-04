from rag.generator import generate_response





if __name__ == "__main__":
    
    sample_prompt = """
    User Query:
    I was charged twice for my subscription
    """

    response = generate_response(sample_prompt)
    print("Generated Response:")
    print(response)
