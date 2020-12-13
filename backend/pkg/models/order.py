from sqlalchemy.sql.schema import ForeignKey
from . import db, order_menu
from sqlalchemy import func

class Order(db.Model):
    """
    order models
    """
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    customer_id  = db.Column(db.Integer, ForeignKey('users.id'))
    shop_id = db.Column(db.Integer, ForeignKey('shops.id'))
    note = db.Column(db.String(120))
    queue = db.Column(db.String(120))
    status = db.Column(db.String(120), default="ordering")
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, default=func.now())

    menus = db.relationship("OrderMenu", lazy='dynamic')

    def __repr__(self):
        return '<Task> %r' %self.id

    def getData(self) -> dict:
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'shop_id': self.shop_id,
            'note': self.note,
            'queue': self.queue,
            'status': self.status,
            'menus': [i.getData() for i in self.menus],
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def get(self, *keys: tuple):
        a = self.getData()
        return dict((key,value) for key, value in a.items() if key in keys)

