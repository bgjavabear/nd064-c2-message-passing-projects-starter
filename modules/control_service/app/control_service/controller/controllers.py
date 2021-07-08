from flask import request
from flask_accepts import responds, accepts
from flask_restx import Namespace, Resource

import app.control_service.service.person_service as person_service
from app.control_service.schemas import PersonSchema

DATE_FORMAT = "%Y-%m-%d"

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
        persons = person_service.get_all()
        return persons


@api.route('/persons/<person_id>')
@api.param("person_id", "Unique ID for a given Person", _in="query")
class PersonResource(Resource):
    @responds(schema=PersonSchema)
    def get(self, person_id):
        person = person_service.get_person_by_id(person_id)
        return person
