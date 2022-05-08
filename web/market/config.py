import os

from dotenv import load_dotenv

load_dotenv()
DEV_DB='sqlite:///market.db'

pg_user= os.environ.get('POSTGRES_USER')
pg_password=os.environ.get('POSTGRES_PASSWORD')
pg_db=os.environ.get('POSTGRES_DB')
pg_host='db'
pg_port=5432

PROD_DB = f'postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}'
