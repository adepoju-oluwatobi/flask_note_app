from datetime import datetime

from . import db


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(225))
    note = db.Column(db.String(10000))
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key

    def __init__(self, title, note, user_id):
        self.title = title
        self.note = note
        self.user_id = user_id
