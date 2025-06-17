FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml .
RUN pip install poetry && poetry config virtualenvs.create false && poetry install

COPY . .

CMD ["gunicorn", "main:app", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]