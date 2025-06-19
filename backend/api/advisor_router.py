from fastapi import APIRouter, Depends
from models.query_model import AdvisorQuery
from auth.token_auth import verify_token
from services.llm_agent import query_llm
# from services.agentic_handler import handle_agentic_query
from agent.agentic_handler import run_agentic_query



#TODO: add repsonse model

router = APIRouter()

@router.post("/query")
def handle_query(query: AdvisorQuery):
    if "grant" in query.query.lower():
        return {"response": query_llm(query.query)}
    else:
        return {"response": run_agentic_query(query.query)}