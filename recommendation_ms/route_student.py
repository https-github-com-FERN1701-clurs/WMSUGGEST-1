from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify, make_response, session
from flask_login import login_required, current_user
from .models import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy import delete
from sqlalchemy import select, asc,desc
import datetime
from datetime import datetime
import json
import numpy as np
import pandas as pd
import pickle
from tkinter import Y
from pandas import DataFrame
from flask import Flask, request, jsonify, render_template
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OrdinalEncoder
from scipy.stats import spearmanr
# import matplotlib.pyplot as plt
import json
# import plotly
# import plotly.express as px
import random
import math
from os import path
import os

from .auth import send_link, send_link_disapproved # for email message

_route_student = Blueprint('_route_student', __name__)
_route_admin = Blueprint('_route_admin', __name__)

@_route_student.route('/index')
@login_required
def dashboard():
    return '1'

# dataset = os.path.join(os.path.abspath(os.path.dirname(__file__)),"model/data_updated.csv")
# model = os.path.join(os.path.abspath(os.path.dirname(__file__)),"model/Trained_Model_knn_updated.pkl")
# model1 = os.path.join(os.path.abspath(os.path.dirname(__file__)),"model/Trained_Model_naive100.pkl")
# model2 = os.path.join(os.path.abspath(os.path.dirname(__file__)),"model/TrainedModel_Forest100.pkl")

# dataset = pd.read_csv(dataset)

# FEATURES = [
#      'Pr1',
#      'Pr2',
#      'Pr3',
#      'Pr4',
#      'Pr5',
#      'Oapr',
# ]

# TARGET = 'College'

# Y = dataset[TARGET]
# X = dataset[FEATURES]
# X = X.replace(np.nan, 0)

# model_stud = pickle.load(open(model, "rb"))

flask_app = Flask(__name__) #Initialize flask_app

@flask_app.route("/")
def Home():
        
    

    return render_template("index.html")

