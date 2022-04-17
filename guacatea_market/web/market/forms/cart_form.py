from flask_wtf import FlaskForm
from wtforms import SubmitField

class AddCartItemForm(FlaskForm):
    submit = SubmitField('Add to Cart')

class RemoveCartItemForm(FlaskForm):
    submit = SubmitField('❌ Remove')