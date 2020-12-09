from sqlalchemy.sql.schema import ForeignKey
from . import db, order_menu

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
    status = db.Column(db.String(120))
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
            'menus': [i.getData() for i in self.menus]
        }

