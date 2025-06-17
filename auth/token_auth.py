from fastapi import Header, HTTPException, Depends
from models.config import settings

def verify_token(authorization: str = Header(...)):
    if authorization != f"Bearer {settings.SECRET_KEY}":
        raise HTTPException(status_code=403, detail="Invalid or missing token")
    return True