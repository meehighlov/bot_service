from marshmallow import Schema, fields, pre_load


class VKUserSchema(Schema):
    id_ = fields.String(allow_none=True, load_from='id')
    first_name = fields.String(allow_none=True)
    last_name = fields.String(allow_none=True)
    is_closed = fields.Boolean(allow_none=True)
    can_access_closed = fields.Boolean(allow_none=True)

    @pre_load
    def process_additional_fields(self, data, **kwargs):
        pass


class VKUsersSchema(Schema):
    response = fields.Nested(VKUserSchema, many=True)
