from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    DEBUG = True
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI") or "default"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
