from Obj.Student import Student
from Data_Structures.List_Year import List_Year


def create_student(tree_student, req):
    tree_student.insert(Student(req['carnet'], req['DPI'], req['nombre'], req['carrera'], req['correo'], req['password']
                                , req['creditos'], req['edad'], List_Year()))

    return {"Exito":"Estudiante creado correctamente"}, 201


def modify_student(tree_student, req):
    node_student = tree_student.search(req['carnet'])
    if node_student is None:
        return {"Warning": f"Estudiante no encontrado -> {req['carnet']}"}, 404
    node_student.student.age = req['edad']
    node_student.student.carnet = req['carnet']
    node_student.student.credits = req['creditos']
    node_student.student.degree = req['carrera']
    node_student.student.dpi = req['DPI']
    node_student.student.email = req['correo']
    node_student.student.name = req['nombre']
    node_student.student.password = req['password']
    return {"Exito": f"Estudiante midificado correctamente."}, 200


def delete_student(tree_student, req):
    if tree_student.search(req['carnet']) is None:
        return {"Warning": f"Estudiante no encontrado -> {req['carnet']}"}, 404
    tree_student.delete_student(req['carnet'])
    tree_student.balance_tree()
    return {"Exito": f"Estudiante eliminado."}, 200


def get_student(tree_student, req):
    node_student = tree_student.search(req['carnet'])
    if node_student is None:
        return {"Warning": f"Estudiante no encontrado -> {req['carnet']}"}, 404

    student_found = node_student.student
    return {"Carnet":f"{student_found.carnet}",
            "DPI":f"{student_found.dpi}",
            "Nombre":f"{student_found.name}",
            "Carrera":f"{student_found.degree}",
            "Correo":f"{student_found.email}",
            "Password":f"{student_found.password}",
            "Creditos":f"{student_found.credits}",
            "Edad":f"{student_found.age}"
            }