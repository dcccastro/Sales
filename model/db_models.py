from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Users %r>' % self.item

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

class Posts(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer(), primary_key=True)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    vehicle_id = db.Column(db.Integer(), db.ForeignKey("vehicles.id"), nullable=False)
    post_link = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text(), nullable=False)

    author_id = db.Column(db.Integer(),db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return '<Posts %r>' % self.item

    def __init__(self, created_at, vehicle_id, post_link, description, author_id):
        self.created_at = created_at
        self.vehicle_id = vehicle_id
        self.post_link = post_link
        self.description = description
        self.author_id = author_id

class Make(db.Model):
    __tablename__ = "make"
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    make_name = db.Column(db.String(20), unique=True, nullable=False)
    category = db.Column(db.Integer(), nullable=True)

    def __repr__(self):
        return '<Make %r>' % self.item

    def __init__(self, make_name, category):
        self.make_name = make_name
        self.category = category

class Vehicles(db.Model):
    __tablename__ = "vehicles"
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    make_id = db.Column(db.Integer(),db.ForeignKey("make.id"), nullable=False)
    model = db.Column(db.String(30), unique=True, nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    gear = db.Column(db.String(15), nullable=False)
    mileage = db.Column(db.Integer(), nullable=False)
    gas_type = db.Column(db.String(30), nullable=False)
    color = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return '<Vehicles %r>' % self.item

    def __init__(self, make_id, model, year, gear, mileage, gas_type, color):
        self.make_id = make_id
        self.model = model
        self.year = year
        self.gear = gear
        self.mileage = mileage
        self.gas_type = gas_type
        self.color = color
