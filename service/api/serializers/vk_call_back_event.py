import json

from marshmallow import Schema, fields, INCLUDE, post_load
from marshmallow.validate import OneOf


event_types = [
    'message_new',
    'confirmation'
]


class VKCallBackAPIMessage(Schema):
    id_ = fields.Int(load_from='id')
    date = fields.Int(description='время отправки в Unixtime')
    peer_id = fields.Int(descriptin='ид назначения')
    from_id = fields.Int(description='отправитель')
    text = fields.String()
    random_id = fields.Int()
    payload = fields.String(description='ожидается словарь в строке')

    class Meta:
        unknown = INCLUDE

    @post_load
    def extract_payload(self, data, **kwargs):
        if 'payload' in data:
            data['payload'] = json.loads(data['payload'])
        return data


class VKCallBackAPIObject(Schema):
    message = fields.Nested(VKCallBackAPIMessage)


class VKCallBackAPIEvent(Schema):
    type_ = fields.String(
        load_from='type',
        validate=OneOf(event_types)
    )
    object_ = fields.Nested(VKCallBackAPIObject, load_from='object')
    group_id = fields.Int()
    secret = fields.String()

    class Meta:
        unknown = INCLUDE
