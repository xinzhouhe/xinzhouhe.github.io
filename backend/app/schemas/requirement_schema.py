from marshmallow import Schema, fields, validate

class RequirementSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(max=255))
    university_id = fields.Integer(required=True)

    courses = fields.List(fields.Nested('CourseRequirementSchema', exclude=('requirement',)))

class CourseRequirementSchema(Schema):
    id = fields.Integer(dump_only=True)
    course_id = fields.Integer(required=True)
    requirement_id = fields.Integer(required=True)
