from app import db
from app.location_service.models import Location
from geoalchemy2.functions import ST_Point


def find_by_id(location_id):
    location, coord_text = db.session \
        .query(Location, Location.coordinate.ST_AsText()) \
        .filter(Location.id == location_id) \
        .one()
    # Rely on database to return text form of point to reduce overhead of conversion in app code
    location.wkt_shape = coord_text
    return location


def create(location):
    new_location = Location()
    new_location.person_id = location["person_id"]
    new_location.creation_time = location["creation_time"]
    new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
    db.session.add(new_location)
    db.session.commit()
    return new_location
