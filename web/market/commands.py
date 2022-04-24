from market import app, db


@app.cli.command("create_db")
def create_db():
    db.create_all()
    print("The tables were created successfully")

@app.cli.command("drop_db")
def drop_db():
    db.drop_all()
    print("The tables were dropped successfully")
