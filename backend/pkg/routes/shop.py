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
from sqlalchemy import func, or_

@app.route('/shops', methods=['GET'])
@private()
def get_shops(data):
    shops = Shop.query.all()
    return jsonify([i.getData() for i in shops])

@app.route('/shops/<int:id>', methods=['GET'])
@private()
def get_shop_byID(data, id):
    shop = Shop.query.filter_by(id=id).first()
    if shop:
        order = Order.query.filter(func.DATE(Order.created_at) == date.today(), Order.shop_id==id, Order.status == 'waiting').first()
        waiting = Order.query.filter(func.DATE(Order.created_at) == date.today(), Order.shop_id==id, or_(Order.status == 'ordering', Order.status == 'waiting')).count()
        queue = {'queue': 'no queue'}
        result = shop.get('name', 'menus', 'open', 'owner_id')
        if order:
            queue = order.get('queue')
            result.update({'order': order.getData()})
        result.update(queue)
        result.update({'waiting': waiting}),
        return {
            "success": True,
            "shop": result
        }, 201
    return {
        "success": False,
        "message": "ไม่พบร้านค้า"
    }, 400
