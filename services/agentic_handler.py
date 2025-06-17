from logic.processing import smart_infer

def handle_agentic_query(query: str) -> str:
    return smart_infer(query)