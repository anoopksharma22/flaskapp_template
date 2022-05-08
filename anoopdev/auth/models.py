from anoopdev.extensions import db
from anoopdev import bcrypt
from flask_login import UserMixin




class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_password):
        self.password_hash = bcrypt.generate_password_hash(plain_password).decode('utf-8')

    def validate_password(self,password_received):
        return bcrypt.check_password_hash(self.password_hash,password_received)