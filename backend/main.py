from fastapi import FastAPI
from api.advisor_router import advisor_router
from models.config import settings

app = FastAPI(title="Participant Advisor Bot")
app.include_router(advisor_router, prefix="/advisor")