# 🧠 Participant Advisor Bot

An AI-powered assistant for equity management built with **FastAPI**, **Streamlit**, and **LLMs**. Supports hybrid reasoning: simple queries are handled via LLMs and complex ones via an agentic framework.

---

## 🚀 Features

- 🔐 Token-based authentication
- 📚 LLM-based defined query resolution
- 🧠 Agentic handling for undefined queries
- 🧾 Session-based memory per user
- 📊 Streamlit UI for participant interaction
- 🐳 Dockerized with `docker-compose`
- 📦 Dependency management via Poetry
- 🌱 `.env` support for secrets

---

## 📁 Project Structure

```
participant_advisor_bot/
├── backend/
    ├── main.py
    ├── agent/
    │   └── agentic_handler.py
    ├── api/
    │   └── advisor_router.py
    ├── auth/
    │   └── token_auth.py
    ├── data/
    │   ├── certent_client.py
    │   └── dummy_data.py
    ├── logic/
    │   ├── processing.py
    │   └── vesting.py
    ├── memory/
    │   └── session_store.py
    ├── models/
    │   ├── config.py
    │   └── query_model.py
    ├── services/
    │   ├── agentic_handler.py
    │   └── llm_agent.py
    ├── scripts/
    │   └── check_env.py
    ├── .gitignore
    ├── Dockerfile
    └── pyproject.toml
    └── requirements.txt    
├── frontend/
    └── streamlit_app.py
    └── .gitignore
    └── Dockerfile
    └── pyproject.toml
    └── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .dockerignore
```

---

## ⚙️ Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/participant-advisor-bot.git
cd participant-advisor-bot
```

### 2️⃣ Create and fill in `.env`
```bash
cp .env.example .env
# Edit with your own keys
```

### 3️⃣ Run with Docker Compose
```bash
docker-compose up --build
```

- FastAPI runs on: `http://localhost:8000`
- Streamlit UI on: `http://localhost:8501`

---

## 🧪 Sample API Request

```bash
curl -X POST http://localhost:8000/advisor/query \
 -H "Authorization: Bearer your-secret-key-here" \
 -H "Content-Type: application/json" \
 -d '{"user_id": "u1", "query": "How many grants do I have?"}'
```

---

## 🛠 Built With

- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)
- [Poetry](https://python-poetry.org/)
- [Docker](https://www.docker.com/)
- [OpenAI](https://platform.openai.com/) (LLM API)

---

## 🔒 Security

- Do not commit `.env` files. Use `.gitignore`
- Rotate secrets if exposed
- Use HTTPS in production

---

## 📄 License

MIT License. © 2025 Your Name or Company