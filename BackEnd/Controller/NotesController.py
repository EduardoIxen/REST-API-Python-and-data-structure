import json
from datetime import date
from BackEnd.Graph.TableHash_Graph import TableHash_Graph
from BackEnd.Encryption.HashPassword import HashPassword

def loadNotes(notes_text, hash_table, listTransactionNotes):
    notes = json.loads(notes_text)
    for usuario in notes["usuarios"]:
        for apunte in usuario['apuntes']:
            hash_table.insertHash(int(usuario['carnet']), apunte['Título'], apunte['Contenido'])

            today = date.today()
            data = today.strftime("%d/%m/%Y") + str(usuario['carnet']) + str(apunte['Título']) + str(apunte['Contenido'])
            hash_data = HashPassword(data)
            listTransactionNotes.append(hash_data.Hash())
    return {"message": "Apuntes cargados con exito."}, 200


def newNote(req, hash_table, listTransactionNotes):
    hash_table.insertHash(int(req['carnet']), req['title'], req['content'])

    today = date.today()
    data = today.strftime("%d/%m/%Y") + str(req['carnet']) + str(req['title']) + str(req['content'])
    hash_data = HashPassword(data)
    listTransactionNotes.append(hash_data.Hash())
    return {'message': 'Apunte agregado correctamente.'}, 200

def notes_student(id, hash_table):
    listNotes = []
    contador = 1
    if hash_table.first is None:
        return {"message": "No hay apuntes cargados."}, 200
    temp = hash_table.first
    while temp is not None:
        note = {}
        if int(temp.carnet) == int(id):
            note["no"] = contador
            note["title"] = temp.title
            note["content"] = temp.content
            listNotes.append(note)
            contador += 1
        temp = temp.next
    return {"message": "Apuntes recuperados", "listNotes":listNotes}, 200


def generateGrah(hash_table):
    newGraph = TableHash_Graph()
    newGraph.graphTable(hash_table)
