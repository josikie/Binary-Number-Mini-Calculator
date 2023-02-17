import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_migrate import Migrate

load_dotenv()

database_path = os.environ.get("DB_PATH")

db = SQLAlchemy()


'''
    bind app with SQLAlchemy
'''
def setDB(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    with db.app.app_context():
        db.init_app(app)
        migrate = Migrate(app, db)


class BinaryAddition(db.Model):
    __tablename__ = 'binary_addition'
    
    id = db.Column(db.Integer, primary_key=True)
    first_binary_number = db.Column(db.String(255))
    second_binary_number = db.Column(db.String(255))
    result = db.Column(db.String)


    def __init__(self, first_binary_number, second_binary_number, result):
        self.first_binary_number = first_binary_number
        self.second_binary_number = second_binary_number
        self.result = result
    

    def insert(self):
        db.session.add(self)
        db.session.commit()
    

    def update(self):
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()
    

    def format(self):
        return {
            'id': self.id,
            'first_number': self.first_binary_number,
            'second_number': self.second_binary_number,
            'result': self.result
        }
    

class BinarySubstraction(db.Model):
    __tablename__ = 'binary_substraction'
    
    id = db.Column(db.Integer, primary_key=True)
    first_binary_number = db.Column(db.String(255))
    second_binary_number = db.Column(db.String(255))
    result = db.Column(db.String)


    def __init__(self, first_binary_number, second_binary_number, result):
        self.first_binary_number = first_binary_number
        self.second_binary_number = second_binary_number
        self.result = result
    

    def insert(self):
        db.session.add(self)
        db.session.commit()
    

    def update(self):
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()
    

    def format(self):
        return {
            'id': self.id,
            'first_number': self.first_binary_number,
            'second_number': self.second_binary_number,
            'result': self.result
        }


class BinaryMultiplication(db.Model):
    __tablename__ = 'binary_multiplication'
    
    id = db.Column(db.Integer, primary_key=True)
    first_binary_number = db.Column(db.String(255))
    second_binary_number = db.Column(db.String(255))
    result = db.Column(db.String)


    def __init__(self, first_binary_number, second_binary_number, result):
        self.first_binary_number = first_binary_number
        self.second_binary_number = second_binary_number
        self.result = result
    

    def insert(self):
        db.session.add(self)
        db.session.commit()
    

    def update(self):
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()
    

    def format(self):
        return {
            'id': self.id,
            'first_number': self.first_binary_number,
            'second_number': self.second_binary_number,
            'result': self.result
        }


class BinaryDivision(db.Model):
    __tablename__ = 'binary_division'
    
    id = db.Column(db.Integer, primary_key=True)
    first_binary_number = db.Column(db.String(255))
    second_binary_number = db.Column(db.String(255))
    result = db.Column(db.String)


    def __init__(self, first_binary_number, second_binary_number, result):
        self.first_binary_number = first_binary_number
        self.second_binary_number = second_binary_number
        self.result = result
    

    def insert(self):
        db.session.add(self)
        db.session.commit()

    
    def update(self):
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()
    

    def format(self):
        return {
            'id': self.id,
            'first_number': self.first_binary_number,
            'second_number': self.second_binary_number,
            'result': self.result
        }