from market import db
from market import bcrypt
from market import login_manager
from flask_login import UserMixin
from market.models import *

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    """
    Class that represents a user of the application

    The following attributes of a user are stored in this table:
        * username - username of the user
        * email - email address of the user
        * password_hash - hashed password (using bcrypt)
        * cash - budget of the user by default is 200

    REMEMBER: Never store the plaintext password in a database!
    """


    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String(60), nullable=False)
    cash = db.Column(db.Integer, nullable=False, default=200)
    items = db.relationship('Item', backref='owned_user', lazy=True, foreign_keys="[Item.owner]")
    artworks = db.relationship('Item', backref='author_user', lazy=True, foreign_keys="[Item.creator]")

    
    def __repr__(self):
        return f'User: {self.username}'
    
    @property
    def prettier_cash(self):
        if len(str(self.cash)) >= 4:
            return f' {str(self.cash)[:-3]},{str(self.cash)[-3:]}$'
        else:
            return f' {self.cash}$'

    @property
    def password(self):
        return self.password
    

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')


    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
    
    """ 
    Funciones para comprar items
    """
    def can_buy(self, item_obj):
        return self.cash >= item_obj.price
    
    def buy(self, item_obj):
        item_obj.owner = self.id
        self.cash -= item_obj.price
        item_obj.author_user.cash += item_obj.price
        db.session.commit()

    def can_buy_all(self, total_price):
        return self.cash >= int(total_price)
    
