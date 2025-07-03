FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["sh", "-c", "alembic upgrade head && uvicorn routing.main:app --host 0.0.0.0 --port 8000 --reload"]