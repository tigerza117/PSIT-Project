from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return "This is home page"

app.run(debug=True)
