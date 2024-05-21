# backend/app/controllers/course_controller.py
from flask import Blueprint, jsonify, request
from ..models import db, StudentCourse, UniversityCourse, University, Department, Requirement, Student, EquivalentCourse, CommunityCollegeCourse, CommunityCollege
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..schemas import UniversityCourseSchema, StudentCourseSchema
import json

course_bp = Blueprint('courses', __name__)

@course_bp.route('/', methods=['GET'])
def get_all_courses():
    courses = UniversityCourse.query.all()
    course_schema = UniversityCourseSchema(many=True)
    course_list = course_schema.dump(courses)
    
    for course in course_list:
        course['university'] = University.query.get_or_404(course['university_id']).name
        course['department'] = Department.query.get_or_404(course['department_id']).name
        course['requirements'] = [Requirement.query.get_or_404(cr["requirement_id"]).name for cr in course["course_requirements"] ]
    
    return jsonify(course_list)

@course_bp.route('/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = UniversityCourse.query.get_or_404(course_id)
    return jsonify({
        "id": course.id,
        "name": course.name,
        "course_code": course.course_code,
        "university": University.query.get_or_404(course.university_id).name,
        "department": Department.query.get_or_404(course.department_id).name,
        "credits": course.credits,
        "requirements": [Requirement.query.get_or_404(cr.requirement_id).name for cr in course.course_requirements ]
    })

@course_bp.route('/me', methods=['GET'])
@jwt_required()
def get_student_courses():
    student_id = get_jwt_identity()
    student_courses = StudentCourse.query.filter_by(student_id=student_id).all()
    courses = []
    for sc in student_courses:
        course = UniversityCourse.query.get_or_404(sc.university_course_id)
        
        courses.append({
            "name": course.name,
            "course_code": course.course_code,
            "university": University.query.get_or_404(course.university_id).name,
            "department": Department.query.get_or_404(course.department_id).name,
            "credits": course.credits,
            "requirements": [Requirement.query.get_or_404(cr.requirement_id).name for cr in course.course_requirements ]
        })
    return jsonify(courses)

@course_bp.route('/me/<int:course_id>', methods=['POST'])
@jwt_required()
def add_student_course(course_id):
    student_id = get_jwt_identity()
    student = Student.query.get_or_404(student_id)
    course = UniversityCourse.query.get_or_404(course_id)
    
    student_course = StudentCourse.query.filter_by(student_id=student_id, university_course_id=course_id).first()
    if student_course:
        return jsonify({"message": "Course already added"}), 400
    
    student_course = StudentCourse(student_id=student_id, university_course_id=course_id)
    db.session.add(student_course)
    db.session.commit()
    
    student.credits += course.credits
    return jsonify({"message": "Course added successfully"}), 201

@course_bp.route('/me/<int:course_id>', methods=['DELETE'])
@jwt_required()
def delete_student_course(course_id):
    student_id = get_jwt_identity()
    student = Student.query.get_or_404(student_id)
    student_course = StudentCourse.query.filter_by(student_id=student_id, university_course_id=course_id).first_or_404()
    
    db.session.delete(student_course)
    db.session.commit()
    
    student.credits -= UniversityCourse.query.get_or_404(course_id).credits
    return jsonify({"message": "Course deleted successfully"}), 200


@course_bp.route('/<int:course_id>/equivalents', methods=['GET'])
def get_equivalent_courses(course_id):
    equivalents = EquivalentCourse.query.filter_by(university_course_id=course_id).all()
    equivalent_list = []
    for equivalent in equivalents:
        college_course = CommunityCollegeCourse.query.get_or_404(equivalent.college_course_id)
        if college_course.online == 1:
            online = "Yes"
        elif college_course.online == 2:
            online = "No"
        elif college_course.online == 3:
            online = "Hybrid"
        equivalent_list.append({
            "id": college_course.id,
            "name": college_course.name,
            "course_code": college_course.course_code,
            "college": CommunityCollege.query.get_or_404(college_course.college_id).name,
            "credits": college_course.credits,
            "online" : online,
            "InStateTuition" : college_course.in_state_fee,
            "OutStateTuition" : college_course.out_state_fee,
            "InternationalTuition" : college_course.international_fee
        })
    return jsonify(equivalent_list)

@course_bp.route('/me/<int:course_id>/equivalents', methods=['GET'])
@jwt_required()
def get_student_equivalent_courses(course_id):
    student_id = get_jwt_identity()
    student = Student.query.get_or_404(student_id)
    equivalent_list = json.loads(get_equivalent_courses(course_id).data)
    equivalent_courses = []
    for equivalent in equivalent_list:
        fee = 0
        community_college_state = CommunityCollege.query.get_or_404(CommunityCollegeCourse.query.get_or_404(equivalent['id']).college_id).state
        if student.us_citizen and student.state == community_college_state:
            fee = equivalent['InStateTuition']
        elif student.us_citizen and student.state != community_college_state:
            fee = equivalent['OutStateTuition']
        else:
            fee = equivalent['InternationalTuition']
        equivalent_courses.append({
            "id": equivalent['id'],
            "name": equivalent['name'],
            "course_code": equivalent['course_code'],
            "college": equivalent['college'],
            "credits": equivalent['credits'],
            "online" : equivalent['online'],
            "tuition": fee
        })
    equivalent_courses = sorted(equivalent_courses, key=lambda x: x['tuition'])
    return jsonify(equivalent_courses)

@course_bp.route('/<int:course_id>/equivalents/<int:college_id>', methods=['GET'])
def get_equivalent_course_by_college(course_id, college_id):
    equivalent_list = json.loads(get_equivalent_courses(course_id).data)
    equivalent_courses = []
    college = CommunityCollege.query.get_or_404(college_id).name
    for equivalent in equivalent_list:
        if equivalent['college'] == college:
            equivalent_courses.append(equivalent)
    return jsonify(equivalent_courses)

@course_bp.route('/me/<int:course_id>/equivalents/<int:college_id>', methods=['GET'])
@jwt_required()
def get_student_equivalent_course_by_college(course_id, college_id):
    student_id = get_jwt_identity()
    student = Student.query.get_or_404(student_id)
    equivalent_list = json.loads(get_equivalent_course_by_college(course_id, college_id).data)
    equivalent_courses = []
    for equivalent in equivalent_list:
        fee = 0
        community_college_state = CommunityCollege.query.get_or_404(CommunityCollegeCourse.query.get_or_404(equivalent['id']).college_id).state
        if student.us_citizen and student.state == community_college_state:
            fee = equivalent['InStateTuition']
        elif student.us_citizen and student.state != community_college_state:
            fee = equivalent['OutStateTuition']
        else:
            fee = equivalent['InternationalTuition']
        equivalent_courses.append({
            "id": equivalent['id'],
            "name": equivalent['name'],
            "course_code": equivalent['course_code'],
            "college": equivalent['college'],
            "credits": equivalent['credits'],
            "online" : equivalent['online'],
            "tuition": fee
        })
    equivalent_courses = sorted(equivalent_courses, key=lambda x: x['tuition'])
    return jsonify(equivalent_courses)

@course_bp.route('/<int:course_id>/equivalents/<string:state>', methods=['GET'])
def get_equivalent_courses_by_state(course_id, state):
    equivalent_list = json.loads(get_equivalent_courses(course_id).data)
    equivalent_courses = []
    for equivalent in equivalent_list:
        community_college_state = CommunityCollege.query.get_or_404(CommunityCollegeCourse.query.get_or_404(equivalent['id']).college_id).state
        if community_college_state == state:
            equivalent_courses.append(equivalent)
    return jsonify(equivalent_courses)

@course_bp.route('/me/<int:course_id>/equivalents/<string:state>', methods=['GET'])
@jwt_required()
def get_student_equivalent_courses_by_state(course_id, state):
    student_id = get_jwt_identity()
    student = Student.query.get_or_404(student_id)
    equivalent_list = json.loads(get_equivalent_courses_by_state(course_id, state).data)
    equivalent_courses = []
    for equivalent in equivalent_list:
        fee = 0
        community_college_state = CommunityCollege.query.get_or_404(CommunityCollegeCourse.query.get_or_404(equivalent['id']).college_id).state
        if student.us_citizen and student.state == community_college_state:
            fee = equivalent['InStateTuition']
        elif student.us_citizen and student.state != community_college_state:
            fee = equivalent['OutStateTuition']
        else:
            fee = equivalent['InternationalTuition']
        equivalent_courses.append({
            "id": equivalent['id'],
            "name": equivalent['name'],
            "course_code": equivalent['course_code'],
            "college": equivalent['college'],
            "credits": equivalent['credits'],
            "online" : equivalent['online'],
            "tuition": fee
        })
    equivalent_courses = sorted(equivalent_courses, key=lambda x: x['tuition'])
    return jsonify(equivalent_courses)

