from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_intervals_status():
    response = client.get("/producers/intervals")
    assert response.status_code == 200

def test_get_intervals_structure():
    response = client.get("/producers/intervals")
    data = response.json()

    assert "min" in data
    assert "max" in data

    assert isinstance(data["min"], list)
    assert isinstance(data["max"], list)

def test_get_intervals_fields():
    response = client.get("/producers/intervals")
    data = response.json()

    if data["min"]:
        item = data["min"][0]
        assert "producer" in item
        assert "interval" in item
        assert "previousWin" in item
        assert "followingWin" in item