""" SQL tables as Python objects using the SQLAlchemy package """


from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


class User(db.Model):
    """
    Tablename is explicit so the package does not define one instead
    Index attribute is indexing the column data. Refer SQL
    Password hash is stored instead of actual password 
    """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    reg_number = db.Column(db.String(16), unique = True, index = True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    department = db.Column(db.String(64), index = True)
    level = db.Column(db.Integer, index = True)
    password_hash = db.Column(db.String(128))
    
    def __init__(self, **kwargs):
        """ Init has no true use yet until roles are added """
        super().__init__(**kwargs)
        

    def __repr__(self):
        return "< User {} >".format(self.reg_number)


    @property
    def password(self):
        raise AttributeError('ACCESS DENIED')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """ check_password_hash re-hashes the second argument passed and com"""
        return check_password_hash(self.password_hash, password)