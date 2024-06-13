from flask_restful import Resource, reqparse
from models import db
from models.user import User, Role

class UserListResource(Resource):
    def get(self):
        """Get all users."""
        users = User.query.all()
        return [user.to_dict() for user in users]

    def post(self):
        """Create a new user."""
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help="Username cannot be blank!")
        parser.add_argument('email', type=str, required=True, help="Email cannot be blank!")
        parser.add_argument('password', type=str, required=True, help="Password cannot be blank!")
        parser.add_argument('role', type=str, choices=[role.value for role in Role], default=Role.CLIENT.value, help="Role must be either 'client' or 'consultant'")
        parser.add_argument('qualification', type=str)  # Optional for consultants
        data = parser.parse_args()

        # Check if the role is valid
        if data['role'] not in [role.value for role in Role]:
            return {'message': 'Invalid role.'}, 400

        # Create the new user
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
    def get(self, user_id):
        """Get a specific user."""
        user = User.query.get_or_404(user_id)
        return user.to_dict()

    def put(self, user_id):
        """Update a user."""
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('role', type=str, choices=[role.value for role in Role])
        parser.add_argument('qualification', type=str)
        data = parser.parse_args()

        user = User.query.get_or_404(user_id)

        # Update fields if provided
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

    def delete(self, user_id):
        """Delete a user."""
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()

        return {'message': 'User deleted successfully.'}
