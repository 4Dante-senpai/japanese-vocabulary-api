FROM python:3.11-slim

RUN apt-get update && apt-get -y install libpq-dev gcc curl

WORKDIR /opt/API

COPY ./API/requeriments.txt .
RUN pip install --upgrade pip
RUN pip install -r requeriments.txt

COPY ./API .

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "--timeout", "600", "main:app"]