from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from database import Base
import uuid


class StarWarsVehicleModel(Base):
    __tablename__ = "star_wars_vehicles"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    model: Mapped[str] = mapped_column(String, nullable=True)
    manufacturer: Mapped[str] = mapped_column(String, nullable=True)
    cost_in_credits: Mapped[str] = mapped_column(String, nullable=True)
    length: Mapped[str] = mapped_column(String, nullable=True)
    max_atmosphere_speed: Mapped[str] = mapped_column(String, nullable=True)
    crew: Mapped[str] = mapped_column(String, nullable=True)
    passengers: Mapped[str] = mapped_column(String, nullable=True)
    cargo_capacity: Mapped[str] = mapped_column(String, nullable=True)
    consumables: Mapped[str] = mapped_column(String, nullable=True)
    vehicle_class: Mapped[str] = mapped_column(String, nullable=True)
    pilots: Mapped[str] = mapped_column(String, nullable=True)
    efficiency: Mapped[str] = mapped_column(String, nullable=True)
