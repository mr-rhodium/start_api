from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from database import Base
from uuid import uuid4, UUID


class StarWarsCharacter(Base):
    __tablename__ = "star_wars_characters"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    height: Mapped[str] = mapped_column(String, nullable=True)
    mass: Mapped[str] = mapped_column(String, nullable=True)
    force: Mapped[int] = mapped_column(Integer, nullable=True)
