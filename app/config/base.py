import os

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret")
    SQLALCHEMY_TRACK_MODIFICATION = False