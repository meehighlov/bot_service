import json

from marshmallow import Schema, fields, EXCLUDE
from marshmallow.validate import OneOf


event_types = [
    'message_new',
    'confirmation',
    'message_reply',
    'group_join'
]


class VKEventSchema(Schema):
    type = fields.String(
        validate=OneOf(event_types)
    )
    group_id = fields.Int()
    secret = fields.String()

    class Meta:
        unknown = EXCLUDE


class VKCallbackAPIMessageSchema(Schema):
    id = fields.Int()
    date = fields.Int(description='время отправки в Unixtime')
    peer_id = fields.Int(descriptin='ид назначения')
    from_id = fields.Int(description='отправитель')
    text = fields.String()
    random_id = fields.Int()
    payload = fields.Function(deserialize=lambda value: json.loads(value))

    class Meta:
        unknown = EXCLUDE


class VKCallbackAPIObjectMessageSchema(Schema):
    message = fields.Nested(VKCallbackAPIMessageSchema)

    class Meta:
        unknown = EXCLUDE


class VKChatSchema(VKEventSchema):
    object = fields.Nested(VKCallbackAPIObjectMessageSchema)


class VKGroupJoinObjectSchema(Schema):
    user_id = fields.Integer()
    join_type = fields.String()


class VKGroupJoinSchema(VKEventSchema):
    object = fields.Nested(VKGroupJoinObjectSchema)
