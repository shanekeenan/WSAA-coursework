

from flask import Flask, jsonify, request, abort
import mysql.connector
import dbconfig as cfg

class UniversityDAO:
    connection = None
    cursor = None

    def __init__(self):
        self.connection = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['user'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database']
        )
        self.cursor = self.connection.cursor()

   

    def closeAll(self):
        self.cursor.close()
        self.connection.close()

    def getAll(self):
        sql = "SELECT * FROM university"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))
        return returnArray

    def findByID(self, id):
        sql = "SELECT * FROM university WHERE ID = %s"
        self.cursor.execute(sql, (id,))
        result = self.cursor.fetchone()
        return self.convertToDictionary(result) if result else None

    def create(self, university):
        sql = "INSERT INTO university (name, address, number_of_pupils) VALUES (%s, %s, %s)"
        values = (university.get("name"), university.get("address"), university.get("number_of_pupils"))
        self.cursor.execute(sql, values)
        self.connection.commit()
        new_id = self.cursor.lastrowid
        university["ID"] = new_id
        return university

    def update(self, id, university):
        sql = "UPDATE university SET name = %s, address = %s, number_of_pupils = %s WHERE ID = %s"
        values = (university.get("name"), university.get("address"), university.get("number_of_pupils"), id)
        self.cursor.execute(sql, values)
        self.connection.commit()

    def delete(self, id):
        sql = "DELETE FROM university WHERE ID = %s"
        self.cursor.execute(sql, (id,))
        self.connection.commit()

    def convertToDictionary(self, resultLine):
        if not resultLine:
            return None
        keys = ['ID', 'name', 'address', 'number_of_pupils']
        return {keys[i]: resultLine[i] for i in range(len(keys))}


universityDAO = UniversityDAO()