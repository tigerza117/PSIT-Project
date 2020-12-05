import mysql.connector
mydb = mysql.connector.connect(
  host="trda002.mysql.database.azure.com",
  user="trda@trda002",
  password="Tadaohm1234",
  database="userdata"
)

mycursor = mydb.cursor()
