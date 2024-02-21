FROM python:3.12-slim

COPY ./app /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["bash", "-c", "uvicorn main:app --host 0.0.0.0 --port $UVICORN_PORT"]