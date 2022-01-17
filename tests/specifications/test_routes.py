import unittest
import pytest
from app.config import TestConfig
from app.db import init as init_db, teardown
from app import create_app


class SpecificationTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config=TestConfig)
        init_db()

    def tearDown(self) -> None:
        teardown()

    def get_all_conditions_returns_200():
        pass
