import logging
from datetime import datetime, timedelta
from typing import Dict, List

from app.connection_service.models import Connection, Location, Person
from app.connection_service.repository.location_repository import find_all, find_all_by_person_location_data
from .person_service import PersonService

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("ConnectionService")


class ConnectionService:
    @staticmethod
    def find_contacts(person_id: int, start_date: datetime, end_date: datetime, meters=5) -> List[Connection]:
        """
        Finds all Person who have been within a given distance of a given Person within a date range.

        This will run rather quickly locally, but this is an expensive method and will take a bit of time to run on
        large datasets. This is by design: what are some ways or techniques to help make this data integrate more
        smoothly for a better user experience for API consumers?
        """
        locations: List = find_all(person_id, start_date, end_date)
        # Cache all users in memory for quick lookup
        person_map: Dict[str, Person] = {person.id: person for person in PersonService.retrieve_all()}

        # Prepare arguments for queries
        data = []
        for location in locations:
            data.append(
                {
                    "person_id": person_id,
                    "longitude": location.longitude,
                    "latitude": location.latitude,
                    "meters": meters,
                    "start_date": start_date.strftime("%Y-%m-%d"),
                    "end_date": (end_date + timedelta(days=1)).strftime("%Y-%m-%d"),
                }
            )

        result: List[Connection] = []
        for person_location_data in tuple(data):
            for (
                    exposed_person_id,
                    location_id,
                    exposed_lat,
                    exposed_long,
                    exposed_time,) in find_all_by_person_location_data(person_location_data):
                location = Location(
                    id=location_id,
                    person_id=exposed_person_id,
                    creation_time=exposed_time,
                )
                location.set_wkt_with_coords(exposed_lat, exposed_long)
                result.append(Connection(person=person_map[exposed_person_id], location=location, ))
        return result
