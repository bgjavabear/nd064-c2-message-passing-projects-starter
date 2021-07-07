from PersonMessage_pb2 import PersonMessage, PersonListMessage
from PersonMessage_pb2_grpc import PersonServiceServicer
from app.repository.person_repository import create, find_by_id, find_all


class PersonServicer(PersonServiceServicer):
    def Create(self, request, context):
        person = {
            "first_name": request.first_name,
            "last_name": request.last_name,
            "company_name": request.company_name
        }
        new_person = create(person)
        return PersonMessage(new_person.first_name, new_person.last_name, new_person.company_name, new_person.id)

    def Retrieve(self, request, context):
        person_id = request.id
        person = find_by_id(person_id)
        return PersonMessage(person.first_name, person.last_name, person.company_name, person.id)

    def RetrieveAll(self, request, context):
        persons = find_all()
        person_messages = []
        for person in persons:
            person_messages.append(PersonMessage(person.first_name, person.last_name, person.company_name, person.id))
        person_list_message = PersonListMessage()
        person_list_message.persons.extend(person_messages)
        return person_list_message
