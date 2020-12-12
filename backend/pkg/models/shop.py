
from sqlalchemy.sql.schema import ForeignKey
from . import db, menu, user, category
from sqlalchemy import func

class Shop(db.Model):
    """
    shop models
    """

    __tablename__ = 'shops'
    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(120))
    description = db.Column(db.String(120))
    owner_id = db.Column(db.Integer, ForeignKey('users.id'))
    categorys = db.relationship("Category", lazy='dynamic')
    img = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, default=func.now())

    owner = db.relationship("User", uselist=False, backref="parent")
    menus = db.relationship("Menu", lazy='dynamic')

    def __repr__(self):
        return '<Task> %r' %self.id

    def getData(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'desciption': self.description,
            'owner_id': self.owner_id,
            'img': self.img
        }

    def get(self, *keys: tuple):
        a = self.getData()
        return dict((key,value) for key, value in a.items() if key in keys)
