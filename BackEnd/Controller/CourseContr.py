import json

from BackEnd.Obj.Course import Course
from BackEnd.Controller.LoadData import load_course


def add_course_student(tree_student, req, listTransactionCourses):
    return load_course(tree_student, req, listTransactionCourses)


def add_course_pensum(tree_B, req):
    dic_courses = {}
    if type(req['Cursos']) == str:
        dic_courses = json.loads(req['Cursos'])
    else:
        dic_courses = req

    for courseP in dic_courses['Cursos']:
        newCourse = Course(int(courseP['Codigo']), courseP['Nombre'], courseP['Creditos'], courseP['Prerequisitos'], courseP['Obligatorio'])
        tree_B.insert(newCourse)
    return {"message":"Cursos de pensum creados correctamente"}


def add_course_graph(req, graph, graph_search):
    listCourses =  []
    dic_courses = {}
    if type(req['Cursos']) == str:
        dic_courses = json.loads(req['Cursos'])
    else:
        dic_courses = req

    for courseP in dic_courses['Cursos']:
        newCourse = Course(int(courseP['Codigo']), courseP['Nombre'], courseP['Creditos'], courseP['Prerequisitos'],
                           courseP['Obligatorio'])
        listCourses.append(newCourse)
        graph.agregarVertice(int(courseP['Codigo']), newCourse)
        graph_search.agregarVertice(int(courseP['Codigo']), newCourse)

    for courseP in dic_courses['Cursos']:
        if courseP['Prerequisitos'] != "":
            prerequisitos = courseP['Prerequisitos'].split(sep=",")
            for cod in prerequisitos:
                ponderacion = searchCourse(listCourses, int(cod))
                if ponderacion is None:
                    ponderacion = 0
                graph.crear_arista(int(cod), int(courseP['Codigo']), ponderacion)
                graph_search.crear_arista(int(courseP['Codigo']), int(cod), ponderacion)
        #agregar los prerequisitos

    return {"message": "Grafo de pensum creado correctamente"},200


def searchCourse(listCourse, code):
    for course in listCourse:
        if int(course.code) == int(code):
            return course.credits
    return None
