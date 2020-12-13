from sqlalchemy.sql.schema import ForeignKey
from . import db
from sqlalchemy import func

class Category(db.Model):
    """
    shop models
    """
    __tablename__ = 'categorys'
    id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.Integer, ForeignKey('shops.id'))
    name = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, default=func.now())

    def __repr__(self):
        return '<Task> %r' %self.id

    def getData(self) -> dict:
        return {
            'id': self.id,
            'shop_id': self.shop_id,
            'name': self.name,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def get(self, *keys: tuple):
        a = self.getData()
        return dict((key,value) for key, value in a.items() if key in keys)
