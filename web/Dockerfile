FROM python:3.9-buster
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
# Run this command for the development server and set FLASK_DEBUG=1
# in env of the docker-compose
# CMD python run.py
# Use this for create tables and run the app
CMD flask create_db && gunicorn --bind 0.0.0.0:5000 -w 3 run:app
# Run this just for run the app and then you could run "flask create_db" in cli
# CMD gunicorn --bind 0.0.0.0:5000 -w 3 run:app
