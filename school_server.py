from flask import Flask, jsonify, request, abort
import pymysql
import mysql.connector
from SchoolDAO import schoolDAO 
from flask_cors import CORS


#app = Flask(__name__, static_url_path='', static_folder='.')

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
        return "Hello Hello"

@app.route('/schools', methods=['GET'])
def get_all_schools():
    schools = schoolDAO.getAll()
    return jsonify(schools)


@app.route('/schools/<int:id>', methods=['GET'])
def get_school_by_rollNumber(id):
    school = schoolDAO.findByRollNumber(id)
    
    if school:
        return jsonify(school)
    else:
        return abort(404, description="school not found")
    

@app.route('/schools/<string:county_description>', methods=['GET'])
def get_schools_by_county(county_description):
    schools = schoolDAO.findByCounty(county_description)
    
    if schools:
        return jsonify(schools)
    else:
        return abort(404, description="Schools not found")





@app.route('/schools', methods=['POST'])
def create_school():
    if not request.json or not 'name' in request.json:
        abort(400, description="Invalid input")
    school = {
    'academic_year_enrolment': request.json.get('academic_year_enrolment', ""),
    'roll_number': request.json.get('roll_number', ""),
    'official_name': request.json.get('official_name', ""),
    'address_line1': request.json.get('address_line1', ""),
    'address_line2': request.json.get('address_line2', ""),
    'address_line3': request.json.get('address_line3', ""),
    'address_line4': request.json.get('address_line4', ""),
    'county_description': request.json.get('county_description', ""),
    'eircode': request.json.get('eircode', ""),
    'latitude': request.json.get('latitude', ""),
    'longitude': request.json.get('longitude', ""),
    'email': request.json.get('email', ""),
    'phone_number': request.json.get('phone_number', ""),
    'principal_name': request.json.get('principal_name', ""),
    'local_authority_description': request.json.get('local_authority_description', ""),
    'deis': request.json.get('deis', ""),
    'irish_classification_description': request.json.get('irish_classification_description', ""),
    'gaeltacht_indicator': request.json.get('gaeltacht_indicator', ""),
    'island': request.json.get('island', ""),
    'ethos_description': request.json.get('ethos_description', ""),
    'female': request.json.get('female', ""),
    'male': request.json.get('male', ""),
    'total': request.json.get('total', "")
    }

    created_school = schoolDAO.create(school)
    schoolDAO.closeAll()
    return jsonify(created_school), 201

@app.route('/schools/<int:id>', methods=['PUT'])
def update_school(id):
    school = schoolDAO.findByID(id)
    if not school:
        return abort(404, description="school not found")

    if not request.json:
        abort(400, description="Invalid input")

    school['academic_year_enrolment'] = request.json.get('academic_year_enrolment', school.get('academic_year_enrolment', ""))
    school['roll_number'] = request.json.get('roll_number', school.get('roll_number', ""))
    school['official_name'] = request.json.get('official_name', school.get('official_name', ""))
    school['address_line1'] = request.json.get('address_line1', school.get('address_line1', ""))
    school['address_line2'] = request.json.get('address_line2', school.get('address_line2', ""))
    school['address_line3'] = request.json.get('address_line3', school.get('address_line3', ""))
    school['address_line4'] = request.json.get('address_line4', school.get('address_line4', ""))
    school['county_description'] = request.json.get('county_description', school.get('county_description', ""))
    school['eircode'] = request.json.get('eircode', school.get('eircode', ""))
    school['latitude'] = request.json.get('latitude', school.get('latitude', ""))
    school['longitude'] = request.json.get('longitude', school.get('longitude', ""))
    school['email'] = request.json.get('email', school.get('email', ""))
    school['phone_number'] = request.json.get('phone_number', school.get('phone_number', ""))
    school['principal_name'] = request.json.get('principal_name', school.get('principal_name', ""))
    school['local_authority_description'] = request.json.get('local_authority_description', school.get('local_authority_description', ""))
    school['deis'] = request.json.get('deis', school.get('deis', ""))
    school['irish_classification_description'] = request.json.get('irish_classification_description', school.get('irish_classification_description', ""))
    school['gaeltacht_indicator'] = request.json.get('gaeltacht_indicator', school.get('gaeltacht_indicator', ""))
    school['island'] = request.json.get('island', school.get('island', ""))
    school['ethos_description'] = request.json.get('ethos_description', school.get('ethos_description', ""))
    school['female'] = request.json.get('female', school.get('female', ""))
    school['male'] = request.json.get('male', school.get('male', ""))
    school['total'] = request.json.get('total', school.get('total', ""))
    
    schoolDAO.update(id, school)
    schoolDAO.closeAll()
    return jsonify(school)



@app.route('/schools/<int:id>', methods=['DELETE'])
def delete_school(id):
    school = schoolDAO.findByID(id)
    if not school:
        return abort(404, description="school not found")
    schoolDAO.delete(id)
    schoolDAO.closeAll()
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)