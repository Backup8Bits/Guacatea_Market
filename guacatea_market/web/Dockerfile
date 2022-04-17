FROM python:3.9-buster
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
# Run this command for the development server ans set DEBUG=0
# CMD python run.py
CMD flask create_db && gunicorn --bind 0.0.0.0:5000 -w 3 run:app

