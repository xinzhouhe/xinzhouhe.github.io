from marshmallow import Schema, fields

class StudentCourseSchema(Schema):
    id = fields.Integer(dump_only=True)
    student_id = fields.Integer(required=True)
    university_course_id = fields.Integer(required=True)
