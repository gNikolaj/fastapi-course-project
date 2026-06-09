import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def sync_client():
    return TestClient(app)


def test_health_check(sync_client):
    response = sync_client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "status_code": 200,
        "detail": "ok",
        "result": "working"
    }
