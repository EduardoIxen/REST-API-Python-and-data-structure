import json
from Data_Structures.ABB import ABB
from Analyzer.Parser import parse
from Controller.LoadData import load_student, load_course
from Controller.GenerateReport import make_report
from Controller.StudentContr import create_student, modify_student, delete_student, get_student
from Controller.TaskContr import create_task, modify_task, get_task, delete_task
from Controller.CourseContr import add_course_student, add_course_pensum
from Data_Structures.B_Tree.B_Tree import B_Tree
from flask import Flask, jsonify, request


tree_student = ABB()
tree_pensum = B_Tree(5)
app = Flask(__name__)

@app.route('/')
def index():
    return "Hola mundo"


@app.post("/carga")
def loadFile():
    req = request.json
    if request.is_json:
        f = open(req['path'], "r", encoding="utf-8")
        content = f.read()
        f.close()
        if req['tipo'].lower() == "estudiante":
            lstValues = parse(content)  # analize content file.txt whith ply and return a list of students and tasks
            load_student(tree_student, lstValues)
            return {"Exito":"Archivo de estudiantes y tareas cargado correctamente"}, 201
        elif req['tipo'].lower() == "curso":
            content_to_dic = json.loads(content)
            return load_course(tree_student, content_to_dic)
        else:
            return {"Error":"Tipo incorrecto."}, 400
    return {"error": "Request must be JSON"}, 415


@app.get("/reporte")
def mekeReports():
    req = request.json
    if request.is_json:
        return make_report(req, tree_student, tree_pensum)
    else:
        return {"error": "Request must be JSON"}, 415


@app.post("/estudiante")
def add_student():
    req = request.json
    if request.is_json:
        return create_student(tree_student, req)
    else:
        return {"error": "Request must be JSON"}, 415


@app.put("/estudiante")
def update_student():
    req = request.json
    if request.is_json:
        return modify_student(tree_student, req)
    else:
        return {"error": "Request must be JSON"}, 415


@app.delete("/estudiante")
def del_student():
    req = request.json
    if request.is_json:
        return delete_student(tree_student, req)
    else:
        return {"error": "Request must be JSON"}, 415

@app.get("/estudiante")
def view_student():
    req = request.json
    if request.is_json:
        return get_student(tree_student, req)
    else:
        return {"error": "Request must be JSON"}, 415

@app.post("/recordatorios")
def new_task():
    req = request.json
    if request.is_json:
        return create_task(tree_student, req)
    else:
        return {"error": "Request must be JSON"}, 415

@app.put("/recordatorios")
def update_task():
    req = request.json
    if request.is_json:
        return modify_task(tree_student, req)
    else:
        return {"error": "Request must be JSON"}, 415

@app.get("/recordatorios")
def view_task():
    req = request.json
    if request.is_json:
        return get_task(tree_student, req)
    else:
        return {"error": "Request must be JSON"}, 415

@app.delete("/recordatorios")
def del_task():
    req = request.json
    if request.is_json:
        return delete_task(tree_student, req)
    else:
        return {"error": "Request must be JSON"}, 415

@app.post("/cursosEstudiante")
def add_course():
    req = request.json
    if request.is_json:
        return add_course_student(tree_student, req)
    else:
        return {"error": "Request must be JSON"}, 415


@app.post("/cursosPensum")
def add_course_pe():
    req = request.json
    if request.is_json:
        return add_course_pensum(tree_pensum, req)
    else:
        return {"error": "Request must be JSON"}, 415


if __name__ == '__main__':
    app.run(debug=True, port=3000)
