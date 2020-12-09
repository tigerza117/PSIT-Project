from sqlalchemy.sql.schema import ForeignKey
from . import db

class Category(db.Model):
    """
    shop models
    """
    __tablename__ = 'categorys'
    id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.Integer, ForeignKey('shops.id'))
    name  = db.Column(db.String(120))

    def __repr__(self):
        return '<Task> %r' %self.id

    def getData(self) -> dict:
        return {
            'id': self.id,
            'shop_id': self.shop_id,
            'name': self.name
        }

    def get(self, *keys: tuple):
        a = self.getData()
        return dict((key,value) for key, value in a.items() if key in keys)
