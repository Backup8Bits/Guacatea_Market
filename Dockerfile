FROM python:3.8-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev build-base

WORKDIR /opt/app
COPY guacatea_market/requirements.txt .
RUN pip install -r requirements.txt