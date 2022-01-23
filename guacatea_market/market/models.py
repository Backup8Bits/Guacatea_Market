from market import db
from market import bcrypt
from market import login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String(60), nullable=False)
    cash = db.Column(db.Integer, nullable=False, default=200)
    items = db.relationship('Item', backref='owned_user', lazy=True)
    

    @property
    def password(self):
        return self.password
    

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')


    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

class ProductItem(db.Model):
     __tablename__='products'
    id_2 = db.Column(db.Integer,primary_key=True)
    name_2 = db.Column(db.String(64),unique=True)
    descrip = db.Column(db.Text,unique=True,nullable=True)
    price = db.Column(db.Float,nullable=False)
    img = db.Column(db.String(64),unique=True)
    cartitems = db.relationship('CartItem', backref='Product')

    def __repr__(self):
            return '<ProductName %r>' % self.name_2

    class CartItem(db.Model):
    __tablename__='cartitems'
    id = db.Column(db.Integer,primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
