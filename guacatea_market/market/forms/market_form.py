from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired

class PurchaseItemForm(FlaskForm):
    submit = SubmitField('Buy article') 
class DeleteItemForm(FlaskForm):
    submit = SubmitField('Delete article') 

class SellItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    image = FileField('Choose file', validators=[
        
        FileAllowed(['png', 'jpg','jpeg'], "Wrong format. Try again!"),
        FileRequired()
        ])
    creator = StringField('Author')
    submit = SubmitField('Upload')

class BuyAllItemsForm(FlaskForm):
    submit = SubmitField('Proceed to Checkout')