#!/bin/sh

python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic --noinput

exec gunicorn django_service.wsgi --bind 0.0.0.0:8000
