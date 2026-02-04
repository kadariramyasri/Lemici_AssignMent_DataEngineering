import pandas as pd

def load_agent_responses(csv_path: str, response_column: str) -> pd.DataFrame:
    """
    Load and clean historical agent responses for RAG knowledge base.
    """
    df = pd.read_csv(csv_path)

    if response_column not in df.columns:
        raise ValueError(f"Column '{response_column}' not found in dataset")

    kb = df[[response_column]].dropna()
    kb = kb[kb[response_column].str.len() > 20]
    kb = kb.reset_index(drop=True)

    return kb

