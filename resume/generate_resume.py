from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import os

pdf_path = r"c:\Users\Brosis\Desktop\anjana-portfolio\resume\Anjana_Suresh_Resume.pdf"
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    rightMargin=36,
    leftMargin=36,
    topMargin=36,
    bottomMargin=36
)

styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=22,
    leading=26,
    textColor=colors.HexColor('#0f172a'),
    alignment=1
)

sub_style = ParagraphStyle(
    'SubTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=14,
    textColor=colors.HexColor('#6b21a8'),
    alignment=1
)

contact_style = ParagraphStyle(
    'Contact',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9,
    leading=13,
    textColor=colors.HexColor('#334155'),
    alignment=1
)

heading_style = ParagraphStyle(
    'SectionHeading',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10.5,
    leading=14,
    textColor=colors.HexColor('#0f172a'),
    spaceBefore=7,
    spaceAfter=3
)

body_style = ParagraphStyle(
    'Body',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.8,
    leading=12.2,
    textColor=colors.HexColor('#1e293b')
)

bold_body = ParagraphStyle(
    'BoldBody',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=8.8,
    leading=12.2,
    textColor=colors.HexColor('#0f172a')
)

bullet_style = ParagraphStyle(
    'Bullet',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=11.6,
    textColor=colors.HexColor('#334155'),
    leftIndent=12,
    firstLineIndent=-8
)

story = []

# Header
story.append(Paragraph("Anjana Suresh", title_style))
story.append(Spacer(1, 2))
story.append(Paragraph("Aspiring MCA Student | Software Developer", sub_style))
story.append(Spacer(1, 3))
story.append(Paragraph("Pathanamthitta, India &nbsp;|&nbsp; anjanasuresh3535@gmail.com<br/>linkedin.com/in/anjanasuresh7404 &nbsp;|&nbsp; github.com/anjanasuresh3535", contact_style))
story.append(Spacer(1, 4))
story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#0f172a'), spaceBefore=2, spaceAfter=6))

# Professional Summary
story.append(Paragraph("PROFESSIONAL SUMMARY", heading_style))
story.append(Paragraph("MCA student with a B.Sc. in Mathematics and a strong interest in software development. Hands-on with <b>Python, Java, SQL, Django REST Framework, Node.js, and MongoDB</b>, with experience building REST APIs and database-driven web applications. Eager to learn new technologies and contribute to real-world software projects.", body_style))
story.append(Spacer(1, 4))

# Technical Skills
story.append(Paragraph("TECHNICAL SKILLS", heading_style))
skills_data = [
    [Paragraph("<b>Backend and APIs:</b>", bold_body), Paragraph("Python, Django, Django REST Framework, Node.js, Express.js, REST APIs, Postman", body_style)],
    [Paragraph("<b>Frameworks &amp; Libraries:</b>", bold_body), Paragraph("Django, Node.js, Express.js", body_style)],
    [Paragraph("<b>Databases:</b>", bold_body), Paragraph("MongoDB, Mongoose, MySQL", body_style)],
    [Paragraph("<b>Web &amp; Frontend:</b>", bold_body), Paragraph("JavaScript, EJS, HTML5, CSS3", body_style)],
    [Paragraph("<b>Tools &amp; Platforms:</b>", bold_body), Paragraph("Git, GitHub, Visual Studio Code, Postman", body_style)],
    [Paragraph("<b>Core CS Foundations:</b>", bold_body), Paragraph("Java, SQL, Object-Oriented Programming (OOP), DBMS, Data Structures", body_style)]
]
t_skills = Table(skills_data, colWidths=[1.8*inch, 5.4*inch])
t_skills.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ('TOPPADDING', (0,0), (-1,-1), 1),
    ('LEFTPADDING', (0,0), (-1,-1), 0),
    ('RIGHTPADDING', (0,0), (-1,-1), 0),
]))
story.append(t_skills)
story.append(Spacer(1, 4))

