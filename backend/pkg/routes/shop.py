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

@app.route('/shops/create', methods=['PUT'])
@required_params({"name": str, "description": str, "owner_id": int, "img": str})
@private()
def creat_shops(data):
    mydb = mysql.connector.connect(
    host="103.91.205.130",
    user="salmon",
    password="_-.*<:e5w`DqqLJW",
    database="salmon"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT id FROM users")
    myresult = mycursor.fetchall()
    body = request.get_json()
    shop = Shop()
    shop.name = body["name"]
    shop.description = body["description"]
    lst = [int(i[0]) for i in myresult]
    if body["owner_id"] not in lst:
        return 'your user not found'
    else:
        shop.owner_id = body["owner_id"]
        shop.img = body["img"]
        db.session.add(shop)
        db.session.commit()
        return {"'success": True}, 201

"""
{
    "email": "helloworld@gmail.com",
    "password": "helloworld"
}

"""