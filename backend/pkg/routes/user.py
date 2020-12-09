from flask.globals import request, session
from ..models.user import User
from ..models import db
from . import app, private

@app.route('/profile', methods=['GET'])
@private()
def profile(data):
    user = getUser(data['user'])
    return user.getData()

def getUser(id: int) -> User:
    return User.query.filter_by(id=id).first()