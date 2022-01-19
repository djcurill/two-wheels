import unittest
from app.config import TestConfig
from flask import current_app
from app import create_app, db


class TestApp(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.drop_all()
        self.app_context.pop()
        self.app = None
        self.app_context = None

    def test_app(self):
        assert self.app is not None
        assert current_app == self.app
