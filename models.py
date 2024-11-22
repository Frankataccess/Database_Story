from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Association Tables

# Parent-Student association
parent_student_association = db.Table(
    'parent_student_association',
    db.Column('student_id', db.String(12), db.ForeignKey('student_details.student_id'), primary_key=True),
    db.Column('parent_id', db.String(12), db.ForeignKey('parents_details.parents_id'), primary_key=True)
)

# Attendance-Student Association
attendance_student_association = db.Table(
    'attendance_student_association',
    db.Column('student_id', db.String(12), db.ForeignKey('student_details.student_id'), primary_key=True),
    db.Column('attendance_id', db.Integer, db.ForeignKey('attendance.attendance_id'), primary_key=True),
    db.Column('present', db.Boolean, nullable=False, default=False),
    db.Column('absence', db.Boolean, nullable=False, default=False)
)

# Behaviour-Student Association
behaviour_student_association = db.Table(
    'behaviour_student_association',
    db.Column('student_id', db.String(12), db.ForeignKey('student_details.student_id'), primary_key=True),
    db.Column('behaviour_id', db.Integer, db.ForeignKey('behaviour.behaviour_id'), primary_key=True),
    db.Column('positive', db.Integer, default=0),
    db.Column('negative', db.Integer, default=0)
)

# Class-Grades Association (Many-to-many relationship between Class and Students)
class_grades_association = db.Table(
    'class_grades_association',
    db.Column('class_id', db.String(20), db.ForeignKey('class_details.class_id'), primary_key=True),
    db.Column('student_id', db.String(12), db.ForeignKey('student_details.student_id'), primary_key=True),
    db.Column('grade', db.String(20), nullable=False)
)

# Models

class StudentDetails(db.Model):
    __tablename__ = 'student_details'
    
    student_id = db.Column(db.String(12), primary_key=True, index=True)
    student_first_name = db.Column(db.String(50), nullable=False)
    student_last_name = db.Column(db.String(50), nullable=False)
    student_email = db.Column(db.String(320), unique=True, nullable=False)
    student_gender = db.Column(db.String(12), nullable=False)
    student_dob = db.Column(db.Date, nullable=False)  # Changed to Date type
    student_year_group = db.Column(db.String(2), nullable=False)
    student_medical = db.Column(db.String(50))
    student_address = db.Column(db.String(200))
    student_photo = db.Column(db.String(50))
    student_roles = db.Column(db.String(20))
    
    # Relationships
    parents = db.relationship('ParentsDetails', secondary=parent_student_association, back_populates='students')
    attendance_records = db.relationship('Attendance', back_populates='student')  
    behaviours = db.relationship('Behaviour', secondary=behaviour_student_association, back_populates='students')
    classes = db.relationship('ClassDetails', secondary=class_grades_association, back_populates='students')


class ParentsDetails(db.Model):
    __tablename__ = 'parents_details'
    
    parents_id = db.Column(db.String(12), unique=True, primary_key=True, index=True)
    parents_first_name = db.Column(db.String(50))
    parents_last_name = db.Column(db.String(50))
    parents_phone_number = db.Column(db.String(15))
    parents_email = db.Column(db.String(320), unique=True)
    parents_gender = db.Column(db.String(12))
    parents_roles = db.Column(db.String(20))
    
    # Relationships
    students = db.relationship('StudentDetails', secondary=parent_student_association, back_populates='parents')


class ClassDetails(db.Model):
    __tablename__ = 'class_details'

    class_id = db.Column(db.String(20), primary_key=True, index=True)
    class_name = db.Column(db.String(200), nullable=False)
    teacher_id = db.Column(db.String(12), db.ForeignKey('teacher_details.teacher_id'), nullable=False)
    class_absent = db.Column(db.Boolean, nullable=False)
    class_late = db.Column(db.String(10), nullable=True)
    class_present = db.Column(db.Boolean, nullable=False)
    class_positive = db.Column(db.Integer, nullable=True)
    positive_reason = db.Column(db.String(50), nullable=True)
    class_negative = db.Column(db.Integer, nullable=True)
    negative_reason = db.Column(db.String(50), nullable=True)

    # Relationships
    teacher = db.relationship('TeacherDetails', back_populates='classes')
    students = db.relationship('StudentDetails', secondary=class_grades_association, back_populates='classes')
    attendance_records = db.relationship('Attendance', back_populates='class_')


class TeacherDetails(db.Model):
    __tablename__ = 'teacher_details'
    
    teacher_id = db.Column(db.String(12), primary_key=True, index=True)
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

    # Relationships
    classes = db.relationship('ClassDetails', back_populates='teacher')


class Attendance(db.Model):
    __tablename__ = 'attendance'

    attendance_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False)  # 'Present', 'Absent', 'Late'
    student_id = db.Column(db.String(12), db.ForeignKey('student_details.student_id'), nullable=False)
    class_id = db.Column(db.String(20), db.ForeignKey('class_details.class_id'), nullable=False)

    # Relationships
    student = db.relationship('StudentDetails', back_populates='attendance_records')
    class_ = db.relationship('ClassDetails', back_populates='attendance_records')


class Behaviour(db.Model):
    __tablename__ = 'behaviour'
    
    behaviour_id = db.Column(db.Integer, primary_key=True)
    behaviour = db.Column(db.Integer, nullable=False)
    positive = db.Column(db.Integer, default=0)
    negative = db.Column(db.Integer, default=0)
    
    # Relationships
    students = db.relationship('StudentDetails', secondary=behaviour_student_association, back_populates='behaviours')


class UserDetails(db.Model):
    __tablename__ = 'user_details'
    
    username = db.Column(db.String(50), primary_key=True)
    user_email = db.Column(db.String(320), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    roles = db.Column(db.String(20))
