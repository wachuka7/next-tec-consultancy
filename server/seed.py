from models.user import User, Role
from models.project import Project
from models import db
from app import app

with app.app_context():
    users = [
        User(username='john.doe', email='john.doe@example.com', password='password123', role=Role.CLIENT),
        User(username='jane.doe', email='jane.doe@example.com', password='password456', role=Role.CLIENT),
        User(username='consultant1', email='consultant1@example.com', password='consultant1', role=Role.CONSULTANT, qualification='Expert in Python and Data Science'),
        User(username='consultant2', email='consultant2@example.com', password='consultant2', role=Role.CONSULTANT, qualification='Experienced Web Developer with React and Node.js'),
        User(username='consultant3', email='consultant3@example.com', password='consultant3', role=Role.CONSULTANT, qualification='Financial Analyst with strong Excel and SQL skills'),
    ]
    for user in users:
        db.session.add(user)
    db.session.commit()

    projects = [
        Project(name='Website Development', description='Build a new website for my business', client_request='Need a modern and responsive website with e-commerce functionality', client_id=users[0].id, user_id=users[2].id),
        Project(name='Data Analysis', description='Analyze sales data to identify trends', client_request='Need help understanding sales patterns and predicting future trends', client_id=users[1].id, user_id=users[3].id),
        Project(name='Financial Modeling', description='Create a financial model for a new project', client_request='Need a detailed financial model to assess the viability of a new investment', client_id=users[0].id, user_id=users[4].id),
    ]
    for project in projects:
        db.session.add(project)
    db.session.commit()
