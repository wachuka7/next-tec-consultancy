from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config
from models import db
from routes.users import UserResource, UserListResource, LoginResource, ClientRegisterResource, ConsultantRegisterResource, ConsultantResource, ConsultantListResource
from routes.projects import ProjectResource, ProjectListResource
from routes.posts import PostResource


app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

secret_key = app.config['SECRET_KEY']

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

api = Api(app)

api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(ConsultantListResource, '/consultants')
api.add_resource(ConsultantResource, '/consultants/<int:consultant_id>')
api.add_resource(ProjectListResource, '/projects')
api.add_resource(ProjectResource, '/projects/<int:project_id>')
api.add_resource(LoginResource, '/login')
api.add_resource(ClientRegisterResource, '/register/client')
api.add_resource(ConsultantRegisterResource, '/register/consultant')
api.add_resource(PostResource, '/posts')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
