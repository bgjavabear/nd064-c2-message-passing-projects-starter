from datetime import timedelta, datetime
from typing import Dict, List

import ConnectionMessage_pb2 as connection_pb2
import PersonMessage_pb2 as person_pb2
from ConnectionMessage_pb2_grpc import ConnectionServiceServicer
from app.config.models import Person, Location
from app.repository.location_repository import find_all as find_all_locations
from app.repository.location_repository import find_all_by_person_location_data
from app.repository.person_repository import find_all as find_all_persons

DATE_FORMAT = "%Y-%m-%d"


class ConnectionServicer(ConnectionServiceServicer):
    def FindConnectionList(self, request, context):
        """
        Find all connections based on distance and date ranges.
        """
        request_data = {
            "person_id": request.person_id,
            "start_date": datetime.strptime(request.start_date, DATE_FORMAT),
            "end_date": datetime.strptime(request.end_date, DATE_FORMAT),
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
                    "start_date": request_data['start_date'].strftime(DATE_FORMAT),
                    "end_date": (request_data['end_date'] + timedelta(days=1)).strftime(DATE_FORMAT),
                }
            )

        connection_messages = []
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
                # get person from cache
                person = person_map[exposed_person_id]

                # convert to protobuf messages
                loc_message = connection_pb2.LocationMessage(id=location.id, person_id=exposed_person_id,
                                                             longitude=location.longitude,
                                                             latitude=location.latitude,
                                                             creation_time=location.creation_time.strftime(DATE_FORMAT))
                person_message = person_pb2.PersonMessage(id=person.id, first_name=person.first_name,
                                                          last_name=person.last_name,
                                                          company_name=person.company_name)

                connection_message = connection_pb2.ConnectionMessage(person=person_message, location=loc_message)
                connection_messages.append(connection_message)

        connection_list_message = connection_pb2.ConnectionListMessage()
        connection_list_message.connections.extend(connection_messages)
        return connection_list_message
