from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from models import db
from routes.users import UserResource, UserListResource
from routes.projects import ProjectResource, ProjectListResource


app = Flask(__name__)
app.config.from_object(Config)

secret_key = app.config['SECRET_KEY']
# print(secret_key)

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)


api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(ProjectListResource, '/projects')
api.add_resource(ProjectResource, '/projects/<int:project_id>')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
