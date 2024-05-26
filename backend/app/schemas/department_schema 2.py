from marshmallow import Schema, fields, validate

class DepartmentSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(max=255))
    university_id = fields.Integer(required=True)
