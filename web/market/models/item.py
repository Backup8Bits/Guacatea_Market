import datetime

from market import db
from market.models import *


class Item(db.Model):
    """
    Class that represents a item of the application

    The following attributes of a item are stored in this table:
        * name - name of the item
        * price - price of the item (int)
        * description - description of the item
        * image - path where the item image is stored
        * date_posted - date & time that the item registered

    """

    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    image = db.Column(db.String, nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    owner = db.Column(db.Integer, db.ForeignKey('user.id'), default=None)
    creator = db.Column(db.Integer, db.ForeignKey('user.id'), default=None)

    def __repr__(self):
        return f'Item: {self.name}'

    @property
    def date_format(self):
        return self.date_format

    @date_format.setter
    def date_format(self, date_without_format):
        self.date_posted = date_without_format.strftime('%m/%d/%Y - %H:%M:%S')
