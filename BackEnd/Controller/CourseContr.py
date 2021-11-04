import json

from Obj.Course import Course
from Controller.LoadData import load_course


def add_course_student(tree_student, req):
    return load_course(tree_student, req)

def add_course_pensum(tree_B, req):
    dic_courses = {}
    if type(req['Cursos']) == str:
        dic_courses = json.loads(req['Cursos'])
    elif type(req['Cursos']) == dict:
        dic_courses = req

    for courseP in dic_courses['Cursos']:
        newCourse = Course(int(courseP['Codigo']), courseP['Nombre'], courseP['Creditos'], courseP['Prerequisitos'], courseP['Obligatorio'])
        tree_B.insert(newCourse)
    return {"message":"Cursos de pensum creados correctamente"}
