from flask_restful import Resource, reqparse
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
import jwt
from models import db
from models.user import User, Role
from models.post import Post

class PostResource(Resource):
    def get(self):
        posts = Post.query.all()
        return jsonify([post.to_dict() for post in posts])

    @jwt_required()  
    def post(self):
        current_user_id = get_jwt_identity()

        current_user = User.query.get_or_404(current_user_id)
        if current_user.role != Role.CONSULTANT:
            return {'message': 'Only consultants can create posts'}, 403

        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help="Title cannot be blank!")
        parser.add_argument('content', type=str, required=True, help="Content cannot be blank!")
        data = parser.parse_args()

        new_post = Post(title=data['title'], content=data['content'], user_id=current_user_id)
        db.session.add(new_post)
        db.session.commit()

        return {'message': 'Post created successfully.'}, 201
