from typing import Type, TypeVar
from . import db

class Order(db.Model):
    """
    order models
    """
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    customer_id  = db.Column(db.Integer)
    shop_id = db.Column(db.Integer)
    note = db.Column(db.String(120))
    queue = db.Column(db.String(120))
    status = db.Column(db.String(120))

    def __repr__(self):
        return '<Task> %r' %self.id

    def getData(self) -> dict:
        return {'id': self.id, 'customer_id': self.customer_id, 'shop_id': self.shop_id,
         'note': self.note, 'queue': self.queue, 'status': self.status
            }
