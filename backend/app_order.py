from flask import Flask, render_template, request, redirect, session, url_for, g
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)
app.secret_key = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testorder2.db'
db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable=False)
    firstname = db.Column(db.String(), nullable=False)
    lastname = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return '<Task> %r' %self.id

class Order(db.Model):
    store_id = db.Column(db.Integer, nullable=False)
    queue_id = db.Column(db.Integer, primary_key=True)
    custumer_id = db.Column(db.Integer, nullable=False)
    menu = db.Column(db.String(50), nullable=False)
    extra = db.Column(db.String)

    def __repr__(self):
        return '<Task> %r' %self.store_id



@app.before_request
def before_request():
    users = User.query.order_by(User.id).all()
    if 'user_id' in session:
        user = [i for i in users if i.id == session['user_id']][0]
        g.user = user
    else:
        g.user = None

@app.route("/", methods=['GET'])
def index():
    users = User.query.order_by(User.id).all()
    return render_template('index.html', table=users)

@app.route("/login", methods=['GET', 'POST'])
def login():
    users = User.query.order_by(User.id).all()
    if request.method == 'POST':
        session.pop('user_id', None)
        email = request.form['email']
        password = request.form['password']

        user = [i for i in users if i.email == email]
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
    return redirect("/")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        session.pop('user_id', None)
        email = request.form['email']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        password = request.form['password']
        new_user = User(email=email, firstname=firstname, lastname=lastname, password=password)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect("/")
        except:
            return "Error"
    return render_template("register.html")

@app.route("/delete/<int:id>")
def delete(id):
    user_delete = User.query.get_or_404(id)
    try:
        db.session.delete(user_delete)
        db.session.commit()
        return redirect("/")
    except:
        return "There was an error with delete"

@app.route("/queue", methods=['GET'])
def queue():
    order_queue = Order.query.order_by(Order.queue_id).all()
    return render_template('queue.html', table=order_queue)

@app.route("/queue_store/<int:store_id>", methods=['GET'])
def queue_store(store_id):
    order_queue = Order.query.order_by(Order.queue_id).all()
    return render_template('queue_store.html', table=order_queue, check=store_id)

@app.route("/order", methods=['GET', 'POST'])
def order():
    if not g.user:
        return redirect("/login")
    if request.method == 'POST':
        store_id = request.form['store_id']
        custumer_id = g.user.id
        menu = request.form['menu']
        extra = request.form['extra']
        new_order = Order(store_id=store_id, custumer_id=custumer_id, menu=menu, extra=extra)
        try:
            db.session.add(new_order)
            db.session.commit()
            return redirect("/queue")
        except:
            return "Error Ordering Food"
    return render_template('order.html')


if __name__ == "__main__":
    app.run(debug=True)
