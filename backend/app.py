from flask import Flask, render_template, g, jsonify
from flask_cors import CORS
#routes
from user.routes import user

app = Flask(__name__)
CORS(app)

import mysql.connector
mydb = mysql.connector.connect(
  host="trda002.mysql.database.azure.com",
  user="trda@trda002",
  password="Tadaohm1234",
  database="userdata"
)

@app.before_first_request
def before_first_request():
    # configure the connection pool in the global object
    g.cnx_pool = mydb

@app.route('/')
def home():
    return render_template('home.html')
# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')

@app.route('/gg')
def gg():
    mycursor = g.cnx_pool.cursor()
    mycursor.execute("SELECT * FROM user")
    columns = [col[0] for col in mycursor.description]
    rows = [dict(zip(columns, row)) for row in mycursor.fetchall()]
    return jsonify(rows)

if __name__ == '__main__':
    app.register_blueprint(user)
    app.run(debug=True, host="0.0.0.0")
