def build_prompt(user_query: str, retrieved_texts: list[str]) -> str:
    """
    Build prompt for LLM with safety and fallback handling.
    """

    if not retrieved_texts:
        context_block = (
            "No relevant historical agent responses were found.\n"
            "Provide a safe, polite, generic customer support response."
        )
    else:
        joined_context = "\n".join(
            f"- {text}" for text in retrieved_texts
        )
        context_block = (
            "You are given historical agent responses below.\n"
            "Use them ONLY if they are relevant and correct.\n\n"
            f"{joined_context}"
        )

    prompt = f"""
You are a customer support assistant.

Context:
{context_block}

User Query:
{user_query}

Instructions:
- Do NOT invent facts
- If context is weak, give a general helpful response
- Be polite, clear, and professional
- Do not mention internal systems or documents

Response:
""".strip()

    return prompt
