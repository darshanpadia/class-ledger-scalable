from flask import Flask
from app.extensions import db, migrate, csrf
import os

def create_app(config_class):
    app = Flask(__name__)

    app.config.from_object(config_class)

    # Initialize extentions
    db.init_app(app)
    migrate.init_app(app,db)
    csrf.init_app(app)

    # Import models *after* db is initialized
    from app.models import Teacher

    # Blueprints here

    return app