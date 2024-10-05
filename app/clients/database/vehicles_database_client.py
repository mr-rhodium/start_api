from sqlalchemy.orm import Session
from app.models.star_wars_vehicle_model import StarWarsVehicleModel
from app.schemas.swapi_vehicle_schema import SwapiVehicle


def insert_new_vehicle(db: Session, swapi_vehicle: SwapiVehicle):
    new_vehicle = StarWarsVehicleModel(
        name=swapi_vehicle.name,
        model=swapi_vehicle.model,
        manufacturer=swapi_vehicle.manufacturer,
        cost_in_credits=swapi_vehicle.cost_in_credits,
        length=swapi_vehicle.length,
        max_atmosphere_speed=swapi_vehicle.max_atmosphere_speed,
        crew=swapi_vehicle.crew,
        passengers=swapi_vehicle.passengers,
        cargo_capacity=swapi_vehicle.cargo_capacity,
        consumables=swapi_vehicle.consumables,
        vehicle_class=swapi_vehicle.vehicle_class,
    )

    db.add(new_vehicle)
    db.flush()
    db.refresh(new_vehicle)
    db.commit()
    return new_vehicle


def get_vehicle_by_id(db: Session, vehicle_id: int) -> StarWarsVehicleModel:
    return (
        db.query(StarWarsVehicleModel)
        .filter(StarWarsVehicleModel.id == vehicle_id)
        .first()
    )
