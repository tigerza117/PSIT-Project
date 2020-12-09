from sqlalchemy.sql.schema import ForeignKey
from . import db, menu

class OrderMenu(db.Model):
    """
    order_menu models
    """
    __tablename__ = 'order_menus'
    id = db.Column(db.Integer, primary_key=True)
    order_id  = db.Column(db.Integer, ForeignKey('orders.id'))
    menu_id = db.Column(db.Integer, ForeignKey('menus.id'))
    extra = db.Column(db.Boolean)
    menu = db.relationship("Menu", uselist=False, backref="parent")

    def __repr__(self):
        return '<Task> %r' %self.id

    def getData(self) -> dict:
        return {
            'id': self.id,
            'order_id': self.order_id,
            'menu_id': self.menu_id,
            'menu': self.menu.getData()
        }
