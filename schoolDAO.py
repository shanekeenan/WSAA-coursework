import mysql.connector
import dbconfig as cfg

class SchoolDAO:
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
        sql = "SELECT * FROM school"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))
        self.closeAll()
        return returnArray

    def findByRollNumber(self, roll_number):
        cursor = self.getcursor()
        sql = "SELECT * FROM school WHERE roll_number = %s"
        cursor.execute(sql, (roll_number,))
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def findByCounty(self, county_description):
        cursor = self.getcursor()
        sql = "SELECT * FROM school WHERE county_description = %s"
        cursor.execute(sql, (county_description,))
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))
        self.closeAll()
        return returnArray


    def create(self, school):
        cursor = self.getcursor()
        sql = """
            INSERT INTO school (
                academic_year_enrolment, roll_number, official_name, address_line1, address_line2,
                address_line3, address_line4, county_description, eircode, latitude, longitude, 
                email, phone_number, principal_name, local_authority_description, deis, 
                irish_classification_description, gaeltacht_indicator, island, ethos_description, 
                female, male, total
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            school.get('academic_year_enrolment'),
            school.get('roll_number'),
            school.get('official_name'),
            school.get('address_line1'),
            school.get('address_line2'),
            school.get('address_line3'),
            school.get('address_line4'),
            school.get('county_description'),
            school.get('eircode'),
            school.get('latitude'),
            school.get('longitude'),
            school.get('email'),
            school.get('phone_number'),
            school.get('principal_name'),
            school.get('local_authority_description'),
            school.get('deis'),
            school.get('irish_classification_description'),
            school.get('gaeltacht_indicator'),
            school.get('island'),
            school.get('ethos_description'),
            school.get('female'),
            school.get('male'),
            school.get('total')
        )

        cursor.execute(sql, values)
        self.connection.commit()
        new_roll_number = cursor.lastrowid
        school["roll_number"] = new_roll_number
        self.closeAll()
        return school

    def update(self, roll_number, school):
        cursor = self.getcursor()
        sql = """
            UPDATE school SET academic_year_enrolment = %s,
                roll_number = %s,
                official_name = %s,
                address_line1 = %s,
                address_line2 = %s,
                address_line3 = %s,
                address_line4 = %s,
                county_description = %s,
                eircode = %s,
                latitude = %s,
                longitude = %s,
                email = %s,
                phone_number = %s,
                principal_name = %s,
                local_authority_description = %s,
                deis = %s,
                irish_classification_description = %s,
                gaeltacht_indicator = %s,
                island = %s,
                ethos_description = %s,
                female = %s,
                male = %s,
                total = %s
            WHERE roll_number = %s
        """
        values = (
            school.get('academic_year_enrolment'),
            school.get('roll_number'),
            school.get('official_name'),
            school.get('address_line1'),
            school.get('address_line2'),
            school.get('address_line3'),
            school.get('address_line4'),
            school.get('county_description'),
            school.get('eircode'),
            school.get('latitude'),
            school.get('longitude'),
            school.get('email'),
            school.get('phone_number'),
            school.get('principal_name'),
            school.get('local_authority_description'),
            school.get('deis'),
            school.get('irish_classification_description'),
            school.get('gaeltacht_indicator'),
            school.get('island'),
            school.get('ethos_description'),
            school.get('female'),
            school.get('male'),
            school.get('total'),
            roll_number
        )

        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def delete(self, roll_number):
        cursor = self.getcursor()
        sql = "DELETE FROM school WHERE roll_number = %s"
        cursor.execute(sql, (roll_number,))
        self.connection.commit()
        self.closeAll()
        print("deletion complete")

    def convertToDictionary(self, resultLine):
        keys = [
            'academic_year_enrolment', 'roll_number', 'official_name', 
            'address_line1', 'address_line2', 'address_line3', 'address_line4', 
            'county_description', 'eircode', 'latitude', 'longitude', 'email', 
            'phone_number', 'principal_name', 'local_authority_description', 'deis', 
            'irish_classification_description', 'gaeltacht_indicator', 'island', 
            'ethos_description', 'female', 'male', 'total'
        ]
        school = {}
        currentkey = 0
        for attrib in resultLine:
            school[keys[currentkey]] = attrib
            currentkey += 1
        return school


schoolDAO = SchoolDAO()
