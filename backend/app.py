from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
my_db = SQLAlchemy(app)



class Todo(my_db.Model):
    id = my_db.Column(my_db.Integer, primary_key=True)
    content = my_db.Column(my_db.String(200), nullable=False)
    date_created = my_db.Column(my_db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<Task> %r' %self.id



@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        try:
            my_db.session.add(new_task)
            my_db.session.commit()
            return redirect("/")
        except:
            return "There was an error with post"
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('indexforapp.html', tasks=tasks)

@app.route("/delete/<int:id>")
def delete(id):
    task_del = Todo.query.get_or_404(id)
    try:
        my_db.session.delete(task_del)
        my_db.session.commit()
        return redirect("/")
    except:
        return "There was an error with delete"

@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    task_update = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task_update.content = request.form['content']
        try:
            my_db.session.commit()
            return redirect("/")
        except:
            return "There was an error with update"
    else:
        return render_template('update.html', task=task_update)

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)