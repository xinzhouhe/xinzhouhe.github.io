from marshmallow import Schema, fields

class UniversityCourseCostSchema(Schema):
    id = fields.Integer(dump_only=True)
    university_id = fields.Integer(required=True)
    total_credits = fields.Integer(required=True)
    total_in_state_cost = fields.Float(required=True)
    total_out_state_cost = fields.Float(required=True)
    total_international_cost = fields.Float(required=True)
