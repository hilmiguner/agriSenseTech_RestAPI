import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "sumeyra",
    password = "Beyribey216"
) 

cursor = mydb.cursor()

cursor.execute("CREATE DATABASE agrisensetech")

databases = cursor.execute("SHOW DATABASES")

for database in databases:
    print(database)