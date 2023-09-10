import pytest
from fastapi.testclient import TestClient

from taskload.app import app


@pytest.fixture
def client():
    return TestClient(app)
