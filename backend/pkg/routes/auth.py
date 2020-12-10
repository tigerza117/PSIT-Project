from flask.globals import request
from ..models.user import User
from ..models import db
from . import app, required_params
import datetime
import hashlib
import jwt

@app.route('/login', methods=["POST"])
@required_params({"email": str, "password": str})
def login():
    body = request.get_json()
    email = body['email']
    password = body['password']
    user = User.query.filter_by(email=email).first()
    if user:
        if user.password == hashlib.md5(password.encode('utf-8')).hexdigest():
            encoded_jwt = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, 'secret', algorithm='HS256')
            print(encoded_jwt)
            return {'access_token': encoded_jwt.decode('utf-8')}, 200
        else:
            return {'message': 'email or password wrong'}, 400
    return body

@app.route('/register', methods=["PUT"])
@required_params({"email": str, "password": str, "fname": str, "lname": str})
def register():
    body = request.get_json()
    user = User()
    user.email = body['email']
    user.password = hashlib.md5(body['password'].encode('utf-8')).hexdigest()
    user.fname = body['fname']
    user.lname = body['lname']
    db.session.add(user)
    db.session.commit()
    return {'success': True}, 201