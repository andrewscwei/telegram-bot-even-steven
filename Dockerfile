# Base target.
FROM python:3.10.3-slim AS base

ARG BUILD_NUMBER

ENV BUILD_NUMBER=$BUILD_NUMBER
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1

WORKDIR /var/app

RUN pip install pipenv

COPY Pipfile* ./

# Test target.
FROM base AS test

RUN pipenv install --system --deploy --dev

COPY main.py ./main.py
COPY app ./app
COPY tests ./tests

# Release target.
FROM base AS release

RUN pipenv install --system --deploy

COPY main.py ./main.py
COPY app ./app

CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 main:app
