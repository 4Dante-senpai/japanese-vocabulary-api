FROM python:3.11

RUN apt-get update


WORKDIR /opt/API

COPY ./API/requeriments.txt .
RUN pip install --upgrade pip
RUN pip install -r requeriments.txt

COPY ./API .

EXPOSE 5000

CMD ["python", "main.py"]
# CMD ["flask", "--app", "main.py", "run"]