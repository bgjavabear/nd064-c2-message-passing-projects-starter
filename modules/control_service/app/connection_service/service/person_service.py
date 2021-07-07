import logging
from typing import List
from app import db
from app.connection_service.models import Person

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("PersonService")


class PersonService:
    @staticmethod
    def retrieve_all() -> List[Person]:
        return db.session.query(Person).all()
