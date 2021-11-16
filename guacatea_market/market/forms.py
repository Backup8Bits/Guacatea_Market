# Aca estaran los formularios que haremos con flask_wtf y wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo

class RegisterForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password_1 = PasswordField('password1', validators=[DataRequired()])
    password_2 = PasswordField('password2', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField('Crear Cuenta')

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(message= u'La contraseña no puede estar vacía ')])
    submit = SubmitField('submit')