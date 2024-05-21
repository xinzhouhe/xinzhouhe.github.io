import unittest
from flask import Flask
from app import register_routes, db, jwt
from app.models import Student, University, UniversityCourseCost
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token

class StudentTestCase(unittest.TestCase):

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

            hashed_password = generate_password_hash('password', method='pbkdf2:sha256')
            student = Student(
                name='Test Student',
                email='test@student.com',
                password=hashed_password,
                university_id=self.university_id,
                state='Test State',
                us_citizen=True,
                credits=30,
                has_paid=False
            )
            db.session.add(student)
            db.session.commit()

            self.student_id = student.id
            self.access_token = create_access_token(identity=self.student_id)

            course_cost = UniversityCourseCost(
                university_id=self.university_id,
                total_credits=30,
                total_in_state_cost=10000,
                total_out_state_cost=20000,
                total_international_cost=30000
            )
            db.session.add(course_cost)
            db.session.commit()

        

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_logged_in_student(self):
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        response = self.client.get('/students/me', headers=headers)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data['name'], "Test Student")
        self.assertEqual(data['email'], "test@student.com")

    def test_update_logged_in_student(self):
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        response = self.client.put('/students/me', headers=headers, json={
            'name': 'Updated Student',
            'email': 'updated@student.com',
            'university_id': self.university_id,
            'has_paid': True,
            'location': 'Updated State',
            'us_citizen': False
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Student updated successfully', response.json['message'])

    def test_change_password(self):
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        response = self.client.put('/students/me/change_password', headers=headers, json={
            'old_password': 'password',
            'new_password': 'new_password',
            'repeat_password': 'new_password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Password updated successfully', response.json['message'])

    def test_delete_logged_in_student(self):
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        response = self.client.delete('/students/me', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Student deleted successfully', response.json['message'])

    def test_get_student_course_cost(self):
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        response = self.client.get('/students/costs', headers=headers)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data['cost'], 10000)

if __name__ == '__main__':
    unittest.main()
