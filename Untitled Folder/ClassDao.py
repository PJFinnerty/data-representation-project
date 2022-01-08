
import mysql.connector
class Student_xDAO:
    db="root"
    def __init__(self):
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="moviesDB"
        )
        
    def createTable(self, values):
        cursor = self.db.cursor()
        sql = "insert into student_x (name, age) values (%s,%s)"
        cursor.execute(sql, values)
    
        self.db.commit()
        return cursor.lastrowid
    
    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from student_x"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
        
    def findByID(self, id):
        cursor = self.db.cursor()
        sql = "select * from student_x where id = %s"
        values = (id,)
        
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return result
        
    def updateTable(self, values):
        cursor = self.db.cursor()
        sql = "update student_x set name=%s, age=%s where id=%s"
        cursor.execute(sql, values)
        self.db.commit()
    
    def deleteRecord(self, id):
        cursor = self.db.cursor()
        sql="delete from student_x where id=%s"
        values = (id,)
        cursor.execute(sql,values)
        
        self.db.commit()
        print("delete done")
       
student_xDAO = Student_xDAO()



        
    
    