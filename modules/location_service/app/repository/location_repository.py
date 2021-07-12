from app.config.models import Location
from geoalchemy2.functions import ST_Point
from app.config.config import config_by_name
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import Session

config = config_by_name[os.getenv("FLASK_ENV") or "test"]
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)


def create(location):
    """
    creates and inserts a new location into the database
    """
    session = Session(engine)
    new_location = Location()
    new_location.person_id = location["person_id"]
    new_location.creation_time = location["creation_time"]
    new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
    session.add(new_location)
    session.commit()
    session.close()
    return new_location
