# Lemici_AssignMent_DataEngineering
Lemici Data Engineering assignment
## Part 3: LLM & RAG System

This project includes a Retrieval-Augmented Generation (RAG) system that suggests customer support responses based on historical agent replies.

### Features
- SentenceTransformer-based semantic embeddings
- FAISS vector database for similarity search
- Score-threshold filtering to avoid hallucinations
- Safe prompt engineering with fallback logic
- Modular, testable RAG pipeline

### How to Run
```bash
pip install -r requirements.txt
python test_pipeline.py
