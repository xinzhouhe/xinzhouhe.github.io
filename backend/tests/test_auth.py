import unittest
from flask import Flask
from app import register_routes, db, jwt
from app.models import Student, University
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token

class AuthTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['JWT_SECRET_KEY'] = 'test_secret'
        db.init_app(self.app)
        jwt.init_app(self.app)
        self.client = self.app.test_client()
        register_routes(self.app)

        with self.app.app_context():
            db.create_all()
            # 创建一个测试大学
            university = University(name="Test University", state="Test State")
            db.session.add(university)
            db.session.commit()
            self.university_id = university.id

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_register(self):
        response = self.client.post('/auth/register', json={
            'name': 'Test Student',
            'email': 'test@student.com',
            'password': 'testpassword',
            'university_id': self.university_id,
            'location': 'Test State',
            'status': True
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Student registered successfully', response.json['message'])

    def test_login(self):
        with self.app.app_context():
            hashed_password = generate_password_hash('testpassword', method='pbkdf2:sha256')
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

        response = self.client.post('/auth/login', json={
            'email': 'test@student.com',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json)

    def test_invalid_login(self):
        response = self.client.post('/auth/login', json={
            'email': 'test@student.com',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 401)
        self.assertIn('Invalid credentials', response.json['message'])

    def test_logout(self):
        with self.app.app_context():
            hashed_password = generate_password_hash('testpassword', method='pbkdf2:sha256')
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

            access_token = create_access_token(identity=student.id)
            headers = {
                'Authorization': f'Bearer {access_token}'
            }

            response = self.client.post('/auth/logout', headers=headers)
            self.assertEqual(response.status_code, 200)
            self.assertIn('Logout successful', response.json['message'])

if __name__ == '__main__':
    unittest.main()