@_route_student.route('/student_page', methods=['GET'])
@login_required
def student_page():
    auth_user=current_user

    details = Description.query.count()
    print("Count:",details)
    if details==0:
        descriptions = [

            {'course': 'BACHELOR OF EARLY CHILDHOOD EDUCATION', 'course_des': 'Bachelor of Early Childhood Education is an undergraduate degree program that focuses on the education and care of children from birth to age eight. The program prepares students to become qualified early childhood educators, teaching them how to develop and implement age-appropriate curriculum, create a safe and healthy learning environment, and assess children\'s learning and development.In this program typically includes early childhood development, child psychology, curriculum design, educational psychology, classroom management, literacy and language development, and assessment and evaluation methods.', 'college': 'College of Teacher Education'},
            {'course': 'BS NURSING', 'course_des': 'Bachelor of Science in Nursing (BSN) is an undergraduate degree program that prepares individuals to become registered nurses (RNs). The program typically takes four years to complete and provides students with a strong foundation in nursing theory and practice. BSN programs usually include a combination of classroom instruction and clinical practice. Students learn about anatomy and physiology, pharmacology, nursing ethics, patient care, and other essential topics. Clinical practice allows students to apply what they have learned in real-world settings, working alongside experienced nurses in hospitals, clinics, and other healthcare facilities.', 'college': 'College of Nursing'},
            {'course': 'BS FORESTRY', 'course_des': 'Bachelor of Science in Forestry (BSF) is an undergraduate degree program that focuses on the scientific study of forest ecosystems and the sustainable management of forest resources. The program usually takes four years to complete and provides students with a strong foundation in natural sciences, environmental management, and forestry practices. BSF programs typically include courses in forest ecology, silviculture, forest management, forest economics, wildlife management, and environmental law and policy. Students also receive hands-on training in fieldwork and data analysis, which prepares them for careers in natural resource management.', 'college': 'College of Forestry and Environmental Studies'},
            {'course': 'AB JOURNALISM', 'course_des': 'Bachelor of Arts in Journalism (AB Journalism) is an undergraduate degree program that prepares students for careers in media and communications. The program usually takes four years to complete and provides students with a broad range of skills in news reporting, writing, editing, and multimedia production. AB Journalism programs typically include courses in media ethics, media law, journalism history, news gathering and reporting, feature writing, photojournalism, broadcast journalism, and digital media. Students also receive hands-on training in various media platforms, including print, broadcast, and online journalism.', 'college': 'College of Liberal Arts'},
            {'course': 'BS COMPUTER ENGINEERING', 'course_des': 'Bachelor of Science in Computer Engineering (BSCE) is an undergraduate degree program that combines principles of computer science and electrical engineering to design, develop, and maintain computer hardware and software systems. The program typically takes four years to complete and provides students with a strong foundation in programming, digital systems, and computer networks. BSCE programs typically include courses in computer programming, digital circuits, microprocessors, computer architecture, software engineering, computer networks, and operating systems. Students also receive hands-on training in various computer technologies, including computer-aided design, microcontroller programming, and networking.', 'college': 'College of Engineering'},
            {'course': 'BS AGRICULTURE', 'course_des': 'Bachelor of Science in Agriculture (BSA) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of agricultural sciences. The program typically takes four years to complete and prepares students for careers in various agricultural fields. BSA programs typically include courses in soil science, crop production, animal science, agricultural economics, plant genetics, horticulture, and farm management. Students also receive hands-on training in various agricultural technologies and practices, including agricultural machinery and equipment, irrigation systems, and pest management.', 'college': 'College of Agriculture'},
            {'course': 'BS MATHEMATICS', 'course_des': 'Bachelor of Science in Mathematics (BS Math) is an undergraduate degree program that provides students with a comprehensive understanding of mathematical theory, methods, and applications. The program typically takes four years to complete and prepares students for careers in various fields that require advanced quantitative and analytical skills. BS Math programs typically include courses in calculus, algebra, number theory, geometry, probability, statistics, and mathematical modeling. Students also receive training in computer programming, data analysis, and computational methods.', 'college': 'College of Science and Mathematics'},
            {'course': 'BS MECHANICAL ENGINEERING', 'course_des': 'Bachelor of Science in Mechanical Engineering (BSME) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of mechanical systems and machinery. The program typically takes four years to complete and prepares students for careers in various industries that require expertise in mechanical engineering. BSME programs typically include courses in calculus, physics, mechanics, thermodynamics, materials science, design, and manufacturing. Students also receive hands-on training in various mechanical engineering technologies and practices, including computer-aided design (CAD), finite element analysis (FEA), and machine tool operations.', 'college': 'College of Engineering'},
            {'course': 'BS ENVIRONMENTAL ENGINEERING', 'course_des': 'Bachelor of Science in Environmental Engineering (BSEnvE) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of environmental engineering. The program typically takes four years to complete and prepares students for careers in various industries that require expertise in environmental engineering. BSEnvE programs typically include courses in chemistry, physics, biology, fluid mechanics, water and wastewater treatment, air pollution control, solid waste management, and environmental law and policy. Students also receive hands-on training in various environmental engineering technologies and practices, including environmental monitoring and analysis, environmental impact assessment, and sustainability analysis.', 'college': 'College of Engineering'},
            {'course': 'AB POLITICAL SCIENCE', 'course_des': 'Bachelor of Arts in Political Science (AB PolSci) is an undergraduate degree program that provides students with a comprehensive understanding of political theory, institutions, and processes. The program typically takes four years to complete and prepares students for careers in various fields that require advanced critical thinking and analytical skills. AB PolSci programs typically include courses in political theory, comparative politics, international relations, political economy, public administration, and political research methods. Students also receive training in communication and negotiation skills, as well as in public policy analysis and development.', 'college': 'College of Liberal Arts'},
            {'course': 'AB HISTORY', 'course_des': 'Bachelor of Arts in History (AB History) is an undergraduate degree program that provides students with a comprehensive understanding of the development of human societies and cultures over time. The program typically takes four years to complete and prepares students for careers in various fields that require advanced critical thinking, research, and communication skills. AB History programs typically include courses in world history, national and regional history, historical methodology, historiography, and historical research and writing. Students also receive training in critical analysis, communication, and research skills, as well as in digital humanities and cultural heritage.', 'college': 'College of Liberal Arts'},
            {'course': 'BS PHYSICS', 'course_des': 'Bachelor of Science in Physics (BS Physics) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of physics. The program typically takes four years to complete and prepares students for careers in various fields that require advanced quantitative and analytical skills. BS Physics programs typically include courses in mechanics, electromagnetism, thermodynamics, quantum mechanics, statistical mechanics, and optics. Students also receive training in laboratory techniques, data analysis, and computational methods.', 'college': 'College of Science and Mathematics'},
            {'course': 'BS AGRI-BUSINESS', 'course_des': 'Bachelor of Agri-business (BS Agribusiness) is an undergraduate degree program that combines the study of agricultural sciences with business management principles. The program typically takes four years to complete and prepares students for careers in various fields that require expertise in agricultural production and management. B.Agri-Business programs typically include courses in agriculture, business management, economics, finance, accounting, marketing, and agricultural policy. Students also receive hands-on training in various agricultural technologies and practices, including crop management, livestock management, and farm management.', 'college': 'College of Agriculture'},
            {'course': 'BS GEODETIC ENGINEERING', 'course_des': 'Bachelor of Science in Geodetic Engineering (BS GE) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of geodetic surveying and mapping. The program typically takes five years to complete and prepares students for careers in various fields that require expertise in geospatial data collection, analysis, and management. BS GE programs typically include courses in geodetic surveying, land surveying, photogrammetry, remote sensing, geographic information systems (GIS), and cartography. Students also receive hands-on training in fieldwork, data analysis, and software applications.', 'college': 'College of Engineering'},
            {'course': 'BS INDUSTRIAL ENGINEERING', 'course_des': 'Bachelor of Science in Industrial Engineering (BSIE) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of designing, developing, and optimizing complex systems and processes. The program typically takes four years to complete and prepares students for careers in various fields that require expertise in engineering, management, and data analysis. BSIE programs typically include courses in operations research, quality control, supply chain management, project management, manufacturing processes, and engineering economics. Students also receive training in computer-aided design (CAD), simulation, and statistical analysis.', 'college': 'College of Engineering'},
            {'course': 'BS AGRO-FORESTRY', 'course_des': 'Bachelor of Science in Agro-Forestry (BS AF) is an undergraduate degree program that combines the principles and practices of agriculture and forestry to promote sustainable land management practices. The program typically takes four years to complete and prepares students for careers in various fields that require expertise in both agriculture and forestry. BS AF programs typically include courses in soil science, plant science, forest ecology, agroforestry systems, silviculture, forest economics, and natural resource management. Students also receive hands-on training in various agricultural and forestry techniques and practices.', 'college': 'College of Forestry and Environmental Studies'},
            {'course': 'BACHELOR OF AGRICULTURAL TECHNOLOGY', 'course_des': 'Bachelor of Agricultural Technology (BAT) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of modern agriculture. The program typically takes four years to complete and prepares students for careers in various fields that require expertise in agriculture and technology. BAT programs typically include courses in crop science, animal science, soil science, agricultural engineering, agricultural economics, and agricultural extension. Students also receive hands-on training in various agricultural technologies and practices, including precision farming, irrigation systems, and farm management software.', 'college': 'College of Agriculture'},
            {'course': 'BS CRIMINOLOGY', 'course_des': 'Bachelor of Science in Criminology (BSCrim) is an undergraduate degree program that provides students with a comprehensive understanding of the nature of crime, the criminal justice system, and the socio-cultural factors that contribute to criminal behavior. The program typically takes four years to complete and prepares students for careers in various fields related to law enforcement, security, and justice. BSCrim programs typically include courses in criminal law, forensic science, investigation, psychology, sociology, and criminology theory. Students also receive practical training in crime scene investigation, evidence collection, and criminal profiling.', 'college': 'College of Criminal Justice and Education'},
            {'course': 'BS ELECTRONICS COMMUNICATION ENGINEERING', 'course_des': 'Bachelor of Science in Electronics Communication Engineering (BS ECE) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of electronic communication systems. The program typically takes four years to complete and prepares students for careers in various fields related to electronics, telecommunications, and networking. BS ECE programs typically include courses in circuit analysis, signal processing, electronic devices, communication systems, digital electronics, and computer networks. Students also receive hands-on training in electronic circuits design, wireless communications, and embedded systems.', 'college': 'College of Engineering'},
            {'course': 'BS CIVIL ENGINEERING', 'course_des': 'Bachelor of Science in Civil Engineering (BSCE) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of designing, constructing, and maintaining physical infrastructure. The program typically takes four years to complete and prepares students for careers in various fields related to civil engineering. BSCE programs typically include courses in structural analysis and design, geotechnical engineering, water resources engineering, transportation engineering, and construction management. Students also receive hands-on training in surveying, materials testing, and project management.', 'college': 'College of Engineering'},
            {'course': 'BS ELECTRICAL ENGINEERING', 'course_des': 'Bachelor of Science in Electrical Engineering (BSEE) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of designing, developing, and maintaining electrical systems and devices. The program typically takes four years to complete and prepares students for careers in various fields related to electrical engineering. BSEE programs typically include courses in circuit analysis, electronics, power systems, electromagnetism, signal processing, and control systems. Students also receive hands-on training in electrical circuits design, programming, and testing.', 'college': 'College of Engineering'},
            {'course': 'BS BIOLOGY', 'course_des': 'Bachelor of Science in Biology (BS Biology) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of biology, the study of living organisms. The program typically takes four years to complete and prepares students for careers in various fields related to biology. BS Biology programs typically include courses in cell biology, genetics, microbiology, ecology, evolution, and anatomy and physiology. Students also receive hands-on training in laboratory techniques, experimental design, and data analysis.', 'college': 'College of Science and Mathematics'},
            {'course': 'BS SOCIAL WORK', 'course_des': 'Bachelor of Science in Social Work (BSSW) is an undergraduate degree program that prepares students for a career in social work, which involves helping individuals, families, and communities to improve their well-being and quality of life. The program typically takes four years to complete and provides students with a comprehensive understanding of social work theories, methods, and practices. BSSW programs typically include courses in human behavior, social welfare policy, research methods, social work practice, and field education. Students also receive hands-on training through internships and practicum experiences in various social service settings.', 'college': 'College of Social Work and Community Development'},
            {'course': 'BS INFORMATION TECHNOLOGY', 'course_des': 'Bachelor of Science in Information Technology (BSIT) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of information technology, the study of computer-based information systems. The program typically takes four years to complete and prepares students for careers in various fields related to information technology. BSIT programs typically include courses in programming, database management, web development, network systems, cybersecurity, and information management. Students also receive hands-on training in computer programming languages, software development, and project management.', 'college': 'College of Computing Studies'},
            {'course': 'BACHELOR OF ELEMENTARY EDUCATION', 'course_des': 'Bachelor of Elementary Education (BEE) is an undergraduate degree program that prepares students to become teachers for grades one to six in elementary schools. The program typically takes four years to complete and provides students with a comprehensive understanding of the principles and practices of teaching and learning. BEE programs typically include courses in educational psychology, teaching methods, child development, curriculum development, and classroom management. Students also receive hands-on training through classroom observations and practice teaching in actual elementary school classrooms.', 'college': 'College of Teacher Education'},
            {'course': 'BS COMMUNITY DEVELOPMENT', 'course_des': 'Bachelor of Science in Community Development (BSCD) is an undergraduate degree program that equips students with the knowledge and skills to address social and economic issues affecting communities. The program typically takes four years to complete and provides students with a comprehensive understanding of community development theories, practices, and approaches. BSCD programs typically include courses in community organizing, project management, community research, social entrepreneurship, and public policy. Students also receive hands-on training through internships and fieldwork experiences in various community development settings.', 'college': 'College of Social Work and Community Development'},
            {'course': 'BA ELS', 'course_des': 'Bachelor of Arts in English Language Studies (BA ELS) is an undergraduate degree program that focuses on the study of the English language and its use in various contexts, including literature, culture, and communication. The program typically takes four years to complete and provides students with a comprehensive understanding of the principles and practices of English language teaching, learning, and research. BA ELS programs typically include courses in English grammar, writing, literature, linguistics, and language teaching methodology. Students also receive hands-on training through teaching practicums and research projects.', 'college': 'College of Liberal Arts'},
            {'course': 'BS COMPUTER SCIENCE', 'course_des': 'Bachelor of Science in Computer Science (BSCS) is an undergraduate degree program that focuses on the study of computer software, hardware, and their applications. The program typically takes four years to complete and provides students with a comprehensive understanding of the principles and practices of computer science. BSCS programs typically include courses in programming languages, data structures, algorithms, operating systems, computer networks, databases, and software engineering. Students also receive hands-on training through laboratory work, programming projects, and internships.', 'college': 'College of Computing Studies'},
            {'course': 'BS ARCHITECTURE', 'course_des': 'Bachelor of Science in Architecture (BS Architecture) is an undergraduate degree program that focuses on the study of architectural design, building systems, construction methods, and architectural history. The program typically takes five years to complete and provides students with a comprehensive understanding of the principles and practices of architecture. BS Architecture programs typically include courses in design theory, drawing and modeling, building materials, structural design, building systems, construction technology, architectural history, and professional practice. Students also receive hands-on training through design studios, construction site visits, and internship programs.', 'college': 'College of Architecture'},
            {'course': 'BS ASIAN STUDIES', 'course_des': 'Bachelor of Science in Asian Studies (BS Asian Studies) is an undergraduate degree program that focuses on the study of the culture, history, politics, economics, and social issues of Asia. The program typically takes four years to complete and provides students with a comprehensive understanding of the diverse and complex aspects of Asian societies. BS Asian Studies programs typically include courses in Asian languages, history, philosophy, religion, art, literature, politics, economics, and social issues. Students also have the opportunity to study abroad, participate in research projects, and complete internships in Asian countries.', 'college': 'College of Asians and Islamic Studies'},
            {'course': 'AB BROADCASTING', 'course_des': 'Bachelor of Arts in Broadcasting (AB Broadcasting) is an undergraduate degree program that focuses on the study of broadcast journalism, radio and television production, media management, and communication theory. The program typically takes four years to complete and provides students with the knowledge and skills necessary to work in the broadcasting industry. AB Broadcasting programs typically include courses in writing for media, news gathering and reporting, video and audio production, media law and ethics, media management, and communication theory. Students also receive hands-on training through internships and practical projects.', 'college': 'College of Liberal Arts'},
            {'course': 'BATSILYER NG SINING SA FILIPINO', 'course_des': 'Ang Batsilyer ng Sining sa Filipino (Bachelor of Arts in Filipino) ay isang programa ng pre-bago na nagbibigay ng edukasyon sa mga mag-aaral tungkol sa wika, panitikan, at kultura ng Filipino. Ang programa ay karaniwang tumatagal ng apat na taon at naglalayong bigyan ng malawak na kaalaman at kasanayan ang mga mag-aaral sa pagsusulat, pagbabasa, at pagsasalin ng iba\'t ibang anyo ng panitikan sa Filipino.Kabilang sa mga kurso sa programa ang Panitikang Pilipino, Pagsulat ng mga Sanaysay, Malikhaing Pagsulat, Panitikan ng mga Rehiyon sa Pilipinas, Pagsasalin ng Panitikan, at Mga Teorya sa Wika at Panitikan. Mayroon ding mga kursong nagbibigay ng praktikal na kasanayan sa paggamit ng mga teknolohiya at media sa pagpapakalat ng wika at kultura ng Filipino.', 'college': 'College of Liberal Arts'},
            {'course': 'BS NUTRITION AND DIETETICS', 'course_des': 'A BS in Nutrition and Dietetics is an undergraduate degree program that focuses on the study of food, nutrition, and health. This program prepares students to become licensed dietitians and nutritionists who can work in a variety of settings, including hospitals, clinics, schools, government agencies, and private practice. The program typically covers a range of topics, including anatomy and physiology, nutrition science, food chemistry, food service management, and public health. Students may also have the opportunity to participate in internships and clinical rotations to gain practical experience in the field.', 'college': 'College of Home Economics'},
            {'course': 'BS ENVIRONMENTAL SCIENCE', 'course_des': 'A BS in Environmental Science is an undergraduate degree program that focuses on the study of the environment, including its natural resources, biodiversity, ecosystems, and human impacts. This program prepares students to become environmental scientists who can work in a variety of settings, including government agencies, non-profit organizations, consulting firms, and private industry. The program typically covers a range of topics, including ecology, geology, climate change, sustainability, environmental policy, and environmental law. Students may also have the opportunity to participate in fieldwork and research projects to gain practical experience in the field.', 'college': 'College of Forestry and Environmental Studies'},
            {'course': 'BS STATISTIC', 'course_des': 'A BS in Statistics is an undergraduate degree program that focuses on the study of statistical theory, data analysis, and mathematical modeling. This program prepares students to become statisticians who can work in a variety of settings, including research institutions, government agencies, healthcare organizations, and private industry. The program typically covers a range of topics, including probability theory, statistical inference, regression analysis, experimental design, and data visualization. Students may also have the opportunity to participate in research projects and internships to gain practical experience in the field.', 'college': 'College of Sceince and Mathematics'},
            {'course': 'BS EXERCISE AND SPORTS SCIENCE', 'course_des': 'A BS in Exercise and Sports Science is an undergraduate degree program that focuses on the study of human movement, exercise physiology, and sports performance. This program prepares students to become exercise physiologists, sports coaches, personal trainers, and other professionals in the field of exercise and sports science. The program typically covers a range of topics, including anatomy and physiology, kinesiology, exercise prescription, sports psychology, and nutrition. Students may also have the opportunity to participate in clinical rotations, internships, or research projects to gain practical experience in the field.', 'college': 'College of Sports and Physical Education'},
            {'course': 'BS CHEMISTRY', 'course_des': 'A BS in Chemistry is an undergraduate degree program that focuses on the study of matter, its properties, and its interactions. This program prepares students to become chemists who can work in a variety of settings, including research institutions, government agencies, pharmaceutical companies, and private industry. The program typically covers a range of topics, including organic chemistry, physical chemistry, analytical chemistry, biochemistry, and chemical engineering. Students may also have the opportunity to participate in laboratory work and research projects to gain practical experience in the field.', 'college': 'College of Sceince and Mathematics'},
            {'course': 'BS HOME ECONOMICS', 'course_des': 'BS Home Economics is an undergraduate program that focuses on the study of various aspects of home management and family life. It aims to equip students with the knowledge and skills to manage households efficiently, promote healthy living, and provide education on child development, family relations, nutrition, and consumer economics. The curriculum typically includes courses such as food science and nutrition, family and child development, consumer economics, textiles and clothing, interior design, and housing and home management. Students may also be required to complete practical training, internships, or community service to gain hands-on experience.', 'college': 'College of Home Economics'},
            {'course': 'BACHELOR OF SPECIAL NEED EDUCATION', 'course_des': 'A Bachelor of Special Needs Education is an undergraduate degree program that focuses on the education of children with special needs. This program prepares students to become special education teachers who can work in a variety of settings, including public and private schools, special education centers, and non-profit organizations. The program typically covers a range of topics, including educational psychology, special education law, behavior management, communication disorders, and curriculum development. Students may also have the opportunity to participate in teaching practicums and internships to gain practical experience in the field.', 'college': 'College of Teacher Education'},
            {'course': 'BS AGRICULTURAL BIOSYSTEM ENGINEERING', 'course_des': 'A BS in Agricultural Biosystems Engineering is an undergraduate degree program that focuses on the application of engineering principles to biological systems used in agriculture, such as crops, livestock, and natural resources. This program prepares students to become agricultural engineers who can work in a variety of settings, including agricultural research institutions, government agencies, and private industry. The program typically covers a range of topics, including mechanics of biological materials, soil and water conservation, sustainable agriculture, precision agriculture, and food processing. Students may also have the opportunity to participate in laboratory work, design projects, and internships to gain practical experience in the field.', 'college': 'College of Engineering'},
            {'course': 'BS ISLAMIC STUDIES', 'course_des': 'A BS in Islamic Studies is an undergraduate degree program that focuses on the academic study of Islam and its history, culture, and traditions. This program prepares students to become experts in Islamic theology, law, and philosophy and to work in a variety of settings, including academic institutions, religious organizations, and government agencies. The program typically covers a range of topics, including Islamic history, Quranic studies, Islamic law, Islamic philosophy, and Islamic art and architecture. Students may also have the opportunity to learn Arabic and other languages used in Islamic scholarship and to participate in study abroad programs to gain first-hand experience of Islamic cultures and traditions.', 'college': 'College of Asians ans Islamic Studies'},
            {'course': 'BS HOME MANAGEMENT', 'course_des': 'A BS in Home Management is an undergraduate degree program that focuses on the study of managing households and households\' resources. This program prepares students to become professionals who can work in a variety of settings, including households, non-profit organizations, and private industry. The program typically covers a range of topics, including financial management, family and consumer sciences education, food and nutrition, housing and interior design, and communication skills. Students may also have the opportunity to participate in internships or research projects to gain practical experience in the field.', 'college': 'College of Home Economics'},
            {'course': 'BS SANITARY ENGINEERING', 'course_des': 'A BS in Sanitary Engineering is an undergraduate degree program that focuses on the study of the design and construction of systems and facilities that promote public health and safety by preventing and controlling the spread of disease. This program prepares students to become professionals who can work in a variety of settings, including government agencies, public health organizations, and private industry. The program typically covers a range of topics, including environmental health, water supply and treatment, wastewater treatment and disposal, solid waste management, and air pollution control. Students may also have the opportunity to participate in laboratory work, design projects, and internships to gain practical experience in the field.', 'college': 'College of Engineering'},
            {'course': 'BACHELOR OF PHYSICAL EDUCATION', 'course_des': 'A Bachelor of Physical Education is an undergraduate degree program that focuses on the study of physical activity, exercise, and sports. This program prepares students to become professionals who can work in a variety of settings, including schools, colleges, universities, fitness centers, and sports organizations. The program typically covers a range of topics, including anatomy, physiology, biomechanics, kinesiology, exercise physiology, sports psychology, and coaching methods. Students may also have the opportunity to participate in teaching practicums and internships to gain practical experience in the field.', 'college': 'College of Sports Science and Physical Education'},
            {'course': 'BACHELOR OF SECONDARY EDUCATION', 'course_des': 'A Bachelor of Secondary Education is an undergraduate degree program that focuses on the study of teaching in secondary schools. This program prepares students to become teachers who can work in a variety of subject areas, including English, mathematics, science, social studies, and foreign languages. The program typically covers a range of topics, including educational psychology, classroom management, curriculum development, assessment and evaluation, and teaching methods. Students may also have the opportunity to participate in teaching practicums and internships to gain practical experience in the field.', 'college': 'College of Teacher Education'},
            {'course': 'BACHELOR OF CULTURE AND ARTS EDUCATION', 'course_des': 'A Bachelor of Culture and Arts Education is an undergraduate degree program that focuses on the study of arts education in a cultural context. This program prepares students to become professionals who can work in a variety of settings, including schools, museums, art centers, and community organizations. The program typically covers a range of topics, including art history, visual arts, performing arts, music, dance, cultural studies, curriculum development, and teaching methods. Students may also have the opportunity to participate in teaching practicums and internships to gain practical experience in the field.', 'college': 'College of Teacher Education'},
            {'course': 'BS FOOD TECHNOLOGY', 'course_des': 'A BS in Food Technology is an undergraduate degree program that focuses on the study of food processing, preservation, and safety. This program prepares students to become professionals who can work in the food industry, research institutions, or government agencies. The program typically covers a range of topics, including food chemistry, microbiology, nutrition, sensory evaluation, food processing, food preservation, food packaging, and quality control. Students may also have the opportunity to participate in laboratory work, research projects, and internships to gain practical experience in the field.', 'college': 'College of Agriculture'},
            {'course': 'BS ACCOUNTANCY', 'course_des': 'A BS in Accountancy is an undergraduate degree program that focuses on the study of accounting principles and practices. This program prepares students to become professionals who can work in a variety of settings, including accounting firms, corporations, government agencies, and non-profit organizations. The program typically covers a range of topics, including financial accounting, managerial accounting, taxation, auditing, financial statement analysis, and accounting information systems. Students may also have the opportunity to participate in internships or practicums to gain practical experience in the field.', 'college': 'College of Liberal Arts'},


        ]

        # Create a new Description instance for each dictionary in the list
        for description in descriptions:
            new_description = Description(**description)

            # Add the instance to the database session
            db.session.add(new_description)

        # Commit the changes to persist the data in the database
        db.session.commit()

    if auth_user.user_type == 1:
        approve_account = User.query.filter_by(id=int(auth_user.id)).first()
        details1 =StudentDetails.query.filter(StudentDetails.user_id==auth_user.id).first()
        details2 =PredictionResult.query.filter(PredictionResult.user_id==auth_user.id).first()
        db.session.commit()
        return render_template("Student/student_page_details.html", auth_user=auth_user,details1=details1,details2=details2)
    else:
        return redirect(url_for('_auth.index'))

