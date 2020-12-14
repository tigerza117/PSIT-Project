from datetime import date
from flask import jsonify
from sqlalchemy.sql.operators import custom_op

from ..models.order_menu import OrderMenu
from ..models.order import Order
from ..models.menu import Menu
from ..models.shop import Shop
from ..models import db
from . import app, private, required_params
from sqlalchemy import func, or_
from flask.globals import request

@app.route('/merchant/state/<action>', methods=['POST'])
@private()
def merchant_state(data, action):
    shop = Shop.query.filter_by(owner_id=data['id']).first()
    if shop:
        if action == 'open':
            shop.open = True
        else:
            shop.open = False
        db.session.commit()
        return {
            'success': True
        }, 200
    return {
        'success': False,
        'message': 'คุณไม่ใช้เจ้าของร้านค้า'
    }, 400

@app.route('/merchant/shop', methods=['GET'])
@private()
def get_merchant_shop(data):
    shop = Shop.query.filter_by(owner_id=data['id']).first()
    if shop:
        result = shop.getData()
        id = result['id']
        order = Order.query.filter(func.DATE(Order.created_at) == date.today(), Order.shop_id==id, Order.status == 'waiting').first()
        waiting = Order.query.filter(func.DATE(Order.created_at) == date.today(), Order.shop_id==id, or_(Order.status == 'ordering', Order.status == 'waiting')).count()
        queue = {'queue': 'no queue'}
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

@app.route('/merchant/orders', methods=['GET'])
@private()
def get_orders(data):
    shop = Shop.query.filter_by(owner_id=data['id']).first()
    if shop:
        shop = shop.getData()
        orderds = Order.query.filter_by(shop_id=shop['id']).all()
        return {
            'success': True,
            'orders': [i.getData() for i in orderds]
        }, 200
    return {
        'success': False,
        'message': 'คุณไม่ใช้เจ้าของร้านค้า'
    }, 400

@app.route('/merchant/orders/<action>', methods=['POST'])
@private()
def action_order(data, action):
    # finish, fail, next
    shop = Shop.query.filter_by(owner_id=data['id']).first()
    if shop:
        shop = shop.getData()
        id = shop['id']
        current_order = Order.query.filter(func.DATE(Order.created_at) == date.today(), Order.shop_id==id, Order.status == 'waiting').first()
        if action == 'finish':
            if current_order:
                current_order.status = 'finished'
                db.session.commit()
                return {
                    'success': True,
                }, 200
            return {
                'success': False,
                'message': 'คุณไม่มีออเดอร์ปัจจุบัน'
            }, 200
        elif action == 'next':
            if current_order:
                current_order.status = 'finished'
                db.session.commit()
            ordering = Order.query.filter(func.DATE(Order.created_at) == date.today(), Order.shop_id==id, Order.status == 'ordering').first()
            if ordering:
                ordering.status = 'waiting'
                db.session.commit()
                return {
                    'success': True,
                }, 200
            return {
                'success': False,
                'message': 'ออเดอร์หมดแล้ว'
            }, 200
        return {
            'success': False,
            'message': 'ไม่พบออเดอร์'
        }, 400

    return {
        'success': False,
        'message': 'คุณไม่ใช้เจ้าของร้านค้า'
    }, 400

@app.route('/merchant/menus', methods=['GET'])
@private()
def get_merchant_menus(data):
    shop = Shop.query.filter_by(owner_id=data['id']).first()
    if shop:
        res = {
            'success': True
        }
        res.update(shop.get('menus'))
        return res, 200
    return {
        'success': False,
        'message': 'คุณไม่ใช้เจ้าของร้านค้า'
    }, 400

@app.route('/merchant/menus', methods=['PUT'])
@required_params({"name": str, "description": str, "price": int, "extra_price": int,  "img": str})
@private()
def add_menu(data):
    shop = Shop.query.filter_by(owner_id=data['id']).first()
    if shop:
        body = request.get_json()
        shop = shop.getData()
        menu = Menu(
            shop_id = shop['id'],
            name = body["name"],
            price = body["price"],
            extra_price = body["extra_price"],
            img = body["img"]
        )
        db.session.add(menu)
        db.session.commit()
        return {
            'success': True,
            'menu': menu.getDataa()
        }, 201
    return {
        'success': False,
        'message': 'คุณไม่ใช้เจ้าของร้านค้า'
    }, 400

@app.route('/merchant/menus/<id>', methods=['PATCH'])
@required_params({"name": str, "description": str, "price": int, "extra_price": int, "img": str})
@private()
def update_menu(data, id):
    shop = Shop.query.filter_by(owner_id=data['id']).first()
    if shop:
        body = request.get_json()
        menu = Menu.query.filter_by(id=id).first()
        if menu:
            menu.name = body['name']
            menu.description = body['description']
            menu.price = body['price']
            menu.extra_price = body['extra_price']
            menu.img = body['img']
            return {
                'success': True,
            }, 200
        return {
            'success': False,
            'message': 'ไม่พบเมนูนี้ในระบบ'
        }, 400
    return {
        'success': False,
        'message': 'คุณไม่ใช้เจ้าของร้านค้า'
    }, 400

@app.route('/merchant/menus/<id>', methods=['DELETE'])
@required_params({"name": str, "description": str, "price": int, "extra_price": int, "img": str})
@private()
def del_menu(data, id):
    shop = Shop.query.filter_by(owner_id=data['id']).first()
    if shop:
        menu = Menu.query.filter_by(id=id).first()
        if menu:
            menu.deleted_at = func.now()
            db.session.commit()
            return {
                'success': True,
            }, 200
        return {
            'success': False,
            'message': 'ไม่พบเมนูนี้ในระบบ'
        }, 400
    return {
        'success': False,
        'message': 'คุณไม่ใช้เจ้าของร้านค้า'
    }, 400
