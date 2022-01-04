import os

db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')
db_password = os.environ.get('DB_PASSWORD')
db_port = os.environ.get('DB_PORT', default='5432')
db_user = os.environ.get('DB_USERNAME')

SQLALCHEMY_DATABASE_URI = f"postgres://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"