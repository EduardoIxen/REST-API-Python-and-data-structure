from Obj.Course import Course
from Controller.LoadData import load_course


def add_course_student(tree_student, req):
    return load_course(tree_student, req)

def add_course_pensum(tree_B, req):
    for courseP in req['Cursos']:
        newCourse = Course(int(courseP['Codigo']), courseP['Nombre'], courseP['Creditos'], courseP['Prerequisitos'], courseP['Obligatorio'])
        tree_B.insert(newCourse)
    return {"Exito":"Cursos de pensum creados correctamente"}
