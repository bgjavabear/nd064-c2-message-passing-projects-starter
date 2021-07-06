import logging
from typing import Dict

from app.location_service.models import Location
from app.location_service.schemas import LocationSchema

from app.location_service.repository.location_repository import find_by_id, create

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("LocationService")


class LocationService:
    @staticmethod
    def retrieve(location_id) -> Location:
        return find_by_id(location_id)

    @staticmethod
    def create(location: Dict) -> Location:
        validation_results: Dict = LocationSchema().validate(location)
        if validation_results:
            logger.warning(f"Unexpected data format in payload: {validation_results}")
            raise Exception(f"Invalid payload: {validation_results}")
        new_location = create(location)
        return new_location
