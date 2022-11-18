import threading
from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required, create_access_token
from model import User, db
from flask_bcrypt import Bcrypt

auth_blue_print = Blueprint('auth', __name__)

update_lock = threading.Lock()

app_name = "auth"
bcrypt = Bcrypt()


@auth_blue_print.route('/', methods=['GET'])
@jwt_required()
def index():
    return jsonify(message="Hello Flask!")


@auth_blue_print.route('/register', methods=['POST'])
def register():
    email = request.json['email']
    test = User.query.filter_by(email=email).first()
    if test:
        return jsonify(message='That email already exists'), 409
    else:
        email = request.json['email']
        password = request.json['password']
        first_name = request.json['first_name']
        age = request.json['age']
        height = request.json['height']
        weight = request.json['weight']
        user = User(email, password, first_name, age, height, weight)
        db.session.add(user)
        db.session.commit()
        return jsonify(message='User created successfully'), 201


@auth_blue_print.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']

    found_user = User.query.filter_by(email=email).first()
    if found_user:
        authenticated_user = bcrypt.check_password_hash(found_user.password, password)
        if authenticated_user:
            access_token = create_access_token(identity=email)
            return jsonify(message='Login Successful', access_token=access_token), 200
        else:
            return jsonify('Wrong email or Password'), 401
    else:
        return jsonify("User not found"), 404


@auth_blue_print.route('/update-user-data', methods=['PUT'])
def update_user():
    email = request.json['email']
    user_data = {key: request.json[key] for key in request.json.keys() if
                 key in ("first_name", "age", "height", "height", "weight")}
    num_rows_updated = User.query.filter_by(email=email).update(user_data)
    db.session.commit()
