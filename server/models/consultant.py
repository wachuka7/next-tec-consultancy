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
    role = db.Column(db.String(20), default=ConsultantRole.CONSULTANT)

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
            'role': self.role
        }
