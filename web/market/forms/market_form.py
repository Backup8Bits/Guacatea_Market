from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import IntegerField, StringField, SubmitField, TextAreaField
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
