import logging
from concurrent import futures

import grpc

import ConnectionMessage_pb2_grpc as connection_pb2_grpc
from app.service.grpc_service import ConnectionServicer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("person_service")


def serve():
    logging.log(logging.INFO, 'Connection Service gRPC server starting on port 5006.')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    connection_pb2_grpc.add_ConnectionServiceServicer_to_server(ConnectionServicer(), server)
    server.add_insecure_port("[::]:5006")
    server.start()
    logging.log(logging.INFO, 'Connection Service gRPC server successfully started.')
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
