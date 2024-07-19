FROM python:3.12-slim

RUN useradd appuser

WORKDIR /home/appuser

# Set environment variables
ENV FLASK_APP=flask_app.py \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY app app
COPY flask_app.py requirements.txt ./
RUN pip install -r requirements.txt \
    && chown -R appuser:appuser ./

USER appuser