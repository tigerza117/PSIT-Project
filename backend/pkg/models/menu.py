from typing import Type, TypeVar
from . import db

class Menu(db.Model):
    """
    menu models
    """
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)
    shop_id  = db.Column(db.Integer)
    name = db.Column(db.String(120))
    price = db.Column(db.Integer)
    extra_price = db.Column(db.Integer)
    category_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Task> %r' %self.id

    def getData(self) -> dict:
        return {'id': self.id, 'shop_id': self.shop_id, 'name': self.name, 'price': self.price,
        'extra_price': self.extra_price, 'category_id': self.category_id
        }
