from marshmallow import Schema, fields
from ConnectionMessage_pb2 import LocationMessage
from PersonMessage_pb2 import PersonMessage


class PersonSchema(Schema):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    company_name = fields.String()

    class Meta:
        model = PersonMessage


class LocationSchema(Schema):
    id = fields.Integer()
    person_id = fields.Integer()
    longitude = fields.String(attribute="longitude")
    latitude = fields.String(attribute="latitude")
    creation_time = fields.String(attribute="creation_time")

    class Meta:
        model = LocationMessage


class ConnectionSchema(Schema):
    location = fields.Nested(LocationSchema)
    person = fields.Nested(PersonSchema)
