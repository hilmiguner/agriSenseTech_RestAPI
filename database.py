import mysql.connector
from hidden_constants import databaseConnectionInformation

def connectDatabase():
    mydb = mysql.connector.connect(**databaseConnectionInformation)
    if mydb.is_connected():
        cursor = mydb.cursor()
        print("Connection successfull")
        return mydb, cursor
    else:
        print("Connection failure!!")
        return -1, -1

def insertUserMessage(title, message, name, email, datetime, fb_local_id):
    try:
        mydb, cursor = connectDatabase()

        query = f"""
            INSERT INTO user_messages(title, message, name, email, datetime, fb_local_id) 
            VALUES ("{title}", "{message}", "{name}", "{email}", "{datetime}", "{fb_local_id}");
        """
        cursor.execute(query)
        mydb.commit()
        return { "status": 200 }
    except Exception as err:
        return { "status": 400, "error": str(err) }
    finally:
        mydb.close()
    
def getWeeds(fb_local_id):
    try:
        mydb, cursor = connectDatabase()

        query = f"""
            SELECT * FROM weeds WHERE fb_local_id='{fb_local_id}';
        """
        cursor.execute(query)

        weedList = cursor.fetchall()

        dataDict = {}
        for weed in weedList:
            dataDict[str(weed[0])] = {}
            dataDict[str(weed[0])]["fb_local_id"] = weed[1]
            dataDict[str(weed[0])]["latitude"] = weed[2]
            dataDict[str(weed[0])]["longitude"] = weed[3]
            dataDict[str(weed[0])]["image_path"] = weed[4]
            dataDict[str(weed[0])]["percentage"] = weed[5]

        return { "status": 200, "data": dataDict }
    except Exception as err:
        return { "status": 400, "error": str(err) }
    finally:
        mydb.close()
    
def deleteWeed(weedID):
    try:
        mydb, cursor = connectDatabase()

        query = f"""
            DELETE FROM weeds WHERE id='{weedID}';
        """
        cursor.execute(query)
        
        mydb.commit()

        return { "status": 200, "data": "Deleting is successful." }
    except Exception as err:
        return { "status": 400, "error": str(err) }
    finally:
        mydb.close()