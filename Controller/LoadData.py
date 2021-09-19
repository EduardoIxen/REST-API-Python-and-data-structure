from Obj.Student import Student
from Obj.Task import Task
from Data_Structures.List_Year import List_Year
from Graph.Matriz_Graph import Matrix_Graph

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
            student.list_year.insert(list_date[2])
            student.list_year.search(list_date[2]).data.list_months.insert(list_date[1])
            node_monthstd = student.list_year.search(list_date[2]).data.list_months.search(list_date[1])
            hourF = task.hour.strip().split(sep=":")
            node_monthstd.data.sparse_matrix.add_task(hourF[0], list_date[0], task)
        else:
            print("Student not founf: ", task.carnet)
