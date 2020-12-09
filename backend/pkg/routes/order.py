from inspect import Parameter
from flask.globals import request
from flask import jsonify
from ..models.order import Order
from ..models import db
from . import app, required_params
import hashlib
import jwt

@app.route('/orders', methods=['GET'])
def orders():
    orderds = Order().query.all()
    return jsonify([i.getData() for i in orderds])

@app.route('/orders', methods=['PUT'])
def put_order():
    return {'success': True}, 201
