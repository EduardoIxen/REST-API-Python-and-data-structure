import json

from BackEnd.Obj.Student import Student
from BackEnd.Obj.Task import Task
from BackEnd.Data_Structures.List_Year import List_Year
from BackEnd.Obj.Course import Course


def load_student(tree_student, list_value):
    list_task = []
    for data in list_value:
        email = " " #i don't know if the mail is in the input file
        if data['type'].lower() == "user":
            for item in data['dicItems']:
                if item['key'].lower() == 'carnet':
                    carnet = item['value']
                elif item['key'].lower() == "dpi":
                    dpi = item['value']
                elif item['key'].lower() == "nombre":
                    name = item['value']
                elif item['key'].lower() == "carrera":
                    degree = item['value']
                elif item['key'].lower() == "correo":
                    email = item['value']
                elif item['key'].lower() == "password":
                    password = item['value']
                elif item['key'].lower() == "creditos":
                    credits = item['value']
                elif item['key'].lower() == "edad":
                    age = item['value']
                else:
                    print("ERROR// Invalid item.")
            newStudent = Student(carnet, dpi, name, degree, email, password, credits, age, List_Year())
            tree_student.insert(newStudent)


        if data['type'].lower() == "task":
            for item in data['dicItems']:
                if item['key'].lower() == "carnet":
                    carnetT = item['value']
                elif item['key'].lower() == "nombre":
                    nameT = item['value']
                elif item['key'].lower() == "descripcion":
                    desctiptionT = item['value']
                elif item['key'].lower() == "materia":
                    courseT = item['value']
                elif item['key'].lower() == "fecha":
                    dateT = item['value']
                elif item['key'].lower() == "hora":
                    hourT = item['value']
                elif item['key'].lower() == "estado":
                    statusT = item['value']
            newTask = Task(carnetT, nameT, desctiptionT, courseT, dateT, hourT, statusT)
            list_task.append(newTask)

    for task in list_task:
        node_student = tree_student.search(task.carnet)
        if node_student is not None:
            student = node_student.student
            list_date = task.date.strip().split(sep="/")
            hourF = task.hour.strip().split(sep=":")
            if int(list_date[0]) < 1 or int(list_date[0]) > get_days_month(int(list_date[1]), int(list_date[2])):
                print("Dia fuera de rango valido.")
                continue
            if int(hourF[0]) < 0 or int(hourF[0]) > 24:
                print("Hora fuera del rango valido.")
                continue

            student.list_year.insert(int(list_date[2]))
            student.list_year.search(int(list_date[2])).data.list_months.insert(int(list_date[1]))
            node_monthstd = student.list_year.search(int(list_date[2])).data.list_months.search(int(list_date[1]))
            node_monthstd.data.sparse_matrix.add_task(int(hourF[0]), int(list_date[0]), task)
        else:
            print("Student not founf: ", task.carnet)


def load_student_frontend(tree_student, list_values):
    for student in list_values['estudiantes']:
        carnet = str(student['carnet'])
        dpi = str(student['DPI'])
        name = student['nombre']
        degree = student['carrera']
        email = student['correo']
        password = student['password']
        #credits = student['creditos']
        credits = 0
        age = student['edad']
        newStudent = Student(carnet, dpi, name, degree, email, password, credits, age, List_Year())
        tree_student.insert(newStudent)



def load_course(tree_student, content):
    for studentC in content['Estudiantes']:
        node_student = tree_student.search(studentC['Carnet'])
        if node_student is None:
            return {"message":"Estudiante no encontrado."}, 404
        student_founf = node_student.student
        for yearC in studentC['Años']:
            student_founf.list_year.insert(int(yearC['Año']))
            for semester in yearC['Semestres']:
                student_founf.list_year.search(int(yearC['Año'])).data.list_semesters.insert(semester['Semestre'])
                for course in semester['Cursos']:
                    b_tree_found = student_founf.list_year.search(int(yearC['Año'])).data.list_semesters.search(semester['Semestre']).data.binary_tree
                    b_tree_found.insert(Course(int(course['Codigo']), course['Nombre'], course['Creditos'], course['Prerequisitos'], course['Obligatorio']))
    return {"message": "Archivo de cursos de estudiantes cargado correctamente"}, 201


def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def get_days_month(month, year):
    #April, June, September, December -> 30 days
    if month in [4, 6, 9, 12]:
        return 30
    #February verify leap year
    if month == 2:
        if leap_year(year):
            return 29
        else:
            return 28
    else:
        return 31

