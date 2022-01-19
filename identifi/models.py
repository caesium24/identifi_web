from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password =

class Income(db.model):
    id = db.Column(db.Integer, primary_key=True)
    user_id =
    income_name = db.Column(db.String(50), nullable=False)
    income_type = db.Column(db.String(50), nullable=False)
    income_schedule = db.Column(db.String(50), nullable=False)
    income_dependants = db.Column(db.Float, nullable=True)
    income_deductions = db.Column(db.Float, nullable=True)
    income_net = db.Column(db.Float, nullable=True)

class Expense(db.model):
    id = db.Column(db.Integer, primary_key=True)
    user_id =
    exp_name = db.Column(db.String(50), nullable=False)
    exp_type = db.Column(db.String(50), nullable=False)
    exp_schedule = db.Column(db.String(50), nullable=False)
    exp_payment = db.Column(db.Float, nullable=True)

class Debt(db.model):
    id = db.Column(db.Integer, primary_key=True)
    user_id =
    debt_name = db.Column(db.String(50), nullable=False)
    debt_type = db.Column(db.String(50), nullable=False)
    debt_schedule = db.Column(db.String(50), nullable=False)
    debt_interest = db.Column(db.Float, nullable=True)
    debt_total = db.Column(db.Float, nullable=True)
    debt_payment = db.Column(db.Float, nullable=True)