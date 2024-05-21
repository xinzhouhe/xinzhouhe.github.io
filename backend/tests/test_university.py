import unittest
from flask import Flask
from app import register_routes, db, jwt
from app.models import University, UniversityCourse, Department, Requirement, CourseRequirement, UniversityCourseCost, Student
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token

class UniversityTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['JWT_SECRET_KEY'] = 'test_secret'
        db.init_app(self.app)
        jwt.init_app(self.app)
        register_routes(self.app)
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

            # 创建测试数据
            university = University(name="Test University", state="Test State")
            db.session.add(university)
            db.session.commit()

            self.university_id = university.id

            department = Department(name="Computer Science", university_id=self.university_id)
            db.session.add(department)
            db.session.commit()

            self.department_id = department.id

            course = UniversityCourse(
                name="Introduction to Programming",
                course_code="CS101",
                credits=3,
                department_id=self.department_id,
                university_id=self.university_id
            )
            db.session.add(course)
            db.session.commit()

            self.course_id = course.id

            requirement = Requirement(name="Core Requirement", university_id=self.university_id)
            db.session.add(requirement)
            db.session.commit()

            self.requirement_id = requirement.id

            course_requirement = CourseRequirement(course_id=self.course_id, requirement_id=self.requirement_id)
            db.session.add(course_requirement)
            db.session.commit()

            course_cost = UniversityCourseCost(
                university_id=self.university_id,
                total_credits=30,
                total_in_state_cost=10000,
                total_out_state_cost=20000,
                total_international_cost=30000
            )
            db.session.add(course_cost)
            db.session.commit()

            self.course_cost_id = course_cost.id

            hashed_password = generate_password_hash('password', method='pbkdf2:sha256')
            student = Student(
                name='Test Student',
                email='test@student.com',
                password=hashed_password,
                university_id=self.university_id,
                state='Test State',
                us_citizen=True,
                credits=0,
                has_paid=False
            )
            db.session.add(student)
            db.session.commit()

            self.student_id = student.id
            self.access_token = create_access_token(identity=self.student_id)
        

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_all_universities(self):
        response = self.client.get('/universities/')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], "Test University")
        self.assertEqual(data[0]['state'], "Test State")

    def test_get_university(self):
        response = self.client.get(f'/universities/{self.university_id}')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data['name'], "Test University")
        self.assertEqual(data['state'], "Test State")

    def test_get_university_courses(self):
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        response = self.client.get('/universities/courses', headers=headers)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], "Introduction to Programming")
        self.assertEqual(data[0]['course_code'], "CS101")

    def test_get_university_requirements(self):
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        response = self.client.get('/universities/requirements', headers=headers)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], "Core Requirement")

    def test_get_university_departments(self):
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        response = self.client.get('/universities/departments', headers=headers)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], "Computer Science")

    def test_get_university_credits_costs(self):
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        response = self.client.get('/universities/costs', headers=headers)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['total_credits'], 30)
        self.assertEqual(data[0]['in-state'], 10000)
        self.assertEqual(data[0]['out-state'], 20000)
        self.assertEqual(data[0]['international'], 30000)

    def test_get_department_courses(self):
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        response = self.client.get(f'/universities/{self.department_id}/courses', headers=headers)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], "Introduction to Programming")
        self.assertEqual(data[0]['course_code'], "CS101")

    def test_get_requirement_courses(self):
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        response = self.client.get(f'/universities/{self.requirement_id}/courses', headers=headers)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], "Introduction to Programming")
        self.assertEqual(data[0]['course_code'], "CS101")

if __name__ == '__main__':
    unittest.main()
