import pytest
from fastapi.testclient import TestClient
from app.schemas.swapi_character_schema import SwapiCharacter
from main import app
from database import get_db_session
from app.schemas.star_wars_character_schema import (
    StarWarsCharacterCreate,
    StarWarsCharacterRead,
)

from mock_alchemy.mocking import UnifiedAlchemyMagicMock

SWAPI_BASE_URL = "https://swapi.dev/api"


@pytest.fixture(scope="function")
def mock_db_session():
    moke_db = UnifiedAlchemyMagicMock()
    return moke_db


@pytest.fixture(scope="function")
def client(mock_db_session):
    def override_get_db():
        yield mock_db_session

    app.dependency_overrides[get_db_session] = override_get_db

    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture(scope="function")
def mock_star_wars_character_create() -> StarWarsCharacterCreate:
    return StarWarsCharacterCreate(
        name="Leia Organa",
    )


@pytest.fixture(scope="function")
def mock_swapi_character() -> StarWarsCharacterCreate:
    return SwapiCharacter(
        name="Leia",
        height="150",
        mass="49",
    )


@pytest.fixture(scope="function")
def mock_star_wars_character_read() -> StarWarsCharacterRead:
    return StarWarsCharacterRead(
        id="4a198219-6167-4088-bfd8-c76cd296ccb3",
        name="Dart",
        height="123",
        mass="200",
        force="1000",
    )


@pytest.fixture(scope="function")
def mock_swapi_response():
    return {
        "count": 1,
        "results": [
            {
                "name": "Dart",
                "height": "123",
                "mass": "200",
            }
        ],
    }
