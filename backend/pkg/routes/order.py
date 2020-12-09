from inspect import Parameter
from flask.globals import request
from flask import jsonify
from ..models.order import Order
from ..models import db
from . import app, required_params
import hashlib
import jwt

@app.route('/orders')
def orders():
    orderds = Order().query.all()
    for i in orderds:
        print(i.getData())
    return jsonify([i.getData() for i in orderds])

# def login():
#     body = request.get_json()
#     email = body['email']
#     password = body['password']
#     user = erUs.query.filter_by(email=email).first()
#     if user:
#         if user.password == hashlib.md5(password.encode('utf-8')).hexdigest():
#             encoded_jwt = jwt.encode({'user': user.id}, 'secret', algorithm='HS256')
#             print(encoded_jwt)
#             return {'access_token': encoded_jwt.decode('utf-8')}, 200
#         else:
#             return {'message': 'email or password wrong'}, 400
#     return body

# @app.route('/register')
# @required_params({"email": str, "password": str, "fname": str, "lname": str})
# def register():
#     body = request.get_json()
#     user = User()
#     user.email = body['email']
#     user.password = hashlib.md5(body['password'].encode('utf-8')).hexdigest()
#     user.name = body['fname']
#     db.session.add(user)
#     db.session.commit()
#     return {'success': True}, 201