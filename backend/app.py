from flask import Flask, render_template, g, jsonify
from flask_cors import CORS
from auth import auth
#routes
app = Flask(__name__)
app.register_blueprint(auth)
CORS(app)
import mysql.connector
mydb = mysql.connector.connect(
  host="103.91.205.130",
  user="trda",
  password="kkgFOpODYIXc1q2S",
  database="trda"
)

@app.before_first_request
def before_first_request():
    # configure the connection pool in the global object
    g.cnx_pool = mydb

@app.route('/')
def home():
    return "This is home page"

if __name__ == '__main__':
  
  app.run(debug=True)
