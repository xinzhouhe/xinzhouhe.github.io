# backend/app/controllers/university_controller.py
from flask import Blueprint, jsonify
from ..models import db, UniversityCourse, Requirement, Department, CourseRequirement, University, UniversityCourseCost
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import Student

university_bp = Blueprint('universities', __name__)

@university_bp.route('/', methods=['GET'])
def get_all_universities():
    universities = University.query.all()
    university_list = [{
        "id": university.id,
        "name": university.name,
        "state": university.state
    } for university in universities]
    return jsonify(university_list)

@university_bp.route('/<int:university_id>', methods=['GET'])
def get_university(university_id):
    university = University.query.get_or_404(university_id)
    return jsonify({
        "id": university.id,
        "name": university.name,
        "state": university.state
    })

@university_bp.route('/courses', methods=['GET'])
@jwt_required()
def get_university_courses():
    student_id = get_jwt_identity()
    student = Student.query.get_or_404(student_id)
    university_id = student.university_id
    
    courses = UniversityCourse.query.filter_by(university_id=university_id).all()
    course_list = []
    for course in courses:
        course_list.append({
            "id": course.id,
            "name": course.name,
            "course_code": course.course_code,
            "department": Department.query.get(course.department_id).name,
            "requirements": [Requirement.query.get(cr.requirement_id).name for cr in course.course_requirements],
            "credits": course.credits
        })
    
    return jsonify(course_list)

@university_bp.route('/requirements', methods=['GET'])
@jwt_required()
def get_university_requirements():
    student_id = get_jwt_identity()
    student = Student.query.get_or_404(student_id)
    university_id = student.university_id
    
    requirements = Requirement.query.filter_by(university_id=university_id).all()
    requirement_list = [{
        "id": requirement.id,
        "name": requirement.name
    } for requirement in requirements]
    
    return jsonify(requirement_list)

@university_bp.route('/departments', methods=['GET'])
@jwt_required()
def get_university_departments():
    student_id = get_jwt_identity()
    student = Student.query.get_or_404(student_id)
    university_id = student.university_id
    
    departments = Department.query.filter_by(university_id=university_id).all()
    department_list = [{
        "id": department.id,
        "name": department.name
    } for department in departments]
    
    return jsonify(department_list)

@university_bp.route('/costs', methods=['GET'])
@jwt_required()
def get_university_credits_costs():
    student_id = get_jwt_identity()
    student = Student.query.get_or_404(student_id)
    university_id = student.university_id
    
    costs = UniversityCourseCost.query.filter_by(university_id=university_id).all()
    costs_list = [{
        "total_credits": cost.total_credits,
        "in-state": cost.total_in_state_cost,
        "out-state": cost.total_out_state_cost,
        "international": cost.total_international_cost
    } for cost in costs]

    return jsonify(costs_list)

@university_bp.route('/<int:department_id>/courses', methods=['GET'])
@jwt_required()
def get_department_courses(department_id):
    student_id = get_jwt_identity()
    student = Student.query.get_or_404(student_id)
    university_id = student.university_id
    department = Department.query.filter_by(id=department_id, university_id=university_id).first_or_404()
    
    courses = UniversityCourse.query.filter_by(department_id=department.id).all()
    course_list = [{
        "id": course.id,
        "name": course.name,
        "course_code": course.course_code,
        "credits": course.credits,
        "requirements": [Requirement.query.get_or_404(cr.requirement_id).name for cr in course.course_requirements]
    } for course in courses]
    
    return jsonify(course_list)

@university_bp.route('/<int:requirement_id>/courses', methods=['GET'])
@jwt_required()
def get_requirement_courses(requirement_id):
    student_id = get_jwt_identity()
    student = Student.query.get_or_404(student_id)
    university_id = student.university_id
    requirement = Requirement.query.filter_by(id=requirement_id, university_id=university_id).first_or_404()
    
    course_requirements = CourseRequirement.query.filter_by(requirement_id=requirement.id).all()
    courses = [{
        "id": cr.course_id,
        "name": UniversityCourse.query.get_or_404(cr.course_id).name,
        "course_code": UniversityCourse.query.get_or_404(cr.course_id).course_code,
        "credits": UniversityCourse.query.get_or_404(cr.course_id).credits,
        "department": Department.query.get_or_404(UniversityCourse.query.get_or_404(cr.course_id).department_id).name
    } for cr in course_requirements]
    
    return jsonify(courses)
