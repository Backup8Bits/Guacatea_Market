"""
This file (test_models.py) contains the unit tests for the models.py file.
"""
import datetime

from web.market.models.user import User


def test_new_user(new_user):
    """
    GIVEN a User model \n
    WHEN a new User is created \n
    THEN check the user, email, password_hash, authenticated, and active fields are defined correctly
    """

    assert new_user.email == 'patkennedy79@gmail.com'
    assert new_user.password_hash != 'KennedyRules'
    assert new_user.__repr__() == 'User: FlaskUser'
    assert new_user.is_authenticated
    assert new_user.is_active
    assert not new_user.is_anonymous

def test_setting_password(new_user):
    """
    GIVEN an existing User \n
    WHEN the password for the user is set \n
    THEN check the password is stored correctly and not as plaintext
    """
    new_user.password = 'MyNewPassword'
    assert new_user.password_hash != 'MyNewPassword'
    assert new_user.check_password('MyNewPassword')
    assert not new_user.check_password('MyNewPassword2')
    assert not new_user.check_password('FlaskIsAwesome')

def test_user_id(new_user):
    """
    GIVEN an existing User \n
    WHEN the ID of the user is defined to a value \n
    THEN check the user ID returns a string (and not an integer) as needed by Flask-WTF
    """
    new_user.id = 17
    assert isinstance(new_user.get_id(), str)
    assert not isinstance(new_user.get_id(), int)
    assert new_user.get_id() == '17'

def test_new_item(new_item):
    """
    GIVEN a Item model \n
    WHEN a new Item is created \n
    THEN check the name, price, description, date_posted fields are defined correctly
    """

    assert new_item.name == 'NewItem'
    assert new_item.price == 100
    assert new_item.description == 'Item Description'
    assert new_item.__repr__() == 'Item: NewItem'
    assert new_item.date_posted != datetime.datetime.now()
