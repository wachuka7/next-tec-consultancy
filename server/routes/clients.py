from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, create_access_token
from models.client import Client, ClientRole
from models import db

class ClientListResource(Resource):
    def get(self):
        clients = Client.query.all()
        return [client.to_dict() for client in clients]

class ClientRegisterResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help="Username cannot be blank!")
        parser.add_argument('email', type=str, required=True, help="Email cannot be blank!")
        parser.add_argument('password', type=str, required=True, help="Password cannot be blank!")
        data = parser.parse_args()

        existing_client = Client.query.filter_by(email=data['email']).first()
        if existing_client:
            return {'message': 'A client with that email already exists'}, 400

        new_client = Client(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        new_client.set_password(new_client.password)
        db.session.add(new_client)
        db.session.commit()

        return {'message': 'Client registered successfully.'}, 201

class ClientResource(Resource):
    def get(self, client_id):
        client = Client.query.get_or_404(client_id)
        return client.to_dict()

    @jwt_required()
    def put(self, client_id):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('photo', type=str)
        parser.add_argument('bio', type=str)
        data = parser.parse_args()

        client = Client.query.get_or_404(client_id)

        if data['username']:
            client.username = data['username']
        if data['email']:
            client.email = data['email']
        if data['password']:
            client.set_password(data['password'])
        if data['photo']:
            client.photo = data['photo']
        if data['bio']:
            client.bio = data['bio']

        db.session.commit()

        return {'message': 'Client updated successfully.'}

    @jwt_required()
    def delete(self, client_id):
        client = Client.query.get_or_404(client_id)
        db.session.delete(client)
        db.session.commit()

        return {'message': 'Client deleted successfully.'}

class ClientLoginResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help="Username cannot be blank!")
        parser.add_argument('password', type=str, required=True, help="Password cannot be blank!")
        data = parser.parse_args()

        client = Client.query.filter_by(username=data['username']).first()
        if not client or not client.check_password(data['password']):
            return {'message': 'Invalid credentials'}, 401

        access_token = create_access_token(identity=client.id, fresh=True, additional_claims={'role': client.role})
        return {'access_token': access_token}, 200
