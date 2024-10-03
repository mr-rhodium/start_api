from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID


class StarWarsCharacterBase(BaseModel):
    name: str


class StarWarsCharacterCreate(StarWarsCharacterBase): ...


class StarWarsCharacterRead(StarWarsCharacterBase):
    id: Optional[UUID]
    height: Optional[str]
    mass: Optional[str]
    force: Optional[str]

    model_config = ConfigDict(from_attributes=True)