@_route_student.route('/student_page_prediction', methods=['GET'])
@login_required
def student_page_prediction():
    auth_user=current_user
    if auth_user.user_type == 1:
        db.session.commit()
        return render_template("Student/student_page_prediction.html", auth_user=auth_user)
    else:
        return redirect(url_for('_auth.index'))
    
@_route_student.route('/prediction_result', methods=['GET'])
@login_required
def prediction_result():
    auth_user=current_user
    if auth_user.user_type == 1:
        return render_template("Student/result.html", auth_user=auth_user)
    else:
        return redirect(url_for('_auth.index'))
   
@_route_student.route('/login_form', methods=['GET'])
def login_form():
    auth_user=current_user
    if auth_user.is_authenticated:
        if auth_user.user_type == 1:
            return redirect(url_for('.student_page'))
        elif auth_user.user_type == 0:
            return render_template('Admin/admin_page.html', auth_user=auth_user)
        else:
            return redirect(url_for('_auth.index'))
    return render_template("Student/login_form.html")

@_route_student.route('/register_form', methods=['GET'])
def register_form():
     auth_user=current_user
     if auth_user.is_authenticated:
          if auth_user.user_type == 1:
               return redirect(url_for('.student_page'))
          else:
               return redirect(url_for('_auth.index'))
     return render_template("Student/register_form.html")

