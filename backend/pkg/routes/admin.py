from flask.globals import request
from flask import jsonify

from ..models.user import User
from ..models.shop import Shop
from ..models import db
from . import app, required_params, private
from sqlalchemy import func, or_

@app.route('/admin/shops', methods=['GET'])
@private()
def get_shops_admin(data):
    shops = Shop.query.all()
    return {
        "success": True,
        "shops": [i.getData() for i in shops]
    }, 200

@app.route('/admin/users', methods=['GET'])
@private()
def get_users(data):
    users = User.query.all()
    return {
        "success": True,
        "users": [i.getData() for i in users]
    }, 200

@app.route('/admin/shops', methods=['PUT'])
@required_params({"name": str, "description": str, "email": int, "img": str})
@private()
def add_shop(data):
    body = request.get_json()
    owner = User.query.filter_by(email=data['email'])
    if owner:
        shop = Shop(
            name=body["name"],
            description=body["description"],
            owner_id=owner.id,
            img=body["img"]
        )
        db.session.add(shop)
        db.session.commit()
        return {
            "success": True,
            "shop": shop.getData()
        }, 201
    return {
        "success": False,
        "message": "ไม่พบผู้ใช้งาน"
    }, 400

@app.route('/admin/users', methods=['PUT'])
@required_params({"name": str, "description": str, "email": str, "img": str})
@private()
def add_user(data):
    body = request.get_json()
    owner = User.query.filter_by(email=data['email'])
    if owner:
        shop = Shop(
            name=body["name"],
            description=body["description"],
            owner_id=owner.id,
            img=body["img"]
        )
        db.session.add(shop)
        db.session.commit()
        return {
            "success": True,
            "shop": shop.getData()
        }, 201
    return {
        "success": False,
        "message": "ไม่พบผู้ใช้งาน"
    }, 400
