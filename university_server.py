from flask import Flask, jsonify, request, abort
import pymysql
import mysql.connector
import universityDAO_pymysql as db 
from UniversityDAO import universityDAO 

from flask_cors import CORS


#app = Flask(__name__, static_url_path='', static_folder='.')

app = Flask(__name__)

CORS(app)

@app.route('/')
def index():
        return "Hello Hello"

@app.route('/universities', methods=['GET'])
def get_all_universities():
    universities = universityDAO.getAll()
    return jsonify(universities)


@app.route('/universities/<int:id>', methods=['GET'])
def get_university_by_id(id):
    university = universityDAO.findByID(id)
    
    if university:
        return jsonify(university)
    else:
        return abort(404, description="University not found")

@app.route('/universities', methods=['POST'])
def create_university():
    if not request.json or not 'name' in request.json:
        abort(400, description="Invalid input")
    university = {
        'name': request.json['name'],
        'address': request.json.get('address', ""),
        'number_of_pupils': request.json.get('number_of_pupils', 0)
    }
    created_university = universityDAO.create(university)
    universityDAO.closeAll()
    return jsonify(created_university), 201

@app.route('/universities/<int:id>', methods=['PUT'])
def update_university(id):
    university = universityDAO.findByID(id)
    if not university:
        return abort(404, description="University not found")



    if not request.json:
        abort(400, description="Invalid input")

    university['name'] = request.json.get('name', university['name'])
    university['address'] = request.json.get('address', university['address'])
    university['number_of_pupils'] = request.json.get('number_of_pupils', university['number_of_pupils'])
    universityDAO.update(id, university)
    universityDAO.closeAll()
    return jsonify(university)

@app.route('/universities/<int:id>', methods=['DELETE'])
def delete_university(id):
    university = universityDAO.findByID(id)
    if not university:
        return abort(404, description="University not found")
    universityDAO.delete(id)
    universityDAO.closeAll()
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)