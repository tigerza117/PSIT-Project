from sqlalchemy.sql.schema import ForeignKey
from . import db, menu
from sqlalchemy import func

class OrderMenu(db.Model):
    """
    order_menu models
    """
    __tablename__ = 'order_menus'
    id = db.Column(db.Integer, primary_key=True)
    order_id  = db.Column(db.Integer, ForeignKey('orders.id'))
    menu_id = db.Column(db.Integer, ForeignKey('menus.id'))
    extra = db.Column(db.Boolean, default=False)
    total  = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, default=func.now())

    menu = db.relationship("Menu", uselist=False, backref="parent")

    def __repr__(self):
        return '<Task> %r' %self.id

    def getData(self) -> dict:
        data = {
            'id': self.id,
            'extra': self.extra,
            'total': self.total
        }
        data.update(self.menu.get('price', 'name', 'extra_price', 'category'))
        return data

    def get(self, *keys: tuple):
        a = self.getData()
        return dict((key,value) for key, value in a.items() if key in keys)
