# Aca estaran los formularios que haremos con flask_wtf y wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from market.models import User

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password_1 = PasswordField('Password1', validators=[DataRequired(), Length(min=6)])
    password_2 = PasswordField('Password2', validators=[DataRequired(), EqualTo('password_1')])
    submit = SubmitField('Create Account')

    def validate_username(self, user_to_verify):
        user = User.query.filter_by(username=user_to_verify.data).first()
        # Si user es True entonces hay un usuario con ese nombre registrado
        if user:
            raise ValidationError('That username already exists. Try another one please')
    
    def validate_email(self, email_to_verify):
        email = User.query.filter_by(email=email_to_verify.data).first()
        if email:
            raise ValidationError('That email already exists. Try another one please')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign in')
