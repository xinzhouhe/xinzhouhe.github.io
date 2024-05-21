from marshmallow import Schema, fields, validate

class UniversityCourseSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=255))
    course_code = fields.String(required=True, validate=validate.Length(min=1, max=255))
    university_id = fields.Integer(required=True)
    department_id = fields.Integer(required=True)
    credits = fields.Integer(required=True)

    equivalents = fields.List(fields.Nested('EquivalentCourseSchema', exclude=('university_course_id',)))
    course_requirements = fields.List(fields.Nested('CourseRequirementSchema', exclude=('course_id',)))

class CommunityCollegeCourseSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=255))
    course_code = fields.String(required=True, validate=validate.Length(min=1, max=255))
    college_id = fields.Integer(required=True)
    credits = fields.Integer(required=True)
    online = fields.Integer(required=True)  # 1-true, 2-false, 3-hybrid
    in_state_fee = fields.Float(required=True)
    out_state_fee = fields.Float(required=True)
    international_fee = fields.Float(required=True)

    equivalents = fields.List(fields.Nested('EquivalentCourseSchema', exclude=('college_course_id',)))

class EquivalentCourseSchema(Schema):
    id = fields.Integer(dump_only=True)
    university_course_id = fields.Integer(required=True)
    college_course_id = fields.Integer(required=True)
