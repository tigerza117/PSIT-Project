from typing import Type, TypeVar

from sqlalchemy.sql.schema import ForeignKey
from . import db, menu, user, category

class Shop(db.Model):
    """
    shop models
    """
    __tablename__ = 'shops'
    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(120))
    description = db.Column(db.String(120))
    owner_id = db.Column(db.Integer, ForeignKey('users.id'))

    owner = db.relationship("User", uselist=False, backref="parent")
    menus = db.relationship("Menu", lazy='dynamic')
    categorys = db.relationship("Category", lazy='dynamic')

    def __repr__(self):
        return '<Task> %r' %self.id

    def getData(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'desciption': self.desciption,
            'owner_id': self.owner_id
        }
