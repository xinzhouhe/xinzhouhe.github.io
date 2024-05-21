from marshmallow import Schema, fields, validate

class StudentSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(max=255))
    email = fields.Email(required=True)
    password = fields.String(required=True, load_only=True, validate=validate.Length(max=128))
    university_id = fields.Integer(required=True)
    has_paid = fields.Boolean()
    state = fields.String(validate=validate.Length(max=255))
    us_citizen = fields.Boolean()
    credits = fields.Integer()

    courses = fields.List(fields.Nested('StudentCourseSchema', exclude=('student',)))
