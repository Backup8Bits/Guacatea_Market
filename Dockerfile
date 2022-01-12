FROM python:3.9-buster

WORKDIR /opt/app
COPY guacatea_market .
RUN pip install -r requirements.txt


