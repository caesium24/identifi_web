from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)

class Income(db.model):
    id = db.Column(db.Integer, primary_key=True)
    income_name = db.Column(db.String(50), nullable=False)
    income_type = db.Column(db.String(50), nullable=False)
    income_schedule = db.Column(db.String(50), nullable=False)
    income_dependants = db.Column(db.Float, nullable=True)
    income_deductions = db.Column(db.Float, nullable=True)
    income_net = db.Column(db.Float, nullable=True)
