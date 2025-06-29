from flask import Flask
from app.config import DevelopmentConfig
from app.extensions import db, migrate, csrf

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extentions
    db.init_app(app)
    migrate.init_app(app,db)
    csrf.init_app(app)

    return app