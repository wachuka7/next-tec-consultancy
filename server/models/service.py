# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash
# from models import db


# class Service(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.Text)
#     consultant_id = db.Column(db.Integer, db.ForeignKey('consultant.id'), nullable=False)

#     # consultant = db.relationship('Consultant', backref='services')

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'description': self.description,
#             'consultant_id': self.consultant_id
#         }
