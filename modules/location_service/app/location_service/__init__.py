from app.location_service.models import Location, Person
from app.location_service.schemas import LocationSchema


def register_routes(api, app, root="api"):
    from app.location_service.controller.location_controller import api as udaconnect_api

    api.add_namespace(udaconnect_api, path=f"/{root}")
