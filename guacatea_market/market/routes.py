from Guacatea_Market.guacatea_market.market.models import User
from market import app
from flask import render_template, redirect, url_for, flash
from market.forms import RegisterForm, LoginForm

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    return render_template("market.html")


@app.route('/register', methods=["GET","POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        flash('Usuario registrado correctamente, ahora puedes iniciar sesión.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login_page():
    if form.validate_on_submit():
        if form.validate_on_submit():
            return redirect(url_for('login'))
    return render_template('login.html')


"""
@app.route("/logout")
def logout_page():
    return redirect(url_for('home_page'))
"""
