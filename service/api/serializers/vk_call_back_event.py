import json

from marshmallow import Schema, fields, INCLUDE, post_load, EXCLUDE
from marshmallow.validate import OneOf


event_types = [
    'message_new',
    'confirmation',
    'message_reply',

    # TODO handle those types in future
    # 'group_join'
]


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
    message = fields.Nested(lambda: VKCallbackAPIMessageSchema())

    class Meta:
        unknown = EXCLUDE


class VKChatSchema(Schema):
    type = fields.String(
        validate=OneOf(event_types)
    )
    object = fields.Nested(lambda: VKCallbackAPIObjectMessageSchema())
    group_id = fields.Int()
    secret = fields.String()

    class Meta:
        unknown = EXCLUDE
