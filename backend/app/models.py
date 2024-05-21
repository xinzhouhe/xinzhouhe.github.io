# backend/app/models.py
from . import db

class University(db.Model):
    __tablename__ = 'university'
    id = db.Column('UniversityID', db.Integer, primary_key=True)
    name = db.Column('Name', db.String(255), nullable=False)
    state = db.Column('State', db.String(255), nullable=False)

    departments = db.relationship('Department', backref='university', lazy=True)
    courses = db.relationship('UniversityCourse', backref='university', lazy=True)
    course_costs = db.relationship('UniversityCourseCost', backref='university', lazy=True)
    requirements = db.relationship('Requirement', backref='university', lazy=True)

    def __repr__(self):
        return f'<University {self.name}>'


class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column('DepartmentID', db.Integer, primary_key=True)
    name = db.Column('DepartmentName', db.String(255), nullable=False)
    university_id = db.Column('UniversityID', db.Integer, db.ForeignKey('university.UniversityID'), nullable=False)

    def __repr__(self):
        return f'<Department {self.name}>'


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column('ID', db.Integer, primary_key=True)
    name = db.Column('Name', db.String(255), nullable=False)
    email = db.Column('Email', db.String(255), unique=True, nullable=False)
    password = db.Column('Password', db.String(128), nullable=False)
    university_id = db.Column('UniversityID', db.Integer, db.ForeignKey('university.UniversityID'), nullable=False)
    has_paid = db.Column('HasPaid', db.Boolean, default=False)
    state = db.Column('Location', db.String(255))
    us_citizen = db.Column('USCitizen', db.Boolean, default=True)
    credits = db.Column('Credits', db.Integer, default=0)

    courses = db.relationship('StudentCourse', backref='student', lazy=True)

    def __repr__(self):
        return f'<Student {self.name}>'


class UniversityCourse(db.Model):
    __tablename__ = 'university_courses'
    id = db.Column('CourseID', db.Integer, primary_key=True)
    name = db.Column('CourseName', db.String(255), nullable=False)
    course_code = db.Column('CourseCode', db.String(255), nullable=False)
    university_id = db.Column('UniversityID', db.Integer, db.ForeignKey('university.UniversityID'), nullable=False)
    department_id = db.Column('DepartmentID', db.Integer, db.ForeignKey('departments.DepartmentID'), nullable=False)
    credits = db.Column('Credits', db.Integer, nullable=False)

    equivalents = db.relationship('EquivalentCourse', backref='university_course', lazy=True)
    course_requirements = db.relationship('CourseRequirement', backref='university_course', lazy=True)

    def __repr__(self):
        return f'<UniversityCourse {self.name}>'


class CommunityCollege(db.Model):
    __tablename__ = 'college'
    id = db.Column('CollegeID', db.Integer, primary_key=True)
    name = db.Column('Name', db.String(255), nullable=False)
    state = db.Column('State', db.String(255), nullable=False)

    courses = db.relationship('CommunityCollegeCourse', backref='college', lazy=True)

    def __repr__(self):
        return f'<College {self.name}>'


class CommunityCollegeCourse(db.Model):
    __tablename__ = 'college_courses'
    id = db.Column('CourseID', db.Integer, primary_key=True)
    name = db.Column('CourseName', db.String(255), nullable=False)
    course_code = db.Column('CourseCode', db.String(255), nullable=False)
    college_id = db.Column('CollegeID', db.Integer, db.ForeignKey('college.CollegeID'), nullable=False)
    credits = db.Column('Credits', db.Integer, nullable=False)
    online = db.Column('Online', db.Integer, nullable=False) # 1-true, 2-false, 3-hybrid
    in_state_fee = db.Column('InStateFee', db.Float, nullable=False)
    out_state_fee = db.Column('OutStateFee', db.Float, nullable=False)
    international_fee = db.Column('InternationalFee', db.Float, nullable=False)

    equivalents = db.relationship('EquivalentCourse', backref='college_course', lazy=True)

    def __repr__(self):
        return f'<CommunityCollegeCourse {self.name}>'


class EquivalentCourse(db.Model):
    __tablename__ = 'equivalent_courses'
    id = db.Column('EquivalentID', db.Integer, primary_key=True)
    university_course_id = db.Column('UniversityCourseID', db.Integer, db.ForeignKey('university_courses.CourseID'), nullable=False)
    college_course_id = db.Column('CommunityCollegeCourseID', db.Integer, db.ForeignKey('college_courses.CourseID'), nullable=False)

    def __repr__(self):
        return f'<EquivalentCourse {self.university_course_id} - {self.college_course_id}>'


class StudentCourse(db.Model):
    __tablename__ = 'student_courses'
    id = db.Column('StudentCourseID', db.Integer, primary_key=True)
    student_id = db.Column('StudentID', db.Integer, db.ForeignKey('students.ID'), nullable=False)
    university_course_id = db.Column('CourseID', db.Integer, db.ForeignKey('university_courses.CourseID'), nullable=False)

    def __repr__(self):
        return f'<StudentCourse {self.student_id} - {self.university_course_id}>'


class Requirement(db.Model):
    __tablename__ = 'requirements'
    id = db.Column('RequirementID', db.Integer, primary_key=True)
    name = db.Column('RequirementName', db.String(255), nullable=False)
    university_id = db.Column('UniversityID', db.Integer, db.ForeignKey('university.UniversityID'), nullable=False)

    courses = db.relationship('CourseRequirement', backref='requirement', lazy=True)

    def __repr__(self):
        return f'<Requirement {self.name}>'


class CourseRequirement(db.Model):
    __tablename__ = 'course_requirements'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column('CourseID', db.Integer, db.ForeignKey('university_courses.CourseID'), nullable=False)
    requirement_id = db.Column('RequirementID', db.Integer, db.ForeignKey('requirements.RequirementID'), nullable=False)

    def __repr__(self):
        return f'<CourseRequirement {self.course_id} - {self.requirement_id}>'


class UniversityCourseCost(db.Model):
    __tablename__ = 'university_course_costs'
    id = db.Column('CostID', db.Integer, primary_key=True)
    university_id = db.Column('UniversityID', db.Integer, db.ForeignKey('university.UniversityID'))
    total_credits = db.Column('TotalCredits', db.Integer, nullable=False)
    total_in_state_cost = db.Column('TotalInStateCost', db.Float, nullable=False)
    total_out_state_cost = db.Column('TotalOutStateCost', db.Float, nullable=False)
    total_international_cost = db.Column('TotalInternationalCost', db.Float, nullable=False)

    def __repr__(self):
        return f'<UniversityCourseCost {self.university_id}>'
