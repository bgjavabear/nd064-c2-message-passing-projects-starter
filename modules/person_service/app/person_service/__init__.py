from app.person_service.models import Person
from app.person_service.schemas import PersonSchema


def register_routes(api, app, root="api"):
    from app.person_service.controller.person_controller import api as udaconnect_api

    api.add_namespace(udaconnect_api, path=f"/{root}")
