from pydantic import BaseModel
from typing import Optional, List


class SwapiVehicle(BaseModel):
    name: str
    model: str
    manufacturer: str
    cost_in_credits: str
    length: str
    max_atmosphere_speed: str
    crew: str
    passengers: str
    cargo_capacity: str
    consumables: str
    vehicle_class: str
    pilots: List[str]
    efficiency: Optional[float] = None
