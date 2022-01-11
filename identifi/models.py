from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.string(100), nullable=False)

class Income(db.model):
    id = db.Column(db.Integer, primary_key=True)
    income_name =
    income_type =
    income_schedule =
    income_dependants =
    income_deductions =
    income_net =
