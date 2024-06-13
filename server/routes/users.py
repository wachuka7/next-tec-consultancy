from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from functools import wraps
import jwt
from flask import request
from models import db
from models.user import User, Role


# def admin_required(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         # Get the JWT token from the Authorization header
#         auth_header = request.headers.get('Authorization')
#         if not auth_header:
#             return {'message': 'Authorization header missing'}, 401

#         # Extract the token from the Authorization header
#         token = auth_header.split(" ")[1]

#         # Decode the JWT token using PyJWT
#         try:
#             decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
#             role = decoded_token['role']  # Access the role claim
#         except jwt.exceptions.InvalidTokenError:
#             return {'message': 'Invalid token'}, 401

#         if role != Role.CONSULTANT.value:
#             return {'message': 'Admin privileges required.'}, 403
#         return fn(*args, **kwargs)
#     return wrapper

class UserListResource(Resource):
    @jwt_required()
    def get(self):
        users = User.query.all()
        return [user.to_dict() for user in users]
    
    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help="Username cannot be blank!")
        parser.add_argument('email', type=str, required=True, help="Email cannot be blank!")
        parser.add_argument('password', type=str, required=True, help="Password cannot be blank!")
        parser.add_argument('role', type=str, choices=[role.value for role in Role], default=Role.CLIENT.value, help="Role must be either 'client' or 'consultant'")
        parser.add_argument('qualification', type=str) 
        data = parser.parse_args()

        if data['role'] not in [role.value for role in Role]:
            return {'message': 'Invalid role.'}, 400

        new_user = User(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            role=Role(data['role']),
            qualification=data['qualification'] if data['role'] == Role.CONSULTANT.value else None
        )
        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User created successfully.'}, 201

class UserResource(Resource):
    @jwt_required()
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user.to_dict()

    @jwt_required()
    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('role', type=str, choices=[role.value for role in Role])
        parser.add_argument('qualification', type=str)
        data = parser.parse_args()

        user = User.query.get_or_404(user_id)

        if data['username']:
            user.username = data['username']
        if data['email']:
            user.email = data['email']
        if data['password']:
            user.password = data['password']
        if data['role']:
            user.role = Role(data['role'])
        if data['qualification']:
            user.qualification = data['qualification']

        db.session.commit()

        return {'message': 'User updated successfully.'}
    
    @jwt_required()
    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()

        return {'message': 'User deleted successfully.'}

class ConsultantListResource(Resource):
    # @admin_required
    def get(self):
        consultants = User.query.filter_by(role=Role.CONSULTANT).all()
        return [consultant.to_dict() for consultant in consultants]

class ConsultantResource(Resource):
    # @admin_required
    def get(self, consultant_id):
        consultant = User.query.get_or_404(consultant_id)
        return consultant.to_dict()

    # @admin_required
    def put(self, consultant_id):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('qualification', type=str)
        data = parser.parse_args()

        consultant = User.query.get_or_404(consultant_id)

        if data['username']:
            consultant.username = data['username']
        if data['email']:
            consultant.email = data['email']
        if data['password']:
            consultant.password = data['password']
        if data['qualification']:
            consultant.qualification = data['qualification']

        db.session.commit()

        return {'message': 'Consultant updated successfully.'}

    # @admin_required
    def delete(self, consultant_id):
        consultant = User.query.get_or_404(consultant_id)
        db.session.delete(consultant)
        db.session.commit()

        return {'message': 'Consultant deleted successfully.'}

class ClientRegisterResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help="Username cannot be blank!")
        parser.add_argument('email', type=str, required=True, help="Email cannot be blank!")
        parser.add_argument('password', type=str, required=True, help="Password cannot be blank!")
        data = parser.parse_args()

        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            return {'message': 'A user with that email already exists'}, 400

        new_client = User(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            role=Role.CLIENT
        )
        new_client.set_password(new_client.password)
        db.session.add(new_client)
        db.session.commit()

        return {'message': 'Client registered successfully.'}, 201
    
class ConsultantRegisterResource(Resource):
    # @admin_required
    def get(self):
        consultants = User.query.filter_by(role=Role.CONSULTANT).all()
        return [consultant.to_dict() for consultant in consultants]
    # @admin_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help="Username cannot be blank!")
        parser.add_argument('email', type=str, required=True, help="Email cannot be blank!")
        parser.add_argument('password', type=str, required=True, help="Password cannot be blank!")
        parser.add_argument('qualification', type=str, required=True, help="Qualification cannot be blank!")
        parser.add_argument('certificate_url', type=str, required=True, help="Certificate URL cannot be blank!")
        data = parser.parse_args()

        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            return {'message': 'A user with that email already exists'}, 400

        is_certificate_valid = verify_certificate(data['certificate_url'])
        if not is_certificate_valid:
            return {'message': 'Invalid certificate.'}, 400

        new_consultant = User(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            role=Role.CONSULTANT,
            qualification=data['qualification']
        )
        new_consultant.set_password(new_consultant.password)
        db.session.add(new_consultant)
        db.session.commit()

        return {'message': 'Consultant registered successfully.'}, 201

def verify_certificate(certificate_url):
    if 'certificate' in certificate_url:
        return True
    else:
        return False

class LoginResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help="Username cannot be blank!")
        parser.add_argument('password', type=str, required=True, help="Password cannot be blank!")
        data = parser.parse_args()

        user = User.query.filter_by(username=data['username']).first()
        if not user or not user.check_password(data['password']):
            return {'message': 'Invalid credentials'}, 401

        access_token = create_access_token(identity=user.id, fresh=True, additional_claims={'role': user.role.value})
        return {'access_token': access_token}, 200
