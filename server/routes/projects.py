from flask_restful import Resource, reqparse
from models.project import Project
from app import db


class ProjectListResource(Resource):
    def get(self):
        """Get all projects."""
        projects = Project.query.all()
        return [project.to_dict() for project in projects]

    def post(self):
        """Create a new project."""
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help="Name cannot be blank!")
        parser.add_argument('description', type=str)
        parser.add_argument('user_id', type=int, required=True, help="User ID cannot be blank!")
        data = parser.parse_args()

        new_project = Project(name=data['name'], description=data['description'], user_id=data['user_id'])
        db.session.add(new_project)
        db.session.commit()

        return {'message': 'Project created successfully.'}, 201

class ProjectResource(Resource):
    def get(self, project_id):
        """Get a specific project."""
        project = Project.query.get_or_404(project_id)
        return project.to_dict()

    def put(self, project_id):
        """Update a project."""
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('description', type=str)
        data = parser.parse_args()

        project = Project.query.get_or_404(project_id)
        project.name = data['name'] if data['name'] else project.name
        project.description = data['description'] if data['description'] else project.description
        db.session.commit()

        return {'message': 'Project updated successfully.'}

    def delete(self, project_id):
        """Delete a project."""
        project = Project.query.get_or_404(project_id)
        db.session.delete(project)
        db.session.commit()

        return {'message': 'Project deleted successfully.'}

# Add a to_dict method to the Project model

