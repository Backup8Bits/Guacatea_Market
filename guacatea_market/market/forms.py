# Aca estaran los formularios que haremos con flask_wtf y wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password_1 = PasswordField('Password1', validators=[DataRequired(), Length(min=6)])
    password_2 = PasswordField('Password2', validators=[DataRequired(), EqualTo('Password1')])
    submit = SubmitField('Crear Cuenta')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')