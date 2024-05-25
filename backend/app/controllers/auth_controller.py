# backend/app/controllers/auth_controller.py
from flask import Blueprint, request, jsonify
from ..models import db, Student
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, unset_jwt_cookies, jwt_required, decode_token
from datetime import timedelta
from ..utils import send_reset_password_email

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    email_exists = Student.query.filter_by(email=data['email']).first()
    if email_exists:
        return jsonify({"message": "Email already exists"}), 400

    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    new_student = Student(
        name=data['name'],
        email=data['email'],
        password=hashed_password,
        university_id=data['university_id'],
        state=data['state'],
        us_citizen=data['us_citizen'],
        credits = 0,
        has_paid=False
    )
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Student registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    student = Student.query.filter_by(email=data['email']).first()
    if not student or not check_password_hash(student.password, data['password']):
        return jsonify({"message": "Mailbox does not exist or password is incorrect."}), 401
    
    access_token = create_access_token(identity=student.id)
    return jsonify(access_token=access_token), 200


@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    response = jsonify({"message": "Logout successful"})
    unset_jwt_cookies(response)
    return response, 200

@auth_bp.route('/send_reset_link', methods=['POST'])
def send_reset_link():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({"message": "Email is required"}), 400

    student = Student.query.filter_by(email=email).first()

    if not student:
        return jsonify({"message": "No user found with this email"}), 404

    token = create_access_token(identity=student.id, expires_delta=timedelta(hours=1))

    if send_reset_password_email(email, token):
        return jsonify({"message": "Reset link sent successfully"}), 200
    else:
        return jsonify({"message": "Failed to send reset link"}), 500

@auth_bp.route('/validate_reset_token/<token>', methods=['GET'])
def validate_reset_link(token):
    try:
        decoded_token = decode_token(token)
        student_id = decoded_token['sub']
        student = Student.query.get(student_id)
        if student:
            return jsonify({"message": "Valid link"}), 200
        else:
            return jsonify({"message": "Invalid link"}), 400
    except Exception as e:
        return jsonify({"message": "Invalid or expired link"}), 400
    
@auth_bp.route('/reset_password/<token>', methods=['POST'])
def reset_password(token):
    data = request.get_json()
    password = data.get('newPassword')

    try:
        decoded_token = decode_token(token)
        student_id = decoded_token['sub']
        student = Student.query.get(student_id)
        if student:
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            student.password = hashed_password
            db.session.commit()
            return jsonify({"message": "Password reset successfully"}), 200
        else:
            return jsonify({"message": "Invalid token"}), 400
    except Exception as e:
        return jsonify({"message": "Invalid or expired token"}), 400
