from datetime import date
from inspect import Parameter
from os import stat_result
from flask.globals import request
from flask import jsonify
from ..models.shop import Shop
from ..models.menu import Menu
from ..models.category import Category
from datetime import date
# from .. models.order_menu import OrderMenu
import mysql.connector
from ..models import db
from . import app, required_params, private
import hashlib
import jwt

@app.route('/shops/<id>/menu', methods=['PUT'])
@required_params({"name": str, "price": int, "extra_price": int, "category": str, "img": str})
@private()
def put_newmenu(data, id):
    body = request.get_json()
    menu = Menu()
    menu.shop_id = id
    menu.name = body["name"]
    menu.price = body["price"]
    menu.extra_price = body["extra_price"]
    mydb = mysql.connector.connect(
    host="103.91.205.130",
    user="salmon",
    password="_-.*<:e5w`DqqLJW",
    database="salmon"
    )
    mycursor = mydb.cursor()
    sql = "SELECT id FROM categorys WHERE shop_id = %s and name = %s"
    val = (str(id), str(body["category"]), )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    lst = [i for i in myresult]
    print(lst)
    if lst != []:
        menu.category_id = lst[0]
        menu.img = body["img"]
        db.session.add(menu)
        db.session.commit()
        return {'success': True}, 201
    elif lst == []:
        category = Category()
        category.shop_id = id
        category.name = body["category"]
        db.session.add(category)
        db.session.commit()
        lst1 = checkforput_menu(id, body["category"])
        menu.category_id = lst1[0]
        menu.img = body["img"]
        db.session.add(menu)
        db.session.commit()
        return {'success2': True}, 201

def checkforput_menu(id, category):
    mydb = mysql.connector.connect(
    host="103.91.205.130",
    user="salmon",
    password="_-.*<:e5w`DqqLJW",
    database="salmon"
    )
    mycursor = mydb.cursor()
    sql2 = "SELECT id FROM categorys WHERE shop_id = %s and name = %s"
    val2 = (str(id), str(category), )
    mycursor.execute(sql2, val2)
    myresults = mycursor.fetchall()
    lst1 = [i for i in myresults]
    return lst1