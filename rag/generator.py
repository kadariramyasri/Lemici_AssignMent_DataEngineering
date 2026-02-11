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
        "We understand your concern "
        "Our support team will review your concern and assist you further."
    )


# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# def generate_response(prompt: str) -> str:
#     """
#     Real OpenAI LLM generator.
#     Uses GPT-4o-mini for cost efficiency.
#     """

#     try:
#         response = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[
#                 {"role": "system", "content": "You are a professional customer support assistant."},
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=0.3,  # Lower = safer
#             max_tokens=300
#         )

#         return response.choices[0].message.content.strip()

#     except Exception as e:
#         return f"Error generating response: {str(e)}"
