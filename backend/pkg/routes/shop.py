from datetime import date
from inspect import Parameter
from os import stat_result
from flask.globals import request
from flask import jsonify
from ..models.shop import Shop
from ..models.menu import Menu
from ..models.order import Order
from datetime import date
# from .. models.order_menu import OrderMenu
import mysql.connector
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

@app.route('/shops/<id>', methods=['PUT'])
@required_params({"note": str})
@private()
def put_inshops(data, id):
    userID = data["id"]
    print(data)
    mydb = mysql.connector.connect(
    host="103.91.205.130",
    user="salmon",
    password="_-.*<:e5w`DqqLJW",
    database="salmon"
    )
    mycursor = mydb.cursor()
    body = request.get_json()
    order = Order()
    body.update({"customer_id": userID})
    body.update({"shop_id": id})
    order.customer_id = body["customer_id"]
    order.shop_id = body["shop_id"]
    order.note = body["note"]
    mycursor.execute("SELECT * FROM orders WHERE DATE(created_at) = DATE(NOW()) and customer_id = %s and shop_id = %s" %(userID,id))
    myresult = mycursor.fetchall()
    print(len(myresult))
    if len(myresult) == 0:
        """queue path"""
        mycursor.execute("SELECT * FROM orders WHERE DATE(created_at) = DATE(NOW())")
        result = mycursor.fetchall()
        body.update({"queue": 'A'+str(len(result))})
        order.queue = body["queue"]
        """queue path"""
    else:
        return 'You have order now'
    order.status = 'ordering'
    db.session.add(order)
    db.session.commit()
    return {'success': True}, 201

@app.route('/shops/<id>/order', methods=['GET'])
@private()
def user_orderonshop(data, id):
    # shop = Shop.query.filter_by(id=id).first()
    userID = data["id"]
    mydb = mysql.connector.connect(
    host="103.91.205.130",
    user="salmon",
    password="_-.*<:e5w`DqqLJW",
    database="salmon"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT queue, note FROM orders WHERE DATE(created_at) = DATE(NOW()) and customer_id = %s and shop_id = %s" %(userID,id))
    myresult = mycursor.fetchall()
    if myresult != None:
        lst = [i for i in myresult]
        print(lst)
        dicts = {'queue': lst[0][0], 'note': lst[0][1]}
        return dicts
    else:
        return 'your order not found'


"""
{
    "email": "helloworld@gmail.com",
    "password": "helloworld"
}

"""