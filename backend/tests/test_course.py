import unittest
from flask import Flask
from app import register_routes, db, jwt
from app.models import UniversityCourse, University, Department, Requirement, Student, EquivalentCourse, CommunityCollegeCourse, CommunityCollege, CourseRequirement
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token

class CourseTestCase(unittest.TestCase):

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

            community_college = CommunityCollege(name="Test Community College", state="Test State")
            db.session.add(community_college)
            db.session.commit()

            self.college_id = community_college.id

            college_course = CommunityCollegeCourse(
                name="Intro to Programming",
                course_code="CCC101",
                credits=3,
                online=1,
                in_state_fee=100.0,
                out_state_fee=200.0,
                international_fee=300.0,
                college_id=self.college_id
            )
            db.session.add(college_course)
            db.session.commit()

            self.college_course_id = college_course.id

            equivalent_course = EquivalentCourse(
                university_course_id=self.course_id,
                college_course_id=self.college_course_id
            )
            db.session.add(equivalent_course)
            db.session.commit()

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

    def test_get_all_courses(self):
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], "Introduction to Programming")
        self.assertEqual(data[0]['course_code'], "CS101")

    def test_get_course(self):
        response = self.client.get(f'/courses/{self.course_id}')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data['name'], "Introduction to Programming")
        self.assertEqual(data['course_code'], "CS101")

    def test_get_student_courses(self):
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        response = self.client.get('/courses/me', headers=headers)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 0)  # No courses initially

        # Add a course to the student
        response = self.client.post(f'/courses/me/{self.course_id}', headers=headers, json={
            'course_id': self.course_id
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Course added successfully', response.json['message'])

        # Get student courses again
        response = self.client.get('/courses/me', headers=headers)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], "Introduction to Programming")

    def test_delete_student_course(self):
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

        # Add a course to the student
        response = self.client.post(f'/courses/me/{self.course_id}', headers=headers, json={
            'course_id': self.course_id
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Course added successfully', response.json['message'])

        # Delete the course from the student
        response = self.client.delete(f'/courses/me/{self.course_id}', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Course deleted successfully', response.json['message'])

        # Get student courses again
        response = self.client.get('/courses/me', headers=headers)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 0)

    def test_get_equivalent_courses(self):
        response = self.client.get(f'/courses/{self.course_id}/equivalents')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], "Intro to Programming")
        self.assertEqual(data[0]['course_code'], "CCC101")

    def test_get_student_equivalent_courses(self):
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        response = self.client.get(f'/courses/me/{self.course_id}/equivalents', headers=headers)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], "Intro to Programming")
        self.assertEqual(data[0]['course_code'], "CCC101")

    def test_get_equivalent_course_by_college(self):
        response = self.client.get(f'/courses/{self.course_id}/equivalents/{self.college_id}')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], "Intro to Programming")
        self.assertEqual(data[0]['course_code'], "CCC101")

    def test_get_student_equivalent_course_by_college(self):
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        response = self.client.get(f'/courses/me/{self.course_id}/equivalents/{self.college_id}', headers=headers)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], "Intro to Programming")
        self.assertEqual(data[0]['course_code'], "CCC101")

    def test_get_equivalent_courses_by_state(self):
        response = self.client.get(f'/courses/{self.course_id}/equivalents/Test State')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], "Intro to Programming")
        self.assertEqual(data[0]['course_code'], "CCC101")

    def test_get_student_equivalent_courses_by_state(self):
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        response = self.client.get(f'/courses/me/{self.course_id}/equivalents/Test State', headers=headers)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], "Intro to Programming")
        self.assertEqual(data[0]['course_code'], "CCC101")

if __name__ == '__main__':
    unittest.main()
