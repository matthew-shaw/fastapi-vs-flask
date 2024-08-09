FROM python:3.12-slim

RUN useradd appuser

WORKDIR /home/appuser

RUN apt-get update && \
    apt-get install -y libpq-dev gcc

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY alembic alembic
COPY app app

RUN chown -R appuser:appuser ./

USER appuser