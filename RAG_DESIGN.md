# RAG System Design
## 1. Chunking Strategy
The historical agent responses in the dataset are short (typically one or two sentences) and represent complete semantic units by themselves. Because of this, traditional document chunking would unnecessarily fragment coherent responses and reduce retrieval quality.

Therefore, each agent response is treated as a single atomic knowledge unit and embedded directly without chunking. This simplifies retrieval, preserves semantic meaning, and avoids introducing noise from overlapping chunks.

If chunking were applied with very small chunk sizes, important contextual meaning would be lost. If chunks were too large, embeddings would become less precise and retrieval quality would degrade. Given the data characteristics, no chunking was the optimal strategy.

## 2. Embedding Model Choice

The system uses the `all-MiniLM-L6-v2` sentence transformer model to generate embeddings. This model was chosen because it provides a strong balance between semantic accuracy, speed, and resource efficiency. It performs well for short-form text, which aligns with the structure of customer support agent responses in the dataset.

The model produces 384-dimensional normalized embeddings, making it suitable for cosine similarity–based retrieval while keeping memory and computation costs low.

To evaluate whether the embedding model works well for this domain, retrieval quality is assessed using manual inspection of top-k retrieved responses and similarity scores for representative customer queries. If semantically unrelated responses are frequently retrieved, it would indicate a mismatch between the embedding model and the domain. In a production setting, feedback from support agents and retrieval precision metrics would be used to further validate performance.

## 3. Retrieval and Re-ranking Strategy

The system initially retrieves the top-k most similar agent responses using cosine similarity over vector embeddings. However, not all retrieved results are suitable to be passed to the LLM.

A similarity score threshold is applied to filter out weak or noisy matches. Only responses whose similarity score exceeds this threshold are included in the final context. This acts as a lightweight re-ranking mechanism that prioritizes semantic relevance over quantity.

By limiting the LLM context to high-confidence matches, the system reduces the risk of hallucinations and prevents irrelevant or low-quality responses from influencing the generated answer. If no retrieved responses pass the threshold, the system intentionally provides no context to the LLM and falls back to a generic but safe response.

## 4. Handling Queries with No Relevant Historical Data

When a user query does not have any high-confidence matches in the vector database, the retrieval component returns an empty result set. Instead of forcing unrelated context into the prompt, the system explicitly detects this scenario.

In such cases, the prompt instructs the language model to generate a safe, generic customer support response without relying on historical data. This design choice prioritizes correctness and user trust over attempting to generate highly specific answers from weak or irrelevant context.

This fallback mechanism is critical for preventing hallucinations and ensures that the system behaves reliably even when the knowledge base has limited coverage.

## 5. Transformer Attention Mechanism

The transformer attention mechanism allows the model to understand a customer query by dynamically focusing on the most relevant words and their relationships rather than reading the text sequentially.

When a customer submits a query, attention helps the model determine which parts of the sentence are most important to each other. For example, in a query like “I was charged twice for my subscription,” the attention mechanism learns the strong relationship between “charged,” “twice,” and “subscription,” which together indicate a billing issue.

This mechanism enables the model to capture context, intent, and meaning even when queries are phrased differently. Unlike traditional models that rely on fixed word order or keywords, attention allows transformers to understand semantic relationships across the entire query simultaneously.



## 6. Embedding Model vs Language Model in RAG

The embedding model and the language model serve two different but complementary purposes in a RAG system.

The embedding model converts text into numerical vector representations that capture semantic meaning. These embeddings are used for similarity search, allowing the system to retrieve relevant historical responses from a vector database efficiently. Embedding models are optimized for comparison, not for generating text.

The language model (LLM), on the other hand, is responsible for understanding context and generating natural language responses. It does not perform retrieval by itself and does not have access to the knowledge base unless relevant information is explicitly provided in the prompt.

Both are needed in a RAG system because embeddings enable accurate and scalable retrieval, while the LLM uses the retrieved information to generate a coherent and helpful response. Without embeddings, retrieval would be inefficient. Without an LLM, the system could not generate flexible, human-like answers.

## 7. Handling LLM Contradictions and Hallucinations

LLMs may generate responses that contradict retrieved documents because they are probabilistic models trained to produce the most likely next tokens based on patterns learned during training. If the retrieved context is weak, ambiguous, or partially relevant, the model may rely more on its pretrained knowledge rather than the provided documents.

