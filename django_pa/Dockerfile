FROM python:3.9.12-buster

ENV PYTHONUNBUFFERED=

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install psycopg

WORKDIR /app

COPY ./requirements.txt ./

run pip install -r requirements.txt

COPY . .