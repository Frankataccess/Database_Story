from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Association Tables

# Parent-Student association
parent_student_association = db.Table(
    'parent_student_association',
    db.Column('student_id', db.String(12), db.ForeignKey('Student_Details.student_id'), primary_key=True),
    db.Column('parent_id', db.String(12), db.ForeignKey('Parents_Details.parents_id'), primary_key=True)
)

# Teacher-Class Association
teacher_class_association = db.Table(
    'teacher_class_association',
    db.Column('teacher_id', db.String(12), db.ForeignKey('Teacher_Details.teacher_id'), primary_key=True),
    db.Column('class_id', db.String(20), db.ForeignKey('Class_Details.class_id'), primary_key=True)
)

# Class-Grades Association
class_grades_association = db.Table(
    'class_grades_association',
    db.Column('class_id', db.String(20), db.ForeignKey('Class_Details.class_id'), primary_key=True),
    db.Column('student_id', db.String(12), db.ForeignKey('Student_Details.student_id'), primary_key=True),
    db.Column('class_grade', db.String(20))
)

# Attendance-Student Association
attendance_student_association = db.Table(
    'attendance_student_association',
    db.Column('student_id', db.String(12), db.ForeignKey('Student_Details.student_id'), primary_key=True),
    db.Column('attendance_id', db.Integer, db.ForeignKey('Attendance.attendance_id'), primary_key=True),
    db.Column('present', db.Boolean, nullable=False, default=False),
    db.Column('absence', db.Boolean, nullable=False, default=False)
)

# Behaviour-Student Association
behaviour_student_association = db.Table(
    'behaviour_student_association',
    db.Column('student_id', db.String(12), db.ForeignKey('Student_Details.student_id'), primary_key=True),
    db.Column('behaviour_id', db.Integer, db.ForeignKey('Behaviour.behaviour_id'), primary_key=True),
    db.Column('positive', db.Integer, default=0),
    db.Column('negative', db.Integer, default=0)
)

# Models

class Student_Details(db.Model):
    __tablename__ = 'Student_Details'
    
    student_id = db.Column(db.String(12), primary_key=True)
    student_first_name = db.Column(db.String(50), nullable=False)
    student_last_name = db.Column(db.String(50), nullable=False)
    student_email = db.Column(db.String(320), unique=True, nullable=False)
    student_gender = db.Column(db.String(12), nullable=False)
    student_dob = db.Column(db.Integer, nullable=False)
    student_year_group = db.Column(db.String(2), nullable=False)
    student_medical = db.Column(db.String(50))
    student_address = db.Column(db.String(200))
    student_photo = db.Column(db.String(50))
    student_class_ids = db.Column(db.String)
    student_roles = db.Column(db.String(20))
    
    # Relationships
    parents = db.relationship('Parents_Details', secondary=parent_student_association, back_populates='students')
    grades = db.relationship('Class_Details', secondary=class_grades_association, back_populates='students_grades')
    attendance_records = db.relationship('Attendance', secondary=attendance_student_association, back_populates='students')
    behaviours = db.relationship('Behaviour', secondary=behaviour_student_association, back_populates='students')


class Parents_Details(db.Model):
    __tablename__ = 'Parents_Details'
    
    parents_id = db.Column(db.String(12), unique=True, primary_key=True)
    parents_first_name = db.Column(db.String(50))
    parents_last_name = db.Column(db.String(50))
    parents_phone_number = db.Column(db.String(15))
    parents_email = db.Column(db.String(320), unique=True)
    parents_gender = db.Column(db.String(12))
    parents_roles = db.Column(db.String(20))
    
    # Relationships
    students = db.relationship('Student_Details', secondary=parent_student_association, back_populates='parents')


class Class_Details(db.Model):
    __tablename__ = 'Class_Details'
    
    class_id = db.Column(db.String(20), primary_key=True)
    class_name = db.Column(db.String(200), nullable=False)
    teacher_id = db.Column(db.String(12), db.ForeignKey('Teacher_Details.teacher_id'), nullable=False)
    teacher_first_name = db.Column(db.String(50), nullable=False)
    teacher_last_name = db.Column(db.String(50), nullable=False)
    
    # Relationships
    students_grades = db.relationship('Student_Details', secondary=class_grades_association, back_populates='grades')


class Teacher_Details(db.Model):
    __tablename__ = 'Teacher_Details'
    
    teacher_id = db.Column(db.String(12), primary_key=True)
    teacher_first_name = db.Column(db.String(50), nullable=False)
    teacher_last_name = db.Column(db.String(50), nullable=False)
    teacher_email = db.Column(db.String(320), unique=True, nullable=False)
    teacher_gender = db.Column(db.String(20))
    teacher_medical = db.Column(db.String(500))
    teacher_address = db.Column(db.String(200))
    teacher_photo = db.Column(db.String(300))
    teacher_dbs = db.Column(db.String(5000))
    teacher_payment_info = db.Column(db.String(500))
    teacher_roles = db.Column(db.String(20))


class Attendance(db.Model):
    __tablename__ = 'Attendance'
    
    attendance_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    
    # Relationships
    students = db.relationship('Student_Details', secondary=attendance_student_association, back_populates='attendance_records')


class Behaviour(db.Model):
    __tablename__ = 'Behaviour'
    
    behaviour_id = db.Column(db.Integer, primary_key=True)
    behaviour = db.Column(db.Integer, nullable=False)
    positive = db.Column(db.Integer, default=0)
    negative = db.Column(db.Integer, default=0)
    
    # Relationships
    students = db.relationship('Student_Details', secondary=behaviour_student_association, back_populates='behaviours')


class Grades(db.Model):
    __tablename__ = 'Grades'
    
    grade_id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.String(20), db.ForeignKey('Class_Details.class_id'))
    student_id = db.Column(db.String(12), db.ForeignKey('Student_Details.student_id'))
    grade = db.Column(db.String(20), nullable=False)


class User_Details(db.Model):
    __tablename__ = 'user_details'
    
    username = db.Column(db.String(50), primary_key=True)
    user_email = db.Column(db.String(320), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    roles = db.Column(db.String(20))
