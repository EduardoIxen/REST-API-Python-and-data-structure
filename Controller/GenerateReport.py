from Grafo.ABB_Graph import ABB_Graph
from Grafo.Matriz_Graph import Matrix_Graph


def make_report(req, tree_student):
    if req['tipo'] == 0:
        if tree_student.root is not None:
            grafo = ABB_Graph()
            grafo.graph_avl(tree_student.root)
            return {"Exito": "Arbol generado correctamente"}, 201
        else:
            return {"Warning": "Arbol no encontrado (cargue estudiantes)."}, 404
    elif req['tipo'] == 1:
        node_student = tree_student.search(req['carnet'])
        if node_student is not None:
            graphM = Matrix_Graph()
            bbb = node_student.student.list_year.search(req['año']).data.list_months.search(req['mes']).data.sparse_matrix
            graphM.graph_matrix(bbb)
                                #.data.list_months.search(req['mes']).sparse_matrix)
            #revisar data, para encontrar la matriz
            return {"Exito": "Matriz dispersa de tareas generada correctamente"}, 201
        else:
            return {"Warning": "Estudiante no encontrado."}, 404
