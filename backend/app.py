from flask import Flask, g
from flask_cors import CORS
from pkg import routes

app = Flask(__name__)

with app.app_context():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://trda:kkgFOpODYIXc1q2S@103.91.205.130/trda'
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    CORS(app)
    routes.init_app(app)
    app.run(debug=True)

@app.route('/')
def home():
    return "hello, world!"
