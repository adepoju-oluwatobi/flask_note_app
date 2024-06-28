from flask import Flask
from dotenv import load_dotenv
from flask_migrate import Migrate
import os
from models import db
from flask_login import LoginManager

# Import User model
from models.user import User

# Import routes
from routes.index import index
from routes.auth import auth
from routes.add_note import addNote
from routes.delete_note import deleteNote

# Create Flask app
app = Flask(__name__)

# Initialize Flask-Login for user authentication
login_manager = LoginManager()
login_manager.login_view = 'auth.user_login'
login_manager.init_app(app)

# Define user_loader callback for loading user from session
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


# Load environment variables from .env file
load_dotenv()

# Get SECRET_KEY from environment variables
secret_key = os.getenv("SECRET_KEY")

# Set the secret key for the Flask app
app.config['SECRET_KEY'] = secret_key

# Get database URL from environment variables
db_url = os.getenv("DATABASE_URL")

# Set database URI for SQLAlchemy to connect
app.config['SQLALCHEMY_DATABASE_URI'] = db_url

# Suppress SQLAlchemy modification tracking overhead
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database with the Flask app
db.init_app(app)

# Initialize Flask-Migrate for database migrations
migrate = Migrate(app, db)

# Register Blueprint routes
app.register_blueprint(index)
app.register_blueprint(auth)
app.register_blueprint(addNote)
app.register_blueprint(deleteNote)

# Run the Flask app if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
