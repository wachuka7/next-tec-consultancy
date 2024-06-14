from flask_restful import Resource, reqparse
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
import jwt
from models import db
from models.consultant import Consultant, ConsultantRole
from models.post import Post

class PostListResource(Resource):
    def get(self):
        posts = Post.query.all()
        return jsonify([post.to_dict() for post in posts])

    @jwt_required()  
    def post(self):
        current_user_id = get_jwt_identity()

        current_user = Consultant.query.get_or_404(current_user_id)
        if current_user.role != ConsultantRole.CONSULTANT:
            return {'message': 'Only consultants can create posts'}, 403

        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help="Title cannot be blank!")
        parser.add_argument('content', type=str, required=True, help="Content cannot be blank!")
        parser.add_argument('category', type=str, required=True, help="Category cannot be blank!")
        data = parser.parse_args()

        valid_categories = ['Data Science', 'Software Engineering', 'Business', 'Leadership', 'Financial Services', 'Education', 'Health', 'Lifestyle']
        if data['category'] not in valid_categories:
            return {'message': 'Invalid category'}, 400
        
        new_post = Post(title=data['title'], content=data['content'], user_id=current_user_id)
        db.session.add(new_post)
        db.session.commit()

        return {'message': 'Post created successfully.'}, 201

class PostResource(Resource):   
    def get(self, post_id):
        post = Post.query.get_or_404(post_id)
        return jsonify(post.to_dict())
