# Aca estaran los formularios que haremos con flask_wtf y wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='Username')
    email = StringField('email')
    password_1 = PasswordField('password1')
    password_2 = PasswordField('password2')
    submit = SubmitField('Crear Cuenta')


class LoginForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')
    submit = SubmitField('submit')

