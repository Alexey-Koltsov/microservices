FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* ./

RUN poetry install

COPY . .


CMD ["sh", "-c", "poetry run alembic upgrade head && exec poetry run uvicorn routing.main:app --host 0.0.0.0 --port 8000 --reload"]
