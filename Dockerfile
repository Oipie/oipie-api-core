# syntax=docker/dockerfile:1

FROM python:3.10-slim

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 8000
CMD [ "python3", "-m" , "gunicorn", "-b", "0.0.0.0:8000","src:create_app()"]