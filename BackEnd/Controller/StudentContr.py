from datetime import date
from BackEnd.Obj.Student import Student
from BackEnd.Data_Structures.List_Year import List_Year
from BackEnd.Encryption.HashPassword import HashPassword
from BackEnd.Encryption.Encryption import Encryption


def create_student(tree_student, req, listTransactionStudent):
    key = "x80AlrHftQ_8Qmh3PbRCPi3BH5SdeX-PBOybGohwCgQ="
    enctyption = Encryption()
    dpi = enctyption.encrypt(key, str(req['DPI']))
    name = enctyption.encrypt(key, str(req['nombre']))
    degree = enctyption.encrypt(key, str(req['carrera']))
    email = enctyption.encrypt(key, str(req['correo']))
    hash_pass = HashPassword(str(req['password']))
    password = enctyption.encrypt(key, hash_pass.Hash())
    credits = enctyption.encrypt(key, str(req['creditos']))
    age = enctyption.encrypt(key, str(req['edad']))
    tree_student.insert(Student(str(req['carnet']), dpi, name, degree, email, password
                                , credits, age, List_Year()))
    today = date.today()
    data = str(req['DPI']) + today.strftime("%d/%m/%Y") + str(req['carnet']) + req['correo']
    hash_data = HashPassword(data)
    listTransactionStudent.append(hash_data.Hash())

    return {"message":"Estudiante creado correctamente"}, 201


def modify_student(tree_student, req):
    node_student = tree_student.search(req['carnet'])
    if node_student is None:
        return {"Warning": f"Estudiante no encontrado -> {req['carnet']}"}, 404
    node_student.student.age = req['edad']
    node_student.student.carnet = req['carnet']
    node_student.student.credits = req['creditos']
    node_student.student.degree = req['carrera']
    node_student.student.dpi = req['DPI']
    node_student.student.email = req['correo']
    node_student.student.name = req['nombre']
    node_student.student.password = req['password']
    return {"Exito": f"Estudiante midificado correctamente."}, 200


def delete_student(tree_student, req):
    if tree_student.search(req['carnet']) is None:
        return {"Warning": f"Estudiante no encontrado -> {req['carnet']}"}, 404
    tree_student.delete_student(req['carnet'])
    tree_student.balance_tree()
    return {"Exito": f"Estudiante eliminado."}, 200


def get_student(tree_student, req):
    node_student = tree_student.search(req['carnet'])
    if node_student is None:
        return {"message": f"Estudiante no encontrado -> {req['carnet']}"}, 404

    student_found = node_student.student
    return {"Carnet":f"{student_found.carnet}",
            "DPI":f"{student_found.dpi}",
            "Nombre":f"{student_found.name}",
            "Carrera":f"{student_found.degree}",
            "Correo":f"{student_found.email}",
            "Password":f"{student_found.password}",
            "Creditos":f"{student_found.credits}",
            "Edad":f"{student_found.age}"
            }

def login_controller(tree_student, req):
    encrypt = Encryption()
    if req['user'] == "admin" and req['password'] == "admin":
        return {'message': 'Bienvenido admin', 'type':'admin', }, 200
    else:
        hash_pass = HashPassword(str(req['password']))
        login_result = tree_student.search_login(tree_student.root, req['user'], hash_pass.Hash())
        if login_result:
            student = tree_student.search(str(req['user'])).student
            return {'message': 'Bienvenido estudiante',
                    'type': 'student',
                    "token": str(encrypt.decrypt("x80AlrHftQ_8Qmh3PbRCPi3BH5SdeX-PBOybGohwCgQ=", student.name).decode() +
                                 encrypt.decrypt("x80AlrHftQ_8Qmh3PbRCPi3BH5SdeX-PBOybGohwCgQ=", student.dpi).decode()),
                    "user": {
                        "carnet": student.carnet,
                        "dpi": encrypt.decrypt("x80AlrHftQ_8Qmh3PbRCPi3BH5SdeX-PBOybGohwCgQ=", student.dpi).decode(),
                        "name": encrypt.decrypt("x80AlrHftQ_8Qmh3PbRCPi3BH5SdeX-PBOybGohwCgQ=", student.name).decode(),
                        "email": encrypt.decrypt("x80AlrHftQ_8Qmh3PbRCPi3BH5SdeX-PBOybGohwCgQ=", student.email).decode(),
                        "credits": "0",
                        "degree": encrypt.decrypt("x80AlrHftQ_8Qmh3PbRCPi3BH5SdeX-PBOybGohwCgQ=", student.degree).decode(),
                        "age": encrypt.decrypt("x80AlrHftQ_8Qmh3PbRCPi3BH5SdeX-PBOybGohwCgQ=", student.age).decode()
                    }
                    }, 200
        else:
            return {'message':'Usuario o contraseña incorrectos.'}, 400
