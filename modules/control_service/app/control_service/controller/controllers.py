from flask import request
from flask_accepts import responds, accepts
from flask_restx import Namespace, Resource

import app.control_service.service.person_service as person_service
import app.control_service.service.connection_service as connection_service
from app.control_service.schemas import PersonSchema, ConnectionSchema

api = Namespace("Control Service", description="Central Service to control all microservices.")


@api.route('/persons')
class PersonsResource(Resource):
    @accepts(schema=PersonSchema)
    @responds(schema=PersonSchema)
    def post(self):
        payload = request.get_json()
        new_person = person_service.create(payload)
        return new_person

    @responds(schema=PersonSchema, many=True)
    def get(self):
        persons = person_service.get_all().persons
        return persons


@api.route('/persons/<int:person_id>')
@api.param("person_id", "Unique ID for a given Person", _in="query")
class PersonResource(Resource):
    @responds(schema=PersonSchema)
    def get(self, person_id):
        person = person_service.get_person_by_id(person_id)
        return person


@api.route("/persons/<int:person_id>/connection")
@api.param("start_date", "Lower bound of date range", _in="query")
@api.param("end_date", "Upper bound of date range", _in="query")
@api.param("distance", "Proximity to a given user in meters", _in="query")
class ConnectionDataResource(Resource):
    @responds(schema=ConnectionSchema, many=True)
    def get(self, person_id) -> ConnectionSchema:
        connection_request_data = {
            "person_id": person_id,
            "start_date": request.args["start_date"],
            "end_date": request.args["end_date"],
            "meters": int(request.args.get("distance", 5))
        }
        connection_list = connection_service.get_connections(connection_request_data)
        return connection_list.connections
