
import os

from dotenv import load_dotenv
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__,
            static_url_path='', 
            static_folder='market/static')

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://guacatea:guacatea@localhost:5432/guacatea'
app.config['SECRET_KEY'] = 'dfadc53023b12714ffe637bd2fad5fb3'
db = SQLAlchemy(app)

from market import routes
