import mysql.connector
from hidden_constants import databaseConnectionInformation

mydb = mysql.connector.connect(**databaseConnectionInformation)
if mydb.is_connected():
    print("Connection successfull")
else:
    print("Connection failure!!")

cursor = mydb.cursor()

cursor.execute("CREATE DATABASE agrisensetech")

databases = cursor.execute("SHOW DATABASES")

for database in databases:
    print(database)