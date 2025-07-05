FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* ./

RUN poetry install

COPY . .

CMD ["sh", "-c", "poetry run python manage.py makemigrations && poetry run python manage.py migrate && poetry run python manage.py collectstatic --noinput && exec poetry run gunicorn django_service.wsgi --bind 0.0.0.0:8000"]