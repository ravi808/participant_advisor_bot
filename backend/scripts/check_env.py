from models.config import settings

import secrets
from pathlib import Path

token = secrets.token_urlsafe(32)

# TODO: remove all emojis, looks like code copied from chatgpt

print("✅ Loaded configuration:")
print(f"OPENAI_API_KEY: {'✅' if settings.OPENAI_API_KEY else '❌'}")
print(f"SECRET_KEY: {'✅' if settings.SECRET_KEY else '❌'}")
print(f"ENVIRONMENT: {settings.ENVIRONMENT}")