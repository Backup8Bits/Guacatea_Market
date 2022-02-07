from flask import flash, redirect, render_template, url_for, request


from market import app
from market import db
from market.forms import LoginForm, RegisterForm, PurchaseItemForm, AddCartItemForm, RemoveCartItemForm
from market.models.user import User
from market.models.item import Item
from market.models.cart import Cart
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market', methods=["GET", "POST"])
def market_page():   
    purchase_form = PurchaseItemForm()
    cart_form = AddCartItemForm()
    if request.method == "POST":
        # Proceso de compra
        purchased_item = request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_buy(p_item_object):
                p_item_object.buy(current_user)
                flash(f"Congratulations! You purchased the '{p_item_object.name}' for {p_item_object.price}$", category='success')
            else:
                flash(f"Unfortunately, you don't have enough money to purchase the '{p_item_object.name}'", category='danger')
        # Proceso de agregar al carrito
        added_item = request.form.get('added_item')
        a_item_object = Item.query.filter_by(name=added_item).first()
        cart = Cart.query.filter_by(userid=current_user.id).first()
        if a_item_object:
            if cart.can_add_item(a_item_object):
                cart.add_item_to_cart(a_item_object)
                flash(f'You added the item: {a_item_object.name} to your cart successfully', category='success')
            else:
                flash(f"You already have the item in your cart.", category='info')
        

        return redirect(url_for('market_page'))

    if request.method == "GET":
        items = Item.query.filter_by(owner=None)
        return render_template("market.html",items=items, purchase_form=purchase_form, cart_form=cart_form)
        

@app.route('/register', methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email=form.email.data,
                              password=form.password_1.data,
                            )
        # item_to_create = Item(name='Remember the Night',
        #     price=100,
        #     description="Everything about the image is very fantastical and surreal and dreamlike, in fact, you get the idea that your soul might have died and gone to hell just for a second suddenly come back to life.",
        #     image='/static/img/items/img_4.jpg'
        #     )
        # db.session.add(item_to_create)

        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account created successfully! You are now logged in as {user_to_create.username}', category='success')
        # Cuando se crea un Usuario se crea un Carrito que tiene el id del Usuario esto lo hace único
        cart_to_create = Cart(userid=user_to_create.id)
        db.session.add(cart_to_create)
        db.session.commit()
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
    cart_form = RemoveCartItemForm()
    user_cart = Cart.query.filter_by(userid=current_user.id).first()
    return render_template('mycart.html', user_cart=user_cart, cart_form=cart_form)


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