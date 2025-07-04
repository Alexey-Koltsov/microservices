#!/bin/sh

poetry run alembic upgrade head

exec poetry run uvicorn routing.main:app --host 0.0.0.0 --port 8000 --reload
