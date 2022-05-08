from market import app, db
from market.models.item import Item


@app.cli.command("create_db")
def create_db():
    try:
        db.create_all()
        print("The tables were created successfully")
    except Exception as e:
        print("Something went wrong creating the tables")

@app.cli.command("drop_db")
def drop_db():
    try:
        db.drop_all()
        print("The tables were dropped successfully")
    except Exception as e:
        print("Something went wrong deleting the tables")


@app.cli.command("add_items")
def add_items():
    data = [
        ['La bella dama',100,
        'Este cuadro fue pintado en las llanuras de la Toscana',
        '/static/upload/122fsdfs.jpg'],
        ['El ogro enfermo', 120, 'Description',
        '/static/upload/122322fsdfs.jpg']
    ]
    for element in data:
        item = Item(name=element[0],price=element[1], description=element[2],
                    path_format=element[3])
        db.session.add(item)
        db.session.commit()
    print('Data was added successfully')
