from unittest.mock import patch
from fastapi import HTTPException

from app.errors.custom_exceptions import CharacterNotFoundError


@patch("app.routers.characters_router.add_new_character")
def test_create_character_valid_data(
    mock_add_new_character, client, mock_star_wars_character_read
):

    character_input_data = {
        "name": "Dart",
    }
    mock_add_new_character.return_value = mock_star_wars_character_read
    response = client.post("/characters/", json=character_input_data)
    assert response.status_code == 200

    assert response.json() == {
        "id": str(mock_star_wars_character_read.id),
        "name": mock_star_wars_character_read.name,
        "height": mock_star_wars_character_read.height,
        "mass": mock_star_wars_character_read.mass,
        "force": mock_star_wars_character_read.force,
    }


@patch("app.routers.characters_router.add_new_character")
def test_create_character_character_not_found(mock_add_new_character, client):
    character_input_data = {
        "name": "Unknown Character",
    }
    mock_add_new_character.side_effect = CharacterNotFoundError("Character not found")
    response = client.post("/characters/", json=character_input_data)

    assert response.status_code == 404


@patch("app.routers.characters_router.add_new_character")
def test_create_character_external_service_error(mock_add_new_character, client):
    character_input_data = {"name": "Leia"}
    mock_add_new_character.side_effect = HTTPException(
        status_code=503, detail="External service unavailable. Please try again later."
    )

    response = client.post("/characters/", json=character_input_data)

    assert response.status_code == 503


@patch("app.routers.characters_router.add_new_character")
def test_create_character_internal_server_error(mock_add_new_character, client):
    character_input_data = {"name": "Leia"}

    mock_add_new_character.side_effect = HTTPException(
        status_code=500, detail="Internal server error. Please try again later."
    )

    response = client.post("/characters/", json=character_input_data)

    assert response.status_code == 500


def test_create_character_invalid_data(client):
    invalid_character_data = {"name": 2}

    response = client.post("/characters/", json=invalid_character_data)

    assert response.status_code == 422
    assert "detail" in response.json()
