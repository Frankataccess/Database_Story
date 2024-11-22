from main import db, app
from models import Student_Details, Teacher_Details, Parents_Details, Class_Details

def insert_dummy_data():
    with app.app_context():
        try:
            # Clear existing data (optional)
            db.session.query(Student_Details).delete()
            db.session.query(Teacher_Details).delete()
            db.session.query(Parents_Details).delete()
            db.session.query(Class_Details).delete()
            db.session.commit()
            
            # Insert dummy students
            students = [
                Student_Details(
                    student_id="S001", student_first_name="John", student_last_name="Doe", 
                    student_email="john.doe@example.com", student_gender="Male", student_dob=20010101, 
                    student_year_group="10", student_medical="None", student_address="123 Main St", 
                    student_photo="john_photo.jpg", student_class_ids="C001", student_roles="Student"
                ),
                Student_Details(
                    student_id="S002", student_first_name="Jane", student_last_name="Smith", 
                    student_email="jane.smith@example.com", student_gender="Female", student_dob=20020202, 
                    student_year_group="10", student_medical="Asthma", student_address="456 Elm St", 
                    student_photo="jane_photo.jpg", student_class_ids="C001", student_roles="Student"
                ),
                Student_Details(
                    student_id="S003", student_first_name="Emily", student_last_name="Johnson", 
                    student_email="emily.johnson@example.com", student_gender="Female", student_dob=20030303, 
                    student_year_group="11", student_medical="None", student_address="789 Oak St", 
                    student_photo="emily_photo.jpg", student_class_ids="C002", student_roles="Student"
                ),
            ]
            
            # Insert dummy teachers
            teachers = [
                Teacher_Details(
                    teacher_id="T001", teacher_first_name="Mr.", teacher_last_name="Brown", 
                    teacher_email="mr.brown@example.com", teacher_gender="Male", teacher_medical="None", 
                    teacher_address="101 Maple St", teacher_photo="mr_brown_photo.jpg", 
                    teacher_dbs="DBS12345", teacher_payment_info="£5000", teacher_roles="Math Teacher"
                ),
                Teacher_Details(
                    teacher_id="T002", teacher_first_name="Ms.", teacher_last_name="White", 
                    teacher_email="ms.white@example.com", teacher_gender="Female", teacher_medical="None", 
                    teacher_address="202 Pine St", teacher_photo="ms_white_photo.jpg", 
                    teacher_dbs="DBS67890", teacher_payment_info="£4500", teacher_roles="English Teacher"
                ),
            ]
            
            # Insert dummy parents
            parents = [
                Parents_Details(
                    parents_id="P001", parents_first_name="Tom", parents_last_name="Doe", 
                    parents_phone_number="1234567890", parents_email="tom.doe@example.com", 
                    parents_gender="Male", parents_roles="Father"
                ),
                Parents_Details(
                    parents_id="P002", parents_first_name="Mary", parents_last_name="Smith", 
                    parents_phone_number="0987654321", parents_email="mary.smith@example.com", 
                    parents_gender="Female", parents_roles="Mother"
                ),
            ]
            
            # Insert dummy classes
            classes = [
                Class_Details(
                    class_id="C001", class_name="Math 101", teacher_id="T001", 
                    teacher_first_name="Mr.", teacher_last_name="Brown"
                ),
                Class_Details(
                    class_id="C002", class_name="English 101", teacher_id="T002", 
                    teacher_first_name="Ms.", teacher_last_name="White"
                ),
            ]
            
            # Add data to session
            db.session.add_all(students)
            db.session.add_all(teachers)
            db.session.add_all(parents)
            db.session.add_all(classes)
            db.session.commit()

            # Linking relationships (example for student-parent relationships)
            students[0].parents.append(parents[0])  # Link Student S001 with Parent P001
            students[1].parents.append(parents[1])  # Link Student S002 with Parent P002
            students[0].student_class_ids = "C001"
            students[1].student_class_ids = "C001"
            students[2].student_class_ids = "C002"

            db.session.commit()
            print("Dummy data inserted successfully!")
        except Exception as e:
            db.session.rollback()
            print(f"Error inserting data: {e}")

# Run the insertion
if __name__ == "__main__":
    insert_dummy_data()
