# backend/app/controllers/student_controller.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, unset_jwt_cookies, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import db, Student, UniversityCourseCost, University

student_bp = Blueprint('students', __name__)

@student_bp.route('/me', methods=['GET'])
@jwt_required()
def get_logged_in_student():
    student_id = get_jwt_identity()
    student = Student.query.get_or_404(student_id)
    
    return jsonify({
        "id": student.id,
        "name": student.name,
        "email": student.email,
        "university": University.query.get(student.university_id).name,
        "has_paid": student.has_paid,
        "location": student.state,
        "us_citizen": student.us_citizen,
        "credits": student.credits
    })

@student_bp.route('/me', methods=['PUT'])
@jwt_required()
def update_logged_in_student():
    student_id = get_jwt_identity()
    student = Student.query.get_or_404(student_id)
    data = request.get_json()
    student.name = data.get('name', student.name)
    student.email = data.get('email', student.email)
    student.university_id = data.get('university_id', student.university_id)
    student.has_paid = data.get('has_paid', student.has_paid)
    student.state = data.get('location', student.state)
    student.us_citizen = data.get('us_citizen', student.us_citizen)
    db.session.commit()
    return jsonify({"message": "Student updated successfully"}), 200

@student_bp.route('/me/change_password', methods=['PUT'])
@jwt_required()
def change_password():
    student_id = get_jwt_identity()
    student = Student.query.get_or_404(student_id)
    data = request.get_json()
    old_password = data.get('old_password')
    if not check_password_hash(student.password, old_password):
        return jsonify({"message": "Invalid password"}), 400

    new_password = data.get('new_password')
    repeat_password = data.get('repeat_password')
    if new_password != repeat_password:
        return jsonify({"message": "Passwords do not match"}), 400
    student.password = generate_password_hash(new_password, method='pbkdf2:sha256')
    db.session.commit()
    return jsonify({"message": "Password updated successfully"}), 200

@student_bp.route('/me', methods=['DELETE'])
@jwt_required()
def delete_logged_in_student():
    student_id = get_jwt_identity()
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    response = jsonify({"message": "Student deleted successfully"})
    unset_jwt_cookies(response)
    return response, 200


# 根据学生的credits和学生的状态来查询课表总费用
@student_bp.route('/costs', methods=['GET'])
@jwt_required()
def get_student_course_cost():
    student_id = get_jwt_identity()
    student = Student.query.get_or_404(student_id)
    credits = student.credits
    university_id = student.university_id
    university_state = University.query.get_or_404(university_id).state
    cost = UniversityCourseCost.query.filter_by(university_id=university_id, total_credits=credits).first()
    if student.us_citizen and student.state == university_state:
        return jsonify({"cost": cost.total_in_state_cost})
    elif student.us_citizen and student.state != university_state:
        return jsonify({"cost": cost.total_out_state_cost})
    else:
        return jsonify({"cost": cost.total_international_cost})

