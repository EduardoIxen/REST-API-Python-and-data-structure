from Data_Structures.ABB import ABB
from Obj.Student import Student
from Grafo.ABB_Graph import ABB_Graph


if __name__ == '__main__':
    arbol = ABB()
    grafo = ABB_Graph()
    arbol.insertar(Student(201800524,3132221122331, "Tomas", "sistemas", "ed@fm.com", "asdasd", 126, 22, None))
    arbol.insertar(Student(201800525,3132221122331, "Tomas", "sistemas", "ed@fm.com", "asdasd", 126, 22, None))
    arbol.insertar(Student(201800526,3132221122331, "Tomas", "sistemas", "ed@fm.com", "asdasd", 126, 22, None))
    arbol.insertar(Student(201533907,3132221122331, "Tomas", "sistemas", "ed@fm.com", "asdasd", 126, 22, None))
    arbol.insertar(Student(201491494 ,3132221122331, "Tomas", "sistemas", "ed@fm.com", "asdasd", 126, 22, None))
    arbol.insertar(Student(201045090 ,3132221122331, "Tomas", "sistemas", "ed@fm.com", "asdasd", 126, 22, None))
    arbol.insertar(Student(201027375 ,3132221122331, "Tomas", "sistemas", "ed@fm.com", "asdasd", 126, 22, None))
    arbol.insertar(Student(201800526,3132221122331, "Tomas", "sistemas", "ed@fm.com", "asdasd", 126, 22, None))
    arbol.insertar(Student(201340841 ,3132221122331, "Tomas", "sistemas", "ed@fm.com", "asdasd", 126, 22, None))
    arbol.insertar(Student(201296311 ,3132221122331, "Tomas", "sistemas", "ed@fm.com", "asdasd", 126, 22, None))
    arbol.insertar(Student(201835603 ,3132221122331, "Tomas", "sistemas", "ed@fm.com", "asdasd", 126, 22, None))
    arbol.insertar(Student(201639410 ,3132221122331, "Tomas", "sistemas", "ed@fm.com", "asdasd", 126, 22, None))
    arbol.insertar(Student(201800526,3132221122331, "Tomas", "sistemas", "ed@fm.com", "asdasd", 126, 22, None))
    arbol.buildTree(arbol.root)
    grafo.graph_avl(arbol.root)

