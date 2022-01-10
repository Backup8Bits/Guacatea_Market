import datetime
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
    sex = db.Column(db.String, nullable=True, unique=False)
    address = db.Column(db.String, nullable=True, unique=False)
    items = db.relationship('Item', backref='owned_user', lazy=True)

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


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    # El autor tiene que tener una relacion con el user
    # author = db.Column(db.String, nullable=False, unique=True)
    image = db.Column(db.String(100), nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item: {self.name}'

    @property
    def date_format(self):
        return self.date_format
    
    @date_format.setter
    def date_format(self, date_without_format):
        self.date_posted = date_without_format.strftime('%m/%d/%Y - %H:%M:%S')

