class SupportAgent:
    """
    Autonomous agent that orchestrates the RAG pipeline.
    Responsibilities:
    - Decide whether to search or escalate
    - Retry with reformulated query if needed
    - Track conversation history
    - Log reasoning steps
    """

    def __init__(self, rag_pipeline, max_retries: int = 2):
        self.rag_pipeline = rag_pipeline
        self.max_retries = max_retries
        self.history = []

        print("[Agent Initialized]")
        print(f"Using RAG pipeline: {type(rag_pipeline).__name__}")
        print(f"Max retries allowed: {self.max_retries}")

    def decide_and_respond(self, user_query: str) -> str:
        """
        Main agent loop:
        - Try RAG
        - Evaluate response confidence
        - Retry if needed
        - Escalate if all retries fail
        """

        print("\n[Agent Thinking]")
        print(f"User Query: {user_query}")

        self.history.append({"role": "user", "content": user_query})

        attempt = 0
        current_query = user_query

        while attempt <= self.max_retries:
            print(f"\n[Attempt {attempt + 1}]")
            print(f"Search Query: {current_query}")

            try:
                response = self._run_rag(current_query)
            except Exception as e:
                print(f"[Error] RAG pipeline failed: {e}")
                return "[ESCALATE] System error during knowledge retrieval."

            if self._is_confident_response(response):
                print("[Decision] Confident response generated")
                self.history.append({"role": "assistant", "content": response})
                return response

            print("[Decision] Response not confident enough")

            attempt += 1
            if attempt <= self.max_retries:
                current_query = self._reformulate_query(user_query)
                print("[Agent] Reformulating query and retrying...")

        print("[Decision] Max retries reached")
        return "[ESCALATE] Unable to confidently answer. Escalating to human agent."

    # ------------------ Helper Methods ------------------

    def _run_rag(self, query: str) -> str:
        """
        Calls the underlying RAG pipeline safely.
        """
        if hasattr(self.rag_pipeline, "run"):
            return self.rag_pipeline.run(query)
        elif hasattr(self.rag_pipeline, "generate"):
            return self.rag_pipeline.generate(query)
        else:
            raise AttributeError("RAG pipeline has no callable run/generate method")

    def _is_confident_response(self, response: str) -> bool:
        """
        Simple confidence heuristic.
        """
        if not response:
            return False
        if len(response.strip()) < 30:
            return False
        if "I don't know" in response.lower():
            return False
        return True

    def _reformulate_query(self, original_query: str) -> str:
        """
        Reformulates the query to improve retrieval.
        """
        return f"Customer support issue related to: {original_query}"

    def get_conversation_history(self):
        """
        Returns conversation memory (multi-turn support).
        """
        return self.history



