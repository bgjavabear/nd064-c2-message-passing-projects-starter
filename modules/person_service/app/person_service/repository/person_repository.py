from app import db
from app.person_service.models import Person


def create(person):
    new_person = Person()
    new_person.first_name = person["first_name"]
    new_person.last_name = person["last_name"]
    new_person.company_name = person["company_name"]

    db.session.add(new_person)
    db.session.commit()
    return new_person


def find_by_id(person_id):
    person = db.session.query(Person).get(person_id)
    return person


def find_all():
    db.session.query(Person).all()
