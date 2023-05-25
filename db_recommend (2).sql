-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 25, 2023 at 11:59 AM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_recommend`
--

-- --------------------------------------------------------

--
-- Table structure for table `description`
--

CREATE TABLE `description` (
  `des_id` int(11) NOT NULL,
  `course` varchar(255) NOT NULL,
  `course_des` varchar(1000) NOT NULL,
  `college` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `description`
--

INSERT INTO `description` (`des_id`, `course`, `course_des`, `college`) VALUES
(63, 'BACHELOR OF EARLY CHILDHOOD EDUCATION', 'Bachelor of Early Childhood Education is an undergraduate degree program that focuses on the education and care of children from birth to age eight. The program prepares students to become qualified early childhood educators, teaching them how to develop and implement age-appropriate curriculum, create a safe and healthy learning environment, and assess children\'s learning and development.In this program typically includes early childhood development, child psychology, curriculum design, educational psychology, classroom management, literacy and language development, and assessment and evaluation methods.', 'College of Teacher Education'),
(64, 'BS NURSING', 'Bachelor of Science in Nursing (BSN) is an undergraduate degree program that prepares individuals to become registered nurses (RNs). The program typically takes four years to complete and provides students with a strong foundation in nursing theory and practice. BSN programs usually include a combination of classroom instruction and clinical practice. Students learn about anatomy and physiology, pharmacology, nursing ethics, patient care, and other essential topics. Clinical practice allows students to apply what they have learned in real-world settings, working alongside experienced nurses in hospitals, clinics, and other healthcare facilities.', 'College of Nursing'),
(65, 'BS FORESTRY', 'Bachelor of Science in Forestry (BSF) is an undergraduate degree program that focuses on the scientific study of forest ecosystems and the sustainable management of forest resources. The program usually takes four years to complete and provides students with a strong foundation in natural sciences, environmental management, and forestry practices. BSF programs typically include courses in forest ecology, silviculture, forest management, forest economics, wildlife management, and environmental law and policy. Students also receive hands-on training in fieldwork and data analysis, which prepares them for careers in natural resource management.', 'College of Forestry and Environmental Studies'),
(66, 'AB JOURNALISM', 'Bachelor of Arts in Journalism (AB Journalism) is an undergraduate degree program that prepares students for careers in media and communications. The program usually takes four years to complete and provides students with a broad range of skills in news reporting, writing, editing, and multimedia production. AB Journalism programs typically include courses in media ethics, media law, journalism history, news gathering and reporting, feature writing, photojournalism, broadcast journalism, and digital media. Students also receive hands-on training in various media platforms, including print, broadcast, and online journalism.', 'College of Liberal Arts'),
(67, 'BS COMPUTER ENGINEERING', 'Bachelor of Science in Computer Engineering (BSCE) is an undergraduate degree program that combines principles of computer science and electrical engineering to design, develop, and maintain computer hardware and software systems. The program typically takes four years to complete and provides students with a strong foundation in programming, digital systems, and computer networks. BSCE programs typically include courses in computer programming, digital circuits, microprocessors, computer architecture, software engineering, computer networks, and operating systems. Students also receive hands-on training in various computer technologies, including computer-aided design, microcontroller programming, and networking.', 'College of Engineering'),
(68, 'BS AGRICULTURE', 'Bachelor of Science in Agriculture (BSA) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of agricultural sciences. The program typically takes four years to complete and prepares students for careers in various agricultural fields. BSA programs typically include courses in soil science, crop production, animal science, agricultural economics, plant genetics, horticulture, and farm management. Students also receive hands-on training in various agricultural technologies and practices, including agricultural machinery and equipment, irrigation systems, and pest management.', 'College of Agriculture'),
(69, 'BS MATHEMATICS', 'Bachelor of Science in Mathematics (BS Math) is an undergraduate degree program that provides students with a comprehensive understanding of mathematical theory, methods, and applications. The program typically takes four years to complete and prepares students for careers in various fields that require advanced quantitative and analytical skills. BS Math programs typically include courses in calculus, algebra, number theory, geometry, probability, statistics, and mathematical modeling. Students also receive training in computer programming, data analysis, and computational methods.', 'College of Science and Mathematics'),
(70, 'BS MECHANICAL ENGINEERING', 'Bachelor of Science in Mechanical Engineering (BSME) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of mechanical systems and machinery. The program typically takes four years to complete and prepares students for careers in various industries that require expertise in mechanical engineering. BSME programs typically include courses in calculus, physics, mechanics, thermodynamics, materials science, design, and manufacturing. Students also receive hands-on training in various mechanical engineering technologies and practices, including computer-aided design (CAD), finite element analysis (FEA), and machine tool operations.', 'College of Engineering'),
(71, 'BS ENVIRONMENTAL ENGINEERING', 'Bachelor of Science in Environmental Engineering (BSEnvE) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of environmental engineering. The program typically takes four years to complete and prepares students for careers in various industries that require expertise in environmental engineering. BSEnvE programs typically include courses in chemistry, physics, biology, fluid mechanics, water and wastewater treatment, air pollution control, solid waste management, and environmental law and policy. Students also receive hands-on training in various environmental engineering technologies and practices, including environmental monitoring and analysis, environmental impact assessment, and sustainability analysis.', 'College of Engineering'),
(72, 'AB POLITICAL SCIENCE', 'Bachelor of Arts in Political Science (AB PolSci) is an undergraduate degree program that provides students with a comprehensive understanding of political theory, institutions, and processes. The program typically takes four years to complete and prepares students for careers in various fields that require advanced critical thinking and analytical skills. AB PolSci programs typically include courses in political theory, comparative politics, international relations, political economy, public administration, and political research methods. Students also receive training in communication and negotiation skills, as well as in public policy analysis and development.', 'College of Liberal Arts'),
(73, 'AB HISTORY', 'Bachelor of Arts in History (AB History) is an undergraduate degree program that provides students with a comprehensive understanding of the development of human societies and cultures over time. The program typically takes four years to complete and prepares students for careers in various fields that require advanced critical thinking, research, and communication skills. AB History programs typically include courses in world history, national and regional history, historical methodology, historiography, and historical research and writing. Students also receive training in critical analysis, communication, and research skills, as well as in digital humanities and cultural heritage.', 'College of Liberal Arts'),
(74, 'BS PHYSICS', 'Bachelor of Science in Physics (BS Physics) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of physics. The program typically takes four years to complete and prepares students for careers in various fields that require advanced quantitative and analytical skills. BS Physics programs typically include courses in mechanics, electromagnetism, thermodynamics, quantum mechanics, statistical mechanics, and optics. Students also receive training in laboratory techniques, data analysis, and computational methods.', 'College of Science and Mathematics'),
(75, 'BS AGRI-BUSINESS', 'Bachelor of Agri-business (BS Agribusiness) is an undergraduate degree program that combines the study of agricultural sciences with business management principles. The program typically takes four years to complete and prepares students for careers in various fields that require expertise in agricultural production and management. B.Agri-Business programs typically include courses in agriculture, business management, economics, finance, accounting, marketing, and agricultural policy. Students also receive hands-on training in various agricultural technologies and practices, including crop management, livestock management, and farm management.', 'College of Agriculture'),
(76, 'BS GEODETIC ENGINEERING', 'Bachelor of Science in Geodetic Engineering (BS GE) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of geodetic surveying and mapping. The program typically takes five years to complete and prepares students for careers in various fields that require expertise in geospatial data collection, analysis, and management. BS GE programs typically include courses in geodetic surveying, land surveying, photogrammetry, remote sensing, geographic information systems (GIS), and cartography. Students also receive hands-on training in fieldwork, data analysis, and software applications.', 'College of Engineering'),
(77, 'BS INDUSTRIAL ENGINEERING', 'Bachelor of Science in Industrial Engineering (BSIE) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of designing, developing, and optimizing complex systems and processes. The program typically takes four years to complete and prepares students for careers in various fields that require expertise in engineering, management, and data analysis. BSIE programs typically include courses in operations research, quality control, supply chain management, project management, manufacturing processes, and engineering economics. Students also receive training in computer-aided design (CAD), simulation, and statistical analysis.', 'College of Engineering'),
(78, 'BS AGRO-FORESTRY', 'Bachelor of Science in Agro-Forestry (BS AF) is an undergraduate degree program that combines the principles and practices of agriculture and forestry to promote sustainable land management practices. The program typically takes four years to complete and prepares students for careers in various fields that require expertise in both agriculture and forestry. BS AF programs typically include courses in soil science, plant science, forest ecology, agroforestry systems, silviculture, forest economics, and natural resource management. Students also receive hands-on training in various agricultural and forestry techniques and practices.', 'College of Forestry and Environmental Studies'),
(79, 'BACHELOR OF AGRICULTURAL TECHNOLOGY', 'Bachelor of Agricultural Technology (BAT) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of modern agriculture. The program typically takes four years to complete and prepares students for careers in various fields that require expertise in agriculture and technology. BAT programs typically include courses in crop science, animal science, soil science, agricultural engineering, agricultural economics, and agricultural extension. Students also receive hands-on training in various agricultural technologies and practices, including precision farming, irrigation systems, and farm management software.', 'College of Agriculture'),
(80, 'BS CRIMINOLOGY', 'Bachelor of Science in Criminology (BSCrim) is an undergraduate degree program that provides students with a comprehensive understanding of the nature of crime, the criminal justice system, and the socio-cultural factors that contribute to criminal behavior. The program typically takes four years to complete and prepares students for careers in various fields related to law enforcement, security, and justice. BSCrim programs typically include courses in criminal law, forensic science, investigation, psychology, sociology, and criminology theory. Students also receive practical training in crime scene investigation, evidence collection, and criminal profiling.', 'College of Criminal Justice and Education'),
(81, 'BS ELECTRONICS COMMUNICATION ENGINEERING', 'Bachelor of Science in Electronics Communication Engineering (BS ECE) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of electronic communication systems. The program typically takes four years to complete and prepares students for careers in various fields related to electronics, telecommunications, and networking. BS ECE programs typically include courses in circuit analysis, signal processing, electronic devices, communication systems, digital electronics, and computer networks. Students also receive hands-on training in electronic circuits design, wireless communications, and embedded systems.', 'College of Engineering'),
(82, 'BS CIVIL ENGINEERING', 'Bachelor of Science in Civil Engineering (BSCE) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of designing, constructing, and maintaining physical infrastructure. The program typically takes four years to complete and prepares students for careers in various fields related to civil engineering. BSCE programs typically include courses in structural analysis and design, geotechnical engineering, water resources engineering, transportation engineering, and construction management. Students also receive hands-on training in surveying, materials testing, and project management.', 'College of Engineering'),
(83, 'BS ELECTRICAL ENGINEERING', 'Bachelor of Science in Electrical Engineering (BSEE) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of designing, developing, and maintaining electrical systems and devices. The program typically takes four years to complete and prepares students for careers in various fields related to electrical engineering. BSEE programs typically include courses in circuit analysis, electronics, power systems, electromagnetism, signal processing, and control systems. Students also receive hands-on training in electrical circuits design, programming, and testing.', 'College of Engineering'),
(84, 'BS BIOLOGY', 'Bachelor of Science in Biology (BS Biology) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of biology, the study of living organisms. The program typically takes four years to complete and prepares students for careers in various fields related to biology. BS Biology programs typically include courses in cell biology, genetics, microbiology, ecology, evolution, and anatomy and physiology. Students also receive hands-on training in laboratory techniques, experimental design, and data analysis.', 'College of Science and Mathematics'),
(85, 'BS SOCIAL WORK', 'Bachelor of Science in Social Work (BSSW) is an undergraduate degree program that prepares students for a career in social work, which involves helping individuals, families, and communities to improve their well-being and quality of life. The program typically takes four years to complete and provides students with a comprehensive understanding of social work theories, methods, and practices. BSSW programs typically include courses in human behavior, social welfare policy, research methods, social work practice, and field education. Students also receive hands-on training through internships and practicum experiences in various social service settings.', 'College of Social Work and Community Development'),
(86, 'BS INFORMATION TECHNOLOGY', 'Bachelor of Science in Information Technology (BSIT) is an undergraduate degree program that provides students with a comprehensive understanding of the principles and practices of information technology, the study of computer-based information systems. The program typically takes four years to complete and prepares students for careers in various fields related to information technology. BSIT programs typically include courses in programming, database management, web development, network systems, cybersecurity, and information management. Students also receive hands-on training in computer programming languages, software development, and project management.', 'College of Computing Studies'),
(87, 'BACHELOR OF ELEMENTARY EDUCATION', 'Bachelor of Elementary Education (BEE) is an undergraduate degree program that prepares students to become teachers for grades one to six in elementary schools. The program typically takes four years to complete and provides students with a comprehensive understanding of the principles and practices of teaching and learning. BEE programs typically include courses in educational psychology, teaching methods, child development, curriculum development, and classroom management. Students also receive hands-on training through classroom observations and practice teaching in actual elementary school classrooms.', 'College of Teacher Education'),
(88, 'BS COMMUNITY DEVELOPMENT', 'Bachelor of Science in Community Development (BSCD) is an undergraduate degree program that equips students with the knowledge and skills to address social and economic issues affecting communities. The program typically takes four years to complete and provides students with a comprehensive understanding of community development theories, practices, and approaches. BSCD programs typically include courses in community organizing, project management, community research, social entrepreneurship, and public policy. Students also receive hands-on training through internships and fieldwork experiences in various community development settings.', 'College of Social Work and Community Development'),
(89, 'BA ELS', 'Bachelor of Arts in English Language Studies (BA ELS) is an undergraduate degree program that focuses on the study of the English language and its use in various contexts, including literature, culture, and communication. The program typically takes four years to complete and provides students with a comprehensive understanding of the principles and practices of English language teaching, learning, and research. BA ELS programs typically include courses in English grammar, writing, literature, linguistics, and language teaching methodology. Students also receive hands-on training through teaching practicums and research projects.', 'College of Liberal Arts'),
(90, 'BS COMPUTER SCIENCE', 'Bachelor of Science in Computer Science (BSCS) is an undergraduate degree program that focuses on the study of computer software, hardware, and their applications. The program typically takes four years to complete and provides students with a comprehensive understanding of the principles and practices of computer science. BSCS programs typically include courses in programming languages, data structures, algorithms, operating systems, computer networks, databases, and software engineering. Students also receive hands-on training through laboratory work, programming projects, and internships.', 'College of Computing Studies'),
(91, 'BS ARCHITECTURE', 'Bachelor of Science in Architecture (BS Architecture) is an undergraduate degree program that focuses on the study of architectural design, building systems, construction methods, and architectural history. The program typically takes five years to complete and provides students with a comprehensive understanding of the principles and practices of architecture. BS Architecture programs typically include courses in design theory, drawing and modeling, building materials, structural design, building systems, construction technology, architectural history, and professional practice. Students also receive hands-on training through design studios, construction site visits, and internship programs.', 'College of Architecture'),
(92, 'BS ASIAN STUDIES', 'Bachelor of Science in Asian Studies (BS Asian Studies) is an undergraduate degree program that focuses on the study of the culture, history, politics, economics, and social issues of Asia. The program typically takes four years to complete and provides students with a comprehensive understanding of the diverse and complex aspects of Asian societies. BS Asian Studies programs typically include courses in Asian languages, history, philosophy, religion, art, literature, politics, economics, and social issues. Students also have the opportunity to study abroad, participate in research projects, and complete internships in Asian countries.', 'College of Asians and Islamic Studies'),
(93, 'AB BROADCASTING', 'Bachelor of Arts in Broadcasting (AB Broadcasting) is an undergraduate degree program that focuses on the study of broadcast journalism, radio and television production, media management, and communication theory. The program typically takes four years to complete and provides students with the knowledge and skills necessary to work in the broadcasting industry. AB Broadcasting programs typically include courses in writing for media, news gathering and reporting, video and audio production, media law and ethics, media management, and communication theory. Students also receive hands-on training through internships and practical projects.', 'College of Liberal Arts'),
(94, 'BATSILYER NG SINING SA FILIPINO', 'Ang Batsilyer ng Sining sa Filipino (Bachelor of Arts in Filipino) ay isang programa ng pre-bago na nagbibigay ng edukasyon sa mga mag-aaral tungkol sa wika, panitikan, at kultura ng Filipino. Ang programa ay karaniwang tumatagal ng apat na taon at naglalayong bigyan ng malawak na kaalaman at kasanayan ang mga mag-aaral sa pagsusulat, pagbabasa, at pagsasalin ng iba\'t ibang anyo ng panitikan sa Filipino.Kabilang sa mga kurso sa programa ang Panitikang Pilipino, Pagsulat ng mga Sanaysay, Malikhaing Pagsulat, Panitikan ng mga Rehiyon sa Pilipinas, Pagsasalin ng Panitikan, at Mga Teorya sa Wika at Panitikan. Mayroon ding mga kursong nagbibigay ng praktikal na kasanayan sa paggamit ng mga teknolohiya at media sa pagpapakalat ng wika at kultura ng Filipino.', 'College of Liberal Arts'),
(95, 'BS NUTRITION AND DIETETICS', 'A BS in Nutrition and Dietetics is an undergraduate degree program that focuses on the study of food, nutrition, and health. This program prepares students to become licensed dietitians and nutritionists who can work in a variety of settings, including hospitals, clinics, schools, government agencies, and private practice. The program typically covers a range of topics, including anatomy and physiology, nutrition science, food chemistry, food service management, and public health. Students may also have the opportunity to participate in internships and clinical rotations to gain practical experience in the field.', 'College of Home Economics'),
(96, 'BS ENVIRONMENTAL SCIENCE', 'A BS in Environmental Science is an undergraduate degree program that focuses on the study of the environment, including its natural resources, biodiversity, ecosystems, and human impacts. This program prepares students to become environmental scientists who can work in a variety of settings, including government agencies, non-profit organizations, consulting firms, and private industry. The program typically covers a range of topics, including ecology, geology, climate change, sustainability, environmental policy, and environmental law. Students may also have the opportunity to participate in fieldwork and research projects to gain practical experience in the field.', 'College of Forestry and Environmental Studies'),
(97, 'BS STATISTIC', 'A BS in Statistics is an undergraduate degree program that focuses on the study of statistical theory, data analysis, and mathematical modeling. This program prepares students to become statisticians who can work in a variety of settings, including research institutions, government agencies, healthcare organizations, and private industry. The program typically covers a range of topics, including probability theory, statistical inference, regression analysis, experimental design, and data visualization. Students may also have the opportunity to participate in research projects and internships to gain practical experience in the field.', 'College of Sceince and Mathematics'),
(98, 'BS EXERCISE AND SPORTS SCIENCE', 'A BS in Exercise and Sports Science is an undergraduate degree program that focuses on the study of human movement, exercise physiology, and sports performance. This program prepares students to become exercise physiologists, sports coaches, personal trainers, and other professionals in the field of exercise and sports science. The program typically covers a range of topics, including anatomy and physiology, kinesiology, exercise prescription, sports psychology, and nutrition. Students may also have the opportunity to participate in clinical rotations, internships, or research projects to gain practical experience in the field.', 'College of Sports and Physical Education'),
(99, 'BS CHEMISTRY', 'A BS in Chemistry is an undergraduate degree program that focuses on the study of matter, its properties, and its interactions. This program prepares students to become chemists who can work in a variety of settings, including research institutions, government agencies, pharmaceutical companies, and private industry. The program typically covers a range of topics, including organic chemistry, physical chemistry, analytical chemistry, biochemistry, and chemical engineering. Students may also have the opportunity to participate in laboratory work and research projects to gain practical experience in the field.', 'College of Sceince and Mathematics'),
(100, 'BS HOME ECONOMICS', 'BS Home Economics is an undergraduate program that focuses on the study of various aspects of home management and family life. It aims to equip students with the knowledge and skills to manage households efficiently, promote healthy living, and provide education on child development, family relations, nutrition, and consumer economics. The curriculum typically includes courses such as food science and nutrition, family and child development, consumer economics, textiles and clothing, interior design, and housing and home management. Students may also be required to complete practical training, internships, or community service to gain hands-on experience.', 'College of Home Economics'),
(101, 'BACHELOR OF SPECIAL NEED EDUCATION', 'A Bachelor of Special Needs Education is an undergraduate degree program that focuses on the education of children with special needs. This program prepares students to become special education teachers who can work in a variety of settings, including public and private schools, special education centers, and non-profit organizations. The program typically covers a range of topics, including educational psychology, special education law, behavior management, communication disorders, and curriculum development. Students may also have the opportunity to participate in teaching practicums and internships to gain practical experience in the field.', 'College of Teacher Education'),
(102, 'BS AGRICULTURAL BIOSYSTEM ENGINEERING', 'A BS in Agricultural Biosystems Engineering is an undergraduate degree program that focuses on the application of engineering principles to biological systems used in agriculture, such as crops, livestock, and natural resources. This program prepares students to become agricultural engineers who can work in a variety of settings, including agricultural research institutions, government agencies, and private industry. The program typically covers a range of topics, including mechanics of biological materials, soil and water conservation, sustainable agriculture, precision agriculture, and food processing. Students may also have the opportunity to participate in laboratory work, design projects, and internships to gain practical experience in the field.', 'College of Engineering'),
(103, 'BS ISLAMIC STUDIES', 'A BS in Islamic Studies is an undergraduate degree program that focuses on the academic study of Islam and its history, culture, and traditions. This program prepares students to become experts in Islamic theology, law, and philosophy and to work in a variety of settings, including academic institutions, religious organizations, and government agencies. The program typically covers a range of topics, including Islamic history, Quranic studies, Islamic law, Islamic philosophy, and Islamic art and architecture. Students may also have the opportunity to learn Arabic and other languages used in Islamic scholarship and to participate in study abroad programs to gain first-hand experience of Islamic cultures and traditions.', 'College of Asians ans Islamic Studies'),
(104, 'BS HOME MANAGEMENT', 'A BS in Home Management is an undergraduate degree program that focuses on the study of managing households and households\' resources. This program prepares students to become professionals who can work in a variety of settings, including households, non-profit organizations, and private industry. The program typically covers a range of topics, including financial management, family and consumer sciences education, food and nutrition, housing and interior design, and communication skills. Students may also have the opportunity to participate in internships or research projects to gain practical experience in the field.', 'College of Home Economics'),
(105, 'BS SANITARY ENGINEERING', 'A BS in Sanitary Engineering is an undergraduate degree program that focuses on the study of the design and construction of systems and facilities that promote public health and safety by preventing and controlling the spread of disease. This program prepares students to become professionals who can work in a variety of settings, including government agencies, public health organizations, and private industry. The program typically covers a range of topics, including environmental health, water supply and treatment, wastewater treatment and disposal, solid waste management, and air pollution control. Students may also have the opportunity to participate in laboratory work, design projects, and internships to gain practical experience in the field.', 'College of Engineering'),
(106, 'BACHELOR OF PHYSICAL EDUCATION', 'A Bachelor of Physical Education is an undergraduate degree program that focuses on the study of physical activity, exercise, and sports. This program prepares students to become professionals who can work in a variety of settings, including schools, colleges, universities, fitness centers, and sports organizations. The program typically covers a range of topics, including anatomy, physiology, biomechanics, kinesiology, exercise physiology, sports psychology, and coaching methods. Students may also have the opportunity to participate in teaching practicums and internships to gain practical experience in the field.', 'College of Sports Science and Physical Education'),
(107, 'BACHELOR OF SECONDARY EDUCATION', 'A Bachelor of Secondary Education is an undergraduate degree program that focuses on the study of teaching in secondary schools. This program prepares students to become teachers who can work in a variety of subject areas, including English, mathematics, science, social studies, and foreign languages. The program typically covers a range of topics, including educational psychology, classroom management, curriculum development, assessment and evaluation, and teaching methods. Students may also have the opportunity to participate in teaching practicums and internships to gain practical experience in the field.', 'College of Teacher Education'),
(108, 'BACHELOR OF CULTURE AND ARTS EDUCATION', 'A Bachelor of Culture and Arts Education is an undergraduate degree program that focuses on the study of arts education in a cultural context. This program prepares students to become professionals who can work in a variety of settings, including schools, museums, art centers, and community organizations. The program typically covers a range of topics, including art history, visual arts, performing arts, music, dance, cultural studies, curriculum development, and teaching methods. Students may also have the opportunity to participate in teaching practicums and internships to gain practical experience in the field.', 'College of Teacher Education'),
(109, 'BS FOOD TECHNOLOGY', 'A BS in Food Technology is an undergraduate degree program that focuses on the study of food processing, preservation, and safety. This program prepares students to become professionals who can work in the food industry, research institutions, or government agencies. The program typically covers a range of topics, including food chemistry, microbiology, nutrition, sensory evaluation, food processing, food preservation, food packaging, and quality control. Students may also have the opportunity to participate in laboratory work, research projects, and internships to gain practical experience in the field.', 'College of Agriculture'),
(110, 'BS ACCOUNTANCY', 'A BS in Accountancy is an undergraduate degree program that focuses on the study of accounting principles and practices. This program prepares students to become professionals who can work in a variety of settings, including accounting firms, corporations, government agencies, and non-profit organizations. The program typically covers a range of topics, including financial accounting, managerial accounting, taxation, auditing, financial statement analysis, and accounting information systems. Students may also have the opportunity to participate in internships or practicums to gain practical experience in the field.', 'College of Liberal Arts');

-- --------------------------------------------------------

--
-- Table structure for table `prediction_result`
--

CREATE TABLE `prediction_result` (
  `result_id` int(11) NOT NULL,
  `main_rank` varchar(255) NOT NULL,
  `sub_rank1` varchar(255) NOT NULL,
  `sub_rank2` varchar(255) NOT NULL,
  `app_no` varchar(255) NOT NULL,
  `oapr` varchar(255) NOT NULL,
  `english` varchar(255) NOT NULL,
  `reading` varchar(255) NOT NULL,
  `science` varchar(255) NOT NULL,
  `math` varchar(255) NOT NULL,
  `logic` varchar(255) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `date_predicted` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `prediction_result`
--

INSERT INTO `prediction_result` (`result_id`, `main_rank`, `sub_rank1`, `sub_rank2`, `app_no`, `oapr`, `english`, `reading`, `science`, `math`, `logic`, `user_id`, `date_predicted`) VALUES
(1, 'BACHELOR OF SECONDARY EDUCATION', 'BS NURSING', 'BS BIOLOGY', '42', '90.60', '87.60', '92.88', '80.93', '84.63', '83.75', 9, '2023-04-03 09:24:25'),
(2, 'BS FORESTRY', 'AB HISTORY', 'BS AGRICULTURE', '34', '8', '50', '41', '28', '34', '93', 12, '2023-04-03 11:13:51'),
(3, 'BS FORESTRY', 'AB HISTORY', 'BS AGRICULTURE', '34', '8', '50', '41', '28', '34', '93', 12, '2023-04-03 11:19:00'),
(4, 'BS GEODETIC ENGINEERING', 'BS ENVIRONMENTAL SCIENCE', 'BS ASIAN STUDIES', '65', '78', '94', '74', '21', '43', '87', 12, '2023-04-03 11:20:16'),
(5, 'AB POLITICAL SCIENCE', 'BACHELOR OF CULTURE AND ARTS EDUCATION', 'BS ENVIRONMENTAL SCIENCE', '8', '87', '89', '78', '42', '67', '90', 12, '2023-04-03 11:20:58'),
(6, 'BS MATHEMATICS', 'BS AGRICULTURE', 'BS ASIAN STUDIES', '33', '41', '3', '81', '7', '87', '73', 13, '2023-04-03 21:49:46'),
(7, 'BS MATHEMATICS', 'BS AGRICULTURE', 'BS ASIAN STUDIES', '33', '41', '3', '81', '7', '87', '73', 13, '2023-04-03 21:56:05'),
(8, 'BS MATHEMATICS', 'BS AGRICULTURE', 'BS ASIAN STUDIES', '33', '41', '3', '81', '7', '87', '73', 13, '2023-04-03 21:57:42'),
(9, 'BS MATHEMATICS', 'BS AGRICULTURE', 'BS ASIAN STUDIES', '33', '41', '3', '81', '7', '87', '73', 13, '2023-04-03 22:00:12'),
(10, 'BS MATHEMATICS', 'BS AGRICULTURE', 'BS ASIAN STUDIES', '33', '41', '3', '81', '7', '87', '73', 13, '2023-04-03 22:01:17'),
(11, 'BS MATHEMATICS', 'BS AGRICULTURE', 'BS ASIAN STUDIES', '33', '41', '3', '81', '7', '87', '73', 13, '2023-04-03 22:03:27'),
(12, 'BS MATHEMATICS', 'BS AGRICULTURE', 'BS ASIAN STUDIES', '33', '41', '3', '81', '7', '87', '73', 13, '2023-04-03 22:05:56'),
(13, 'BS MATHEMATICS', 'BS AGRICULTURE', 'BS ASIAN STUDIES', '33', '41', '3', '81', '7', '87', '73', 13, '2023-04-03 22:08:31'),
(14, 'BS MATHEMATICS', 'BS AGRICULTURE', 'BS ASIAN STUDIES', '33', '41', '3', '81', '7', '87', '73', 13, '2023-04-03 22:15:08'),
(15, 'BS MATHEMATICS', 'BS AGRICULTURE', 'BS ASIAN STUDIES', '33', '41', '3', '81', '7', '87', '73', 13, '2023-04-03 22:16:02'),
(16, 'BS MATHEMATICS', 'BS AGRICULTURE', 'BS ASIAN STUDIES', '33', '41', '3', '81', '7', '87', '73', 13, '2023-04-03 22:16:39'),
(17, 'BS MATHEMATICS', 'BS AGRICULTURE', 'BS ASIAN STUDIES', '33', '41', '3', '81', '7', '87', '73', 13, '2023-04-03 22:20:33'),
(18, 'BS MATHEMATICS', 'BS AGRICULTURE', 'BS ASIAN STUDIES', '33', '41', '3', '81', '7', '87', '73', 13, '2023-04-03 22:31:23'),
(19, 'BS INDUSTRIAL ENGINEERING', 'BS ISLAMIC STUDIES', 'BS ASIAN STUDIES', '92', '31', '33', '77', '34', '8', '43', 13, '2023-04-04 08:25:49'),
(20, 'BS HOME ECONOMICS', 'BA ELS', 'BS AGRICULTURE', '41', '50', '19', '24', '35', '69', '6', 13, '2023-04-04 11:55:19'),
(21, 'BS HOME ECONOMICS', 'BA ELS', 'BS AGRICULTURE', '41', '50', '19', '24', '35', '69', '6', 13, '2023-04-04 11:58:42'),
(22, 'BS HOME ECONOMICS', 'BA ELS', 'BS AGRICULTURE', '41', '50', '19', '24', '35', '69', '6', 13, '2023-04-04 11:59:32'),
(23, 'BS HOME ECONOMICS', 'BA ELS', 'BS AGRICULTURE', '69', '87', '17', '65', '18', '40', '99', 13, '2023-04-04 12:04:10'),
(24, 'BS SANITARY ENGINEERING', 'BS ELECTRONICS COMMUNICATION ENGINEERING', 'BS ELECTRICAL ENGINEERING', '6723', '91.56', '84.91', '92.88', '96.28', '89.31', '63.1', 16, '2023-04-04 14:09:49'),
(25, 'BS SANITARY ENGINEERING', 'BS ELECTRONICS COMMUNICATION ENGINEERING', 'BS ELECTRICAL ENGINEERING', '6723', '91.56', '84.91', '92.88', '96.28', '89.31', '63.1', 16, '2023-04-04 14:09:49'),
(26, 'AB HISTORY', 'BS FORESTRY', 'BS AGRICULTURE', '5832', '61.37', '68.5', '48.4', '44.12', '34.54', '72.9', 16, '2023-04-04 14:12:26'),
(27, 'BS ASIAN STUDIES', 'BS HOME MANAGEMENT', 'BS NUTRITION AND DIETETICS', '4567', '64.72', '61.05', '77.12', '44.12', '63.45', '53.29', 16, '2023-04-04 14:13:52'),
(28, 'BS ASIAN STUDIES', 'BS HOME MANAGEMENT', 'BS NUTRITION AND DIETETICS', '4567', '64.72', '61.05', '77.12', '44.12', '63.45', '53.29', 16, '2023-04-04 14:16:11'),
(29, 'BS AGRICULTURE', 'BS EXERCISE AND SPORTS SCIENCE', 'BS HOME ECONOMICS', '36', '42', '74', '53', '15', '80', '35', 13, '2023-05-09 10:47:37'),
(30, 'BS ISLAMIC STUDIES', 'BS INDUSTRIAL ENGINEERING', 'BS ASIAN STUDIES', '1', '52', '31', '69', '26', '91', '20', 13, '2023-05-09 10:53:43'),
(31, 'BS ISLAMIC STUDIES', 'BS INDUSTRIAL ENGINEERING', 'BS ASIAN STUDIES', '1', '52', '31', '69', '26', '91', '20', 13, '2023-05-09 10:54:05'),
(32, 'BS HOME ECONOMICS', 'BS INDUSTRIAL ENGINEERING', 'BS AGRICULTURE', '62', '13', '1', '43', '92', '86', '70', 13, '2023-05-09 10:54:16'),
(33, 'BS HOME ECONOMICS', 'AB JOURNALISM', 'BS ARCHITECTURE', '29', '94', '42', '86', '97', '78', '24', 13, '2023-05-09 10:54:32'),
(34, 'BS FOOD TECHNOLOGY', 'BS EXERCISE AND SPORTS SCIENCE', 'BS ISLAMIC STUDIES', '84', '42', '41', '70', '87', '11', '33', 13, '2023-05-09 10:54:40'),
(35, 'BS ISLAMIC STUDIES', 'BS ASIAN STUDIES', 'BS AGRO-FORESTRY', '37', '33', '89', '95', '17', '49', '55', 13, '2023-05-09 10:54:52'),
(36, 'BS EXERCISE AND SPORTS SCIENCE', 'BS STATISTIC', 'BS HOME ECONOMICS', '87', '54', '82', '66', '43', '85', '86', 13, '2023-05-09 10:55:05'),
(37, 'BS ACCOUNTANTCY', 'BS MECHANICAL ENGINEERING', 'BS CIVIL ENGINEERING', '34', '99', '99', '99', '99', '99', '99', 13, '2023-05-09 10:55:32'),
(38, 'BS EXERCISE AND SPORTS SCIENCE', 'BS AGRICULTURE', 'BS HOME ECONOMICS', '11', '33', '56', '95', '84', '41', '88', 13, '2023-05-09 10:56:00'),
(39, 'BS ASIAN STUDIES', 'BS ISLAMIC STUDIES', 'BS ENVIRONMENTAL SCIENCE', '43', '80', '80', '80', '80', '80', '88', 13, '2023-05-09 10:56:23'),
(40, 'BS SANITARY ENGINEERING', 'BS ELECTRICAL ENGINEERING', 'BACHELOR OF PHYSICAL EDUCATION', '96', '93', '85', '53', '76', '61', '47', 13, '2023-05-09 10:56:33'),
(41, 'BS HOME ECONOMICS', 'BA ELS', 'BS AGRICULTURE', '76', '61', '17', '55', '5', '93', '88', 13, '2023-05-09 10:56:47'),
(42, 'BS INDUSTRIAL ENGINEERING', 'BS EXERCISE AND SPORTS SCIENCE', 'BS MATHEMATICS', '68', '38', '66', '88', '64', '91', '95', 13, '2023-05-09 10:56:56'),
(43, 'BS INDUSTRIAL ENGINEERING', 'BS ENVIRONMENTAL ENGINEERING', 'BS HOME MANAGEMENT', '10', '86', '94', '90', '61', '37', '42', 13, '2023-05-09 10:57:14'),
(44, 'BS EXERCISE AND SPORTS SCIENCE', 'AB HISTORY', 'BA ELS', '55', '36', '75', '29', '54', '24', '66', 13, '2023-05-09 10:57:52'),
(45, 'BS INDUSTRIAL ENGINEERING', 'AB JOURNALISM', 'BS HOME ECONOMICS', '29', '88', '77', '47', '4', '36', '86', 13, '2023-05-09 10:58:02'),
(46, 'BS AGRICULTURE', 'BS INDUSTRIAL ENGINEERING', 'AB JOURNALISM', '46', '19', '45', '70', '3', '67', '26', 13, '2023-05-09 10:59:13'),
(47, 'BS AGRICULTURE', 'BS INDUSTRIAL ENGINEERING', 'AB JOURNALISM', '46', '19', '45', '70', '3', '67', '26', 13, '2023-05-09 10:59:55'),
(48, 'AB JOURNALISM', 'BACHELOR OF ELEMENTARY EDUCATION', 'BS EXERCISE AND SPORTS SCIENCE', '52', '80', '69', '45', '65', '36', '94', 17, '2023-05-23 09:58:26');

-- --------------------------------------------------------

--
-- Table structure for table `studentcsv`
--

CREATE TABLE `studentcsv` (
  `id` int(11) NOT NULL,
  `student_id_csv` varchar(255) NOT NULL,
  `firstname_csv` varchar(255) NOT NULL,
  `middlename_csv` varchar(255) DEFAULT NULL,
  `lastname_csv` varchar(255) NOT NULL,
  `oapr_csv` varchar(120) NOT NULL,
  `english_csv` varchar(120) NOT NULL,
  `reading_csv` varchar(120) NOT NULL,
  `science_csv` varchar(120) NOT NULL,
  `math_csv` varchar(120) NOT NULL,
  `logic_csv` varchar(120) NOT NULL,
  `course_csv` varchar(120) NOT NULL,
  `college_csv` varchar(120) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `studentcsv`
--

INSERT INTO `studentcsv` (`id`, `student_id_csv`, `firstname_csv`, `middlename_csv`, `lastname_csv`, `oapr_csv`, `english_csv`, `reading_csv`, `science_csv`, `math_csv`, `logic_csv`, `course_csv`, `college_csv`) VALUES
(1, 'Student ID', 'First Name ', 'Middle Name', 'Last Name', 'OAPR', 'Pr1', 'Pr2', 'Pr3', 'Pr4', 'Pr5', 'Course', 'College'),
(2, '93265', 'Adelaida', 'bareto', 'Santos', '75.16', '70.75', '87.4', '59.25', '44.18', '83.75', 'BS CHEMISTRY', 'COLLEGE OF SCIENCE AND MATHEMATICS'),
(3, '42186', 'Arianne', 'Alfonso', 'Santos', '66.95', '80.58', '66.85', '29.96', '44.18', '43.49', 'BACHELOR IN ELEMENTARY EDUCATION', 'COLLEGE OF TEACHER EDUCATION'),
(4, '83224', 'Arnel', 'Ramos', 'Reyes', '91.08', '88.66', '77.12', '91.97', '94.54', '63.1', 'BS COMPUTER ENGINEERING', 'COLLEGE OF ENGINEERING'),
(5, '73888', 'Angelica', 'Villanueva', 'Garcia', '72.43', '61.05', '48.4', '85.06', '89.31', '53.29', 'BS COMPUTER SCIENCE', 'COLLEGE OF COMPUTING STUDIES'),
(6, '64940', 'Anselmo', 'Santos', 'Cruz', '72.43', '61.05', '66.85', '59.25', '92.22', '63.1', 'AB POLITICAL SCIENCE', 'COLLEGE OF LIBERAL ARTS'),
(7, '87955', 'Aldrin', 'Sandoval', 'Gonzales', '62.48', '68.5', '35.7', '13.15', '92.22', '63.1', 'BS ARCHITECTURE', 'COLLEGE OF ARCHITECTURE'),
(8, '22873', 'Armand', 'Escalante', 'Ramos', '70.3', '76.83', '82.26', '13.15', '53.82', '79.78', 'AB POLITICAL SCIENCE', 'COLLEGE OF LIBERAL ARTS'),
(9, '61474', 'Angelito', 'Sanchez', 'Fernandez', '87.64', '89.71', '77.12', '91.97', '53.82', '72.9', 'BS ELECTRICAL ENGINEERING', 'COLLEGE OF ENGINEERING'),
(10, '72722', 'Agatha', 'Espino', 'Rivera', '65.83', '58.56', '82.26', '85.06', '34.54', '26.06', 'BS COMMUNITY DEVELOPMENT', 'COLLEGE OF SOCIAL WORK & COMMUNITY DEVELOPMENT'),
(11, '40966', 'Amado', 'Razon', 'Perez', '70.3', '70.75', '54.75', '80.93', '53.82', '53.29', 'BS ELECTRICAL ENGINEERING', 'COLLEGE OF ENGINEERING'),
(12, '17492', 'Arlene', 'Cayetano', 'Alvarez', '92.03', '94.81', '90.94', '80.93', '79.96', '63.1', 'BS NURSING', 'COLLEGE OF NURSING'),
(13, '90485', 'Adolfo', 'Valdez', 'Torres', '80.63', '70.75', '77.12', '80.93', '70.61', '87.72', 'BS ECONOMICS', 'COLLEGE OF LIBERAL ARTS'),
(14, '26807', 'Arjay', 'Agustin', 'Hernandez', '96.35', '89.71', '92.88', '96.28', '94.54', '98.34', 'BS ELECTRICAL ENGINEERING', 'COLLEGE OF ENGINEERING'),
(15, '54618', 'Abegail', 'Pascual', 'Santiago', '69.19', '66.01', '25.06', '66.81', '92.22', '72.9', 'BACHELOR OF PHYSICAL EDUCATION', 'COLLEGE OF SPORTS SCIENCE AND PHYSICAL EDUCATION'),
(16, '68397', 'Amor', 'Lomibao', 'Lopez', '87.64', '83.47', '94.82', '94.84', '24.91', '79.78', 'BS FORESTRY', 'COLLEGE OF FORESTRY & ENVIRONMENTAL STUDIES'),
(17, '47433', 'Bryan', 'Villaruel', 'Lim', '65.83', '78.85', '66.85', '18.75', '63.45', '43.49', 'BS ARCHITECTURE', 'COLLEGE OF ARCHITECTURE'),
(18, '68650', 'Bianca', 'Flores', 'Yu', '75.16', '76.83', '66.85', '51.68', '79.96', '63.1', 'AB POLITICAL SCIENCE', 'COLLEGE OF LIBERAL ARTS'),
(19, '12599', 'Benjie', 'Molina', 'Tan', '65.83', '68.5', '54.75', '76.79', '34.54', '53.29', 'BS HOSPITALITY MANAGEMENT', 'COLLEGE OF HOME ECONOMICS'),
(20, '74575', 'Bea', 'Dela Cruz', 'Ng', '66.95', '63.53', '54.75', '51.68', '84.63', '53.29', 'BS MATHEMATICS', 'COLLEGE OF SCIENCE AND MATHEMATICS'),
(21, '71990', 'Brixton', 'Salazar', 'Ong', '60.09', '41.05', '82.26', '66.81', '63.45', '43.49', 'BS COMMUNITY DEVELOPMENT', 'COLLEGE OF SOCIAL WORK & COMMUNITY DEVELOPMENT'),
(22, '57808', 'Belen', 'Pineda', 'Chua', '91.08', '94.11', '96.76', '59.25', '53.82', '87.72', 'BS NURSING', 'COLLEGE OF NURSING'),
(23, '38289', 'Bernadette', 'Enriquez', 'Reyes', '60.09', '74.8', '15.12', '66.81', '63.45', '33.69', 'BAELS', 'COLLEGE OF LIBERAL ARTS'),
(24, '26354', 'Bonifacio', 'Cruz', 'Rodriguez', '88.22', '88.66', '66.85', '76.79', '79.96', '91.68', 'BACHELOR OF SECONDARY EDUCATION', 'COLLEGE OF TEACHER EDUCATION'),
(25, '35058', 'Bong', 'Rodriguez', 'Espino', '61.37', '61.05', '42.05', '51.68', '70.61', '63.1', 'BS INFORMATION TECHNOLOGY', 'COLLEGE OF COMPUTING STUDIES'),
(26, '73137', 'Belinda', 'Villanueva', 'Cruz', '94.79', '92.71', '66.85', '93.41', '97.62', '87.72', 'BS ELECTRONICS AND COMMUNICATION ENGINEERING', 'COLLEGE OF ENGINEERING'),
(27, '79714', 'Benedicto', 'Estrella', 'Macapagal', '92.51', '92.71', '77.12', '85.06', '92.22', '83.75', 'BS SANITARY ENGINEERING', 'COLLEGE OF ENGINEERING'),
(28, '83339', 'Betty', 'De Guzman', 'Padilla', '79.72', '74.8', '77.12', '80.93', '44.18', '87.72', 'BS ENVIRONMENTAL ENGINEERING', 'COLLEGE OF ENGINEERING'),
(29, '89335', 'Baltazar', 'Alcantara', 'Uy', '88.22', '84.91', '94.82', '80.93', '75.28', '72.9', 'BS ACCOUNTANCY', 'COLLEGE OF LIBERAL ARTS'),
(30, '63033', 'Brando', 'Tungpalan', 'Lao', '88.7', '96.08', '61.11', '72.66', '63.45', '79.78', 'BS SANITARY ENGINEERING', 'COLLEGE OF ENGINEERING'),
(31, '16036', 'Beverly', 'Alonzo', 'Tan', '83.5', '83.47', '87.4', '89.19', '34.54', '72.9', 'BACHELOR OF SECONDARY EDUCATION', 'COLLEGE OF TEACHER EDUCATION'),
(32, '96369', 'Christopher', 'de la Rosa', 'Chan', '72.43', '61.05', '48.4', '85.06', '89.31', '53.29', 'BS NURSING', 'COLLEGE OF NURSING'),
(33, '92485', 'Catherine', 'Abad', 'Go', '72.43', '61.05', '66.85', '59.25', '92.22', '63.1', 'BS ARCHITECTURE', 'COLLEGE OF ARCHITECTURE'),
(34, '37044', 'Cristina', 'Luna', 'Villanueva', '62.48', '68.5', '35.7', '13.15', '92.22', '63.1', 'BS CRIMINOLOGY', 'COLLEGE OF CRIMINAL JUSTICE EDUCATION'),
(35, '73721', 'Cedric', 'Mendoza', 'Villar', '70.3', '76.83', '82.26', '13.15', '53.82', '79.78', 'BS BIOLOGY', 'COLLEGE OF SCIENCE AND MATHEMATICS'),
(36, '35667', 'Clarissa', 'Miranda', 'Tan', '87.64', '89.71', '77.12', '91.97', '53.82', '72.9', 'BACHELOR IN ELEMENTARY EDUCATION', 'COLLEGE OF TEACHER EDUCATION'),
(37, '40984', 'Carlo', 'Zamora', 'Solis', '65.83', '58.56', '82.26', '85.06', '34.54', '26.06', 'AB POLITICAL SCIENCE', 'COLLEGE OF LIBERAL ARTS'),
(38, '42273', 'Cecilia', 'Gonzales', 'Caballero', '70.3', '70.75', '54.75', '80.93', '53.82', '53.29', 'BS ACCOUNTANCY', 'COLLEGE OF LIBERAL ARTS'),
(39, '52096', 'Cesar', 'Garcia', 'De Guzman', '92.03', '94.81', '90.94', '80.93', '79.96', '63.1', 'BS CIVIL ENGINEERING', 'COLLEGE OF ENGINEERING'),
(40, '42092', 'Criselda', 'Villena', 'Agustin', '80.63', '70.75', '77.12', '80.93', '70.61', '87.72', 'BS ECONOMICS', 'COLLEGE OF LIBERAL ARTS'),
(41, '95506', 'Celine', 'Oliva', 'Pascual', '96.35', '89.71', '92.88', '96.28', '94.54', '98.34', 'BACHELOR OF SECONDARY EDUCATION', 'COLLEGE OF TEACHER EDUCATION'),
(42, '57585', 'Claire', 'Sta. Ana', 'Mendoza', '69.19', '66.01', '25.06', '66.81', '92.22', '72.9', 'BS COMPUTER SCIENCE', 'COLLEGE OF COMPUTING STUDIES'),
(43, '86701', 'Conrado', 'Aquino', 'Lucero', '87.64', '83.47', '94.82', '94.84', '24.91', '79.78', 'BS INFORMATION TECHNOLOGY', 'COLLEGE OF COMPUTING STUDIES'),
(44, '65644', 'Cenon', 'Bacani', 'Matias', '65.83', '78.85', '66.85', '18.75', '63.45', '43.49', 'BACHELOR OF PHYSICAL EDUCATION', 'COLLEGE OF SPORTS SCIENCE AND PHYSICAL EDUCATION'),
(45, '24048', 'Celestina', 'Tumulak', 'Velasco', '75.16', '76.83', '66.85', '51.68', '79.96', '63.1', 'BS PSYCHOLOGY', 'COLLEGE OF LIBERAL ARTS'),
(46, '45595', 'Charlie', 'Reyes', 'Bautista', '65.83', '68.5', '54.75', '76.79', '34.54', '53.29', 'BAELS', 'COLLEGE OF LIBERAL ARTS'),
(47, '70685', 'Daphne', 'Santiago', 'Ocampo', '69.19', '66.01', '25.06', '66.81', '92.22', '72.9', 'BS MECHANICAL ENGINEERING', 'COLLEGE OF ENGINEERING'),
(48, '98896', 'David', 'Evangelista', 'Bonifacio', '87.64', '83.47', '94.82', '94.84', '24.91', '79.78', 'AB HISTORY', 'COLLEGE OF LIBERAL ARTS'),
(49, '14391', 'Dario', 'Sison', 'Guevarra', '65.83', '78.85', '66.85', '18.75', '63.45', '43.49', 'BS SOCIAL WORK', 'COLLEGE OF SOCIAL WORK & COMMUNITY DEVELOPMENT'),
(50, '26893', 'Diane', 'Cadiz', 'Galang', '75.16', '76.83', '66.85', '51.68', '79.96', '63.1', 'BS ELECTRICAL ENGINEERING', 'COLLEGE OF ENGINEERING'),
(51, '54297', 'Danilo', 'Guinto', 'Quizon', '65.83', '68.5', '54.75', '76.79', '34.54', '53.29', 'BATSILER NG SINING SA FILIPINO', 'COLLEGE OF LIBERAL ARTS'),
(52, '94072', 'Dolores', 'Lobo', 'Concepcion', '66.95', '63.53', '54.75', '51.68', '84.63', '53.29', 'BS COMMUNITY DEVELOPMENT', 'COLLEGE OF SOCIAL WORK & COMMUNITY DEVELOPMENT'),
(53, '49694', 'Dindo', 'Lucero', 'Francisco', '60.09', '41.05', '82.26', '66.81', '63.45', '43.49', 'AB JOURNALISM', 'COLLEGE OF LIBERAL ARTS'),
(54, '49409', 'Divina', 'Domingo', 'Sy', '91.08', '94.11', '96.76', '59.25', '53.82', '87.72', 'BS NUTRITION AND DIETETICS', 'COLLEGE OF HOME ECONOMICS'),
(55, '19825', 'Donato', 'Tumulak', 'Dizon', '60.09', '74.8', '15.12', '66.81', '63.45', '33.69', 'BACHELOR OF SPECIAL NEEDS EDUCATION', 'COLLEGE OF TEACHER EDUCATION'),
(56, '71810', 'Dennis', 'Guzman', 'Santos', '88.22', '88.66', '66.85', '76.79', '79.96', '91.68', 'BS INDUSTRIAL ENGINEERING', 'COLLEGE OF ENGINEERING'),
(57, '19750', 'Domingo', 'Cruzado', 'Villanueva', '61.37', '61.05', '42.05', '51.68', '70.61', '63.1', 'AB BROADCASTING', 'COLLEGE OF LIBERAL ARTS'),
(58, '45638', 'Dolly', 'Pineda', 'Navarro', '94.79', '92.71', '66.85', '93.41', '97.62', '87.72', 'BS HOSPITALITY MANAGEMENT', 'COLLEGE OF HOME ECONOMICS'),
(59, '56328', 'Dominador', 'Natividad', 'Reyes', '92.51', '92.71', '77.12', '85.06', '92.22', '83.75', 'BS HOME ECONOMICS', 'COLLEGE OF HOME ECONOMICS'),
(60, '54218', 'Daisy', 'Penaflor', 'Dela Cruz', '79.72', '74.8', '77.12', '80.93', '44.18', '87.72', 'BS SANITARY ENGINEERING', 'COLLEGE OF ENGINEERING'),
(61, '89615', 'Dina', 'Vargas', 'Sarmiento', '88.22', '84.91', '94.82', '80.93', '75.28', '72.9', 'BS CHEMISTRY', 'COLLEGE OF SCIENCE AND MATHEMATICS'),
(62, '71809', 'Eddison', 'Navarro', 'Abad', '88.7', '96.08', '61.11', '72.66', '63.45', '79.78', 'BS COMPUTER ENGINEERING', 'COLLEGE OF ENGINEERING'),
(63, '65261', 'Emma', 'De Leon', 'Fernandez', '83.5', '83.47', '87.4', '89.19', '34.54', '72.9', 'COLLEGE OF AGRICULTURE', 'COLLEGE OF AGRICULTURE'),
(64, '70136', 'Edgar', 'Atienza', 'Gamboa', '61.37', '61.05', '42.05', '51.68', '70.61', '63.1', 'BS MATHEMATICS', 'COLLEGE OF SCIENCE AND MATHEMATICS'),
(65, '69355', 'Elvira', 'Ang', 'Aguilar', '94.79', '92.71', '66.85', '93.41', '97.62', '87.72', 'BS ENVIRONMENTAL ENGINEERING', 'COLLEGE OF ENGINEERING'),
(66, '15209', 'Eduardo', 'Dalisay', 'Basco', '92.51', '92.71', '77.12', '85.06', '92.22', '83.75', 'BS ELECTRONICS AND COMMUNICATION ENGINEERING', 'COLLEGE OF ENGINEERING'),
(67, '84583', 'Evelyn', 'Quimbo', 'Cagampang', '79.72', '74.8', '77.12', '80.93', '44.18', '87.72', 'BS STATISTICS', 'COLLEGE OF SCIENCE AND MATHEMATICS'),
(68, '46797', 'Ester', 'Hernandez', 'Cervantes', '88.22', '84.91', '94.82', '80.93', '75.28', '72.9', 'BS AGRICULTURE', 'COLLEGE OF AGRICULTURE'),
(69, '89733', 'Edwin', 'Sy', 'De Leon', '88.7', '96.08', '61.11', '72.66', '63.45', '79.78', 'BS AGRICULTURAL AND BIOSYSTEMS ENGINEERING', 'COLLEGE OF ENGINEERING'),
(70, '79566', 'Eloisa', 'Singson', 'Ebora', '83.5', '83.47', '87.4', '89.19', '34.54', '72.9', 'BS ISLAMIC STUDIES', 'COLLEGE OF ASIAN & ISLAMIC STUDIES'),
(71, '19909', 'Estrella', 'Bonifacio', 'Feliciano', '72.43', '61.05', '48.4', '85.06', '89.31', '53.29', 'BACHELOR OF CULTURE AND ARTS EDUCATION', 'COLLEGE OF TEACHER EDUCATION');

-- --------------------------------------------------------

--
-- Table structure for table `student_details`
--

CREATE TABLE `student_details` (
  `student_id` int(11) NOT NULL,
  `height` varchar(255) NOT NULL,
  `weight` varchar(255) NOT NULL,
  `bmi` varchar(255) NOT NULL,
  `types` varchar(255) NOT NULL,
  `track` varchar(255) NOT NULL,
  `school` varchar(255) NOT NULL,
  `gpa` varchar(255) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `date_registered` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_details`
