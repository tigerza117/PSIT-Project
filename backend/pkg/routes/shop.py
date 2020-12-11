from inspect import Parameter
from os import stat_result
from flask.globals import request
from flask import jsonify
from ..models.shop import Shop
from ..models.menu import Menu
from ..models.order import Order
# from .. models.order_menu import OrderMenu
import mysql.connector
from ..models import db
from . import app, required_params, private
import hashlib
import jwt

mydb = mysql.connector.connect(
  host="103.91.205.130",
  user="salmon",
  password="_-.*<:e5w`DqqLJW",
  database="salmon"
)

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

@app.route('/shops/<id>', methods=['PUT'])
@required_params({"note": str, "queue": str, "status": str})
@private()
def put_inshops(data, id):
    userID = 5
    print(data)
    body = request.get_json()
    order = Order()
    body.update({"customer_id": userID})
    body.update({"shop_id": id})
    order.customer_id = body["customer_id"]
    order.shop_id = body["shop_id"]
    order.note = body["note"]
    order.queue = body["queue"]
    order.status = body["status"]
    db.session.add(order)
    db.session.commit()
    return {'success': True}, 201


"""
{
    "customer_id": 1,
    "note": "ไม่เอาอะไรเลย",
    "queue": "A4",
    "status": "ordering"
}

"""