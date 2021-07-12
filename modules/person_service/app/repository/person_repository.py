from app.config.models import Person
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import os
from app.config.config import config_by_name

# Initialize database access

config = config_by_name[os.getenv("FLASK_ENV") or "test"]
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)


def create(person):
    """
    Create a new person and inserts into the database
    """
    session = Session(engine)
    new_person = Person()
    new_person.first_name = person["first_name"]
    new_person.last_name = person["last_name"]
    new_person.company_name = person["company_name"]
    session.add(new_person)
    new_person_data = {
        "id": new_person.id,
        "first_name": new_person.first_name,
        "last_name": new_person.last_name,
        "company_name": new_person.company_name
    }

    session.commit()
    session.close()
    return new_person_data


def find_by_id(person_id):
    """
    Returns a person with the specified id
    """
    session = Session(engine)
    person = session.query(Person).get(person_id)
    session.close()
    return person


def find_all():
    """
    Returns all persons
    """
    session = Session(engine)
    persons = session.query(Person).all()
    session.close()
    return persons
