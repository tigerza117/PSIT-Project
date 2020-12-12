from datetime import date
from flask import jsonify
from ..models.order import Order
from ..models import db
from . import app, private, required_params
from sqlalchemy import func
from flask.globals import request

@app.route('/orders', methods=['GET'])
@private()
def orders(data):
    print(data)
    orderds = Order().query.all()
    return {'success': True, 'orders': [i.getData() for i in orderds]}, 200

@app.route('/shops/<id>', methods=['PUT'])
@required_params({"note": str})
@private()
def add_order(data, id):
    userID = data["id"]
    body = request.get_json()
    have_order = Order.query.filter(func.DATE(Order.created_at) == date.today(), Order.shop_id==id, Order.customer_id==userID).count()
    if not have_order:
        new_order = Order(
            customer_id=userID,
            shop_id=id, note=body["note"],
            queue='A%02d' % Order.query.filter(func.DATE(Order.created_at) == date.today()).count()
        )
        db.session.add(new_order)
        db.session.commit()
        return {
            'success': True,
            'order': new_order.getData(),
        }, 201
    return {
        'success': False,
        'message': 'you already have order'
    }, 400

@app.route('/shops/<id>/order', methods=['GET'])
@private()
def user_order(data, id):
    # shop = Shop.query.filter_by(id=id).first()
    userID = data["id"]
    order = Order.query.filter(func.DATE(Order.created_at) == date.today(), Order.shop_id==id, Order.customer_id==userID).first()
    if order:
        return {
            'success': True,
            'order': order.getData()
        }, 200
    else:
        return {
            'success': False,
            'message': 'your order not found'
        }, 400
