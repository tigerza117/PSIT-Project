from typing import Type, TypeVar
from . import db

T = TypeVar('T')

class User(db.Model):
    """
    user models
    """
    __tablename__ = 'userdata'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120))
    password = db.Column(db.String(120))

    def __repr__(self):
        return '<Task> %r' %self.id

    def getData(self) -> dict:
        return {'id': self.id, 'name': self.name, 'email': self.email, 'password': self.password}
