#! /bin/bash

python3 manage.py makemigrations users

#python3 manage.py makemigrations bot_api

python3 manage.py migrate --no-input

python3 manage.py collectstatic --no-input

gunicorn factory_bot_r.wsgi:application --bind 0.0.0.0:8000
