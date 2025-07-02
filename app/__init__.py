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
    from app.auth.routes import auth_bp
    from app.dashboard.routes import dashboard_bp

    # Blueprints here
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)

    return app