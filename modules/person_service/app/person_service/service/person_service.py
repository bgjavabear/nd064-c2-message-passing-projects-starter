import logging
from typing import Dict, List

from app.person_service.models import Person
from app.person_service.repository.person_repository import create, find_by_id, find_all

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("PersonService")


class PersonService:
    @staticmethod
    def create(person: Dict) -> Person:
        return create(person)

    @staticmethod
    def retrieve(person_id: int) -> Person:
        return find_by_id(person_id)

    @staticmethod
    def retrieve_all() -> List[Person]:
        return find_all()
