from inspect import Parameter
from flask.globals import request
from flask import jsonify
from ..models.shop import Shop
from ..models.menu import Menu
from ..models.order import Order
from ..models import db
from . import app, required_params, private
import hashlib
import jwt

@app.route('/shops', methods=['GET'])
@private()
def get_shops(data):
    shops = Shop().query.all()
    return jsonify([i.getData() for i in shops])

@app.route('/shops', methods=['PUT'])
@private()
def put_shops(data):
    return {'success': True}, 201

@app.route('/shops/<id>', methods=['GET'])
@private()
def get_inshops(data, id):
    shop = Shop.query.filter_by(id=id).first()
    menus = Menu.query.filter_by(shop_id=id)
    order = Order.query.filter_by(shop_id=id, status='waiting').first()
    queue = {'queue': 'close'}
    if order != None: 
        queue = order.get('queue')
    result = shop.get('name')
    result.update({'menus': [i.get('name', 'price', 'extra_price', 'category') for i in menus]})
    result.update(queue)
    # print(result)
    return result

