# from models.config import settings

# def query_llm(prompt: str) -> str:
#     return f"[LLM Response]: {prompt} (🔑 {settings.OPENAI_API_KEY[:1]}***)"


from data.dummy_data import defined_queries

def query_llm(prompt: str) -> str:
    for item in defined_queries:
        if item["query"].lower() in prompt.lower():
            return item["expected_response"]
    return "[LLM Stub] No mock response found for this query."
