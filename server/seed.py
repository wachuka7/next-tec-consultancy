from models.user import User, Role
from models.project import Project
from models.post import Post
from models import db
from app import app
import re



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


with app.app_context():
    users = [
        User(username='john.doe', email='john.doe@example.com', password='Password@123', role=Role.CLIENT),
        User(username='jane.doe', email='jane.doe@example.com', password='Password@456', role=Role.CLIENT),
        User(username='consultant1', email='consultant1@example.com', password='Consultant@1', role=Role.CONSULTANT, qualification='Expert in Python and Data Science'),
        User(username='consultant2', email='consultant2@example.com', password='Consultant@2', role=Role.CONSULTANT, qualification='Experienced Web Developer with React and Node.js'),
        User(username='consultant3', email='consultant3@example.com', password='Consultant@3', role=Role.CONSULTANT, qualification='Financial Analyst with strong Excel and SQL skills'),
    ]
    for user in users:
        if validate_password(user.password):
            user.set_password(user.password)
            db.session.add(user)
        else:
            print(f"Invalid password for user: {user.username}")
    db.session.commit()

    projects = [
        Project(name='Website Development', description='Build a new website for my business', client_request='Need a modern and responsive website with e-commerce functionality', client_id=users[0].id, user_id=users[2].id),
        Project(name='Data Analysis', description='Analyze sales data to identify trends', client_request='Need help understanding sales patterns and predicting future trends', client_id=users[1].id, user_id=users[3].id),
        Project(name='Financial Modeling', description='Create a financial model for a new project', client_request='Need a detailed financial model to assess the viability of a new investment', client_id=users[0].id, user_id=users[4].id),
    ]
    for project in projects:
        db.session.add(project)
    db.session.commit()

    # Seed some posts for the consultants
    posts = [
        {
            'title': 'Introduction to Python for Beginners',
            'content': 'This post will guide you through the basics of Python programming, covering data types, variables, and control flow.',
            'user_id': users[2].username
        },
        {
            'title': 'Building a React App with a Node.js Backend',
            'content': 'Learn how to create a full-stack web application using React for the frontend and Node.js for the backend.',
            'user_id': users[3].username
        },
        {
            'title': 'Financial Modeling with Excel and SQL',
            'content': 'This post explores how to use Excel and SQL to create powerful financial models for business analysis.',
            'user_id': users[4].username
        },
        {
            'title': 'Advanced Python Data Structures',
            'content': 'Dive deeper into advanced Python data structures like dictionaries, sets, and tuples.',
            'user_id': users[2].username 
        },
        {
            'title': 'Best Practices for React Development',
            'content': 'Learn about best practices for building maintainable and scalable React applications.',
            'user_id': users[3].username
        }
    ]

    for post_data in posts:
        post = Post(**post_data)
        db.session.add(post)
    db.session.commit()
