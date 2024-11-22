from random import choice, randint
from datetime import datetime
from models import db, StudentDetails, ParentsDetails, TeacherDetails, ClassDetails, Behaviour, Attendance, UserDetails
from main import app

# Manually generated data

# Parents Data
parents_data = [
    {"parents_id": "P001", "parents_first_name": "John", "parents_last_name": "Doe", "parents_phone_number": "1234567890", "parents_email": "john.doe@example.com", "parents_gender": "Male", "parents_roles": "Father"},
    {"parents_id": "P002", "parents_first_name": "Jane", "parents_last_name": "Doe", "parents_phone_number": "0987654321", "parents_email": "jane.doe@example.com", "parents_gender": "Female", "parents_roles": "Mother"},
    {"parents_id": "P003", "parents_first_name": "Michael", "parents_last_name": "Smith", "parents_phone_number": "1122334455", "parents_email": "michael.smith@example.com", "parents_gender": "Male", "parents_roles": "Father"},
    {"parents_id": "P004", "parents_first_name": "Sarah", "parents_last_name": "Lee", "parents_phone_number": "2233445566", "parents_email": "sarah.lee@example.com", "parents_gender": "Female", "parents_roles": "Mother"},
    {"parents_id": "P005", "parents_first_name": "David", "parents_last_name": "Johnson", "parents_phone_number": "3344556677", "parents_email": "david.johnson@example.com", "parents_gender": "Male", "parents_roles": "Father"}
]

# Students Data
students_data = [
    {"student_id": "S001", "student_first_name": "Alice", "student_last_name": "Williams", "student_email": "alice.williams@example.com", "student_gender": "Female", "student_dob": datetime(2005, 5, 15), "student_year_group": "1", "student_medical": "None", "student_address": "123 Elm Street", "student_photo": "alice_photo.jpg", "student_roles": "Student", "parents": [parents_data[0], parents_data[1]]},
    {"student_id": "S002", "student_first_name": "Bob", "student_last_name": "Brown", "student_email": "bob.brown@example.com", "student_gender": "Male", "student_dob": datetime(2006, 8, 22), "student_year_group": "2", "student_medical": "Asthma", "student_address": "456 Oak Avenue", "student_photo": "bob_photo.jpg", "student_roles": "Student", "parents": [parents_data[2]]},
    {"student_id": "S003", "student_first_name": "Charlie", "student_last_name": "Davis", "student_email": "charlie.davis@example.com", "student_gender": "Male", "student_dob": datetime(2004, 3, 10), "student_year_group": "3", "student_medical": "None", "student_address": "789 Pine Lane", "student_photo": "charlie_photo.jpg", "student_roles": "Student", "parents": [parents_data[3]]},
    {"student_id": "S004", "student_first_name": "Diana", "student_last_name": "Evans", "student_email": "diana.evans@example.com", "student_gender": "Female", "student_dob": datetime(2007, 1, 5), "student_year_group": "1", "student_medical": "Allergies", "student_address": "101 Maple Drive", "student_photo": "diana_photo.jpg", "student_roles": "Student", "parents": [parents_data[4]]},
    {"student_id": "S005", "student_first_name": "Edward", "student_last_name": "Miller", "student_email": "edward.miller@example.com", "student_gender": "Male", "student_dob": datetime(2005, 12, 17), "student_year_group": "2", "student_medical": "None", "student_address": "202 Cedar Road", "student_photo": "edward_photo.jpg", "student_roles": "Student", "parents": [parents_data[0]]}
]

# Teachers Data
teachers_data = [
    {"teacher_id": "T001", "teacher_first_name": "Emma", "teacher_last_name": "Scott", "teacher_email": "emma.scott@example.com", "teacher_gender": "Female", "teacher_medical": "None", "teacher_address": "333 Birch Street", "teacher_photo": "emma_photo.jpg", "teacher_dbs": "DBS12345", "teacher_payment_info": "Bank Transfer", "teacher_roles": "Math Teacher"},
    {"teacher_id": "T002", "teacher_first_name": "Frank", "teacher_last_name": "King", "teacher_email": "frank.king@example.com", "teacher_gender": "Male", "teacher_medical": "None", "teacher_address": "444 Willow Lane", "teacher_photo": "frank_photo.jpg", "teacher_dbs": "DBS67890", "teacher_payment_info": "Cheque", "teacher_roles": "Science Teacher"},
    {"teacher_id": "T003", "teacher_first_name": "Grace", "teacher_last_name": "Taylor", "teacher_email": "grace.taylor@example.com", "teacher_gender": "Female", "teacher_medical": "None", "teacher_address": "555 Pine Avenue", "teacher_photo": "grace_photo.jpg", "teacher_dbs": "DBS11223", "teacher_payment_info": "Cash", "teacher_roles": "History Teacher"}
]

