import datetime
from market import db
from market.models import *

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    image = db.Column(db.String(100), nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))
    creator = db.Column(db.Integer, db.ForeignKey('user.id')) 
 
    def __repr__(self):
        return f'Item: {self.name}'

    @property
    def date_format(self):
        return self.date_format
    
    @date_format.setter
    def date_format(self, date_without_format):
        self.date_posted = date_without_format.strftime('%m/%d/%Y - %H:%M:%S')