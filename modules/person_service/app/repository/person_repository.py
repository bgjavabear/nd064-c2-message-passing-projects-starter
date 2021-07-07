from app.config.models import Person
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import os
from app.config.config import config_by_name

# Retrieve config parameters

# Initialize database access

config = config_by_name[os.getenv("FLASK_ENV") or "test"]
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)


def create(person):
    new_person = Person()
    new_person.first_name = person["first_name"]
    new_person.last_name = person["last_name"]
    new_person.company_name = person["company_name"]

    with Session(engine) as session:
        session.add(new_person)
        session.commit()
    return new_person


def find_by_id(person_id):
    with Session(engine) as session:
        return session.query(Person).get(person_id)


def find_all():
    with Session(engine) as session:
        return session.query(Person).all()
