from enum import Enum
from models import db

class Role(Enum):
    CLIENT = "client"
    CONSULTANT = "consultant"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  # Store hashed passwords
    role = db.Column(db.Enum(Role), default=Role.CLIENT)  # Use Enum for role
    qualification = db.Column(db.Text, nullable=True)  # Qualification for consultants

    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role': self.role.value,  # Return the value of the Enum
            'qualification': self.qualification
        }
