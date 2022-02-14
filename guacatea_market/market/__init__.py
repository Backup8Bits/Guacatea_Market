from dotenv import load_dotenv
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.utils import secure_filename

app = Flask(__name__, static_url_path='/static')
# Configuración de la base de datos
app.config[
    'SQLALCHEMY_DATABASE_URI'
        ] = 'postgresql://guacatea:guacatea@db:5432/guacatea'

app.config['SECRET_KEY'] = 'dfadc53023b12714ffe637bd2fad5fb3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Please login to the page if you want to access'
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'jpeg', 'jpg', 'png'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from market import routes
