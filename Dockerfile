# syntax=docker/dockerfile:1

FROM python:3.10-slim

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV FLASK_APP=src/app.py

COPY . .
RUN chmod +x ./scripts/entrypoint.sh
ENTRYPOINT [ "./scripts/entrypoint.sh" ]