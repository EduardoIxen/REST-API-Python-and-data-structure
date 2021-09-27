from Obj.Task import Task
from Controller.LoadData import get_days_month


def create_task(tree_student, req):
    node_student = __verify_student(tree_student, req)
    if node_student is None:
        return {"Warning": f"Estudiante no encontrado -> {req['carnet']}"}, 404
    student = node_student.student
    list_date = req['Fecha'].strip().split(sep="/")
    hour = req['Hora'].strip().split(sep=":")
    if int(list_date[0]) < 1 or int(list_date[0]) > get_days_month(int(list_date[1]), int(list_date[2])):
        return {"Error": "Dia fuera del rango valido."}
    if int(hour[0]) < 0 or int(hour[0]) > 24:
        return {"Error": "Hora fuera del rango valido."}

    student.list_year.insert(int(list_date[2]))
    student.list_year.search(int(list_date[2])).data.list_months.insert(int(list_date[1]))
    node_monthstd = student.list_year.search(int(list_date[2])).data.list_months.search(int(list_date[1]))
    new_task = Task(req['Carnet'], req['Nombre'], req['Descripcion'], req['Materia'], req['Fecha'], req['Hora'], req['Estado'])
    node_monthstd.data.sparse_matrix.add_task(int(hour[0]), int(list_date[0]), new_task)
    return {"Exito": "Recordatorio creado correctamente"}, 201


def modify_task(tree_student, req):
    node_student = __verify_student(tree_student, req)
    if node_student is None:
        return {"Warning": f"Estudiante no encontrado -> {req['carnet']}"}, 404
    student = node_student.student
    list_date = req['Fecha'].strip().split(sep="/")
    get_year = student.list_year.search(int(list_date[2]))
    if get_year is None:
        return {"Warning": f"Año no encontrado -> {list_date[2]}"}, 404
    get_month = get_year.data.list_months.search(int(list_date[1]))
    if get_month is None:
        return {"Warning": f"Mes no encontrado -> {list_date[1]}"}, 404
    hour = req['Hora'].strip().split(sep=":")
    return get_month.data.sparse_matrix.update_task(int(hour[0]), int(list_date[0]), req)

def get_task(tree_student, req):
    node_student = __verify_student(tree_student, req)
    if node_student is None:
        return {"Warning": f"Estudiante no encontrado -> {req['Carnet']}"}, 404
    student = node_student.student
    list_date = req['Fecha'].strip().split(sep="/")
    get_year = student.list_year.search(int(list_date[2]))
    if get_year is None:
        return {"Warning": f"Año no encontrado -> {list_date[2]}"}, 404
    get_month = get_year.data.list_months.search(int(list_date[1]))
    if get_month is None:
        return {"Warning": f"Mes no encontrado -> {list_date[1]}"}, 404
    hour = req['Hora'].strip().split(sep=":")
    task_obtained = get_month.data.sparse_matrix.view_task(int(hour[0]), int(list_date[0]), int(req['Posicion']))
    if isinstance(task_obtained, dict):
        return task_obtained, 201
    return {"Warning": "Tarea no encontrada."}, 404


def delete_task(tree_student, req):
    node_student = __verify_student(tree_student, req)
    if node_student is None:
        return {"Warning": f"Estudiante no encontrado -> {req['Carnet']}"}, 404
    student = node_student.student
    list_date = req['Fecha'].strip().split(sep="/")
    get_year = student.list_year.search(int(list_date[2]))
    if get_year is None:
        return {"Warning": f"Año no encontrado -> {list_date[2]}"}, 404
    get_month = get_year.data.list_months.search(int(list_date[1]))
    if get_month is None:
        return {"Warning": f"Mes no encontrado -> {list_date[1]}"}, 404
    hour = req['Hora'].strip().split(sep=":")
    #asd = get_month.data.sparse_matrix.search_list(int(list_date[0]), int(hour[0]))
    if get_month.data.sparse_matrix.delete_list(int(list_date[0]), int(hour[0]), int(req['Posicion'])):
        return {"Exito": f"Tarea {req['Posicion']} eliminada"}, 201
    else:
        return {"Warning" : "Tarea no encontrada."}, 404
    #asd.first = None
    #asd.last = None
    #asd.size = 0




def __verify_student(tree_student, req):
    node_student = tree_student.search(req['Carnet'])
    if node_student is None:
        return None
    return node_student

