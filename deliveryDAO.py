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
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDict(result))

        return returnArray
        
    def findItem(self, id):
        cursor = self.db.cursor()
        sql="select * from delivery where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
            
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into delivery (Item, Type, Quantity, TotPrice) values (%s,%s,%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def update(self, values):
        cursor = self.db.cursor()
        sql="update delivery set Item=%s, Type=%s, Quantity=%s, TotPrice=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()

    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from delivery where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

    def convertToDict(self, result):
        colnames=['id','Item','Type', 'Quantity',"TotPrice"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
        
deliveryDAO = DeliveryDAO()


