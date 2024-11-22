import os
from flask import Flask
from models import db
from models import StudentDetails, ParentsDetails, ClassDetails, TeacherDetails, Attendance, Behaviour, UserDetails

# Base directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Flask app setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SECRET_KEY'] = 'hard to guess key'

# Initialize SQLAlchemy
db.init_app(app)

# Create all tables
with app.app_context():
    db.create_all()

