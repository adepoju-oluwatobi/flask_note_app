from . import db
from datetime import datetime
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(225))
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(225), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.relationship('Note', backref='user', lazy=True)  # Relationship definition

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password
