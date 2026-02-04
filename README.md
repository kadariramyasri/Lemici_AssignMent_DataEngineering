# L# Data Engineer Technical Assignment – Lemici IQ

This repository contains my solution for the **Lemici IQ – Data Engineer Technical Assignment**.  
The project focuses on exploratory data analysis, machine learning fundamentals, and the design of a safe and explainable Retrieval-Augmented Generation (RAG) system for customer support use cases.

---

## 📂 Project Structure

├── data/
│ ├── raw/
│ │ └── customer_support_tickets.csv
│ └── processed/
│
├── notebooks/
│ ├── EDA_Customer_Satisfaction.ipynb
│ └── Part_2_ML.ipynb
│ └── Part_3_ML.ipynb
│
├── rag/
│ ├── data_loader.py
│ ├── embeddings.py
│ ├── vector_store.py
│ ├── retriever.py
│ ├── prompt.py
│ ├── generator.py
│ └── pipeline.py
│
├── RAG_DESIGN.md
├── README.md
├── requirements.txt
└── test_*.py


---

## 🧪 Part 1: Exploratory Data Analysis (EDA)

- Performed data quality checks (missing values, duplicates, anomalies)
- Analyzed resolution times across ticket categories and priorities
- Conducted text analysis on customer messages
- Explored relationships between features and customer satisfaction
- Documented insights and critical thinking directly in the notebook

📁 **Notebook**: `EDA_Customer_Satisfaction.ipynb`

---

## 🤖 Part 2: Machine Learning Fundamentals

- Built a multi-class classifier to predict ticket priority
- Implemented and compared multiple models (e.g., Logistic Regression, Tree-based models)
- Applied text feature engineering techniques
- Evaluated models using appropriate metrics (accuracy, precision, recall, F1, confusion matrix)
- Performed hyperparameter tuning with justification
- Discussed business impact and model limitations

📁 **Notebook**: `Part_2_ML.ipynb`

---

## 🧠 Part 3: LLM & RAG System

This project includes a **Retrieval-Augmented Generation (RAG)** system that suggests customer support responses based on historical agent replies.

### 🔑 Key Design Choices
- Each historical agent response is treated as a **single semantic unit** (no chunking)
- SentenceTransformer (`all-MiniLM-L6-v2`) used for embedding generation
- FAISS used as a local vector database for similarity search
- Similarity score threshold applied to filter weak or noisy matches
- Safe prompt engineering to discourage hallucinations
- Fallback logic for queries with no relevant historical context

### 🏗️ RAG Pipeline Flow

User Query
↓
Query Embedding
↓
Vector Similarity Search (FAISS)
↓
Filtered Context Retrieval
↓
Prompt Construction
↓
LLM Response Generation


### ▶️ How to Run the RAG Pipeline

1. Install dependencies:
```bash
pip install -r requirements.txt

python test_pipeline.py

python evaluate_rag.py

### How to Run
```bash
pip install -r requirements.txt
python test_pipeline.

NOTE

A mock LLM generator is used to focus on RAG architecture, retrieval quality, and safety mechanisms.
This component can be easily replaced with an API-based or local open-source LLM without modifying the pipeline design.

Evaluation

Implemented basic retrieval evaluation metrics

Measured retrieval hit rate across representative test queries

Prioritized precision and safety over recall due to noisy historical data

Designed system to avoid hallucinations when confidence is low


Design Philosophy

Emphasis on explainability and safety

Conservative retrieval to prevent incorrect suggestions

Modular, testable, and extensible architecture

Practical handling of real-world data limitations

Future Improvements

Integrate a real LLM (OpenAI / Mistral / Llama)

Add re-ranking using cross-encoders

Improve knowledge base quality with ticket–response pairing

Add unit tests for critical RAG components

Expose the pipeline via a lightweight API (FastAPI)

Notes

This assignment prioritizes design reasoning and understanding over heavy frameworks

All major design decisions are documented in RAG_DESIGN.md

The solution is intentionally conservative to ensure correctness and trustworthiness


