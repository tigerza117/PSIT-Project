from flask import Flask, Blueprint
from user.models import User
from . import user
import uuid

# @user.route('/user/signup', methods=['PUT'])
# def signup():
#     return User().signup()

@user.route('/user/get', methods=['GET'])
def get_userdata():
    return User().signup()

@user.route('/users')
def get_users():
   return User().checking()