import grpc
import ConnectionMessage_pb2_grpc as connection_pb2_grpc
import ConnectionMessage_pb2 as connection_pb2

connection_channel = grpc.insecure_channel("connection-service:5006")
connection_stub = connection_pb2_grpc.ConnectionServiceStub(connection_channel)


def get_connections(connection_request_data):
    connection_request_message = connection_pb2.ConnectionRequestMessage(
        person_id=connection_request_data['person_id'],
        start_date=connection_request_data['start_date'],
        end_date=connection_request_data['end_date'],
        meters=connection_request_data['meters']
    )
    return connection_stub.FindConnectionList(connection_request_message)
