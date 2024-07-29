FROM python:3.12-slim

RUN useradd appuser

WORKDIR /home/appuser

RUN apt-get update && \
    apt-get install -y libpq-dev gcc

# Set environment variables
ENV FLASK_APP=flask_app.py \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY flask_app.py config.py openapi.json requirements.txt ./
RUN pip install -r requirements.txt

COPY migrations migrations
COPY app app

RUN chown -R appuser:appuser ./

USER appuser