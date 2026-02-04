from rag.data_loader import load_agent_responses





if __name__ == "__main__":
        

    CSV_PATH = "data/raw/tickets.csv"   # update if name is different
    RESPONSE_COLUMN = "agent_response"  # update this

    kb = load_agent_responses(CSV_PATH, RESPONSE_COLUMN)

    print("Total KB documents:", len(kb))
    print(kb.head(3))

