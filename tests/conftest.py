import datetime

import pytest

from web.market import app, db
from web.market.models.item import Item
from web.market.models.user import User


@pytest.fixture(scope='module')
def new_user():
    user = User(username='FlaskUser',
                email='patkennedy79@gmail.com',
                password='KennedyRules')
    return user

@pytest.fixture(scope='module')
def new_item():
    item = Item(name='NewItem',
                price=100,
                description='Item Description',
                path_format='/opt/app/market/static/uploads/e57399e1133330ap.png',
                date_format= datetime.datetime.now()
               )
    return item

# Necesito una instancia prueba de la aplicación Flask para realizar estos tests

# @pytest.fixture(scope='module')
# def test_client():
#     flask_app = create_app('flask_test.cfg')

#     # Create a test client using the Flask application configured for testing
#     with flask_app.test_client() as testing_client:
#         # Establish an application context
#         with flask_app.app_context():
#             yield testing_client  # this is where the testing happens!

# @pytest.fixture(scope='module')
# def init_database(test_client):
#     # Create the database and the database table
#     db.create_all()

#     # Insert user data
#     user1 = User(username='FlaskUser',
#                 email='patkennedy79@gmail.com',
#                 password='KennedyRules')

#     user2 = User(username='SecondUser',
#                 email='something12@gmail.com',
#                 password='PaSsWoRd')

#     db.session.add(user1)
#     db.session.add(user2)

#     # Commit the changes for the users
#     db.session.commit()

#     yield  # this is where the testing happens!

#     db.drop_all()
