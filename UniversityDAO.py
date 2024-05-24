


import mysql.connector
import dbconfig as cfg

class UniversityDAO:
    connection = ""
    cursor = ''
    host = ''
    user = ''
    password = ''
    database = ''

    def __init__(self):
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']

    def getcursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.cursor.close()
        self.connection.close()

    def getAll(self):
        cursor = self.getcursor()
        sql = "SELECT * FROM university"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))
        self.closeAll()
        return returnArray

    def findByID(self, id):
        cursor = self.getcursor()
        sql = "SELECT * FROM university WHERE ID = %s"
        cursor.execute(sql, (id,))
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def create(self, university):
        cursor = self.getcursor()
        sql = "INSERT INTO university (name, address, number_of_pupils) VALUES (%s, %s, %s)"
        values = (university.get("name"), university.get("address"), university.get("number_of_pupils"))
        cursor.execute(sql, values)
        self.connection.commit()
        new_id = cursor.lastrowid
        university["ID"] = new_id
        self.closeAll()
        return university

    def update(self, id, university):
        cursor = self.getcursor()
        sql = "UPDATE university SET name = %s, address = %s, number_of_pupils = %s WHERE ID = %s"
        values = (university.get("name"), university.get("address"), university.get("number_of_pupils"), id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def delete(self, id):
        cursor = self.getcursor()
        sql = "DELETE FROM university WHERE ID = %s"
        cursor.execute(sql, (id,))
        self.connection.commit()
        self.closeAll()
        print("deletion complete")

    def convertToDictionary(self, resultLine):
        keys = ['ID', 'name', 'address', 'number_of_pupils']
        university = {}
        currentkey = 0
        for attrib in resultLine:
            university[keys[currentkey]] = attrib
            currentkey += 1
        return university

universityDAO = UniversityDAO()
