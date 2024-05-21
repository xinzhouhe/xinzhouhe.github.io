# backend/app/controllers/auth_controller.py
from flask import Blueprint, request, jsonify
from ..models import db, Student, University
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, unset_jwt_cookies, jwt_required
from marshmallow import ValidationError
from ..schemas.auth_schema import RegisterSchema, LoginSchema

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    try:
        register_data = RegisterSchema().load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    new_student = Student(
        name=data['name'],
        email=data['email'],
        password=hashed_password,
        university_id=data['university_id'],
        state=data['location'],
        us_citizen=data['status'],
        credits = 0,
        has_paid=False
    )
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Student registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    try:
        login_data = LoginSchema().load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    student = Student.query.filter_by(email=data['email']).first()
    if not student or not check_password_hash(student.password, data['password']):
        return jsonify({"message": "Invalid credentials"}), 401
    access_token = create_access_token(identity=student.id)
    return jsonify(access_token=access_token), 200


@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    response = jsonify({"message": "Logout successful"})
    unset_jwt_cookies(response)
    return response, 200
