from sqlalchemy.orm import Session
from app.models.star_wars_character_model import StarWarsCharacter
from app.schemas.swapi_character_schema import SwapiCharacter


def insert_character(db: Session, characters: SwapiCharacter) -> StarWarsCharacter:
    new_character = StarWarsCharacter(
        name=characters.name,
        height=characters.height,
        mass=characters.mass,
    )
    db.add(new_character)
    db.flush()
    db.refresh(new_character)
    db.commit()
    return new_character
