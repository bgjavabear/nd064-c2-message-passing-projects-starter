from app.repository.location_repository import create


def create_location(location_data):
    """
    creates and inserts a new location into the database
    """
    return create(location_data)
