from pydantic import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    SECRET_KEY: str
    ENVIRONMENT: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()