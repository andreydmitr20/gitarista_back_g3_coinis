#!/bin/bash
LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8
PYTHONPATH=/lib/
#alembic upgrade head
gunicorn -c ini.gunicorn.py --bind 0.0.0.0:8080 app:gunicorn_app
exec "$@"
