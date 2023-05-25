from sqlalchemy.sql import func
from sqlalchemy import column, func
from . import db, marsh, app
from flask_login import UserMixin

from marshmallow import Schema, fields

class UserSchema(marsh.Schema):
    class Meta:
        fields = ('id', 'first_name', 'middle_name', 'last_name','sex' , 'email', 'password',  'detail_no', 'predict_no', 'user_type')
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    middle_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255), nullable=False)
    sex = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    # is_approve = db.Column(db.Boolean, nullable=False, default=0)
    detail_no = db.Column(db.Boolean, nullable=False, default=0)
    predict_no = db.Column(db.Boolean, nullable=False, default=0)
    user_type = db.Column(db.SmallInteger, nullable=False, default=1)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    pred_results = db.relationship('PredictionResult', backref='user', uselist=False)
    stud_details = db.relationship('StudentDetails', backref='user', uselist=False)

    def __init__(self, first_name, middle_name, last_name, sex, email, password, is_approve, detail_no, predict_no, user_type):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.sex = sex
        self.email = email
        self.password = password
        # self.is_approve = is_approve
        self.detail_no = detail_no
        self.predict_no = predict_no
        self.user_type = user_type


class PredictionResultSchema(marsh.Schema):
    class Meta:
        fields = ('result_id' , 'main_rank', 'sub_rank1', 'sub_rank2','app_no' 'oapr', 'english', 'reading', 'science', 'math', 'logic', 'user_id', 'date_predicted')

class PredictionResult(db.Model):
    result_id = db.Column(db.Integer, primary_key=True)
    main_rank = db.Column(db.String(255), nullable=False)
    sub_rank1 = db.Column(db.String(255), nullable=False)
    sub_rank2 = db.Column(db.String(255), nullable=False)
    app_no = db.Column(db.String(255), nullable=False)
    oapr = db.Column(db.String(255), nullable=False)
    english = db.Column(db.String(255), nullable=False)
    reading = db.Column(db.String(255), nullable=False)
    science = db.Column(db.String(255), nullable=False)
    math = db.Column(db.String(255), nullable=False)
    logic = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_predicted = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self, main_rank, sub_rank1, sub_rank2,app_no, oapr, english, reading, science, math, logic, user_id, date_predicted):
       
        self.main_rank = main_rank
        self.sub_rank1 = sub_rank1
        self.sub_rank2 = sub_rank2
        self.app_no = app_no
        self.oapr = oapr
        self.english = english
        self.reading = reading
        self.science = science
        self.math = math
        self.logic = logic
        self.user_id = user_id
        self.date_predicted = date_predicted
        

class StudentDetailsSchema(marsh.Schema):
    class Meta:
        fields = ('student_id', 'height','weight','bmi', 'types', 'track', 'school', 'gpa', 'user_id', 'date_registered')

class StudentDetails(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.String(255), nullable=False)
    weight = db.Column(db.String(255), nullable=False)
    bmi = db.Column(db.String(255), nullable=False)
    types = db.Column(db.String(255), nullable=False)
    track = db.Column(db.String(255), nullable=False)
    school = db.Column(db.String(255), nullable=False)
    gpa = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_registered = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self, height, weight, bmi, types, track, school, gpa, user_id, date_registered):
        self.height = height
        self.weight = weight
        self.bmi = bmi
        self.types = types
        self.track = track
        self.school = school
        self.gpa = gpa
        self.user_id = user_id
        self.date_registered = date_registered


class DescriptionSchema(marsh.Schema):
    class Meta:
        fields = ('des_id','course', 'course_des', 'college')

class Description(db.Model):
    des_id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(255), unique=True, nullable=False)
    course_des = db.Column(db.String(1000), nullable=False)
    college = db.Column(db.String(255), nullable=False)

    def __init__(self, course, course_des, college):
        self.course = course
        self.course_des = course_des
        self.college = college


class StudentCSV(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id_csv = db.Column(db.String(255), nullable=False)
    firstname_csv = db.Column(db.String(255), nullable=False)
    middlename_csv = db.Column(db.String(255), nullable=True)
    lastname_csv = db.Column(db.String(255), nullable=False)
    oapr_csv = db.Column(db.String(120), nullable=False)
    english_csv = db.Column(db.String(120), nullable=False)
    reading_csv = db.Column(db.String(120), nullable=False)
    science_csv = db.Column(db.String(120), nullable=False)
    math_csv = db.Column(db.String(120), nullable=False)
    logic_csv = db.Column(db.String(120), nullable=False)
    course_csv = db.Column(db.String(120), nullable=False)
    college_csv = db.Column(db.String(120), nullable=False)
    
    def __init__(self, student_id_csv, firstname_csv, middlename_csv, lastname_csv, oapr_csv, english_csv, reading_csv, science_csv, math_csv, logic_csv, course_csv,college_csv):
        self.student_id_csv = student_id_csv
        self.firstname_csv = firstname_csv
        self.middlename_csv = middlename_csv
        self.lastname_csv = lastname_csv
        self.oapr_csv = oapr_csv
        self.english_csv = english_csv
        self.reading_csv = reading_csv
        self.science_csv = science_csv
        self.math_csv = math_csv
        self.logic_csv = logic_csv
        self.course_csv = course_csv
        self.college_csv = college_csv

        