import random
from faker import Faker
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.consultant import Consultant, ConsultantRole
from models.post import Post
from models.project import Project
from models.client import Client, ClientRole
import re
from app import app
from models import db

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
                'role': ConsultantRole.CONSULTANT
            },
            {
                'username': 'consultant2',
                'email': 'consultant2@example.com',
                'password': 'Consultant2@password',
                'qualification': 'MSc in Finance',
                'role': ConsultantRole.CONSULTANT
            },
            {
                'username': 'consultant3',
                'email': 'consultant3@example.com',
                'password': 'Consultant3@password',
                'qualification': 'MD in Medicine',
                'role': ConsultantRole.CONSULTANT
            },
            {
                'username': 'consultant4',
                'email': 'consultant4@example.com',
                'password': 'Consultant4@password',
                'qualification': 'PhD in Physics',
                'role': ConsultantRole.CONSULTANT
            },
            {
                'username': 'consultant5',
                'email': 'consultant5@example.com',
                'password': 'Consultant5@password',
                'qualification': 'MA in Literature',
                'role': ConsultantRole.CONSULTANT
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

if __name__ == '__main__':
    seed_consultants()
    seed_clients()
    seed_posts()
    seed_projects()
    
   

