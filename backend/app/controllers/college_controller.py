# backend/app/controllers/college_controller.py
from flask import Blueprint, jsonify
from ..models import CommunityCollege, CommunityCollegeCourse
from ..schemas.college_schema import CommunityCollegeSchema
from ..schemas.course_schema import CommunityCollegeCourseSchema

college_bp = Blueprint('colleges', __name__)

@college_bp.route('/<int:college_id>/courses', methods=['GET'])
def get_college_courses(college_id):
    college = CommunityCollege.query.get_or_404(college_id)
    courses = CommunityCollegeCourse.query.filter_by(college_id=college.id).all()
    course_schema = CommunityCollegeCourseSchema(many=True)
    course_list = course_schema.dump(courses)
    return jsonify(course_list)

@college_bp.route('/', methods=['GET'])
def get_all_colleges():
    colleges = CommunityCollege.query.all()
    college_schema = CommunityCollegeSchema(many=True)
    college_list = college_schema.dump(colleges)
    return jsonify(college_list)

@college_bp.route('/<int:college_id>', methods=['GET'])
def get_college(college_id):
    college = CommunityCollege.query.get_or_404(college_id)
    college_schema = CommunityCollegeSchema()
    college_data = college_schema.dump(college)
    return jsonify(college_data)
