import mysql.connector
import hashlib
mydb = mysql.connector.connect(
  host="103.91.205.130",
  user="trda",
  password="kkgFOpODYIXc1q2S",
  database="trda"
)

mycursor = mydb.cursor()


# sql = "DROP TABLE users"

# mycursor.execute(sql)

# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#   print(x)

# """" test add data to table """
# sql = "INSERT INTO userdata (name, email, password) VALUES (%s, %s, %s)"
# val = (input(), input(), (hashlib.md5(input().encode())).hexdigest())
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")


""" look around data from table"""
mycursor.execute("SELECT *")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)