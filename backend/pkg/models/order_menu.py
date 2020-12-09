from typing import Type, TypeVar
from . import db

class Order_menu(db.Model):
    """
    order_menu models
    """
    __tablename__ = 'order_menu'
    id = db.Column(db.Integer, primary_key=True)
    order_id  = db.Column(db.Integer)
    menu_id = db.Column(db.Integer)
    extra = db.Column(db.Boolean)

    def __repr__(self):
        return '<Task> %r' %self.id

    def getData(self) -> dict:
        return {'id': self.id, 'order_id': self.order_id, 'menu_id': self.menu_id, 'note': self.note}