Another reason for contradictions is insufficient prompt guidance. If the prompt does not clearly instruct the model to prioritize retrieved context, the LLM may override it with general knowledge.

To mitigate this, the system applies multiple safeguards. First, low-confidence retrieved documents are filtered out using similarity score thresholds. Second, the prompt explicitly instructs the LLM to use retrieved context only if it is relevant and correct. Finally, a fallback mechanism is used when no strong context exists, ensuring the model produces a safe, generic response instead of hallucinating details.

## 8. LLM Inference Process (API-based Models)

When a request is sent to an LLM such as GPT-4 via an API, the input prompt is first tokenized into numerical representations. These tokens are passed through multiple transformer layers where self-attention and feed-forward networks process the input to build contextual understanding.

During inference, the model predicts the next token iteratively based on the input prompt and previously generated toke

## 9. Prompt Design and Explanation

The final prompt is structured to clearly separate context, user intent, and instructions to the language model.

The prompt begins by defining the role of the model as a customer support assistant, which sets the tone and expected behavior. Next, a context section is included, where retrieved historical agent responses are provided when available. The prompt explicitly instructs the model to use this context only if it is relevant and correct.

The user query is then presented clearly to ensure the model understands the exact issue being addressed. Finally, a set of instructions is included to discourage hallucination, enforce polite and professional language, and prevent the model from referencing internal systems or documents.

This structured prompt de

## 10. Handling Context Window Limitations

When the total retrieved context exceeds the model’s context window, the system prioritizes relevance over completeness. Instead of passing all retrieved documents, only the top-ranked responses with the highest similarity scores are included in the prompt.

A similarity score threshold is applied to remove weak matches, and the remaining results are capped to a fixed number (top-k

## 11. Techniques for Improving Response Quality

The primary technique used to improve response quality was clear and explicit prompt instructions rather than complex prompting strategies. The prompt explicitly discourages hallucination, instructs the model to rely on retrieved context only when relevant, and allows a safe fallback when context quality is low.

Few-shot examples and chain-of-thought prompting were intentionally avoided in this implementation to reduce prompt length and complexity, given the short and noisy nature of the historical agent responses. Structured output was also not required since the system’s goal was to generate natural language responses for customer support agents.

In a production setting, few-shot examples could be added for common issue types such as billing or account access to further improve consistency.

## 12. Production Bottlenecks and Optimization

The main bottlenecks in the system would be embedding generation, vector similarity search, and LLM inference latency. Embedding generation can be optimized by caching embeddings for repeated queries and precomputing embeddings for all knowledge base entries.

Vector search performance can be improved by using approximate nearest neighbor indexes, batching queries, or persisting the vector index to disk. LLM latency can be reduced by limiting context size, using smaller models where possible, and applying request batching.

At a scale of 1000 queries per day, the system would comfortably operate on modest infrastructure, but these optimizations would become important as traffic increases.


## 13. Debugging Incorrect or Harmful Responses

To debug an incorrect response, the first step would be to inspect the retrieved context and similarity scores used for that query. This helps determine whether the issue originated from poor retrieval or from the language model ignoring relevant context.

Additional data needed would include the user query, retrieved documents, prompt sent to the LLM, and the final generated response. Logging these components allows tracing errors end-to-end.

Based on the findings, fixes may include adjusting similarity thresholds, improving prompt instructions, filtering low-quality knowledge base entries, or retraining embeddings. Agent feedback would also be incorporated to continuously improve system reliability.

## 14. Evaluating RAG System Effectiveness

To evaluate whether the RAG system is helpful to support agents, both qualitative and quantitative metrics are important. Quantitative metrics include retrieval hit rate, average similarity score, and the percentage of responses accepted or edited by agents.

Qualitative feedback from agents is critical, including whether suggested responses save time, improve consistency, or reduce cognitive load. Tracking resolution time, escalation rates, and customer satisfaction before and after deployment would provide further insight.

Together, these metrics help determine whether the system delivers real operational value rather than just generating text.

## 14. Evaluating RAG System Effectiveness

To evaluate whether the RAG system is helpful to support agents, both qualitative and quantitative metrics are important. Quantitative metrics include retrieval hit rate, average similarity score, and the percentage of responses accepted or edited by agents.

Qualitative feedback from agents is critical, including whether suggested responses save time, improve consistency, or reduce cognitive load. Tracking resolution time, escalation rates, and customer satisfaction before and after deployment would provide further insight.

Together, these metrics help determine whether the system delivers real operational value rather than just generating text.
