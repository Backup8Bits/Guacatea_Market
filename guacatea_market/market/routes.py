from flask import flash, redirect, render_template, url_for

from market import app
from market import db
from market.forms import LoginForm, RegisterForm
from market.models import Item, User
from flask_login import login_user, logout_user


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    return render_template("market.html")


@app.route('/register', methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email=form.email.data,
                              password=form.password_1.data,
                            )
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'You have an account now', category='success')
        return redirect(url_for('market_page'))

    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        user_to_verify = User.query.filter_by(username=form.username.data).first()
        # 1ro Verifica que el usuario exista
        # 2do Verifica que la contraseña sea correcta
        if user_to_verify and user_to_verify.check_password(
                                                attempted_password=form.password.data):
            login_user(user_to_verify)
            flash(f'You are logging now! Welcome {user_to_verify.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')
        
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('login.html', form=form)


@app.route("/logout")
def logout_page():
    logout_user()
    flash(f"You've been logged out now ", category='info')
    return redirect(url_for('home_page'))


@app.errorhandler(404)
def not_found(e):
  return render_template("404.html"), 404