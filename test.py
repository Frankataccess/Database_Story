# pytest -v test.py

import pytest
import re
from datetime import datetime
from models import db, StudentDetails, ParentsDetails, TeacherDetails, Attendance, UserDetails, ClassDetails, Behaviour
from main import app


@pytest.fixture
def client():
    """Fixture for initializing app and database connection."""
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create tables
            from dummy_data import fill_database
            fill_database()  # Populate the database
            db.session.commit()  # Ensure data is committed to the DB
        yield client  # Return client to the test function


# Helper functions for validations
def is_valid_id(id: str) -> bool:
    return len(id) == 12 and id.isdigit()


def is_valid_name(name: str) -> bool:
    return name.isalpha()


def is_valid_email(email: str) -> bool:
    return "@" in email and "." in email


def is_valid_gender(gender: str) -> bool:
    return gender.isalpha()


def is_valid_year_group(year_group: str) -> bool:
    return year_group.isdigit() and len(year_group) <= 2


def is_valid_grades(grade: str) -> bool:
    return grade in ["A", "B", "C", "D", "E", "F"]


def is_valid_percentage(percentage: int) -> bool:
    return isinstance(percentage, int) and 0 <= percentage <= 100


def is_valid_roles(role: str) -> bool:
    return role in ["Admin", "Student", "Teacher"]


def is_valid_phone_number(phone: str) -> bool:
    return len(phone) == 10 and phone.isdigit()


def is_valid_password(password: str) -> bool:
    return len(password) >= 8 and any(char.isdigit() for char in password)


def is_valid_boolean(value: bool) -> bool:
    return isinstance(value, bool)


# Test the validity of the fields in the database
def test_valid_ids(client):
    """Test that IDs are 12 digits long."""
    students = StudentDetails.query.all()
    parents = ParentsDetails.query.all()
    teachers = TeacherDetails.query.all()

    for student in students:
        assert is_valid_id(student.student_id), f"Invalid student ID: {student.student_id}"
    for parent in parents:
        assert is_valid_id(parent.parents_id), f"Invalid parent ID: {parent.parents_id}"
    for teacher in teachers:
        assert is_valid_id(teacher.teacher_id), f"Invalid teacher ID: {teacher.teacher_id}"


def test_valid_names(client):
    """Test that names contain only letters."""
    students = StudentDetails.query.all()
    parents = ParentsDetails.query.all()
    teachers = TeacherDetails.query.all()

    for student in students:
        assert is_valid_name(student.student_first_name), f"Invalid student first name: {student.student_first_name}"
        assert is_valid_name(student.student_last_name), f"Invalid student last name: {student.student_last_name}"
    for parent in parents:
        assert is_valid_name(parent.parents_first_name), f"Invalid parent first name: {parent.parents_first_name}"
        assert is_valid_name(parent.parents_last_name), f"Invalid parent last name: {parent.parents_last_name}"
    for teacher in teachers:
        assert is_valid_name(teacher.teacher_first_name), f"Invalid teacher first name: {teacher.teacher_first_name}"
        assert is_valid_name(teacher.teacher_last_name), f"Invalid teacher last name: {teacher.teacher_last_name}"


# More tests follow, but the pattern remains the same...

