import json
from Data_Structures.ABB import ABB
from Analyzer.Parser import parse
from Controller.LoadData import load_student, load_course, load_student_frontend
from Controller.GenerateReport import make_report
from Controller.StudentContr import create_student, modify_student, delete_student, get_student, login_controller
from Controller.TaskContr import create_task, modify_task, get_task, delete_task
from Controller.CourseContr import add_course_student, add_course_pensum
from Data_Structures.B_Tree.B_Tree import B_Tree
from Data_Structures.Hash_Table.Hash_Table import Hash_Table
from Controller.NotesController import loadNotes, newNote, notes_student
from flask import Flask, jsonify, request
from flask_cors import CORS



tree_student = ABB()
tree_pensum = B_Tree(5)
table_notes = Hash_Table(7)
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hola mundo"


@app.post("/carga")
def loadFile():
    req = request.json
    if request.is_json:
        if req['path'] == "":
            content_to_dic = json.loads(req['contenido'])
            if req['tipo'] == "estudiante":
                load_student_frontend(tree_student, content_to_dic)
                #load_student(tree_student, content_to_dic)
                return {"message": "Archivo de estudiantes y tareas cargado correctamente"}, 201
            elif req['tipo'] == "curso":
                return load_course(tree_student, content_to_dic)
        else:
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
    return {"message": "Request must be JSON"}, 415


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
        print("llego", req)
        return create_student(tree_student, req)
    else:
        return {"message": "Request must be JSON"}, 415


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
        return {"message": "Request must be JSON"}, 415

@app.post("/login")
def login():
    req = request.json
    if request.is_json:
        print("usuario:",req["user"])
        print("contra:",req["password"])
        #return jsonify({'message':'Logeado correctemente'}), 200
        return login_controller(tree_student, req)

@app.post("/loadNotes")
def loadFileNotes():
    req = request.json
    if request.is_json:
        return loadNotes(req["contenido"], table_notes)
    return {"message":"Request must be JSON"}, 415

@app.post("/newNote")
def new_note():
    req = request.json
    if request.is_json:
        return newNote(req, table_notes)
    return {"message":"Request must be JSON"}, 415

@app.get("/notesStudent/<id_student>")
def view_notes(id_student):
    print(id_student)
    return notes_student(id_student, table_notes)



if __name__ == '__main__':
    app.run(debug=True, port=3000)
