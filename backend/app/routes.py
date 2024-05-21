# backend/app/routes.py
from .controllers import auth_bp, student_bp, course_bp, university_bp, college_bp

def register_routes(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(student_bp, url_prefix='/students')
    app.register_blueprint(course_bp, url_prefix='/courses')
    app.register_blueprint(university_bp, url_prefix='/universities')
    app.register_blueprint(college_bp, url_prefix='/colleges')
