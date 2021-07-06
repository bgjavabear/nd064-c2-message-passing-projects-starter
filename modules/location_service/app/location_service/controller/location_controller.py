from app.location_service.models import Location
from app.location_service.schemas import (LocationSchema, )
from app.location_service.service.location_service import LocationService
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource

api = Namespace("LocationService", description="Locations")


@api.route("/locations")
@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self) -> Location:
        request.get_json()
        location: Location = LocationService.create(request.get_json())
        return location

    @responds(schema=LocationSchema)
    def get(self, location_id) -> Location:
        location: Location = LocationService.retrieve(location_id)
        return location
