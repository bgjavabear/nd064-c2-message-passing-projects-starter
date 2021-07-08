import logging
from concurrent import futures

import grpc

import PersonMessage_pb2_grpc as person_pb2_grpc
from app.service.grpc_service import PersonServicer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("person_service")


def serve():
    logging.log(logging.INFO, 'Person Service gRPC server starting on port 5005.')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    person_pb2_grpc.add_PersonServiceServicer_to_server(PersonServicer(), server)
    server.add_insecure_port("[::]:5005")
    server.start()
    logging.log(logging.INFO, 'Person Service gRPC server successfully started.')
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
