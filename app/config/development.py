from config import Config, basedir
import os


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or \
    f"sqlite:///{os.path.join(basedir, 'instance', 'classledger.db')}"