from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, create_access_token
from functools import wraps
from models import db
from models.user import User, Role

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        claims = get_jwt_claims()
        if claims['role'] != Role.CONSULTANT.value:
            return {'message': 'Admin privileges required.'}, 403
        return fn(*args, **kwargs)
    return wrapper


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


