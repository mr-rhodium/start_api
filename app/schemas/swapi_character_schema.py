from pydantic import BaseModel
from typing import Optional


class SwapiCharacter(BaseModel):
    name: str
    height: Optional[str]
    mass: Optional[str]