# Classes Data
classes_data = [
    {"class_id": "C001", "class_name": "Math 101", "teacher_id": "T001", "class_absent": False, "class_late": "No", "class_present": True, "class_positive": 4, "positive_reason": "Good Participation", "class_negative": 1, "negative_reason": "Late Submission"},
    {"class_id": "C002", "class_name": "Science 102", "teacher_id": "T002", "class_absent": False, "class_late": "Yes", "class_present": True, "class_positive": 3, "positive_reason": "Focused on Experiments", "class_negative": 2, "negative_reason": "Distraction"},
    {"class_id": "C003", "class_name": "History 201", "teacher_id": "T003", "class_absent": True, "class_late": "No", "class_present": False, "class_positive": 2, "positive_reason": "Answered Questions", "class_negative": 3, "negative_reason": "Talked Too Much"}
]

# Behaviours Data
behaviours_data = [
    {"behaviour_id": 1, "behaviour": 8, "positive": 5, "negative": 2},
    {"behaviour_id": 2, "behaviour": 6, "positive": 3, "negative": 4},
    {"behaviour_id": 3, "behaviour": 7, "positive": 4, "negative": 3}
]

# Attendance Data
attendance_data = [
    {"date": datetime(2024, 11, 1), "status": "Present", "student_id": "S001", "class_id": "C001"},
    {"date": datetime(2024, 11, 1), "status": "Absent", "student_id": "S002", "class_id": "C001"},
    {"date": datetime(2024, 11, 1), "status": "Late", "student_id": "S003", "class_id": "C002"},
    {"date": datetime(2024, 11, 2), "status": "Present", "student_id": "S004", "class_id": "C003"},
    {"date": datetime(2024, 11, 2), "status": "Absent", "student_id": "S005", "class_id": "C003"}
]

# User Data (Admin and Student)
users_data = [
    {"username": "admin", "user_email": "admin@example.com", "password": "admin123", "roles": "Admin"},
    {"username": "alicew", "user_email": "alice.williams@example.com", "password": "password123", "roles": "Student"},
    {"username": "bobbr", "user_email": "bob.brown@example.com", "password": "password123", "roles": "Student"},
    {"username": "charlied", "user_email": "charlie.davis@example.com", "password": "password123", "roles": "Student"},
    {"username": "edwardm", "user_email": "edward.miller@example.com", "password": "password123", "roles": "Student"}
]

def fill_database():
    with app.app_context():
        db.create_all()  # Ensure tables are created

        # Insert Parents
        parents_instances = {}
        for parent_data in parents_data:
            parent = ParentsDetails(**parent_data)
            db.session.add(parent)
            parents_instances[parent_data["parents_id"]] = parent
        
        # Insert Students
        for student_data in students_data:
            student_parents = [parents_instances[parent["parents_id"]] for parent in student_data["parents"]]
            student_data["parents"] = student_parents
            student = StudentDetails(**student_data)
            db.session.add(student)
        
        # Insert Teachers
        for teacher_data in teachers_data:
            teacher = TeacherDetails(**teacher_data)
            db.session.add(teacher)
        
        # Insert Classes
        for class_data in classes_data:
            class_obj = ClassDetails(**class_data)
            db.session.add(class_obj)
        
        # Insert Behaviours
        for behaviour_data in behaviours_data:
            behaviour = Behaviour(**behaviour_data)
            db.session.add(behaviour)
        
        # # Insert Attendance
        # for attendance_data in attendance_data:
        #     attendance = Attendance(**attendance_data)
        #     db.session.add(attendance)
        
        # Insert Users
        for user_data in users_data:
            user = UserDetails(**user_data)
            db.session.add(user)
        
        db.session.commit()
        print("Database filled with dummy data successfully!")


if __name__ == "__main__":
    fill_database()
