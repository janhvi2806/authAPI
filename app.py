from flask import Flask
import os
from flask_jwt_extended import JWTManager
from config import SQLALCHEMY_DATABASE_URI, JWT_SECRET_KEY
from auth_blue_print import auth_blue_print
from model import db, ma
from flask_migrate import Migrate

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY

db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
app.register_blueprint(auth_blue_print, url_prefix='')


# DB set up and seeders
@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database created')


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped')

# @app.cli.command('db_seed')
# def db_seed():
#     test_user = User(first_name='Stephen',
#                      last_name='Hawking',
#                      email='admin@admin.com',
#                      password='admin')
#     db.session.add(test_user)
#     db.session.commit()
#     print('Database seeded')


# # Planet Routes
# @app.route('/', methods=['GET'])
# @jwt_required()
# def index():
#     return jsonify(message="Hello Flask!")
