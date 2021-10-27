
import os

from dotenv import load_dotenv
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Configuración de la base de datos
# app.config['SQLALCHEMY_DATABASE_URI'] = ''
# app.config['SECRET_KEY'] = ''
# db = SQLAlchemy(app)

from market import routes
