import random
from faker import Faker
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.consultant import Consultant, ConsultantRole
from models.post import Post
from models.project import Project
from models.client import Client, ClientRole
# from models.service import Service
import re
from app import app
from models import db
import json


fake = Faker()

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

def seed_clients():
    with app.app_context():
        clients_data = [
            {
                'username': 'client1',
                'email': 'client1@example.com',
                'password': 'Client1@password',
                'role': ClientRole.CLIENT
            },
            {
                'username': 'client2',
                'email': 'client2@example.com',
                'password': 'Client2@password',
                'role': ClientRole.CLIENT
            },
            {
                'username': 'client3',
                'email': 'client3@example.com',
                'password': 'Client3@password',
                'role': ClientRole.CLIENT
            },
            {
                'username': 'client4',
                'email': 'client4@example.com',
                'password': 'Client4@password',
                'role': ClientRole.CLIENT
            },
            {
                'username': 'client5',
                'email': 'client5@example.com',
                'password': 'Client5@password',
                'role': ClientRole.CLIENT
            }
        ]

        for client_data in clients_data:
            if validate_password(client_data['password']):
                client = Client(**client_data)
                client.set_password(client_data['password'])
                db.session.add(client)
            else:
                print(f"Invalid password for {client_data['username']}")

        db.session.commit()

def seed_consultants():
    with app.app_context():
        consultants_data = [
            {
                'username': 'consultant1',
                'email': 'consultant1@example.com',
                'password': 'Consultant1@password',
                'qualification': 'PhD in Psychology',
                'location': 'New York, USA',
                'services': json.dumps(['Cognitive Behavioral Therapy', 'Family Counseling']),
                'linkedin': 'https://www.linkedin.com/consultant1',
                'twitter': 'https://twitter.com/consultant1',
                'about': 'Experienced psychologist with a focus on cognitive behavioral therapy.',
                'projects': json.dumps(['Study on Anxiety Disorders', 'Family Counseling Program']),
                'testimonials': json.dumps(['Great experience working with consultant1.', 'Highly recommend.'])
            },
            {
                'username': 'consultant2',
                'email': 'consultant2@example.com',
                'password': 'Consultant2@password',
                'qualification': 'MSc in Finance',
                'location': 'London, UK',
                'services': json.dumps(['Financial Analysis', 'Investment Planning']),
                'linkedin': 'https://www.linkedin.com/consultant2',
                'twitter': 'https://twitter.com/consultant2',
                'about': 'Financial consultant specializing in investment planning and financial analysis.',
                'projects': json.dumps(['Market Analysis Report', 'Investment Portfolio Management']),
                'testimonials':json.dumps(['Very knowledgeable and helpful.', 'Made a significant impact on our financial strategy.'])
            },
            {
                'username': 'consultant3',
                'email': 'consultant3@example.com',
                'password': 'Consultant3@password',
                'qualification': 'MD in Medicine',
                'location': 'Los Angeles, USA',
                'services': json.dumps(['Cardiology', 'Pediatrics']),
                'linkedin': 'https://www.linkedin.com/consultant3',
                'twitter': 'https://twitter.com/consultant3',
                'about': 'Specializing in cardiology with extensive experience in pediatric care.',
                'projects': json.dumps(['Research on Heart Disease Prevention', 'Pediatric Health Initiative']),
                'testimonials': json.dumps(['Dr. Consultant3 saved my child\'s life!', 'Highly skilled and compassionate physician.'])
            },
            {
                'username': 'consultant5',
                'email': 'consultant5@example.com',
                'password': 'Consultant5@password',
                'qualification': 'MA in Literature',
                'location': 'London, UK',
                'services': json.dumps(['Literary Criticism', 'Creative Writing Workshops']),
                'linkedin': 'https://www.linkedin.com/consultant5',
                'twitter': 'https://twitter.com/consultant5',
                'about': 'Passionate about literature and promoting creative writing skills.',
                'projects': json.dumps(['Literary Analysis of Classic Novels', 'Creative Writing Program for Schools']),
                'testimonials': json.dumps(['An inspiring teacher and mentor.', 'Transformed my approach to literature.'])
            },
            {
                'username': 'consultant7',
                'email': 'consultant7@example.com',
                'password': 'Consultant7@password',
                'qualification': 'PhD in Computer Science',
                'location': 'San Francisco, USA',
                'services': json.dumps(['Machine Learning', 'Software Architecture']),
                'linkedin': 'https://www.linkedin.com/consultant7',
                'twitter': 'https://twitter.com/consultant7',
                'about': 'Expertise in machine learning algorithms and scalable software design.',
                'projects': json.dumps(['Development of AI-driven Applications', 'Optimization of Cloud-based Systems']),
                'testimonials': json.dumps(['Outstanding technical knowledge and problem-solving skills.', 'Delivered exceptional results on our AI project.'])
            }
        ]
        for consultant_data in consultants_data:
            if validate_password(consultant_data['password']):
                consultant = Consultant(**consultant_data)
                consultant.set_password(consultant_data['password'])
                db.session.add(consultant)
            else:
                print(f"Invalid password for {consultant_data['username']}")

        db.session.commit()

def seed_posts():
    with app.app_context():
        consultants = Consultant.query.all()

        if not consultants:
            print("No consultants found. Seed consultants first.")
            return

        for _ in range(20):
            random_consultant = random.choice(consultants)
  
            title = fake.sentence()
            content = fake.paragraph()

            new_post = Post(title=title, content=content, user_id=random_consultant.id)

            db.session.add(new_post)
        db.session.commit()

def seed_projects():
    with app.app_context():
        clients = Client.query.all()
        consultants = Consultant.query.all()

        for _ in range(10):
            random_client = random.choice(clients)
            random_consultant = random.choice(consultants)
            name = fake.company()
            description = fake.catch_phrase()
            client_request = fake.text()

            new_project = Project(
                name=name,
                description=description,
                client_id=random_client.id,
                consultant_id=random_consultant.id,
                client_request=client_request
            )
            db.session.add(new_project)

        db.session.commit()

# def seed_services():
#     with app.app_context():
#         services = [
#             {
#                 'name': 'Web Development',
#                 'description': 'Expert web development services, including custom websites, e-commerce platforms, and mobile-responsive designs.',
#                 'consultant_id': 1  
#             },
#             {
#                 'name': 'Data Analysis',
#                 'description': 'Data-driven insights and solutions using advanced analytics techniques. We help you understand your data and make informed decisions.',
#                 'consultant_id': 2 
#             },
#             {
#                 'name': 'Marketing Strategy',
#                 'description': 'Develop and implement effective marketing strategies to reach your target audience and achieve your business goals.',
#                 'consultant_id': 1  
#             },
#             {
#                 'name': 'Project Management',
#                 'description': 'Experienced project managers to guide your projects from initiation to completion, ensuring on-time and on-budget delivery.',
#                 'consultant_id': 3 
#             }
#         ]


#         for service_data in services:
#             new_service = Service(
#                 name=service_data['name'],
#                 description=service_data['description'],
#                 consultant_id=service_data['consultant_id']
#             )
#             db.session.add(new_service)

#         db.session.commit()

if __name__ == '__main__':
    seed_consultants()
    seed_clients()
    seed_posts()
    seed_projects()
    
   

