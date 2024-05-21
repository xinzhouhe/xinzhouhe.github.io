import unittest
from flask import Flask
from app import register_routes, db, jwt
from app.models import CommunityCollege, CommunityCollegeCourse

class CollegeTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.init_app(self.app)
        jwt.init_app(self.app)
        self.client = self.app.test_client()
        register_routes(self.app)

        with self.app.app_context():
            db.create_all()

            # 创建测试数据
            college = CommunityCollege(name="Test College", state="Test State")
            db.session.add(college)
            db.session.commit()

            self.college_id = college.id

            course1 = CommunityCollegeCourse(
                name="Course 1",
                course_code="C1",
                credits=3,
                online=False,
                in_state_fee=100.0,
                out_state_fee=200.0,
                international_fee=300.0,
                college_id=self.college_id
            )
            course2 = CommunityCollegeCourse(
                name="Course 2",
                course_code="C2",
                credits=4,
                online=True,
                in_state_fee=150.0,
                out_state_fee=250.0,
                international_fee=350.0,
                college_id=self.college_id
            )
            db.session.add(course1)
            db.session.add(course2)
            db.session.commit()

        

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_all_colleges(self):
        response = self.client.get('/colleges/')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], "Test College")
        self.assertEqual(data[0]['state'], "Test State")

    def test_get_college(self):
        response = self.client.get(f'/colleges/{self.college_id}')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data['name'], "Test College")
        self.assertEqual(data['state'], "Test State")

    def test_get_college_courses(self):
        response = self.client.get(f'/colleges/{self.college_id}/courses')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['name'], "Course 1")
        self.assertEqual(data[0]['course_code'], "C1")
        self.assertEqual(data[1]['name'], "Course 2")
        self.assertEqual(data[1]['course_code'], "C2")

if __name__ == '__main__':
    unittest.main()
