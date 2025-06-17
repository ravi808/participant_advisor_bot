from fastapi import FastAPI
from api.advisor_router import router
from models.config import settings

app = FastAPI(title="Participant Advisor Bot")
app.include_router(router, prefix="/advisor")