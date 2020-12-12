from flask.globals import request
from flask import jsonify

from ..models.user import User
from ..models.shop import Shop
from ..models.menu import Menu
from ..models.order import Order
from datetime import date
# from .. models.order_menu import OrderMenu
from ..models import db
from . import app, required_params, private
from sqlalchemy import func

@app.route('/shops', methods=['GET'])
@private()
def get_shops(data):
    shops = Shop().query.all()
    return jsonify([i.getData() for i in shops])

@app.route('/shops', methods=['PUT'])
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
        "message": "user not found"
    }, 400

@app.route('/shops/<id>', methods=['GET'])
@private()
def get_shop_byID(data, id):
    shop = Shop.query.filter_by(id=id).first()
    if shop:
        order = Order.query.filter(func.DATE(Order.created_at) == date.today(), Order.shop_id==id, Order.status=='waiting').first()
        queue = {'queue': 'no queue'}
        if order:
            queue = order.get('queue')
        result = shop.get('name', 'menus')
        result.update(queue)
        return {
            "success": True,
            "shop": result
        }, 201
    return {
        "success": False,
        "message": "shop not found"
    }, 400
