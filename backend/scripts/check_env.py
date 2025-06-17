from models.config import settings

print("✅ Loaded configuration:")
print(f"OPENAI_API_KEY: {'✅' if settings.OPENAI_API_KEY else '❌'}")
print(f"SECRET_KEY: {'✅' if settings.SECRET_KEY else '❌'}")
print(f"ENVIRONMENT: {settings.ENVIRONMENT}")