from pydantic import BaseModel, ConfigDict
from typing import List
from uuid import UUID


class StarWarsVehicleBase(BaseModel):
    name: str
    model: str
    manufacturer: str


class StarWarsVehicleCreate(StarWarsVehicleBase): ...


class StarWarsVehicleRead(StarWarsVehicleBase):
    id: UUID
    cost_in_cents: str
    length: str
    max_atmosphere_speed: str
    crew: str
    passengers: str
    cargo_capacity: str
    vehicle_class: str
    pilots: List[str]
    engineering: str

    model_config = ConfigDict(from_attributes=True)
