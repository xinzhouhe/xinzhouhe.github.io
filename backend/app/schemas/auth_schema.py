from marshmallow import Schema, fields

class RegisterSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    university_id = fields.Integer(required=True)
    location = fields.String(required=True)
    status = fields.Boolean(required=True)

class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)
