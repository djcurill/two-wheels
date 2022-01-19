# import py
import pytest
from app import create_app, db
from app.config import TestConfig

# from tests.test_two_wheels import TestApp
from app.specifications.models import Condition


@pytest.fixture
def init_app():
    app = create_app(TestConfig)
    app_ctx = app.app_context()
    app_ctx.push()

    yield

    app_ctx.pop()


@pytest.fixture
def populate_db():
    db.create_all()

    db.session.add(Condition(id=1, value="new"))
    db.session.commit()

    yield db

    db.drop_all()


def test_get_condition(init_app, populate_db):
    assert len(Condition.query.all()) == 1