--

INSERT INTO `student_details` (`student_id`, `height`, `weight`, `bmi`, `types`, `track`, `school`, `gpa`, `user_id`, `date_registered`) VALUES
(1, '26', '90', '0.13', 'ESFP-A', 'SPORTS', 'Enim dolore sed sint', '53', 1, '2023-04-02 00:23:54'),
(2, '4', '59', '3.69', 'ENTJ-T', 'ICT', 'Ipsam id aut deseru', '57', 9, '2023-04-03 09:22:00'),
(3, '1.67', '55', '19.72', 'INTP-A', 'ICT', 'Laborum Quia Nam vo', '34', 12, '2023-04-03 11:20:43'),
(4, '57', '8', '0', 'INTP-T', 'SPORTS', 'Irure cumque volupta', '74', 13, '2023-05-09 10:58:48'),
(5, '1.61', '45', '17.36', 'ENFP-T', 'ICT', 'WMSU', '70', 16, '2023-04-04 14:08:12'),
(6, '156', '45', '0', 'INTP-T', 'HUMSS', 'Sti', '89', 17, '2023-05-23 09:57:49');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `middle_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) NOT NULL,
  `sex` varchar(255) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(255) NOT NULL,
  `detail_no` tinyint(1) NOT NULL,
  `predict_no` tinyint(1) NOT NULL,
  `user_type` smallint(6) NOT NULL,
  `date_created` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `first_name`, `middle_name`, `last_name`, `sex`, `email`, `password`, `detail_no`, `predict_no`, `user_type`, `date_created`) VALUES
(1, 'Lysandra', 'Fallon Berger', 'Lowery', 'Female', 'mexurela@mailinator.com', 'sha256$06UW37Nf9zrGFkb3$1ead7505434818ae35c74480e4e9398a56fc6ac7b88e90aa6492bb6b32b114bb', 0, 0, 1, '2023-04-02 00:08:53'),
(2, 'Regan', 'Alvin Blackwell', 'Walters', 'Female', 'tywo@mailinator.com', 'sha256$VRoTgoIdHwdI7LBv$0edeea1d1be0cadbbeca4c585868cc3764417ab85cc6970ccd57fb16cbaedc87', 0, 0, 1, '2023-04-02 00:29:26'),
(3, 'Yeo', 'Herrod Nash', 'Chen', 'Male', 'byqidyxela@mailinator.com', 'sha256$IUHnhElpSBlAvk1j$6895ff703f01829353a62fd35422ef9a4d6067b92ad8bb83d9d425189c32ea41', 0, 0, 1, '2023-04-02 00:30:15'),
(4, 'Courtney', 'Salvador Phillips', 'Logan', 'Female', 'lenu@mailinator.com', 'sha256$5DN9pLVeRKjqFE3J$2dda976917bb0206dd91794497330efc13f49ba111d0244d9ce7952ef698179a', 0, 0, 1, '2023-04-02 00:49:03'),
(5, 'Nichole', 'Lunea Peck', 'Dejesus', 'Male', 'nucogujaf@mailinator.com', 'sha256$tg9eRQb8YyXBAYP5$d4f3b0a7fb1dc11e95b56be3bd3729e6dc0c2cd309ad4c686ba9106629458ef4', 0, 0, 1, '2023-04-02 00:49:34'),
(6, 'Luke', 'Kimberley Phillips', 'Gay', 'Male', 'xodusyle@mailinator.com', 'sha256$mv9FR9227YLxk5SE$d1b5fc3fc27917d5bf5d8350f4a22be933ccdf7740772b49a95b2d135632015a', 0, 0, 1, '2023-04-02 00:53:44'),
(9, 'Hiroko', 'Mollie Snow', 'Howe', 'Female', 'sukici@mailinator.com', 'sha256$BAPxJsupwO3rGY5b$36694b324007d45c9a0aadd2b4d474061524862fd6cd4118fa40a70b9ccb7761', 0, 0, 1, '2023-04-02 01:09:01'),
(10, 'Jessa ', 'Manico', 'Francisco', 'Female', 'admin@email.com', 'sha256$OeuNYDzQPSPatijD$19136f968332e6ccec5930405c37e025746aff9507cd019d7c3cc4cbc1687ed1', 0, 0, 0, '2023-04-03 09:07:11'),
(11, 'Kelly', 'Chantale Buckner', 'Long', 'Female', 'ryniz@mailinator.com', 'sha256$iyQETUVYC8DqMlEv$36c56dde6d35063d828a7748ee6e49d0ad640e2ab5251a354d2e0098a7083ea9', 0, 0, 0, '2023-04-03 11:02:57'),
(12, 'Carolyn', 'Caleb Murray', 'Guzman', 'Male', 'lyku@mailinator.com', 'sha256$WnfioU8XhVepl13U$354a459ae0bbfa8655841f27f481b2722f608e00752499d627cc2c3e5074e2fa', 0, 0, 1, '2023-04-03 11:12:59'),
(13, 'Jessa ', 'Manico', 'Francisco', 'Female', 'lc201700492@wmsu.edu.ph', 'sha256$q1isGhaCS6I6lAk1$5d020a698bfc45c982fe4e7387f1570f2bdb4106cc7556f6172eb7adddbfb7de', 0, 0, 1, '2023-04-03 21:30:05'),
(15, 'Jessa ', 'Manico', 'Francisco', 'Female', 'jessafrancisco@email.com', 'sha256$e7t1wwrK8VWvJw6V$47b4c4eeb4c2875d975ebffc6a41156700684bbb478abf3e9cbd210458c32ba9', 0, 0, 1, '2023-04-04 14:04:35'),
(16, 'Arden', 'Clarke Spears', 'Stevenson', 'Male', 'tymi@mailinator.com', 'sha256$vi1wyj7IvOhOQNFJ$d66b40340d840c71de31f2cb09204d6c20cf6b5a6d6770672b7acad8bd94802f', 0, 0, 1, '2023-04-04 14:06:03'),
(17, 'Erica', 'Sungkip', 'Ignacio', 'Female', 'gt201900458@wmsu.edu.ph', 'sha256$PMyaPWUecwqb566B$4244bac11fe891471a7944706e6036c9bf57f6df40375ac19dfd0375b78d9b14', 0, 0, 1, '2023-05-23 09:56:44');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `description`
--
ALTER TABLE `description`
  ADD PRIMARY KEY (`des_id`),
  ADD UNIQUE KEY `course` (`course`);

--
-- Indexes for table `prediction_result`
--
ALTER TABLE `prediction_result`
  ADD PRIMARY KEY (`result_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `studentcsv`
--
ALTER TABLE `studentcsv`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `student_details`
--
ALTER TABLE `student_details`
  ADD PRIMARY KEY (`student_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `description`
--
ALTER TABLE `description`
  MODIFY `des_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=111;

--
-- AUTO_INCREMENT for table `prediction_result`
--
ALTER TABLE `prediction_result`
  MODIFY `result_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `studentcsv`
--
ALTER TABLE `studentcsv`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=72;

--
-- AUTO_INCREMENT for table `student_details`
--
ALTER TABLE `student_details`
  MODIFY `student_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `prediction_result`
--
ALTER TABLE `prediction_result`
  ADD CONSTRAINT `prediction_result_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `student_details`
--
ALTER TABLE `student_details`
  ADD CONSTRAINT `student_details_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
