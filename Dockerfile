# syntax=docker/dockerfile:1

FROM python:3.10-slim

WORKDIR /python-docker

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN pip install poetry==1.2.0

ENV FLASK_APP=src/app.py

RUN poetry config virtualenvs.create false
RUN poetry install --only main

COPY . .
RUN chmod +x ./scripts/entrypoint.sh
ENTRYPOINT [ "./scripts/entrypoint.sh" ]