# Projects
story.append(Paragraph("PROJECTS", heading_style))
p1_head = [
    [Paragraph("<b>AptitudePro — Online Aptitude Learning &amp; Performance Analysis System</b>", bold_body), Paragraph("<para align='right'><font color='#6b21a8'>github.com/anjanasuresh3535</font></para>", body_style)]
]
t_p1 = Table(p1_head, colWidths=[5.2*inch, 2.0*inch])
t_p1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('TOPPADDING', (0,0), (-1,-1), 0), ('LEFTPADDING', (0,0), (-1,-1), 0)]))
story.append(t_p1)
story.append(Paragraph("<i>Technologies: Node.js, Express.js, MongoDB, Mongoose, EJS, JavaScript, HTML5, CSS3, sql.js</i>", body_style))
story.append(Paragraph("&bull; Built a full-stack aptitude practice platform for placement preparation with <b>195 levels across 9 tiers</b>, timed quizzes in 5 sections (Maths, Logical, English, Programming, Mixed) and company-specific tracks such as <b>TCS, Infosys, and Wipro</b>.", bullet_style))
story.append(Paragraph("&bull; Designed a MongoDB schema with Mongoose for users, questions, results, section progress, user stats and XP history; stored answer snapshots so past attempts keep their solutions and formulas even if questions change.", bullet_style))
story.append(Paragraph("&bull; Implemented session-based authentication with bcryptjs password hashing, express-validator input checks, role-based route protection (user/admin) and Helmet security headers.", bullet_style))
story.append(Paragraph("&bull; Developed quiz evaluation, XP and level services, and section progress tracking, with score, accuracy, time taken and question-by-question review with step-by-step solutions.", bullet_style))
story.append(Paragraph("&bull; Added an in-browser SQL practice console using <b>sql.js</b>.", bullet_style))
story.append(Spacer(1, 4))

# Internship Experience
story.append(Paragraph("INTERNSHIP EXPERIENCE", heading_style))
intern_head = [
    [Paragraph("<b>Full Stack Development Intern</b> — <i>Faith Infotech, Kerala</i>", bold_body), Paragraph("<para align='right'><b>(One-week internship)</b></para>", body_style)]
]
t_intern = Table(intern_head, colWidths=[5.2*inch, 2.0*inch])
t_intern.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('TOPPADDING', (0,0), (-1,-1), 0), ('LEFTPADDING', (0,0), (-1,-1), 0)]))
story.append(t_intern)
story.append(Paragraph("<i>Technology/Tools used: Python, Django REST Framework, REST APIs, MySQL, Postman</i>", body_style))
story.append(Paragraph("&bull; Implemented Python-based backend and REST API workflows using Django REST Framework, covering request handling and integration between application components.", bullet_style))
story.append(Paragraph("&bull; Tested API endpoints with Postman to verify request and response behavior.", bullet_style))
story.append(Spacer(1, 4))

# Certifications / Courses
story.append(Paragraph("CERTIFICATIONS / COURSES", heading_style))
story.append(Paragraph("&bull; <b>Data Analytics with Python</b> — NPTEL SWAYAM", bullet_style))
story.append(Spacer(1, 4))

# Education
story.append(Paragraph("EDUCATION", heading_style))

edu_data1 = [
    [
        Paragraph("<b>Master of Computer Applications (MCA)</b><br/>MACFAST, Thiruvalla, Kerala", bold_body),
        Paragraph("<para align='right'><b>2025 – 2027</b><br/>First Sem CGPA: <b>8.72/10</b> | Second Sem CGPA: <b>8.39/10</b></para>", body_style)
    ]
]
t_edu1 = Table(edu_data1, colWidths=[4.8*inch, 2.4*inch])
t_edu1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 2), ('TOPPADDING', (0,0), (-1,-1), 0), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
story.append(t_edu1)
story.append(Spacer(1, 3))

edu_data2 = [
    [
        Paragraph("<b>B.Sc. in Mathematics</b><br/>Catholicate College, Pathanamthitta, Kerala", bold_body),
        Paragraph("<para align='right'><b>2022 – 2025</b></para>", body_style)
    ]
]
t_edu2 = Table(edu_data2, colWidths=[4.8*inch, 2.4*inch])
t_edu2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 2), ('TOPPADDING', (0,0), (-1,-1), 0), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
story.append(t_edu2)
story.append(Spacer(1, 4))

# Languages
story.append(Paragraph("LANGUAGES", heading_style))
story.append(Paragraph("Malayalam, English", body_style))

doc.build(story)
print(f"Generated verified PDF resume at: {pdf_path}")
