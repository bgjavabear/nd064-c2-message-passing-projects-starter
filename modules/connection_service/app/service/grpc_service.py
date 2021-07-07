from datetime import timedelta
from typing import Dict, List

from ConnectionMessage_pb2_grpc import ConnectionServiceServicer
from app.config.models import Person, Location, Connection
from app.repository.location_repository import find_all as find_all_locations
from app.repository.location_repository import find_all_by_person_location_data
from app.repository.person_repository import find_all as find_all_persons


class ConnectionServicer(ConnectionServiceServicer):
    def FindConnectionList(self, request, context):
        request_data = {
            "person_id": request.person_id,
            "start_date": request.start_date,
            "end_date": request.end_date,
            "meters": request.meters
        }
        locations: List = find_all_locations(request_data['person_id'],
                                             request_data['start_date'],
                                             request_data['end_date'])
        person_map: Dict[str, Person] = {person.id: person for person in find_all_persons()}

        # Prepare arguments for queries
        data = []
        for location in locations:
            data.append(
                {
                    "person_id": request_data['person_id'],
                    "longitude": location.longitude,
                    "latitude": location.latitude,
                    "meters": request_data['meters'],
                    "start_date": request_data['start_date'].strftime("%Y-%m-%d"),
                    "end_date": (request_data['end_date'] + timedelta(days=1)).strftime("%Y-%m-%d"),
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
