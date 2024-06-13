from enum import Enum
from werkzeug.security import generate_password_hash, check_password_hash
from models import db

class Role(Enum):
    CLIENT = "client"
    CONSULTANT = "consultant"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False) 
    role = db.Column(db.Enum(Role), default=Role.CLIENT)  
    qualification = db.Column(db.Text, nullable=True)  

    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role': self.role.value, 
            'qualification': self.qualification
        }
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

