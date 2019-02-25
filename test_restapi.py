import requests
from encryption import *
import json

from config import Config


def test_insertStudent():
    student = '{"username":"BSEF14A548", "password":"12345", "name":"Waleed", "degree":"CS", "cgpa":"3.42"}'
    student_enc = encryption(Config.enc_key, student.encode())
    result = requests.post('http://localhost:5000/api', data=student_enc)
    assert result.text == "Student is added successfully" or result.text == "Student already exists"


def test_getStudent():
    password = "12345"
    password_enc = encryption(Config.enc_key, password.encode())
    result = requests.get('http://localhost:5000/api/BSEF14A548', data=password_enc)
    assert result.status_code == 200 or result.text == "Student does not exist" or result.text == "Unauthenticated request"


def test_updateStudent():
    student = '{"old_password":"12345", "new_password":"6789", "name":"Waleed Ahmed", "degree":"SE", "cgpa":"2.7"}'  # updated student
    student_enc = encryption(Config.enc_key, student.encode())
    result = requests.put('http://localhost:5000/api/BSEF14A548', data=student_enc)
    assert result.text == "Student is updated successfully" or result.text == "Student does not exist" or result.text == "Unauthenticated request"


def test_deleteStudent():
    password = "12345"
    password_enc = encryption(Config.enc_key, password.encode())
    result = requests.delete('http://localhost:5000/api/BSEF14A548', data=password_enc)
    assert result.text == "Student is deleted successfully" or result.text == "Student does not exist" or result.text == "Unauthenticated request"
