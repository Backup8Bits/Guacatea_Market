from dotenv import load_dotenv
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


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


""" #######################
#### Configuration ####
#######################

# Create the instances of the Flask extensions (flask-sqlalchemy, flask-login, etc.) in
# the global scope, but without any arguments passed in.  These instances are not attached
# to the application at this point.

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Please login to the page if you want to access'
ALLOWED_EXTENSIONS = {'jpeg', 'jpg', 'png'}    

def create_app(test_config=None):

    app = Flask(__name__, static_url_path='/static')
    
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            UPLOAD_FOLDER=os.environ.get("UPLOAD_FOLDER")
        )
    else:
        app.config.from_mapping(test_config)
    
    # Initialize Plugins   
    initialize_extensions(app)
    from . import routes
    
    return app

##########################
#### Helper Functions ####
##########################

def initialize_extensions(app):
    # Since the application instance is now created, pass it to each Flask
    # extension instance to bind it to the Flask application instance (app)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    #Flask-Login configuration
    from market.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
 """

""" def register_blueprints(app):
    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)
    from market.auth import auth
    from market.ecommerce import ecommerce
    app.register_blueprint(auth)
    app.register_blueprint(ecommerce) """