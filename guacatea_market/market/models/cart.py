from market import db
from market.models import *


carts_items = db.Table('carts_items',
            db.Column('cart.userid', db.Integer, db.ForeignKey('cart.userid')),
            db.Column('item.id', db.Integer, db.ForeignKey('item.id'))
            ) 
            
class Cart(db.Model):
    userid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, primary_key=True)
    items = db.relationship('Item', secondary=carts_items, backref='carts') 

    def __repr__(self):
        return f'Cart N° {self.userid}'

    def can_add_item(self, a_item_object):
        return a_item_object not in self.items # Return True if the item is not added yet
    
    def add_item_to_cart(self, a_item_object):
        self.items.append(a_item_object)
        db.session.add(a_item_object)
        db.session.commit()
        
    def remove_item_from_cart(self, r_item_object):
        self.items.remove(r_item_object)
        db.session.commit()
    
    def get_total_price(self):
        return sum(item.price for item in self.items)
    
    def clear_all_cart(self):
        self.items.clear()
        db.session.commit()
        