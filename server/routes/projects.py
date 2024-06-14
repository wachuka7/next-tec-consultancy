from flask_restful import Resource, reqparse
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.project import Project
from app import db

class ProjectListResource(Resource):
    def get(self):
        projects = Project.query.all()
        return jsonify([project.to_dict() for project in projects])

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help="Name cannot be blank!")
        parser.add_argument('description', type=str)
        parser.add_argument('client_id', type=int, required=True, help="Client ID cannot be blank!")
        parser.add_argument('consultant_id', type=int, required=True, help="Consultant ID cannot be blank!")
        parser.add_argument('client_request', type=str)
        data = parser.parse_args()

        new_project = Project(name=data['name'], 
                              description=data['description'], 
                              client_id=data['client_id'], 
                              consultant_id=data['consultant_id'], 
                              client_request=data['client_request'])
        db.session.add(new_project)
        db.session.commit()

        return {'message': 'Project created successfully.'}, 201

class ProjectResource(Resource):
    def get(self, project_id):
        project = Project.query.get_or_404(project_id)
        return project.to_dict()

    def put(self, project_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('client_request', type=str)
        data = parser.parse_args()

        project = Project.query.get_or_404(project_id)
        if data['name']:
            project.name = data['name']
        if data['description']:
            project.description = data['description']
        if data['client_request']:
            project.client_request = data['client_request']
        
        db.session.commit()

        return {'message': 'Project updated successfully.'}

    def delete(self, project_id):
        project = Project.query.get_or_404(project_id)
        db.session.delete(project)
        db.session.commit()

        return {'message': 'Project deleted successfully.'}
