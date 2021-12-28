FROM python:3.9-alpine

RUN apk update && \
    apk add postgresql-dev gcc python3-dev \
    musl-dev build-base libffi-dev

WORKDIR /opt/app
COPY guacatea_market .
RUN pip install -r requirements.txt


