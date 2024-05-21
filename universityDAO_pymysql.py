import pymysql
import dbconfig as cfg

conn = None
def connect():
    global conn
    conn = pymysql.connect(host="localhost", user="root", autocommit=True, password="ashtrA123xyz!", db="primary_schools", cursorclass=pymysql.cursors.DictCursor)



def getAll():
    try:
        if not conn:
            connect()
        sql = "Select * from university"
        with conn.cursor() as cursor:
            cursor.execute(sql)
            x = cursor.fetchall()
            return x
    except pymysql.Error as e:
        print("Error:", e)
        return []



def findByID(id):
    try:
        if not conn:
            connect()
        sql = "SELECT * from university WHERE id = %s "
        with conn.cursor() as cursor:
            cursor.execute(sql, (id))
            x = cursor.fetchall()
            return x
    except pymysql.Error as e:
        print("Error:", e)
        return []



def select_roll(roll):
    try:
        if not conn:
            connect()
        sql = "SELECT * from school WHERE roll_number = %s "
        with conn.cursor() as cursor:
            cursor.execute(sql, (roll))
            x = cursor.fetchall()
            return x
    except pymysql.Error as e:
        print("Error:", e)
        return []
 



