from Graph.ABB_Graph import ABB_Graph
from Graph.Matriz_Graph import Matrix_Graph
from Graph.List_Graph import List_Graph


def make_report(req, tree_student):
    if req['tipo'] == 0:
        if tree_student.root is not None:
            grafo = ABB_Graph()
            grafo.graph_avl(tree_student.root)
            return {"Exito": "Arbol generado correctamente"}, 201
        else:
            return {"Warning": "Arbol no encontrado (cargue estudiantes)."}, 404
    elif req['tipo'] == 1 or req['tipo'] == 2:
        node_student = tree_student.search(req['carnet'])
        if node_student is not None:
            graphM = Matrix_Graph()
            get_year = node_student.student.list_year.search(req['año'])
            if get_year is not None:
                get_month = get_year.data.list_months.search(req['mes'])
                if get_month is not None:
                    get_matrix = get_month.data.sparse_matrix
                    if req['tipo'] == 1:
                        graphM.graph_matrix(get_matrix)
                    if req['tipo'] == 2:
                        ss = get_matrix.head_column.search(req['dia'])
                        print(ss)
                        temp = ss.down
                        while temp is not None:
                            if int(temp.row) == int(req['hora']):
                                enco = temp
                                grapLs = List_Graph()
                                grapLs.graph_list(temp.first)
                                #controlar si  no se encuentra
                            temp = temp.down
                else:
                    return {"Warning": "Mes no encontrado."}, 404
            else:
                return {"Warning": "Año no encontrado."}, 404
            #bbb = node_student.student.list_year.search(req['año']).data.list_months.search(req['mes']).data.sparse_matrix
            return {"Exito": "Matriz dispersa de tareas generada correctamente"}, 201
        else:
            return {"Warning": "Estudiante no encontrado."}, 404


