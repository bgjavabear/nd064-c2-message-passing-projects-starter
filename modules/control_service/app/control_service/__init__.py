from app.control_service.schemas import ConnectionSchema, PersonSchema


def register_routes(api, app, root="api"):
    from app.control_service.controller.controllers import api as udaconnect_api

    api.add_namespace(udaconnect_api, path=f"/{root}")
