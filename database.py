import mysql.connector
from hidden_constants import databaseConnectionInformation

mydb = mysql.connector.connect(**databaseConnectionInformation)
if mydb.is_connected():
    print("Connection successfull")
else:
    print("Connection failure!!")

cursor = mydb.cursor()

def insertUserMessage(title, message, name, email, datetime, fb_local_id):
    try:
        query = f"""
            INSERT INTO user_messages(title, message, name, email, datetime, fb_local_id) 
            VALUES ("{title}", "{message}", "{name}", "{email}", "{datetime}", "{fb_local_id}");
        """
        cursor.execute(query)
        mydb.commit()
        return { "status": 200 }
    except Exception as err:
        return { "status": 400, "error": str(err) }
    