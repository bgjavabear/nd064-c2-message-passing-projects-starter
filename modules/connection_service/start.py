import logging
from concurrent import futures

import grpc

import ConnectionMessage_pb2_grpc as connection_pb2_grpc
from app.service.grpc_service import ConnectionServiceServicer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("person_service")


def serve():
    logging.log(logging.INFO, 'gRPC server starting on port 5000.')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    connection_pb2_grpc.add_ConnectionServiceServicer_to_server(ConnectionServiceServicer(), server)
    server.add_insecure_port("[::]:5000")
    server.start()
    logging.log(logging.INFO, 'gRPC server successfully started.')
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
