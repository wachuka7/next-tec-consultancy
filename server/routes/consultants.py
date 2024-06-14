from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, create_access_token
from models.consultant import Consultant, ConsultantRole
from models import db

class ConsultantListResource(Resource):
    def get(self):
        consultants = Consultant.query.all()
        return [consultant.to_dict() for consultant in consultants]

class ConsultantRegisterResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help="Username cannot be blank!")
        parser.add_argument('email', type=str, required=True, help="Email cannot be blank!")
        parser.add_argument('password', type=str, required=True, help="Password cannot be blank!")
        parser.add_argument('qualification', type=str, required=True, help="Qualification cannot be blank!")
        
        data = parser.parse_args()

        existing_consultant = Consultant.query.filter_by(email=data['email']).first()
        if existing_consultant:
            return {'message': 'A consultant with that email already exists'}, 400

        new_consultant = Consultant(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            qualification=data['qualification']
        )
        new_consultant.set_password(new_consultant.password)
        db.session.add(new_consultant)
        db.session.commit()

        return {'message': 'Consultant registered successfully.'}, 201

class ConsultantResource(Resource):
    def get(self, consultant_id):
        consultant = Consultant.query.get_or_404(consultant_id)
        return consultant.to_dict()

    @jwt_required()
    def put(self, consultant_id):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('qualification', type=str)
        parser.add_argument('photo', type=str)
        parser.add_argument('bio', type=str)
        parser.add_argument('location', type=str) 
        parser.add_argument('services', type=list)
        parser.add_argument('linkedin', type=str)
        parser.add_argument('twitter', type=str)
        parser.add_argument('about', type=str)
        # parser.add_argument('projects', type=list)
        parser.add_argument('testimonials', type=list)
        data = parser.parse_args()

        consultant = Consultant.query.get_or_404(consultant_id)

        if data['username']:
            consultant.username = data['username']
        if data['email']:
            consultant.email = data['email']
        if data['password']:
            consultant.set_password(data['password'])
        if data['qualification']:
            consultant.qualification = data['qualification']
        if data['photo']:
            consultant.photo = data['photo']
        if data['bio']:
            consultant.bio = data['bio']
        if data['location']:
            consultant.location = data['location']
        if data['services']:
            consultant.services = data['services']
        if data['linkedin']:
            consultant.linkedin = data['linkedin']
        if data['twitter']:
            consultant.twitter = data['twitter']
        if data['about']:
            consultant.about = data['about']
        # if data['projects']:
        #     consultant.projects = data['projects']
        if data['testimonials']:
            consultant.testimonials = data['testimonials']

        db.session.commit()

        return {'message': 'Consultant updated successfully.'}

    @jwt_required()
    def delete(self, consultant_id):
        consultant = Consultant.query.get_or_404(consultant_id)
        db.session.delete(consultant)
        db.session.commit()

        return {'message': 'Consultant deleted successfully.'}

class ConsultantLoginResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help="Username cannot be blank!")
        parser.add_argument('password', type=str, required=True, help="Password cannot be blank!")
        data = parser.parse_args()

        consultant = Consultant.query.filter_by(username=data['username']).first()
        if not consultant or not consultant.check_password(data['password']):
            return {'message': 'Invalid credentials'}, 401

        access_token = create_access_token(identity=consultant.id, fresh=True, additional_claims={'role': consultant.role})
        return {'access_token': access_token}, 200
