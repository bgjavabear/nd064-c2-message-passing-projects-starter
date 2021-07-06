from app.connection_service.models import Connection, Location, Person
from app.connection_service.schemas import ConnectionSchema, LocationSchema, PersonSchema


def register_routes(api, app, root="api"):
    from app.connection_service.controller.controllers import api as udaconnect_api

    api.add_namespace(udaconnect_api, path=f"/{root}")
