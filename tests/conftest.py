import datetime

import pytest

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
