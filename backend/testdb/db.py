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

sql = "INSERT INTO `uesrs` (`fname`, `lname`, `password`, `email`) VALUES (%s, %s, %s, %s)"
val = (input(), input(), input(), input())
mycursor.execute(sql, val)

mydb.commit()

# don't use %d