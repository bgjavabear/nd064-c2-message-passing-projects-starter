from sqlalchemy.sql import text
from app.config.config import config_by_name
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import os
from app.config.models import Location

# Initialize database access

config = config_by_name[os.getenv("FLASK_ENV") or "test"]
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)

FIND_PEOPLE_NEARBY_QUERY = text(
    """
    SELECT  person_id, id, ST_X(coordinate), ST_Y(coordinate), creation_time
    FROM    location
    WHERE   ST_DWithin(coordinate::geography,ST_SetSRID(ST_MakePoint(:latitude,:longitude),4326)::geography, :meters)
    AND     person_id != :person_id
    AND     TO_DATE(:start_date, 'YYYY-MM-DD') <= creation_time
    AND     TO_DATE(:end_date, 'YYYY-MM-DD') > creation_time;
    """
)


def find_all(person_id, start_date, end_date):
    """
    Retrieves all locations which the specified person attended from start to end dates.
    :param person_id: person id
    :param start_date: start date
    :param end_date: end date
    :return: locations with the specified column values
    """
    session = Session(engine)
    persons = Session(engine).query(Location) \
        .filter(Location.person_id == person_id) \
        .filter(Location.creation_time < end_date) \
        .filter(Location.creation_time >= start_date) \
        .all()
    session.close()
    return persons


def find_all_by_person_location_data(person_location_data):
    """
    Returns all locations based on distance and date range
    """
    session = Session(engine)
    locations = session.execute(FIND_PEOPLE_NEARBY_QUERY, person_location_data)
    session.close()
    return locations
