from typing import Type, TypeVar
from . import db

class Shop(db.Model):
    """
    shop models
    """
    __tablename__ = 'shop'
    id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.Integer)
    name  = db.Column(db.String(120))

    def __repr__(self):
        return '<Task> %r' %self.id

    def getData(self) -> dict:
        return {'id': self.id, 'shop_id': self.shop_id, 'name': self.name}
