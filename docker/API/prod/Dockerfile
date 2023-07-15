FROM python:3.10

RUN apt-get update


WORKDIR /opt/API

COPY ./API/requeriments.txt .
RUN pip install --upgrade pip
RUN pip install -r requeriments.txt

COPY ./API .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]