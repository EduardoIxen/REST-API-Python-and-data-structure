import json
from Data_Structures.ABB import ABB
from Data_Structures.Grafo.Grafo import Grafo
from Graph.Pensum_Graph import Pensum_Graph
from Analyzer.Parser import parse
from Controller.LoadData import load_student, load_course, load_student_frontend, getListCrypted, getListDecrypted
from Controller.GenerateReport import make_report
from Controller.StudentContr import create_student, modify_student, delete_student, get_student, login_controller
from Controller.TaskContr import create_task, modify_task, get_task, delete_task
from Controller.CourseContr import add_course_student, add_course_pensum, add_course_graph
from Data_Structures.B_Tree.B_Tree import B_Tree
from Data_Structures.Hash_Table.Hash_Table import Hash_Table
from Controller.NotesController import loadNotes, newNote, notes_student, generateGrah
from BackEnd.Graph.BTree_Graph import graphTree
from Data_Structures.Merkle_Tree.Merkle_Tree import MerkleTree
from flask import Flask, jsonify, request
from flask_cors import CORS
from graphviz import Digraph



tree_student = ABB()
tree_pensum = B_Tree(5)
graph_pensum = Grafo()
graph_search = Grafo()
table_notes = Hash_Table(7)
listTransactionStudent = []
listTransactionCourses = []
listTransactionNotes = []
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
                load_student_frontend(tree_student, content_to_dic, "x80AlrHftQ_8Qmh3PbRCPi3BH5SdeX-PBOybGohwCgQ=", listTransactionStudent)
                return {"message": "Archivo de estudiantes cargado correctamente"}, 201
            elif req['tipo'] == "curso":
                return load_course(tree_student, content_to_dic, listTransactionCourses)
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
        return {"message": "Request must be JSON"}, 415

@app.post("/reportCourseStd")
def report_course_student():
    req = request.json
    if request.is_json:

        node_student = tree_student.search(req['carnet'])
        if node_student is None:
            return {"message": "Estudiante no encontrado."}, 404
        get_year = node_student.student.list_year.search(int(req['year']))
        if get_year is None:
            return {"message": "Año no encontrado."}, 404
        get_semester = get_year.data.list_semesters.search(str(req['semestre']))
        if get_semester is None:
            return {"message": "Semestre no encontrado."}, 404
        if get_semester.data.binary_tree.root.count == 0:
            return {"message": "Arbol de cursos vacio."}, 404
        graphTree(get_semester.data.binary_tree.root, f"DEL ESTUDIANTE {req['carnet']}")
        return {"message": "Arbol de cursos generado correctamente."}, 201
    else:
        return {"message": "Request must be JSON"}, 415


@app.post("/estudiante")
def add_student():
    req = request.json
    if request.is_json:
        return create_student(tree_student, req, listTransactionStudent)
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
        return add_course_student(tree_student, req, listTransactionCourses)
    else:
        return {"message": "Request must be JSON"}, 415


@app.post("/cursosPensum")
def add_course_pe():
    req = request.json
    if request.is_json:
        add_course_pensum(tree_pensum, req)
        add_course_graph(req, graph_pensum, graph_search)
        return {"message":"Pensum cargado correctamente"}, 200
    else:
        return {"message": "Request must be JSON"}, 415

@app.get("/cursosPensum")
def reportGraphPensum():
    newGraph = Pensum_Graph()
    newGraph.generateGraph(graph_pensum)  #make a graph of courses pensum
    return {"message": "Reporte generado correctemente"},200

@app.get("/searchCourse/<code>")
def search_course(code):
    newGraph = Pensum_Graph()
    newGraph.graphCourse(int(code), graph_search)
    return {"message": "Reporte generado correctemente"},200


@app.post("/login")
def login():
    req = request.json
    if request.is_json:
        #return jsonify({'message':'Logeado correctemente'}), 200
        return login_controller(tree_student, req)

@app.post("/loadNotes")
def loadFileNotes():
    req = request.json
    if request.is_json:
        return loadNotes(req["contenido"], table_notes, listTransactionNotes)
    return {"message":"Request must be JSON"}, 415

@app.post("/newNote")
def new_note():
    req = request.json
    if request.is_json:
        return newNote(req, table_notes, listTransactionNotes)
    return {"message":"Request must be JSON"}, 415

@app.get("/notesStudent/<id_student>")
def view_notes(id_student):
    return notes_student(id_student, table_notes)

@app.get("/reportHash")
def reportHash():
    generateGrah(table_notes)
    return {"message":"exito"}, 200


@app.get("/listStudents/<type>/<key>")
def getListStudents(type, key):
    if type == "1":
        return getListCrypted(tree_student, key)
    if type == "2":
        return getListDecrypted(tree_student, key)
    return {"message": "Error al cargar datos."}, 415


@app.get("/merkleStd")
def getMerkelTree():
    if listTransactionStudent:
        dot = Digraph(filename="merkleTree", format="svg")
        dot.attr('node', shape='rectangle')
        dot.graph_attr["labelloc"] = "t"
        dot.graph_attr["label"] = "ARBOL MERKLE DE ESTUDIANTES"
        dot.graph_attr["fontsize"] = "22"
        mrk = MerkleTree()
        rootMk = mrk.create_merkle_tree(listTransactionStudent, dot)
        dot.render("./Report/merkleTree", view=True)
        print(rootMk)
        return {"message": "Arbol Merkle de estudiantes generado correctamente."}, 200
    else:
        return {"message":"No hay transacciones almacenadas."},400


@app.get("/merkleNotes")
def getMerkelTreeNotes():
    if listTransactionNotes:
        dot = Digraph(filename="merkleTreeN", format="svg")
        dot.attr('node', shape='rectangle')
        dot.graph_attr["labelloc"] = "t"
        dot.graph_attr["label"] = "ARBOL MERKLE DE APUNTES"
        dot.graph_attr["fontsize"] = "22"
        mrk = MerkleTree()
        rootMk = mrk.create_merkle_tree(listTransactionNotes, dot)
        dot.render("./Report/merkleTreeN", view=True)
        return {"message": "Arbol Merkle de apuntes generado correctamente."}, 200
    else:
        return {"message":"No hay transacciones almacenadas."}, 400


@app.get("/merkleCourses")
def getMerkelTreeCourses():
    if listTransactionCourses:
        dot = Digraph(filename="merkleTreeC", format="svg")
        dot.attr('node', shape='rectangle')
        dot.graph_attr["labelloc"] = "t"
        dot.graph_attr["label"] = "ARBOL MERKLE DE CURSOS"
        dot.graph_attr["fontsize"] = "22"
        mrk = MerkleTree()
        rootMk = mrk.create_merkle_tree(listTransactionNotes, dot)
        dot.render("./Report/merkleTreeC", view=True)
        return {"message": "Arbol Merkle de cursos generado correctamente."}, 200
    else:
        return {"message":"No hay transacciones almacenadas."},400


if __name__ == '__main__':
    app.run(debug=True, port=3000)
