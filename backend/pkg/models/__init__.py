from flask.globals import current_app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(current_app)