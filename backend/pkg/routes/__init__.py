

from flask.app import Flask, jsonify, request
from flask.blueprints import Blueprint
from functools import wraps
import jwt

from sqlalchemy.util.langhelpers import NoneType

app = Blueprint('routes', __name__)

def private():
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            auth_header = request.headers.get('Authorization', '')
            if not auth_header:
                return {
                    "status": False,
                    'message': 'Access denied'
                }, 401
            token = auth_header.split()[1]
            user = None
            try:
                user = jwt.decode(token, 'secret', algorithms=['HS256'])
            except (jwt.ExpiredSignature, jwt.InvalidSignatureError):
                return {
                    "status": False,
                    'message': 'Invalid Token'
                }, 401
            return fn(user, *args, **kwargs)
        return wrapper
    return decorator

def required_params(required):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            _json = request.get_json()
            if isinstance(_json, NoneType):
                response = {
                    "status": False,
                    "message": "Request JSON is missing some required params",
                    #"missing": missing
                }
                return jsonify(response), 400
            missing = [r for r in required.keys()
                       if r not in _json]
            if missing:
                response = {
                    "status": False,
                    "message": "Request JSON is missing some required params",
                    #"missing": missing
                }
                return jsonify(response), 400
            wrong_types = [r for r in required.keys()
                           if not isinstance(_json[r], required[r])]
            if wrong_types:
                response = {
                    "status": False,
                    "message": "Data types in the request JSON doesn't match the required format",
                    #"param_types": {k: str(v) for k, v in required.items()}
                }
                return jsonify(response), 400
            return fn(*args, **kwargs)
        return wrapper
    return decorator



def init_app(app: Flask):
    from . import auth, user, order, shop, admin, merchant
    app.register_blueprint(auth.app)
    app.register_blueprint(user.app)
    app.register_blueprint(order.app)
    app.register_blueprint(shop.app)
    app.register_blueprint(admin.app)
    app.register_blueprint(merchant.app)
