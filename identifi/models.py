from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.string(100), nullable=False)
    