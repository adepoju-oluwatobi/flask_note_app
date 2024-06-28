# __init__.py
from flask_sqlalchemy import SQLAlchemy
# Initialize SQLAlchemy
db = SQLAlchemy()


from .user import User
from .note import Note
