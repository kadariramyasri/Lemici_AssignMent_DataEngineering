# Exploratory Data Analysis (EDA) – Customer Support Tickets

## Dataset Overview
The dataset contains customer support tickets with:
- Textual descriptions
- Ticket metadata
- Resolution details
- Customer satisfaction scores

Total records: ~8,400  
Target variable: `Ticket Priority`

---

## Data Quality Assessment

### Missing Values
- No critical missing values in target column
- Minor missing values in resolution-related fields

### Duplicates
- Some agent responses were exact duplicates
- These were retained as they reflect real-world operational behavior

### Anomalies
- Very short and very long ticket descriptions
- Negative or zero handling times filtered out where applicable

---

## Ticket Priority Distribution

Ticket priorities are **well balanced**:

- Medium ≈ 26%
- Critical ≈ 25%
- High ≈ 25%
- Low ≈ 24%

This confirms the dataset does not suffer from class imbalance.

---

## Text Analysis

### Message Length
- Average length ≈ 290 characters
- Long-tail distribution with some very verbose tickets

### Common Patterns
- Repeated templates in descriptions
- Polite phrasing even for critical issues
- Generic issue descriptions lacking urgency cues

---

## Resolution Time vs Priority

### Observation
~15% of Critical tickets were resolved faster than High priority tickets.

### Possible Explanations
- Critical tickets may bypass normal queues
- Dedicated escalation workflows
- Agent prioritization rules

### How to Investigate Further
- Compare agent assignment patterns
- Analyze escalation flags
- Check SLA-based routing rules

---

## Satisfaction Score Insights

### Billing Tickets
Billing-related tickets showed:
- Faster resolution times
- Lower customer satisfaction scores

### Hypothesis
Resolution speed does not equal resolution quality. Billing issues may:
- Involve refunds or disputes
- Leave customers unhappy despite quick closure

### Additional Data Needed
- Refund amount
- Resolution outcome type
- Customer follow-up actions

---

## Duplicate Agent Responses

### Observation
Some responses were exact duplicates.

### Impact on Analysis
- May artificially reduce text diversity
- Reflects realistic copy-paste operational behavior

### Decision
Duplicates were retained to preserve real-world patterns.

---

## Correlation Analysis

- Weak correlation between text length and priority
- Moderate correlation between sentiment and satisfaction
- No single feature strongly predicts priority

---

## Key Insights

1. Ticket priority is **not strongly determined by customer language**
2. Operational processes influence resolution more than text
3. Customer satisfaction depends on outcome quality, not speed alone
4. Priority prediction requires richer contextual and system-level data

---

## EDA Conclusion

The EDA highlights a fundamental limitation:
> Customer-generated text alone is insufficient to accurately infer ticket priority.

This insight directly informed the modeling strategy and explains the performance ceiling observed in Part 2.

