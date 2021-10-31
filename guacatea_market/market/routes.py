from market import app
from flask import render_template


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/login')
def home_login():
    return render_template('login.html')


@app.route('/market')
def market_page():
    return render_template("market.html")


@app.route('/register', methods=["GET","POST"])
def register_page():
    return render_template('register.html')


@app.route('/login', methods=["GET", "POST"])
def login_page():
    return render_template('login.html')


"""
@app.route("/logout")
def logout_page():
    return redirect(url_for('home_page'))
"""
