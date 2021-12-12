from market import app
from flask import render_template, redirect, url_for, flash, request
from market.forms import RegisterForm, LoginForm
from market.models import User, Item
from market import db

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
                              password_hash=form.password_1.data,
                            )
        db.session.add(user_to_create)
        db.session.commit()
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
        flash(f'You are logging now!', category='success')
        return redirect(url_for('market_page'))
        
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('login.html', form=form)


"""
@app.route("/logout")
def logout_page():
    return redirect(url_for('home_page'))
"""
