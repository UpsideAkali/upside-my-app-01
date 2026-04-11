from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"message": "Hello, World!"}


def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "ok"


def test_get_item():
    res = client.get("/items/42")
    assert res.status_code == 200
    assert res.json()["item_id"] == 42


def test_create_item():
    res = client.post("/items", json={"name": "Widget", "price": 9.99})
    assert res.status_code == 200
    assert res.json()["created"] is True
    assert res.json()["item"]["name"] == "Widget"