@_route_student.route('/register_student', methods=['POST'])
def register_student():
     try:
        msg=''
        if request.form['password']==request.form['cpassword']:
            new_user = User(request.form['first_name'], request.form['middle_name'], request.form['last_name'], request.form['sex'], request.form['email'],  (generate_password_hash(request.form['password'], method="sha256")), True, False, False, 1)
            db.session.add(new_user)
            db.session.commit()
            msg='success'
            # return redirect(url_for('_auth.index'))
            return render_template("index.html",msg=msg)
        else:
            msg='pass'
            return render_template("Student/register_form.html",msg=msg)

     except:
          msg='email'
          flash('Invalid credentials', category='error')
         #return redirect(url_for('.register_form',msg=msg))
          return render_template("Student/register_form.html",msg=msg)

      
@_route_student.route('/register_student_details', methods=["GET", "POST"])
def register_student_details():

    auth_user=current_user
    stud =StudentDetails.query.filter(StudentDetails.user_id==auth_user.id).first()
    if auth_user.detail_no == False:
        user =StudentDetails.query.filter(StudentDetails.user_id==auth_user.id).count()
        if user==0:
            try:
                date_pred = datetime.now()
                h=float(request.form['stud_height'])
                w=float(request.form['stud_weight'])
                h=round(h,2)
                w=round(w,2)
                bmi=h*h
                bmi=round(w/bmi,2)
                new_user = StudentDetails(h, w,bmi, request.form['stud_type'], request.form['stud_track'], request.form['stud_school'],  request.form['stud_gpa'], current_user.id, date_registered=date_pred)
                db.session.add(new_user)
                approve_account = User.query.filter_by(id=int(auth_user.id)).first()
                approve_account.detail_no = False
                db.session.commit()
                # flash('Account successfully created', category='success_register')
                return redirect(url_for('.student_page_prediction'))
            except:
                flash('You can only add details and prediction once, kindly check your student details for the results', category='error')
                return redirect(url_for('.student_page'))
        
        else:
            try:
                user =StudentDetails.query.filter(StudentDetails.user_id==auth_user.id).first()
                date_pred = datetime.now()
                h=float(request.form['stud_height'])
                w=float(request.form['stud_weight'])
                h=round(h,2)
                w=round(w,2)
                bmi=h*h
                bmi=round(w/bmi,2)
                # new_user = StudentDetails(h, w,bmi, request.form['stud_gsa'], request.form['stud_tva'], request.form['stud_at'], request.form['stud_track'], request.form['stud_school'],  request.form['stud_gpa'], current_user.id, date_registered=date_pred)
                approve_account = User.query.filter_by(id=int(auth_user.id)).first()
                approve_account.detail_no = False 
                user.height=h
                user.weight=w
                user.bmi=bmi
                user.types=request.form['stud_type']
                user.track=request.form['stud_track']
                user.school=request.form['stud_school']
                user.gpa=request.form['stud_gpa']
                user.user.id=current_user.id
                user.date_registered=date_pred
                db.session.commit()
                # flash('Account successfully created', category='success_register')
                return redirect(url_for('.student_page_prediction'))
            except:
                flash('You can only add details and prediction once, kindly check your student details for the results', category='error')
                return redirect(url_for('.student_page'))

    else: 
        flash('You can only add details and prediction once, kindly check your student details for the results', category='error')
        return redirect(url_for('.student_page'))
   

