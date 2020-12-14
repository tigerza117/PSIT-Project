from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import func

class Menu(db.Model):
    """
    menu models
    """
    __tablename__ = 'menus'
    id = db.Column(db.Integer, primary_key=True)
    shop_id  = db.Column(db.Integer, ForeignKey('shops.id'))
    name = db.Column(db.String(120))
    description = db.Column(db.String(4096))
    price = db.Column(db.Integer)
    extra_price = db.Column(db.Integer)
    img = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, default=func.now())
    deleted_at = db.Column(db.DateTime)

    def __repr__(self):
        return '<Task> %r' %self.id

    def getData(self) -> dict:
        return {
            'id': self.id,
            'shop_id': self.shop_id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'extra_price': self.extra_price,
            'img': self.img,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def get(self, *keys: tuple):
        a = self.getData()
        return dict((key,value) for key, value in a.items() if key in keys)
