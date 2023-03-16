FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

COPY requirements.txt .
COPY app app

RUN pip install -r requirements.txt

ENV MODULE_NAME=app.main
ENV APP=app/main.py