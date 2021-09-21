import json
from Data_Structures.ABB import ABB
from Analyzer.Parser import parse
from Controller.LoadData import load_student, load_course
from Controller.GenerateReport import make_report
from Controller.StudentContr import create_student, modifi_student, delete_student, get_student
from flask import Flask, jsonify, request


tree_student = ABB()
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
            return {"Exito":"Archivo cargado correctamente"}, 201
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
        return make_report(req, tree_student)
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
        return modifi_student(tree_student, req)
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


if __name__ == '__main__':
    app.run(debug=True)

