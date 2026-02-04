def generate_response(prompt: str) -> str:
    """
    Mock LLM generator.
    Replace with real LLM call if needed.
    """

    # Simple heuristic-based fallback response
    if "No relevant historical agent responses" in prompt:
        return (
            "I’m sorry for the inconvenience. "
            "If you were charged twice, please share your billing details "
            "or transaction ID so we can investigate and resolve this promptly."
        )

    return (
        "Thank you for reaching out. "
        "We understand your concern regarding duplicate charges. "
        "Our support team will review your subscription billing and assist you further."
    )
