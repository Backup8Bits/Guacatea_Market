from market import db
from market import bcrypt
from market import login_manager
from flask_login import UserMixin
from market.models import *

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String(60), nullable=False)
    cash = db.Column(db.Integer, nullable=False, default=200)
    items = db.relationship('Item', backref='owned_user', lazy=True, foreign_keys="[Item.owner]")
    artworks = db.relationship('Item', backref='author_user', lazy=True, foreign_keys="[Item.creator]")
    cart = db.relationship('Cart', backref='user_id', uselist=False)
    
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

    def can_buy(self, item_obj):
        return self.cash >= item_obj.price
    
    def buy(self, item_obj, u_to_pay):
        item_obj.owner = self.id
        self.cash -= item_obj.price
        u_to_pay.cash += item_obj.price
        db.session.commit()