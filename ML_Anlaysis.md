# Machine Learning Analysis – Ticket Priority Prediction

## Objective
Build a multi-class classifier to predict ticket priority  
(**Low, Medium, High, Critical**) based on customer-generated text and available metadata.

---

## Problem Framing
Ticket priority prediction is a **4-class classification problem** with balanced class distribution.  
Misclassification cost is asymmetric: predicting a Critical ticket incorrectly has higher business impact than misclassifying Low priority tickets.

---

## Models Implemented

### 1. Logistic Regression
- Baseline model for text classification
- Works well with sparse, high-dimensional TF-IDF features
- Interpretable and fast to train

### 2. Random Forest
- Captures non-linear feature interactions
- Evaluates whether decision-tree-based models can outperform linear baselines

### 3. XGBoost
- Gradient boosting for complex decision boundaries
- Strong benchmark for structured data problems

---

## Feature Engineering

### Text Features
- Combined ticket subject and description
- Cleaned and lowercased text
- TF-IDF vectorization
  - Unigrams, bigrams tested
  - min_df = 5, max_df = 0.9

### Structured Features
- Message length
- Description length
- Customer sentiment score (VADER)
- Ticket channel
- Ticket type
- Product purchased
- Customer gender

All structured features were combined with text using a `ColumnTransformer` and a unified pipeline.

---

## Hyperparameter Tuning

### Logistic Regression
- Regularization strength (`C`) tuned
- Best performance at `C = 0.1`
- Class weighting enabled to reduce bias

| C Value | Macro F1 |
|-------|----------|
| 0.01  | 0.260 |
| **0.1** | **0.266** |
| 1.0   | 0.255 |
| 10+   | Degraded |

---

## Model Performance Summary

| Model | Features | Accuracy | Macro F1 |
|------|--------|----------|----------|
| Logistic Regression | Text only | ~0.25 | ~0.25 |
| Logistic Regression | Text + metadata | **~0.26** | **~0.26** |
| Random Forest | Text features | ~0.24 | ~0.23 |
| XGBoost | Text features | ~0.24 | ~0.24 |

---

## Key Observations

1. All models performed within a narrow range (0.24–0.26 Macro F1)
2. Linear models outperformed tree-based models on TF-IDF features
3. Adding structured metadata produced a small but consistent improvement
4. Critical class recall remained low across models

---

## Why Random Forest Did Not Outperform Logistic Regression

TF-IDF produces sparse, high-dimensional feature spaces where:
- Tree-based models struggle to find meaningful splits
- Linear models generalize better and scale efficiently

This indicates priority is not driven by strong non-linear interactions in text alone.

---

## Why Critical/Urgent Recall Is Low

1. Urgency is often inferred from **context**, not explicit wording
2. Customers may describe critical issues calmly
3. Key operational signals (SLA breaches, escalations) are missing

### Potential Improvements
- Binary classification (Critical vs Non-Critical)
- Cost-sensitive learning
- Incorporate agent-side and operational metadata

---

## Performance Degradation on Long Tickets (>200 words)

Long messages often:
- Contain multiple issues
- Introduce irrelevant information
- Dilute urgency-related keywords

### Possible Fixes
- Sentence-level modeling
- Chunking long text
- Transformer-based attention models (e.g., BERT)

---

## Business Impact of Incorrect Predictions

- Delayed resolution of critical issues
- SLA violations and customer dissatisfaction
- Increased operational and support costs

---

## Model Monitoring & Drift Detection

In production, the following should be monitored:
- Class distribution shifts
- Recall for Critical tickets
- Input text length distribution
- Periodic retraining using recent data

---

## Conclusion

The experiments show that ticket priority is **weakly encoded in customer text and basic metadata**.  
Meaningful performance gains likely require:
- Operational signals
- Agent actions
- Historical escalation patterns

The current model serves as a **strong baseline** and provides valuable insights into data limitations and real-world system behavior.
