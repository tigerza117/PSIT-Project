from inspect import Parameter
from flask.globals import request
from flask import jsonify
from ..models.shop import Shop
# from ..models.menu import Menu
from ..models import db
from . import app, required_params
import hashlib
import jwt

@app.route('/shops', methods=['GET'])
def get_shops():
    shops = Shop().query.all()
    return jsonify([i.getData() for i in shops])

@app.route('/shops', methods=['PUT'])
def put_shops():
    return {'success': True}, 201

@app.route('/shops/<id>', methods=['GET'])
def get_inshops(id):
    shop = Shop.query.filter_by(id=id).first()
    return shop.getData()

