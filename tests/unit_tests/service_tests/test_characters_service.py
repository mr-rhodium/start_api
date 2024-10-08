from unittest.mock import patch
from app.services.characters_service import add_new_character
from app.schemas.star_wars_character_schema import StarWarsCharacterRead


@patch("app.services.characters_service.get_character_from_swapi")
@patch("app.services.characters_service.transform_swapi_character_json_to_pydantic")
@patch("app.services.characters_service.insert_character")
@patch("app.services.characters_service.format_star_wars_name")
def test_add_new_character_success(
    mock_format_star_wars_name,
    mock_insert_character,
    mock_transform_swapi_character_json_to_pydantic,
    mock_get_character_from_swapi,
    mock_db_session,
    mock_star_wars_character_create,
    mock_swapi_character,
    mock_star_wars_character_read,
):
    mock_get_character_from_swapi.return_value = {"results": [mock_swapi_character]}
    mock_transform_swapi_character_json_to_pydantic.return_value = mock_swapi_character
    mock_format_star_wars_name.return_value = "Leia_Organa_from_the_starwars_universe"
    mock_insert_character.return_value = mock_star_wars_character_read

    result = add_new_character(mock_star_wars_character_create, mock_db_session)

    # Then
    mock_get_character_from_swapi.assert_called_once_with("Leia Organa")
    mock_transform_swapi_character_json_to_pydantic.assert_called_once_with(
        {"results": [mock_swapi_character]}
    )
    mock_format_star_wars_name.assert_called_once_with("Leia Organa")
    mock_insert_character.assert_called_once_with(mock_db_session, mock_swapi_character)
    assert isinstance(result, StarWarsCharacterRead)
    assert result.name == "Dart"
    assert result.height == "123"
