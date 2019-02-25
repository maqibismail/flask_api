from models import *
from flask import request, jsonify
from encryption import *
import json
from app import app, basic_auth

from config import Config


@app.route('/')
def index():
    return "<h2>Rest API is working....</h2>"


@app.route('/api', methods=['POST'])
def insertStudent():
    student_data_enc = request.data
    student_data_dec = decryption(Config.enc_key, student_data_enc)
    student_json = json.loads(student_data_dec.decode())
    username = student_json['username']
    student = Student.query.get(username)
    if not student:
        password = student_json['password']
        name = student_json['name']
        degree = student_json['degree']
        cgpa = student_json['cgpa']

        s = Student(username, password, name, degree, cgpa)
        db.session.add(s)
        db.session.commit()

        return "Student is added successfully"
    else:
        return "Student already exists"


@app.route('/api/<username>', methods=['GET'])
def getStudent(username):
    student = Student.query.get(username)
    if not student:
        return "Student does not exist"
    else:
        app.config['BASIC_AUTH_USERNAME'] = student.username
        app.config['BASIC_AUTH_PASSWORD'] = student.password
        password_enc = request.data
        password_dec = decryption(Config.enc_key, password_enc)
        password = password_dec.decode()

        if basic_auth.check_credentials(username, password):
            student_schema = StudentSchema()
            result = student_schema.dump(student).data
            result_json = jsonify(result)
            result_str = str(result_json)
            result_bytes = result_str.encode()
            result_enc = encryption(Config.enc_key, result_bytes)
            return result_enc.decode()
        else:
            return "unauthenticated request"


@app.route('/api/<username>', methods=['PUT'])
def updateStudent(username):
    student = Student.query.get(username)
    if not student:
        return "Student does not exist"
    else:
        app.config['BASIC_AUTH_USERNAME'] = student.username
        app.config['BASIC_AUTH_PASSWORD'] = student.password
        student_data_enc = request.data
        student_data_dec = decryption(Config.enc_key, student_data_enc)
        student_json = json.loads(student_data_dec.decode())
        old_password = student_json['old_password']

        if basic_auth.check_credentials(username, old_password):
            new_password = student_json['new_password']
            name = student_json['name']
            degree = student_json['degree']
            cgpa = student_json['cgpa']

            student.password = new_password
            student.name = name
            student.degree = degree
            student.cgpa = cgpa
            db.session.commit()
            return "Student is updated successfully"
        else:
            return "Unauthenticated request"


@app.route('/api/<username>', methods=['DELETE'])
def deleteStudent(username):
    student = Student.query.get(username)
    if not student:
        return "Student does not exist"
    else:
        app.config['BASIC_AUTH_USERNAME'] = student.username
        app.config['BASIC_AUTH_PASSWORD'] = student.password
        password_enc = request.data
        password_dec = decryption(Config.enc_key, password_enc)
        password = password_dec.decode()

        if basic_auth.check_credentials(username, password):
            db.session.delete(student)
            db.session.commit()
            return "Student is deleted successfully"
        else:
            return "Unauthenticated request"


# Main Function
if __name__ == "__main__":
    app.debug = True
    app.run()
    app.run(debug=True)
