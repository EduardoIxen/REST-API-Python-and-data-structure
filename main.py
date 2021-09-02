#from Data_Structures.ABB import ABB
#from Obj.Student import Student
#from Grafo.ABB_Graph import ABB_Graph
from Data_Structures.Double_Linked_List import Double_Linked_List


if __name__ == '__main__':
    # arbol = ABB()
    # grafo = ABB_Graph()
    # arbol.insertar(Student(201800524,3132221122331, "encontrado", "sistemas", "ed@fm.com", "asdasd", 126, 22, None))
    # arbol.buildTree(arbol.root)
    # grafo.graph_avl(arbol.root)
    # result = arbol.search(arbol.root, 201800527)
    # if result:
    #     print(f"carnet: {result.student.carnet}, nombre: {result.student.name}")
    # else:
    #     print("no se encontro el carnet ingresado")

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
