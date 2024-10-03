import os

import requests
from typing import Dict

from app.errors.custom_exceptions import (
    CharacterNotFoundError,
    SwapiCharacterError,
    VehicleNotFoundError,
)

from app.schemas.swapi_vehicle_schema import SwapiVehicle
from app.schemas.swapi_character_schema import SwapiCharacter

SWAPI_BASE_URL = os.environ.get("SWAPI_BASE_URL")


def get_character_from_swapi(name: str) -> Dict:
    url = f"{SWAPI_BASE_URL}/people/?search={name}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data


def get_vehicle_from_swapi(name: str) -> Dict:
    url = f"{SWAPI_BASE_URL}/vehicles/?search={name}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data


def transform_swapi_character_json_to_pydantic(swapi_character: Dict) -> SwapiCharacter:
    results = swapi_character.get("results", [])
    if not results:
        raise CharacterNotFoundError("Character not found in SWAPI response")
    try:
        character = results[0]
        return SwapiCharacter(
            name=character.get("name"),
            height=character.get("height"),
            mass=character.get("mass"),
        )
    except KeyError as e:
        raise SwapiCharacterError(f"Error parsing SWAPI data: {e}")


def transform_swapi_vehicle_json_to_pydantic(swapi_vehicle: Dict) -> SwapiVehicle:
    results = swapi_vehicle.get("results", [])
    if not results:
        raise VehicleNotFoundError("Vehicle not found in SWAPI response")

    try:
        vehicle = results[0]
        return SwapiVehicle(
            name=vehicle.get("name"),
            model=vehicle.get("model"),
            manufacturer=vehicle.get("manufacturer"),
            cost_in_centst=vehicle.get("cost_in_cents"),
            length=vehicle.get("length"),
            max_atmosphere_speed=vehicle.get("max_atmosphere_speed"),
            crew=vehicle.get("crew"),
            passengers=vehicle.get("passengers"),
            cargo_capacity=vehicle.get("cargo_capacity"),
            consumables=vehicle.get("consumables"),
            vehicle_class=vehicle.get("vehicle_class"),
        )
    except KeyError as e:
        raise VehicleNotFoundError(f"Vehicle not found in SWAPI response: {e}")
