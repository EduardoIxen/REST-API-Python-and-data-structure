from Graph.ABB_Graph import ABB_Graph
from Graph.Matriz_Graph import Matrix_Graph
from Graph.List_Graph import List_Graph
from  Graph.BTree_Graph import graphTree


def make_report(req, tree_student, tree_pensum):
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
            get_year = node_student.student.list_year.search(int(req['año']))
            if get_year is not None:
                get_month = get_year.data.list_months.search(int(req['mes']))
                if get_month is not None:
                    get_matrix = get_month.data.sparse_matrix
                    if req['tipo'] == 1:
                        if get_matrix.head_column.first is not None:
                            graphM.graph_matrix(get_matrix)
                            return {"Exito": "Matriz dispersa de tareas generada correctamente"}, 201
                        else:
                            return {"Warning": "Matriz vacia."}, 200
                    if req['tipo'] == 2:
                        get_day = get_matrix.head_column.search(int(req['dia']))
                        if get_day is None:
                            return {"Warning": "Dia no encontrado."}, 404
                        temp = get_day.down
                        while temp is not None:
                            if int(temp.row) == int(req['hora']):
                                if temp.first is not None:
                                    grapLs = List_Graph()
                                    grapLs.graph_list(temp.first)
                                    return {"Exito": "Lista de tareas generada correctamente"}, 201
                                else:
                                    return {"Warning": "Lista vacia."}, 200
                            temp = temp.down
                        return {"Warning": "No se encontro la hora."}, 404
                else:
                    return {"Warning": "Mes no encontrado."}, 404
            else:
                return {"Warning": "Año no encontrado."}, 404
            #return {"Exito": "Matriz dispersa de tareas generada correctamente no encontrada"}, 201
        else:
            return {"Warning": "Estudiante no encontrado."}, 404
    elif req['tipo'] == 4:
        node_student = tree_student.search(req['carnet'])
        if node_student is None:
            return {"Warning": "Estudiante no encontrado."}, 404
        get_year = node_student.student.list_year.search(int(req['año']))
        if get_year is None:
            return {"Warning": "Año no encontrado."}, 404
        get_semester = get_year.data.list_semesters.search(req['semestre'])
        if get_semester is None:
            return {"Warning": "Semestre no encontrado."}, 404
        if get_semester.data.binary_tree.root.count == 0:
            return {"Warning": "Arbol de cursos vacio."}, 404
        graphTree(get_semester.data.binary_tree.root, f"DEL ESTUDIANTE {req['carnet']}")
        return {"Exito": "Arbol de cursos generado correctamente."}, 201
    elif req['tipo'] == 3:
        if tree_pensum.root.count > 0:
            graphTree(tree_pensum.root, "DEL PENSUM")
            return {"Exito": "Arbol de cursos de pensum generado correctamente."}, 201
        else:
            return {"Warning": "Arbol de cursos de pensum vacio."}, 404
    else:
        return {"Error": "Tipo de reporte invalido."}, 400
