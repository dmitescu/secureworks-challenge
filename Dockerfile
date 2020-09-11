FROM debian:buster

RUN apt-get update -y
RUN apt-get install -y python3-pip

RUN mkdir /tmp/work
WORKDIR /tmp/work

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "manage.py", "runserver", "0:8000"]
