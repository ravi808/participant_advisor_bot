FROM python:3.11-slim
WORKDIR /app/
COPY . /app
COPY pyproject.toml /app
RUN pip install requirements.txt
# RUN pip install poetry && poetry config virtualenvs.create false && poetry install
# COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]