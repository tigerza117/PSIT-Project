from flask import Flask, g
from flask_cors import CORS
from pkg import routes

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "hello, world!"

with app.app_context():

    app.config['SQLALCHEMY_DATABASE_URI'] = ''
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    routes.init_app(app)
app.run(debug=True, host='0.0.0.0')
