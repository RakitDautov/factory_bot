FROM python:3.11-slim

RUN mkdir /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY . /app

WORKDIR /app

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]

#CMD ["gunicorn", "factory_bot.wsgi:application", "--bind", "0:8000" ]