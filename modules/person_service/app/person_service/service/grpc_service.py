import app.person_service.proto.PersonMessage_pb2 as PersonMessage_pb2
import app.person_service.proto.PersonMessage_pb2_grpc as PersonMessage_pb2_grpc
from app.person_service.proto.PersonMessage_pb2 import PersonMessage, PersonListMessage
from app.person_service.proto.PersonMessage_pb2_grpc import PersonServiceServicer
from person_service import PersonService
from concurrent import futures
import app.person_service.proto.PersonMessage_pb2_grpc as person_pb2_grpc
import grpc
import logging

# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
person_pb2_grpc.add_PersonServiceServicer_to_server(PersonServiceServicer(), server)
logging.log(logging.INFO, 'gRPC server starting on port 5000.')
server.add_insecure_port("[::]:5005")
server.start()

channel = grpc.insecure_channel("localhost:5005")
stub = PersonMessage_pb2_grpc.PersonServiceStub(channel)


class PersonServicer(PersonServiceServicer):
    def Create(self, request, context):
        person = {
            "first_name": request.first_name,
            "last_name": request.last_name,
            "company_name": request.company_name
        }
        new_person = PersonService.create(person)
        return PersonMessage(new_person.first_name, new_person.last_name, new_person.company_name, new_person.id)

    def Retrieve(self, request, context):
        person_id = request.id
        person = PersonService.retrieve(person_id)
        return PersonMessage(person.first_name, person.last_name, person.company_name, person.id)

    def RetrieveAll(self, request, context):
        persons = PersonService.retrieve_all()
        person_messages = []
        for person in persons:
            person_messages.append(PersonMessage(person.first_name, person.last_name, person.company_name, person.id))
        response = PersonListMessage()
        response.persons.extend(person_messages)
        return response


def send_message(first_name, last_name, company_name):
    person = PersonMessage_pb2.PersonMessage(first_name=first_name,
                                             last_name=last_name,
                                             company_name=company_name)
    response = stub.Create(person)
