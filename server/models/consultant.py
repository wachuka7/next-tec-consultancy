from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from models import db


class ConsultantRole:
    CONSULTANT = 'consultant'

class Consultant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    qualification = db.Column(db.String(200))
    photo = db.Column(db.String(200))
    bio = db.Column(db.Text)
    location = db.Column(db.String(100))  # New field: Location
    services = db.Column(db.Text)  # New field: Services (array of strings)
    linkedin = db.Column(db.String(200))  # New field: LinkedIn URL
    twitter = db.Column(db.String(200))  # New field: Twitter URL
    about = db.Column(db.Text)  # New field: About Me
    testimonials = db.Column(db.Text)

    role = db.Column(db.String(20), default=ConsultantRole.CONSULTANT)
    projects = db.relationship('Project', backref='consultant', lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'qualification': self.qualification,
            'photo': self.photo,
            'bio': self.bio,
            'location': self.location,
            'services': self.services.split(',') if self.services else [],
            'linkedin': self.linkedin,
            'twitter': self.twitter,
            'about': self.about,
            'testimonials': self.testimonials.split(',') if self.testimonials else [],
            'role': self.role
        }
