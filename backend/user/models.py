from flask import Flask,jsonify,request, g
# from passlib.hash import pbkdf2_sha256
import uuid
import mysql.connector
class User:
    def checking(self):
        mycursor = g.cnx_pool.cursor()
        mycursor.execute("SELECT * FROM user")
        columns = [col[0] for col in mycursor.description]
        rows = [dict(zip(columns, row)) for row in mycursor.fetchall()]
        return jsonify(rows)


    def signup(self):
        print(request.form)
    
    # create user object
        user = {
            '_id':uuid.uuid4().hex,
            'name':request.form.get('name'),
            'email':request.form.get('email'),
            'password':request.form.get('password')
        }
    # encrypt pass
        # user['password'] = pbkdf2_sha256.encrypt(user['password'])

        return jsonify(user), 200
