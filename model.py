from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

bcrypt = Bcrypt()


# Database models
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    first_name = Column(String)
    age = Column(Integer)
    height = Column(Integer)
    weight = Column(Integer)

    def __init__(self, email, password, first_name, age, height, weight):
        self.first_name = first_name
        self.email = email
        self.password = password
        self.age = age
        self.height = height
        self.weight = weight
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')


# DB Schemas
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'password', 'first_name', 'age', 'height', 'weight')
