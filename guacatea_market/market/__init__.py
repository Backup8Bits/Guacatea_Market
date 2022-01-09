from dotenv import load_dotenv
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__, static_url_path='/static')
# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://guacatea:guacatea@db:5432/guacatea'
app.config['SECRET_KEY'] = 'dfadc53023b12714ffe637bd2fad5fb3'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Please login to the page if you want to access'

from market import routes
