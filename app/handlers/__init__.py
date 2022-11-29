import json
import hashlib
from . import conection_db

db = conection_db.conection()

def hashear_password(pwd):
    return hashlib.sha256(str(pwd).encode('utf8')).hexdigest()


def validate_password(pwd, pwdHash):    
    return hashear_password(pwd) == pwdHash


def validate_user(user, pwd):
    try:
        cursor = db.cursor()
        sql="""SELECT id, username, password, name, email from users 
                WHERE username = '{}'""".format(user)
        cursor.execute(sql)
        row=cursor.fetchone()
        print(row)
        print(row[2])
        print(hashear_password(pwd))     
        if row[2] == hashear_password(pwd):
            return True            
        else:
            return False
    except Exception as ex:
        raise Exception(ex)

def upload_people():
    people = [
      {
            "fecha": "2022-11-12",
            "nombre": "Gonzalo",
            "apellido": "Gonzalez",
            "dni": "33212188",
            "motivo": "particular",
            "id": 3
      }
    ]
    return people


def select_person(person_id):
    people = [
      {
            "fecha": "2022-11-12",
            "nombre": "Gonzalo",
            "apellido": "Gonzalez",
            "dni": "33212188",
            "motivo": "particular",
            "id": 3
      }
    ]
    for person in people:
        if person['id'] == person_id:
            return person
    return None


def register_person(data):
    people = [
      {
            "fecha": "2022-11-12",
            "nombre": "Gonzalo",
            "apellido": "Gonzalez",
            "dni": "33212188",
            "motivo": "particular",
            "id": 3
      }
    ]   
    if not people:
        new_id = 1
    else:
        new_id = int(max(people, key=lambda x:x['id'])['id']) + 1
    data['id'] = new_id
    people.append(data)
    

def delet_person(person_id):
    person_id= int(person_id)
    people = [
      {
            "fecha": "2022-11-12",
            "nombre": "Gonzalo",
            "apellido": "Gonzalez",
            "dni": "33212188",
            "motivo": "particular",
            "id": 3
      }
    ]  
    people = [p for p in people if p['id'] != person_id]