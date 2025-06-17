from models.config import settings

def query_llm(prompt: str) -> str:
    return f"[LLM Response]: {prompt} (🔑 {settings.OPENAI_API_KEY[:4]}***)"