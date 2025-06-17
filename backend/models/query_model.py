from pydantic import BaseModel

class AdvisorQuery(BaseModel):
    user_id: str
    query: str