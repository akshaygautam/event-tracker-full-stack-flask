from flask import Flask
from app.db import db
from app.config.config import DATABASE_URI
from app.routes import init_routes
from app.errors import init_error_handlers

def create_app():
    app = Flask(__name__, static_folder="../../frontend/build/static", template_folder="../../frontend/build")
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    
    db.init_app(app)

    with app.app_context():
        from app.models import Event  # Import the Event model to create tables
        db.create_all()
        init_routes(app)  # Initialize routes
        init_error_handlers(app)  # Initialize error handlers

    return app
