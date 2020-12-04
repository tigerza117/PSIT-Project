from flask import Flask, render_template, request, redirect, session, url_for, g
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)
app.secret_key = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testlogin.db'
db = SQLAlchemy(app)



class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return "<User: %s>" %self.username

class Sign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<Task> %r' %self.id



users = []
users.append(User(id=1, username='kaho', password='1910'))
users.append(User(id=2, username='hima', password='1234'))
users.append(User(id=3, username='jpan', password='1911'))



@app.before_request
def before_request():
    if 'user_id' in session:
        user = [i for i in users if i.id == session['user_id']][0]
        g.user = user
    else:
        g.user = None

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']

        user = [i for i in users if i.username == username]
        if user:
            user = user[0]
        else:
            return redirect('/login')
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect("/profile")
    return render_template("login.html")

@app.route("/profile")
def profile():
    if not g.user:
        return redirect("/login")
    return render_template("profile.html")

@app.route("/logout")
def logout():
    session.pop('user_id', None)
    return redirect("/login")

@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
