from fastapi import APIRouter, Depends
from models.query_model import AdvisorQuery
from auth.token_auth import verify_token
from services.llm_agent import query_llm
from services.agentic_handler import handle_agentic_query

router = APIRouter()

@router.post("/query")
def handle_query(query: AdvisorQuery):
    if "grant" in query.query.lower():
        return {"response": query_llm(query.query)}
    else:
        return {"response": handle_agentic_query(query.query)}