# backend/manage.py
from flask.cli import with_appcontext
from flask_migrate import Migrate
from app import create_app, db
from app.models import*
from flask_cors import CORS
import click
import os
import json
import unittest

app = create_app()
CORS(app)
migrate = Migrate(app, db)

@app.cli.command("init-db")
@with_appcontext
def init_db():
    """Initialize the database."""
    db.create_all()
    click.echo("Database initialized.")

@app.cli.command("clean-db")
@with_appcontext
def clean_db():
    """Clean the database by dropping all tables."""
    db.drop_all()
    click.echo("Database cleaned.")

@app.cli.command("pump-db")
@with_appcontext
def pump_db():
    """Pump the database with data in the folder."""
    data_folder = os.path.join(os.path.dirname(__file__), "data")
    university_folder = os.path.join(data_folder, 'university')
    course_folder = os.path.join(data_folder, 'course')

    # Process university data
    for filename in os.listdir(university_folder):
        if filename.endswith('.json'):
            with open(os.path.join(university_folder, filename), 'r') as uf:
                university_data = json.load(uf)

                for uni in university_data['data']:
                    university = University.query.filter_by(
                        name=uni['university_name'],
                        state=uni['university_state']
                    ).first()

                    if not university:
                        university = University(
                            name=uni['university_name'],
                            state=uni['university_state']
                        )
                        db.session.add(university)
                        db.session.commit()  # Commit to generate the ID

                    for price in uni['prices']:
                        course_cost = UniversityCourseCost.query.filter_by(
                            university_id=university.id,
                            total_credits=price['credits']
                        ).first()

                        if not course_cost:
                            course_cost = UniversityCourseCost(
                                university_id=university.id,
                                total_credits=price['credits'],
                                total_in_state_cost=price['in_state'],
                                total_out_state_cost=price['out_of_state'],
                                total_international_cost=price['international']
                            )
                            db.session.add(course_cost)
                        else:
                            course_cost.total_in_state_cost = price['in_state']
                            course_cost.total_out_state_cost = price['out_of_state']
                            course_cost.total_international_cost = price['international']
                    db.session.commit()

    # Process course data
    for filename in os.listdir(course_folder):
        if filename.endswith('.json'):
            with open(os.path.join(course_folder, filename), 'r') as cf:
                courses_data = json.load(cf)

                for course_set in courses_data['data']:
                    university = University.query.filter_by(
                        name=course_set['university_name'],
                        state=course_set['university_state']
                    ).first()

                    if not university:
                        university = University(
                            name=course_set['university_name'],
                            state=course_set['university_state']
                        )
                        db.session.add(university)
                        db.session.commit()
                    
                    community_college = CommunityCollege.query.filter_by(
                        name=course_set['community_college_name'],
                        state=course_set['community_college_state']
                    ).first()

                    if not community_college:
                        community_college = CommunityCollege(
                            name=course_set['community_college_name'],
                            state=course_set['community_college_state']
                        )
                        db.session.add(community_college)
                        db.session.commit()

                    for course in course_set['courses']:
                        # Insert or get department
                        department = Department.query.filter_by(
                            name=course['university_department'],
                            university_id=university.id
                        ).first()
                        if not department:
                            department = Department(
                                name=course['university_department'],
                                university_id=university.id
                            )
                            db.session.add(department)
                            db.session.commit()

                        # Insert or get UniversityCourse
                        university_course = UniversityCourse.query.filter_by(
                            course_code=course['university_course_code'],
                            name=course['university_course_name'],
                            university_id=university.id,
                            department_id=department.id,
                            credits=course['uc_credits']
                        ).first()

                        if not university_course:
                            university_course = UniversityCourse(
                                course_code=course['university_course_code'],
                                name=course['university_course_name'],
                                university_id=university.id,
                                department_id=department.id,
                                credits=course['uc_credits']
                            )
                            db.session.add(university_course)
                            db.session.commit()

                        # Insert CourseRequirement
                        for general_ed in course['gen_ed_attributes']:
                            requirement = Requirement.query.filter_by(
                                name=general_ed,
                                university_id=university.id
                            ).first()
                            if not requirement:
                                requirement = Requirement(
                                    name=general_ed,
                                    university_id=university.id
                                )
                                db.session.add(requirement)
                                db.session.commit()
                            
                            course_requirement = CourseRequirement.query.filter_by(
                                requirement_id=requirement.id,
                                course_id=university_course.id
                            ).first()
                            if not course_requirement:
                                course_requirement = CourseRequirement(
                                    requirement_id=requirement.id,
                                    course_id=university_course.id
                                )
                                db.session.add(course_requirement)
                                db.session.commit()

                        # Insert or get CollegeCourse
                        college_course = CommunityCollegeCourse.query.filter_by(
                            course_code=course['cc_class_code'],
                            name=course['cc_course_name'],
                            college_id=community_college.id,
                            credits=course['cc_credits'],
                            online=course['cc_online']
                        ).first()
                        if not college_course:
                            college_course = CommunityCollegeCourse(
                                course_code=course['cc_class_code'],
                                name=course['cc_course_name'],
                                college_id=community_college.id,
                                credits=course['cc_credits'],
                                in_state_fee=course['cc_in_state_fee'],
                                out_state_fee=course['cc_out_state_fee'],
                                international_fee=course['cc_international_fee'],
                                online=course['cc_online']
                            )
                            db.session.add(college_course)
                            db.session.commit()
                        else:
                            college_course.in_state_fee = course['cc_in_state_fee']
                            college_course.out_state_fee = course['cc_out_state_fee']
                            college_course.international_fee = course['cc_international_fee']
                            college_course.online = course['cc_online']
                            db.session.commit()

                        # Insert EquivalentCourse
                        equivalent_course = EquivalentCourse.query.filter_by(
                            university_course_id=university_course.id,
                            college_course_id=college_course.id
                        ).first()
                        if not equivalent_course:
                            equivalent_course = EquivalentCourse(
                                university_course_id=university_course.id,
                                college_course_id=college_course.id
                            )
                            db.session.add(equivalent_course)
                    db.session.commit()

    click.echo("Database pumped with data.")

@app.cli.command("run-tests")
@with_appcontext
def run_tests():
    """Run the tests."""
    tests = unittest.TestLoader().discover('tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        print("All tests passed.")
        return 0
    print("Some tests failed.")
    return 1

@app.cli.command("reset-db")
@with_appcontext
def reset_db():
    """Reset the database by cleaning and pumping data."""
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run()
