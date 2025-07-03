FROM python:3.12-slim

WORKDIR /app

RUN pip install gunicorn==20.1.0

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

# Скопируйте entrypoint.sh и сделайте его исполняемым
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Укажите entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
