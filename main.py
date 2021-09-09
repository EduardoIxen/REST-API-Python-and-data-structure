from Data_Structures.ABB import ABB
from Analyzer.Parser import parse
from Controller.LoadData import load_student
#from Obj.Student import Student
from Grafo.ABB_Graph import ABB_Graph
import flask.cli

from Data_Structures.Double_Linked_List import Double_Linked_List
from flask import Flask, jsonify, request


#if __name__ == '__main__':
tree_student = ABB()
# grafo = ABB_Graph()
# arbol.insertar(Student(201800524,3132221122331, "encontrado", "sistemas", "ed@fm.com", "asdasd", 126, 22, None))
# arbol.buildTree(arbol.root)
# grafo.graph_avl(arbol.root)
# result = arbol.search(arbol.root, 201800527)
# if result:
#     print(f"carnet: {result.student.carnet}, nombre: {result.student.name}")
# else:
#     print("no se encontro el carnet ingresado")

'''
lista = Double_Linked_List()
lista.insert_year(2020)
lista.insert_year(2022)
lista.insert_year(2021)
lista.insert_year(1999)

listaM = Double_Linked_List()
listaM.insert_month(4)
listaM.insert_month(8)
listaM.insert_month(9)
listaM.insert_month(4)
listaM.insert_month(10)
listaM.insert_month(6)

listaS = Double_Linked_List()
listaS.insert_semester("2")
listaS.insert_semester("1")
print(lista.first.data.number_year)
'''
app = Flask(__name__)

@app.route('/')
def index():
    return "Hola mundo"

@app.post("/carga")
def loadFile():
    req = request.json
    if request.is_json:
        print(f"tipo: {req['tipo']}, path: {req['path']}")
        f = open(req['path'], "r", encoding="utf-8")
        content = f.read()
        f.close()
        lstValues = parse(content)
        load_student(tree_student, lstValues)
        grafo = ABB_Graph()
        grafo.graph_avl(tree_student.root)
        return {"Exito":"Insertado correctamente"}, 201
    return {"error": "Request must be JSON"}, 415

if __name__ == '__main__':
    app.run(debug=True)

