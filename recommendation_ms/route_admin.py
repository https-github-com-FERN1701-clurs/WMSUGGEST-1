from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify, make_response, session,Response
from flask_login import login_required, current_user
from .models import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy import delete, desc, asc
from sqlalchemy import delete
from sqlalchemy import select
import json
from os import path
import os
import pandas as pd
from io import TextIOWrapper
import csv
from .auth import send_link, send_link_disapproved 
import matplotlib.pyplot as plt
import io
import random
import base64

_route_admin = Blueprint('_route_admin', __name__)

dataset = os.path.join(os.path.abspath(os.path.dirname(__file__)),"model/populations.csv")
dataset = pd.read_csv(dataset)

def plot_graph():
    

    x =['2018-2019','2019-2020','2020-2021','2021-2022','2022-2023']
    y =[3305,3749,3977,3730,3044]
    plt.bar(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Bar Chart Example')

    # convert plot to PNG image
    pngImage = io.BytesIO()
    plt.savefig(pngImage, format='png')
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String



@_route_admin.route('/export/csv')
def export_csv():
   
    # Query data from the database
    data = db.session.query(User, StudentDetails,PredictionResult).join(StudentDetails).join(PredictionResult).all()

    # Convert data to a pandas DataFrame
    df = pd.DataFrame([{ 'Student_id': student.student_id, 'First Name': user.first_name, 'Middle Name': user.middle_name, 'Last Name': user.last_name, 'Sex': user.sex, 'Email': user.email,  'Height': student.height, 'Weight': student.weight, 'BMI': student.bmi, 'Perosnality type': student.types, 'SHS Strand/Track': student.track, 'SHS School': student.school, 'SHS GPA': student.gpa, 'Application No.': result.app_no,'OAPR': result.oapr,'English Proficiency': result.english,'Reading Comprehension': result.reading,'Sceince Process': result.science,'Quantitative Skills': result.math,'Abstract Thinking Skills': result.logic,'Suggestion 1': result.main_rank,'Suggestion 2': result.sub_rank1,'Suggestion 3': result.sub_rank2,} for user, student, result in data])

    # Create a CSV file in memory
    csv_output = df.to_csv(index=False)

    # Return the CSV file as a response
    response = Response(csv_output, mimetype='text/csv')
    response.headers.set("Content-Disposition", "attachment", filename="data.csv")
    return response

@_route_admin.route('/admin_form', methods=['GET'])
def admin_form():
    auth_user=current_user
    if auth_user.is_authenticated:
        if auth_user.user_type == 1:
            return redirect(url_for('.admin_dashboard'))
        else:
            return redirect(url_for('_auth.index'))
    return render_template('Admin/admin_form.html')

@_route_admin.route('/admin_dashboard', methods=['GET',  'POST'])
# @login_required
def admin_dashboard():

    if request.method == 'GET':
        # Current Logged User
        auth_user=current_user
        page = request.args.get('page', 1, type=int)

        # Data for search
        search = request.args.getlist('search')
        search = (','.join(search))

        male =db.session.query(User,StudentDetails).join(StudentDetails).filter(User.user_type == 1,User.sex=='Male').count()
        female = db.session.query(User,StudentDetails).join(StudentDetails).filter(User.user_type == 1,User.sex=='Female').count()

        stem = StudentDetails.query.filter(StudentDetails.track=='STEM').count()
        abm = StudentDetails.query.filter(StudentDetails.track=='ABM').count()
        humss = StudentDetails.query.filter(StudentDetails.track=='HUMSS').count()
        gas = StudentDetails.query.filter(StudentDetails.track=='GAS').count()
        afa = StudentDetails.query.filter(StudentDetails.track=='AFA').count()
        he = StudentDetails.query.filter(StudentDetails.track=='HE').count()
        ia = StudentDetails.query.filter(StudentDetails.track=='IA').count()
        ict = StudentDetails.query.filter(StudentDetails.track=='ICT').count()
        arts = StudentDetails.query.filter(StudentDetails.track=='ARTS AND DESIGN').count()
        sports = StudentDetails.query.filter(StudentDetails.track=='SPORTS').count()
        under = StudentDetails.query.filter(StudentDetails.bmi<18.5).count()
        normal = StudentDetails.query.filter(StudentDetails.bmi>=18.5,StudentDetails.bmi<24.9 ).count()
        over = StudentDetails.query.filter(StudentDetails.bmi>24.9,StudentDetails.bmi<30 ).count()
        obese = StudentDetails.query.filter(StudentDetails.bmi>30 ).count()

        intja = StudentDetails.query.filter(StudentDetails.types=='INTJ-A').count()
        intjt = StudentDetails.query.filter(StudentDetails.types=='INTJ-T').count()
        intpa = StudentDetails.query.filter(StudentDetails.types=='INTP-A').count()
        intpt = StudentDetails.query.filter(StudentDetails.types=='INTP-T').count()
        entja = StudentDetails.query.filter(StudentDetails.types=='ENTJ-A').count()
        entjt = StudentDetails.query.filter(StudentDetails.types=='ENTJ-T').count()
        entpa = StudentDetails.query.filter(StudentDetails.types=='ENTP-A').count()
        entpt = StudentDetails.query.filter(StudentDetails.types=='ENTP-T').count()

        infja = StudentDetails.query.filter(StudentDetails.types=='INFJ-A').count()
        infjt = StudentDetails.query.filter(StudentDetails.types=='INFJ-T').count()
        infpa = StudentDetails.query.filter(StudentDetails.types=='INFP-A').count()
        infpt = StudentDetails.query.filter(StudentDetails.types=='INFP-T').count()
        enfja = StudentDetails.query.filter(StudentDetails.types=='ENFJ-A').count()
        enfjt = StudentDetails.query.filter(StudentDetails.types=='ENFJ-T').count()
        enfpa = StudentDetails.query.filter(StudentDetails.types=='ENFP-A').count()
        enfpt = StudentDetails.query.filter(StudentDetails.types=='ENFP-T').count()

        istja = StudentDetails.query.filter(StudentDetails.types=='ISTJ-A').count()
        istjt = StudentDetails.query.filter(StudentDetails.types=='ISTJ-T').count()
        isfja = StudentDetails.query.filter(StudentDetails.types=='ISFJ-A').count()
        isfjt = StudentDetails.query.filter(StudentDetails.types=='ISFJ-T').count()
        estja = StudentDetails.query.filter(StudentDetails.types=='ESTJ-A').count()
        estjt = StudentDetails.query.filter(StudentDetails.types=='ESTJ-T').count()
        esfja = StudentDetails.query.filter(StudentDetails.types=='ESFJ-A').count()
        esfjt = StudentDetails.query.filter(StudentDetails.types=='ESFJ-T').count()

        istpa = StudentDetails.query.filter(StudentDetails.types=='ISTP-A').count()
        istpt = StudentDetails.query.filter(StudentDetails.types=='ISTP-T').count()
        isfpa = StudentDetails.query.filter(StudentDetails.types=='ISFP-A').count()
        isfpt = StudentDetails.query.filter(StudentDetails.types=='ISFP-T').count()
        estpa = StudentDetails.query.filter(StudentDetails.types=='ESTP-A').count()
        estpt = StudentDetails.query.filter(StudentDetails.types=='ESTP-T').count()
        esfpa = StudentDetails.query.filter(StudentDetails.types=='ESFP-A').count()
        esfpt = StudentDetails.query.filter(StudentDetails.types=='ESFP-T').count()
        
   
    students_record = db.session.query(User,PredictionResult).join(PredictionResult).filter( User.user_type == 1,User.id==PredictionResult.user_id).paginate(page=page)
    auth_user=current_user
    return render_template("Admin/admin_page.html", auth_user=auth_user, students_record=students_record, search=search,male = json.dumps(male), female = json.dumps(female),
      stem = json.dumps(stem), abm = json.dumps(abm),humss = json.dumps(humss), gas = json.dumps(gas),afa = json.dumps(afa), he = json.dumps(he),ia = json.dumps(ia), ict = json.dumps(ict), arts = json.dumps(arts), sports = json.dumps(sports),under = json.dumps(under), normal = json.dumps(normal), over = json.dumps(over), obese = json.dumps(obese),
      intja = json.dumps(intja),intjt = json.dumps(intjt),intpa = json.dumps(intpa),intpt = json.dumps(intpt),entja = json.dumps(entja),entjt = json.dumps(entjt),entpa = json.dumps(entpa),entpt = json.dumps(entpt),
      infja = json.dumps(infja),infjt = json.dumps(infjt),infpa = json.dumps(infpa),infpt = json.dumps(infpt),enfja = json.dumps(enfja),enfjt = json.dumps(enfjt),enfpa = json.dumps(enfpa),enfpt = json.dumps(enfpt),
      istja = json.dumps(istja),istjt = json.dumps(istjt),isfja = json.dumps(isfja),isfjt = json.dumps(isfjt),estja = json.dumps(estja),estjt = json.dumps(estjt),esfja = json.dumps(esfja),esfjt = json.dumps(esfjt),
      istpa = json.dumps(istpa),istpt = json.dumps(istpt),isfpa = json.dumps(isfpa),isfpt = json.dumps(isfpt),estpa = json.dumps(estpa),estpt = json.dumps(estpt),esfpa = json.dumps(esfpa),esfpt = json.dumps(esfpt))


@_route_admin.route('/admin_result',methods=['GET', 'POST'])
@login_required
def admin_result():
    
    if request.method == 'POST':

        auth_user=current_user
        
        # students_record = db.session.query(User, PredictionResult).filter(stud_id.id == int(request.form['user_id'])).filter(PredictionResult.user_id == int(request.form['user_id'])).group_by(PredictionResult.result_id).paginate(page=page)
        stud_id = PredictionResult.query.filter(PredictionResult.user_id==request.form['user_id'],PredictionResult.app_no==request.form['user_app'])
        stud_bmi = StudentDetails.query.filter(StudentDetails.user_id==request.form['user_id']).first()
        bmi=''
        if float(stud_bmi.bmi)<18.5:
            bmi='Underweight'
        elif float(stud_bmi.bmi)>18.5 and float(stud_bmi.bmi)<24.9:
            bmi='Normal'
        elif float(stud_bmi.bmi)>24.9 and float(stud_bmi.bmi)<30:
            bmi='Overweight'
        else:
            bmi='Obese'
        
        students_record = db.session.query(User,StudentDetails).filter(StudentDetails.user_id==request.form['user_id']).first()
        return render_template("Admin/admin_results.html", auth_user=auth_user,stud_id=stud_id,stud_bmi=stud_bmi,bmi=bmi)



@_route_admin.route('/admin_result_csv',methods=['GET', 'POST'])
@login_required
def admin_result_csv():
    
    if request.method == 'POST':

        auth_user=current_user
        
        # students_record = db.session.query(User, PredictionResult).filter(stud_id.id == int(request.form['user_id'])).filter(PredictionResult.user_id == int(request.form['user_id'])).group_by(PredictionResult.result_id).paginate(page=page)
        stud = User.query.filter(User.first_name==request.form['first_csv'],User.middle_name==request.form['middle_csv'],User.last_name==request.form['last_csv']).first()
        stud_count=User.query.filter(User.first_name==request.form['first_csv'],User.middle_name==request.form['middle_csv'],User.last_name==request.form['last_csv']).count()
        if stud_count == 0:
            stud_id=0
            main='No data'
            sub1='No data'
            sub2='No data'
            stud = StudentCSV.query.filter(StudentCSV.firstname_csv==request.form['first_csv'],StudentCSV.middlename_csv==request.form['middle_csv'],StudentCSV.lastname_csv==request.form['last_csv'],StudentCSV.course_csv==request.form['course_csv']).first()

        else:
            stud_id=stud.id
            stud_course = PredictionResult.query.filter(PredictionResult.user_id==stud_id).first()
            main=stud_course.main_rank
            sub1=stud_course.sub_rank1
            sub2=stud_course.sub_rank2
    
        
        
        stud_csv=StudentCSV.query.filter(StudentCSV.firstname_csv==request.form['first_csv'],StudentCSV.middlename_csv==request.form['middle_csv'],StudentCSV.lastname_csv==request.form['last_csv'],StudentCSV.course_csv==request.form['course_csv']).first()
        acc=''
        if main==stud_csv.course_csv:
            acc='100'
        elif sub1==stud_csv.course_csv:
            acc='66'
        elif sub2==stud_csv.course_csv:
            acc='33'
        else :
            acc='0'
    
        
        
        return render_template("Admin/admin_results_csv.html", auth_user=auth_user,stud=stud,main=main,sub1=sub1,sub2=sub2,stud_csv=stud_csv,acc=acc)



@_route_admin.route('/admin_analytic', methods=['GET'])
@login_required
def admin_analytic():
    if request.method == 'GET':
        male = User.query.filter(User.sex=='Male').count()
        female = User.query.filter(User.sex=='Female').count()
       
        broad = StudentCSV.query.filter(StudentCSV.course_csv=='AB BROADCASTING').count()
        hist = StudentCSV.query.filter(StudentCSV.course_csv=='AB HISTORY').count()
        journ = StudentCSV.query.filter(StudentCSV.course_csv=='AB JOURNALISM').count()
        polsci = StudentCSV.query.filter(StudentCSV.course_csv=='AB POLITICAL SCIENCE').count()
        bat = StudentCSV.query.filter(StudentCSV.course_csv=='BACHELOR AGRICULTURAL TECHNOLOGY').count()
        beed = StudentCSV.query.filter(StudentCSV.course_csv=='BACHELOR IN ELEMENTARY EDUCATION').count()
        bcae = StudentCSV.query.filter(StudentCSV.course_csv=='BACHELOR OF CULTURE AND ARTS EDUCATION').count()
        bece = StudentCSV.query.filter(StudentCSV.course_csv=='BACHELOR OF EARLY CHILDHOOD EDUCATION').count()
        pe = StudentCSV.query.filter(StudentCSV.course_csv=='BACHELOR OF PHYSICAL EDUCATION ').count()
        bse = StudentCSV.query.filter(StudentCSV.course_csv=='BACHELOR OF SECONDARY EDUCATION').count()
        special = StudentCSV.query.filter(StudentCSV.course_csv=='BACHELOR OF SPECIAL NEEDS EDUCATION').count()

        baels = StudentCSV.query.filter(StudentCSV.course_csv=='BAELS').count()
        fil = StudentCSV.query.filter(StudentCSV.course_csv=='BATSILER NG SINING SA FILIPINO').count()
        acc = StudentCSV.query.filter(StudentCSV.course_csv=='BS ACCOUNTANCY').count()
        agribus = StudentCSV.query.filter(StudentCSV.course_csv=='BS AGRI-BUSINESS').count()
        agri_bio = StudentCSV.query.filter(StudentCSV.course_csv=='BS AGRICULTURAL AND BIOSYSTEMS ENGINEERING').count()
        agri = StudentCSV.query.filter(StudentCSV.course_csv=='BS AGRICULTURE').count()
        agro = StudentCSV.query.filter(StudentCSV.course_csv=='BS AGRO-FORESTY').count()
        arch = StudentCSV.query.filter(StudentCSV.course_csv=='BS ARCHITECTURE').count()
        asian = StudentCSV.query.filter(StudentCSV.course_csv=='BS ASIAN STUDIES').count()
        bio = StudentCSV.query.filter(StudentCSV.course_csv=='BS BIOLOGY').count()

        chem = StudentCSV.query.filter(StudentCSV.course_csv=='BS CHEMISTRY').count()
        ce = StudentCSV.query.filter(StudentCSV.course_csv=='BS CIVIL ENGINEERING').count()
        cd = StudentCSV.query.filter(StudentCSV.course_csv=='BS COMMUNITY DEVELOPMENT').count()
        coe = StudentCSV.query.filter(StudentCSV.course_csv=='BS COMPUTER ENGINEERING').count()
        cs = StudentCSV.query.filter(StudentCSV.course_csv=='BS COMPUTER SCIENCE').count()
        crim = StudentCSV.query.filter(StudentCSV.course_csv=='BS CRIMINOLOGY').count()
        eco = StudentCSV.query.filter(StudentCSV.course_csv=='BS ECONOMICS').count()
        ee = StudentCSV.query.filter(StudentCSV.course_csv=='BS ELECTRICAL ENGINEERING').count()
        elec = StudentCSV.query.filter(StudentCSV.course_csv=='BS ELECTRONICS AND COMMUNICATION ENGINEERING').count()
        envi = StudentCSV.query.filter(StudentCSV.course_csv=='BS ENVIRONMENTAL ENGINEERING').count()

        ft = StudentCSV.query.filter(StudentCSV.course_csv=='BS FOOD TECHNOLOGY').count()
        forest = StudentCSV.query.filter(StudentCSV.course_csv=='BS FORESTRY').count()
        ge = StudentCSV.query.filter(StudentCSV.course_csv=='BS GEODETIC ENGINEERING').count()
        he = StudentCSV.query.filter(StudentCSV.course_csv=='BS HOME ECONOMICS').count()
        hm = StudentCSV.query.filter(StudentCSV.course_csv=='BS HOSPITALITY MANAGEMENT').count()
        ie = StudentCSV.query.filter(StudentCSV.course_csv=='BS INDUSTRIAL ENGINEERING').count()
        it = StudentCSV.query.filter(StudentCSV.course_csv=='BS INFORMATION TECHNOLOGY').count()
        islamic = StudentCSV.query.filter(StudentCSV.course_csv=='BS ISLAMIC STUDIES').count()
        math = StudentCSV.query.filter(StudentCSV.course_csv=='BS MATHEMATICS').count()
        me = StudentCSV.query.filter(StudentCSV.course_csv=='BS MECHANICAL ENGINEERING').count()

        bsn = StudentCSV.query.filter(StudentCSV.course_csv=='BS NURSING').count()
        nd = StudentCSV.query.filter(StudentCSV.course_csv=='BS NUTRITION AND DIETETICS').count()
        physics = StudentCSV.query.filter(StudentCSV.course_csv=='BS PHYSICS').count()
        psych = StudentCSV.query.filter(StudentCSV.course_csv=='BS PSYCHOLOGY').count()
        sanitary = StudentCSV.query.filter(StudentCSV.course_csv=='BS SANITARY ENGINEERING').count()
        sw = StudentCSV.query.filter(StudentCSV.course_csv=='BS SOCIAL WORK').count()
        stat = StudentCSV.query.filter(StudentCSV.course_csv=='BS STATISTICS').count()
        
        auth_user=current_user
        students_record = db.session.query(User, StudentDetails).join(StudentDetails).filter( User.user_type == 1)
        students_csv = db.session.query(StudentCSV)

 
    return render_template("Admin/admin_page_analytics.html", auth_user=auth_user,students_record=students_record,students_csv=students_csv, male = json.dumps(male), female = json.dumps(female),
    broad = json.dumps(broad),hist = json.dumps(hist),journ = json.dumps(journ),polsci = json.dumps(polsci),bat = json.dumps(bat),beed = json.dumps(beed),bcae = json.dumps(bcae),bece = json.dumps(bece),pe = json.dumps(pe),bse = json.dumps(bse),special = json.dumps(special),
    baels = json.dumps(baels),fil = json.dumps(fil),acc = json.dumps(acc),agribus = json.dumps(agribus),agri_bio = json.dumps(agri_bio),agri = json.dumps(agri),agro = json.dumps(agro),arch = json.dumps(arch),asian = json.dumps(asian),bio = json.dumps(bio),
    chem = json.dumps(chem),ce = json.dumps(ce),cd = json.dumps(cd),coe = json.dumps(coe),cs = json.dumps(cs),crim = json.dumps(crim),eco = json.dumps(eco),ee = json.dumps(ee),elec = json.dumps(elec),envi = json.dumps(envi),
    ft = json.dumps(ft),forest = json.dumps(forest),ge = json.dumps(ge),he = json.dumps(he),hm = json.dumps(hm),ie = json.dumps(ie),it = json.dumps(it),islamic = json.dumps(islamic),math = json.dumps(math),me = json.dumps(me),
    bsn = json.dumps(bsn),nd = json.dumps(nd),physics = json.dumps(physics),psych = json.dumps(psych),sanitary = json.dumps(sanitary),sw = json.dumps(sw),stat = json.dumps(stat),)

@_route_admin.route('/admin',methods=['GET', 'POST'])
@login_required
def admin():
    auth_user=current_user
    admin_record = db.session.query(User).filter( User.user_type == 0)
    return render_template("Admin/admin.html",auth_user=auth_user,admin_record=admin_record)
   

@_route_admin.route('/login_admin_form', methods=['GET'])
def login_admin_form():
    auth_user=current_user
    if auth_user.is_authenticated:
        if auth_user.user_type == 0:
            return redirect(url_for('.admin_form'))
        else:
            return redirect(url_for('_auth.index'))
    return render_template("Admin/admin_form.html")

@_route_admin.route('/login_admin', methods=['GET', 'POST'])
def login_admin():
    auth_user=current_user
    if auth_user.is_authenticated:
        if auth_user.user_type == 0:
            return redirect(url_for('.admin_dashboard'))
        else:
            flash('Only admin is permitted', category='error')
            return redirect(url_for('.admin_form'))
    else:
        if request.method == 'POST':
            user = User.query.filter_by(email=request.form['email'], user_type=0).first()
            if user:
                if user.is_approve == True:
                    if check_password_hash(user.password, request.form['password']):
                        login_user(user, remember=True)
                        return redirect(url_for('.admin_dashboard'))
                    else:
                        flash('Invalid or wrong password', category='error')
                else:
                    flash('Account is not approve yet, wait for further notice.', category='info')
            else:
                flash('No record found', category='error')
    return redirect(url_for('.register_form_admin'))

@_route_admin.route('/register_form_admin', methods=['GET'])
def register_form_admin():
     auth_user=current_user
     
     return render_template("Admin/register_form_admin.html")

@_route_admin.route('/register_admin', methods=['POST'])
def register_admin():
     try:
        new_user = User(request.form['first_name'], request.form['middle_name'], request.form['last_name'], request.form['sex'], request.form['email'],  (generate_password_hash(request.form['password'], method="sha256")), True, False, False, 0)
        db.session.add(new_user)
        db.session.commit()
        flash('Account successfully created', category='success_register')
        return redirect(url_for('.register_form_admin'))
        
     except:
        flash('Invalid credentials', category='error')
        return redirect(url_for('.register_form_admin'))

@_route_admin.route("/upload_csv", methods=['GET', 'POST'])
def upload_csv():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        

        try:
            for row in csv_reader:
                upload = StudentCSV(student_id_csv=row[0],firstname_csv=row[1], middlename_csv=row[2], lastname_csv=row[3], oapr_csv=row[4], english_csv=row[5], reading_csv=row[6], science_csv=row[7], math_csv=row[8], logic_csv=row[9], course_csv=row[10],college_csv=row[11])
                db.session.add(upload)
                db.session.commit()
            flash('File Succesfully Uploaded ', category='info')
        except:
            flash('Invalid Format', category='error')
    
    return redirect(url_for('.admin_analytic'))