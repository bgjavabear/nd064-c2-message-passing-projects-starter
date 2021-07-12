from app.config.models import Person
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import os
from app.config.config import config_by_name

# Initialize database access

config = config_by_name[os.getenv("FLASK_ENV") or "test"]
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)


def find_all():
    """
    Returns all persons in the database
    """
    session = Session(engine)
    persons = session.query(Person).all()
    session.close()
    return persons
