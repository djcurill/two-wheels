from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ["DEV_DATABASE_URI"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ["TEST_DATABASE_URI"]
