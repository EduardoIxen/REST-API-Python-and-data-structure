from Obj.Student import Student
from Obj.Task import Task
from Data_Structures.Double_Linked_List import Double_Linked_List

def load_student(tree_student, list_value):
    listTask = []
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
            newStudent = Student(carnet, dpi, name, degree, email, password, credits, age, Double_Linked_List())
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
            listTask.append(newTask)

    print(len(listTask))
