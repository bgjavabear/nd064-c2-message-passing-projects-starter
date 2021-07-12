from PersonMessage_pb2 import PersonMessage, PersonListMessage
from PersonMessage_pb2_grpc import PersonServiceServicer
from app.repository.person_repository import create, find_by_id, find_all


class PersonServicer(PersonServiceServicer):
    def Create(self, request, context):
        """
        The implementation of gRPC method Create.
        Inserts a new person into the database and returns it as proto message
        """
        person = {
            "first_name": request.first_name,
            "last_name": request.last_name,
            "company_name": request.company_name
        }
        new_person = create(person)
        return PersonMessage(
            first_name=new_person["first_name"],
            last_name=new_person["last_name"],
            company_name=new_person["company_name"],
            id=new_person["id"]
        )

    def Retrieve(self, request, context):
        """
        The implementation of gRPC method Retrieve.
        Returns the person with the specified id as proto message
        """
        person_id = request.id
        person = find_by_id(person_id)
        return PersonMessage(
            first_name=person.first_name,
            last_name=person.last_name,
            company_name=person.company_name,
            id=person.id
        )

    def RetrieveAll(self, request, context):
        """
        The implementation of gRPC method RetrieveAll.
        Returns all persons as proto messages
        """
        persons = find_all()
        person_messages = []
        for person in persons:
            person_message = PersonMessage(
                first_name=person.first_name,
                last_name=person.last_name,
                company_name=person.company_name,
                id=person.id
            )
            person_messages.append(person_message)
        person_list_message = PersonListMessage()
        person_list_message.persons.extend(person_messages)
        return person_list_message
