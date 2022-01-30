from flask import flash, redirect, render_template, url_for, request


from market import app
from market import db
from market.forms import LoginForm, RegisterForm, PurchaseItem
from market.models import Item, User
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market', methods=["GET", "POST"])
def market_page():   
    purchase_form = PurchaseItem()
    if request.method == "POST":
        purchased_item = request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_buy(p_item_object):
                p_item_object.buy(current_user)
                flash(f"Congratulations! You purchased the '{p_item_object.name}' for {p_item_object.price}$", category='success')
            else:
                flash(f"Unfortunately, you don't have enough money to purchase the '{p_item_object.name}'", category='danger')
        else:
            flash(f"We can't find the item '{p_item_object.name}' right now. Please try later.", category='error')
        return redirect(url_for('market_page'))

    if request.method == "GET":
        items = Item.query.filter_by(owner=None)
        return render_template("market.html",items=items, purchase_form=purchase_form)
        


@app.route('/register', methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email=form.email.data,
                              password=form.password_1.data,
                            )
        # item_to_create = Item(name='Lost in Translation',
        #     price=150,
        #     description="This is the image of a neighborhood in Venice is one of narrow, winding streets and canals, lined with beautiful old buildings and homes. It is a wonderfully romantic and picturesque area, and a popular tourist destination.",
        #     image='/static/img/items/img_5.jpg'
        #     )
        # db.session.add(item_to_create)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account created successfully! You are now logged in as {user_to_create.username}', category='success')
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

@app.route("/mycart")
@login_required
def cart_page():
    return render_template('mycart.html')
    
@app.route("/profile/<int:user_id>")
@login_required
def profile_page(user_id):
    user = User.query.filter_by(id=user_id).first()
    return render_template('profile.html', user=user)

@app.route("/logout")
@login_required
def logout_page():
    logout_user()
    flash(f"You've been logged out now ", category='info')
    return redirect(url_for('home_page'))


@app.errorhandler(404)
def not_found(e):
  return render_template("404.html"), 404