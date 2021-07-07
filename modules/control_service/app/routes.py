def register_routes(api, app, root="api"):
    from app.connection_service import register_routes as attach_udaconnect
    # Add routes
    attach_udaconnect(api, app)
