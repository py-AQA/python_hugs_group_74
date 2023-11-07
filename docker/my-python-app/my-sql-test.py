import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="my_db"
)

cur = mydb.cursor()
cur.execute("SELECT * FROM user")
r = cur.fetchall()
for row in r:
    print(row)
