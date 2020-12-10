from flask import jsonify
from ..models.order import Order
from ..models import db
from . import app, private

@app.route('/orders', methods=['GET'])
@private()
def orders(data):
    print(data)
    orderds = Order().query.all()
    return jsonify([i.getData() for i in orderds])

@app.route('/orders', methods=['PUT'])
@private()
def put_order(data):
    print(data)
    return {'success': True}, 201
