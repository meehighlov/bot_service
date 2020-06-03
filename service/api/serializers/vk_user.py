from marshmallow import Schema, fields, post_load


class VKUserSchema(Schema):
    id_ = fields.String(allow_none=True, load_from='id')
    first_name = fields.String(allow_none=True)
    last_name = fields.String(allow_none=True)
    is_closed = fields.Boolean(allow_none=True)
    can_access_closed = fields.Boolean(allow_none=True)

    @post_load(pass_original=True)
    def process_additional_fields(self, data, original, **kwargs):
        uncaught_fields = set(original) - set(data)
        for field_name in uncaught_fields:
            data[field_name] = original[field_name]
        return data


class VKUsersSchema(Schema):
    response = fields.List(fields.Nested(VKUserSchema))
