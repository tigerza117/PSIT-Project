from flask.globals import request
from flask import jsonify

from ..models.user import User
from ..models.shop import Shop
from ..models import db
from . import app, required_params, private
from sqlalchemy import func, or_
import hashlib

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
@required_params({"name": str, "description": str, "email": str, "img": str})
@private()
def add_shop(data):
    body = request.get_json()
    owner = User.query.filter_by(email=body['email']).first()
    if owner:
        img = body['img']
        if img == '':
            img = 'https://lme-me.web.app/logo.png'
        shop = Shop(
            name=body["name"],
            description=body["description"],
            owner_id=owner.id,
            img=img
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

@app.route('/admin/shops/<int:id>', methods=['PATCH'])
@required_params({"name": str, "description": str, "email": str, "img": str})
@private()
def update_shop(data, id):
    body = request.get_json()
    owner = User.query.filter_by(email=body['email']).first()
    if owner:
        shop = Shop.query.filter_by(id=id).first()
        img = body['img']
        if img == '':
            img = 'https://lme-me.web.app/logo.png'
        if shop:
            shop.name = body['name']
            shop.description = body['description']
            shop.owner_id = owner.id
            shop.img = img
            db.session.commit()
            return {
                "success": True,
                "shop": shop.getData()
            }, 200
        return {
            "success": False,
            "message": "ไม่พบร้านค้า"
        }, 400
    return {
        "success": False,
        "message": "ไม่พบผู้ใช้งาน"
    }, 400

@app.route('/admin/users/<id>', methods=['PATCH'])
@required_params({"fname": str, "lname": str, "email": str})
@private()
def add_user(data, id):
    body = request.get_json()
    user = User.query.filter_by(id=id).first()
    if user:
        user.fname = body['fname']
        user.lname = body['lname']
        user.email = body['email']
        if body.get('password', '') != '':
            user.password = hashlib.md5(body['password'].encode('utf-8')).hexdigest()
        db.session.commit()
        return {
            "success": True,
        }, 200
    return {
        "success": False,
        "message": "ไม่พบผู้ใช้งาน"
    }, 400
