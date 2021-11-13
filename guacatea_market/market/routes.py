from market import app
from flask import render_template
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
    
    return render_template('register.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login_page():
    return render_template('login.html')


"""
@app.route("/logout")
def logout_page():
    return redirect(url_for('home_page'))
"""
