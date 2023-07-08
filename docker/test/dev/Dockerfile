FROM python:3.10

RUN apt-get update


WORKDIR /opt/tests

COPY ./API/requeriments.txt .
RUN pip install --upgrade pip
RUN pip install -r requeriments.txt
RUN apt-get install nano

COPY ./tests .
# COPY ./tests .

# CMD [ "pytest", "--log-cli-level=DEBUG", "--capture=tee-sys", "-s" ]
# CMD [ "python", "-m", "unittest", "-v" ]
CMD [ "tail", "-f", "/dev/null" ]