@_route_student.route('/login_student', methods=['GET', 'POST'])
def login_student():
    auth_user=current_user
    if auth_user.is_authenticated:
        if auth_user.user_type == 1:
            return redirect(url_for('.student_page'))
        elif auth_user.user_type == 0:
            return redirect(url_for('_route_admin.admin_dashboard'))
        else:
            return redirect(url_for('_auth.index'))
    else:
        if request.method == 'POST':
            user = User.query.filter_by(email=request.form['email'], user_type=1).first()
            user1 = User.query.filter_by(email=request.form['email'], user_type=0).first()

            msg=''
            if user:
                if check_password_hash(user.password, request.form['password']):
                    login_user(user, remember=True)
                    return redirect(url_for('.student_page'))
                else:
                    msg='invalid'
            elif user1:
                if check_password_hash(user1.password, request.form['password']):
                    login_user(user1, remember=True)
                    return render_template("Admin/admin_form.html",auth_user=auth_user)
                else:
                    msg='invalid'
            else:
                msg='invalid'
    # return redirect(url_for('_auth.index',msg=msg))
    return render_template("index.html",msg=msg)


@_route_student.route('/result', methods=['GET'])
def result():
    auth_user=current_user
    if auth_user.is_authenticated:
        if auth_user.user_type == 1:
            return redirect(url_for('.student_page'))
        else:
            return redirect(url_for('_auth.index'))

    
    return render_template("Student/result.html")


