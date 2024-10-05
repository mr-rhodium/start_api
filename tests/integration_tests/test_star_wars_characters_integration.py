from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_character():
    character = {"name": "Luke Skywalker"}
    response = client.post("/characters/", json=character)

    assert response.status_code == 200
    assert "id" in response.json()


def test_create_character_not_found():
    non_existent_character_data = {"name": "Unknown Character"}
    response = client.post("/characters/", json=non_existent_character_data)
    assert response.status_code == 404
