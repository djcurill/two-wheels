import unittest

import pytest
from app.config import TestConfig
from app.database import init_db, wipe_db
from app import create_app


@pytest.fixture
def client():
    app = create_app(config=TestConfig)
    with app.test_client() as client:
        with app.app_context():
            wipe_db()
            init_db()
        yield client


def test_get_conditions(client):
    response = client.get("/specs")
    print(response)
    assert response.status_code == 200
