from unittest.mock import Base
from sqlalchemy import create_engine
import os


def connect(env_key: str):
    connection_string = os.getenv(env_key)
    return create_engine(connection_string)
