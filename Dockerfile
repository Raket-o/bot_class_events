FROM python:3-alpine

RUN mkdir /app

COPY requirements.txt /app/

RUN python -m pip install -r /app/requirements.txt

COPY . /app/

WORKDIR /app

ENTRYPOINT ["python", "main.py"]