@_route_student.route("/start_pred", methods=["GET", "POST"])
def start_pred():
    auth_user=current_user
    # check_detail_no = db.session.query(StudentDetails).filter(StudentDetails.detail_no)
    if auth_user.predict_no == True:
        flash('You can only add details and prediction once, kindly check your student details for the results', category='error')
        return redirect(url_for('.student_page'))
    else:
        data = os.path.join(os.path.abspath(os.path.dirname(__file__)),"model/data.csv")
        model1 = os.path.join(os.path.abspath(os.path.dirname(__file__)),"model/Trained_Model_knn_updated.pkl")
        model_1 = os.path.join(os.path.abspath(os.path.dirname(__file__)),"model/model_1.pkl")
        model_2 = os.path.join(os.path.abspath(os.path.dirname(__file__)),"model/model_2.pkl")

        data = pd.read_csv(data)

        model_1 = pickle.load(open(model_1, "rb"))
        model_2 = pickle.load(open(model_2, "rb"))
        # float_features = [float(x) for x in request.form.values()]
        float_features = [float(request.form['Pr1']),float(request.form['Pr2']),float(request.form['Pr3']),float(request.form['Pr4']),float(request.form['Pr5']),float(request.form['Oapr'])]
        features = [np.array(float_features)]
        # new_x=features
        new_x = pd.DataFrame(features)
        new_x['Pr1']=new_x[0]
        new_x['Pr2']=new_x[1]
        new_x['Pr3']=new_x[2]
        new_x['Pr4']=new_x[3]
        new_x['Pr5']=new_x[4]
        new_x['Oapr']=new_x[5]
        print("dataframe:\n",new_x)
        features = [
            'Pr1',
            'Pr2',
            'Pr3',
            'Pr4',
            'Pr5',
            'Oapr',
        ]

        new_x=new_x[features]

        # assume clf is your trained classifier and X is your test input data
        proba_scores = model_1.predict_proba(new_x) # get the predicted probabilities

        class_labels = model_1.classes_ # get the class labels

        # get the top 3 results with the highest probability rank
        top_3_indices = proba_scores.argsort()[:, :][:, ::-1]
        print(new_x)
        arr = np.array([])
        acc = np.array([])
        # display the top 3 results with their probability rank

        for i, indices in enumerate(top_3_indices):
            print(f"Top 3 results for test input {i}:")
            for j, index in enumerate(indices):
                label = class_labels[index]
                proba = proba_scores[i, index]
                print(f"Rank {j+1}: Class {label} with probability {proba:.4f}")
                
                # find the row index that matches the label
        #         row_index = data.index[data['Course'] == label].tolist()[0]
                row_index=data.loc[data['Course'] == label, 'Numerical_Course'].values[0]
            
                # extract the Numerical_course value at the row index
        #         fetch_course = data.loc[row_index, 'Numerical_Course']
                arr = np.append(arr,row_index)
                acc = np.append(acc,proba)
            
        print(arr)
        print(acc)
        # class_labels = model_1.classes_ # get the class labels

        grad_fetch = np.array([])
        arr1 = np.array([])
        acc1 = np.array([])
        # arr = list(map(int, arr))
        new_x = pd.DataFrame(new_x)
        print(new_x)
        
        for index in range(len(arr)):
            new_x['Numerical_Course'] = arr[index]
            # new_x = np.append(new_x, arr[index])
            # new_x=np.array(new_x)
            # new_x.columns = new_x.columns.astype(str)
            print(new_x)
            y_pred = model_2.predict(new_x)
            print("feature:",new_x)
            print("Predicted: ",y_pred)
            print("\n")
            print(y_pred)
            if y_pred==1:
                   
                if arr1.size == 3:
                    break
                else:
                    grad_fetch=int(arr[index])
                    label = data.loc[data['Numerical_Course'] == grad_fetch, 'Course'].values[0]
                    arr1 = np.append(arr1, label)
                    percent=float(acc[index])*100
                    percent=round(percent, 2)
                    acc1 = np.append(acc1, percent)

        if arr1.size == 0:
            label = data.loc[data['Numerical_Course'] == int(arr[0]), 'Course'].values[0]
            arr1 = np.append(arr1, label)
            percent=float(acc[0])*100
            percent=round(percent, 2)
            acc1 = np.append(acc1, percent)
            label = data.loc[data['Numerical_Course'] == int(arr[1]), 'Course'].values[0]
            arr1 = np.append(arr1, label)
            percent=float(acc[1])*100
            percent=round(percent, 2)
            acc1 = np.append(acc1, percent)
            label = data.loc[data['Numerical_Course'] == int(arr[2]), 'Course'].values[0]
            arr1 = np.append(arr1, label)
            percent=float(acc[2])*100
            percent=round(percent, 2)
            acc1 = np.append(acc1, percent)


        print(arr1, acc1)
        


        stud_details =StudentDetails.query.filter(StudentDetails.user_id==auth_user.id).first()
        stud_bmi=float(stud_details.bmi)
        bmi=''
        if stud_bmi<18.5:
            bmi='Underweight'
        elif stud_bmi>18.5 and stud_bmi<30:
            bmi='Normal'
        else:
            bmi='Overweight'

        des1 =Description.query.filter(Description.course==arr1[0]).first()
        des2 =Description.query.filter(Description.course==arr1[1]).first()
        des3 =Description.query.filter(Description.course==arr1[2]).first()
        date_pred = datetime.now()
        new_pred = PredictionResult( arr1[0], arr1[1], arr1[2],request.form['App'], request.form['Oapr'], request.form['Pr1'], request.form['Pr2'], request.form['Pr3'], request.form['Pr4'],  request.form['Pr5'], current_user.id, date_predicted=date_pred)
        db.session.add(new_pred)
        db.session.commit()  
        return render_template("Student/result.html", auth_user=auth_user,prediction_text1=arr1[0],prediction_text2=arr1[1],prediction_text3=arr1[2],des1=des1,des2=des2,des3=des3, bmi=bmi,stud_details=stud_details,percent1=acc1[0],percent2=acc1[1],percent3=acc1[2])