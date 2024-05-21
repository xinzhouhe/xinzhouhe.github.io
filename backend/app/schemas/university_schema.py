from marshmallow import Schema, fields, validate

class UniversitySchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=255))
    state = fields.String(required=True, validate=validate.Length(min=1, max=255))
    departments = fields.List(fields.Nested('DepartmentSchema', exclude=('university_id',)))
    courses = fields.List(fields.Nested('UniversityCourseSchema', exclude=('university_id',)))
    course_costs = fields.List(fields.Nested('UniversityCourseCostSchema', exclude=('university_id',)))
    requirements = fields.List(fields.Nested('RequirementSchema', exclude=('university_id',)))
