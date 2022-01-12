# Core libraries
import time

# Third libraries
import click
from dotenv import load_dotenv

# owner libraries
from market import app, db


@click.group()
def cli():
    pass


@cli.command()
def run_app():
    app.run("0.0.0.0")


@cli.command()
def migrate_db():
    for i in range(3):
        try:
            db.create_all()
            print("db created")
            break
        except Exception:
            time.sleep(5)
            print("Creating db")


load_dotenv()

# Checa si el run.py ha sido ejecutado directamente y no importado
if __name__ == '__main__':
    # PORT = int(os.getenv("FLASK_RUN_PORT", 5000))
    # HOST = os.getenv("FLASK_RUN_HOST", "0.0.0.0")
    # DEBUG = os.getenv("DEBUG", False)

    # app.run(host=HOST, port=PORT, debug=DEBUG)
    cli()
