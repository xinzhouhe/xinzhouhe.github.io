from marshmallow import Schema, fields, validate

class CommunityCollegeSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=255))
    state = fields.String(required=True, validate=validate.Length(min=1, max=255))

    courses = fields.List(fields.Nested('CommunityCollegeCourseSchema', exclude=('college_id',)))
