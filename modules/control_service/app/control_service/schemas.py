from marshmallow import Schema, fields
from ConnectionMessage_pb2 import ConnectionMessage
from PersonMessage_pb2 import PersonMessage


class PersonSchema(Schema):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    company_name = fields.String()

    class Meta:
        model = PersonMessage


class ConnectionSchema(Schema):
    class Meta:
        model = ConnectionMessage
