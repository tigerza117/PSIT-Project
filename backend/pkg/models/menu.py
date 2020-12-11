from sqlalchemy.sql.schema import ForeignKey
from . import db, category

class Menu(db.Model):
    """
    menu models
    """
    __tablename__ = 'menus'
    id = db.Column(db.Integer, primary_key=True)
    shop_id  = db.Column(db.Integer, ForeignKey('shops.id'))
    name = db.Column(db.String(120))
    price = db.Column(db.Integer)
    extra_price = db.Column(db.Integer)
    category_id = db.Column(db.Integer, ForeignKey('categorys.id'))

    category = db.relationship("Category", uselist=False, backref="parent")

    def __repr__(self):
        return '<Task> %r' %self.id

    def getData(self) -> dict:
        return {
            'id': self.id,
            'shop_id': self.shop_id,
            'name': self.name,
            'price': self.price,
            'extra_price': self.extra_price,
            'category_id': self.category_id,
            'category': self.category.get('name')['name']
        }

    def get(self, *keys: tuple):
        a = self.getData()
        return dict((key,value) for key, value in a.items() if key in keys)
