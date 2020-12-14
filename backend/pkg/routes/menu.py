from datetime import date
from inspect import Parameter
from os import stat_result
from flask.globals import request
from flask import jsonify
from ..models.shop import Shop
from ..models.menu import Menu
from datetime import date
# from .. models.order_menu import OrderMenu
import mysql.connector
from ..models import db
from . import app, required_params, private
import hashlib
import jwt

@app.route('/shops/<id>/menu', methods=['PUT'])
@required_params({"name": str, "description": str, "price": int, "extra_price": int, "img": str})
@private()
def add_menu(data, id):
    body = request.get_json()
    menu = Menu(
        shop_id = id,
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