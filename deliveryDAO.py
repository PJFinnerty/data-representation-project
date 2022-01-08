import mysql.connector
#import dbconfig as cfg
class DeliveryDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="delivery"
        )
  
    def findAll(self):
        cursor = self.db.cursor()
        sql="select * from delivery"
        cursor.execute(sql)
        results = cursor.fetchall()
        itemArray = []
        print(results)
        for result in results:
            print(result)
            itemArray.append(result)

        return itemArray  
        
    def findItem(self, id):
        cursor = self.db.cursor()
        sql="select * from delivery where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return result

deliveryDAO = DeliveryDAO()


