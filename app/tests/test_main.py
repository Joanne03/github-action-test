import pytest

from app.main import handler


@pytest.fixture
def context():
    return None


def test_handler(context):
    assert handler({"payload": "hello world!"}, context).startswith(
        "Hello from AWS Lambda using Python"
    )