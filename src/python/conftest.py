import pytest
from app import app
from datetime import datetime

@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client
