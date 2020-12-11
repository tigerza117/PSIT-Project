import mysql.connector

mydb = mysql.connector.connect(
  host="103.91.205.130",
  user="salmon",
  password="_-.*<:e5w`DqqLJW",
  database="salmon"
)

mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM orders")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

mycursor.execute("SELECT * FROM orders WHERE DATE(created_at) = DATE(NOW())")
myresult = mycursor.fetchall()
print(len(myresult))

# don't use %d