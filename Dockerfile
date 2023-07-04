#FROM ubuntu:latest
#LABEL authors="comp1"
#
#ENTRYPOINT ["top", "-b"]

#FROM test_app

#FROM python:3.7.9-slim-stretch

FROM python:3-alpine

RUN mkdir /app

COPY requirements.txt /app/

RUN python -m pip install -r /app/requirements.txt

COPY app.py /app/

WORKDIR /app

ENTRYPOINT ["python", "main.py"]