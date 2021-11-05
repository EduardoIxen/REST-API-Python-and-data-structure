from graphviz import Source
import os

class TableHash_Graph:
    def __init__(self):
        pass

    def graphTable(self, hash_table):
        listStudent = []
        temp = hash_table.first
        while temp is not None:
            dicNote = {}
            dicNote['carnet'] = temp.carnet
            position = self.searchStudent(listStudent, temp.carnet)
            if position is not None:
                listStudent[position]['listNotes'].append({"title":temp.title, "content":temp.content})
            else:
                dicNote['listNotes'] = [{"title":temp.title, "content":temp.content}]
                listStudent.append(dicNote)
            temp = temp.next

        acumInfo = "digraph G{\n" \
                   "node[shape=box, width = 1.5];\n" \
                   "rankdir=UD;\n"
        ranks = ""
        labelsAcum = ""
        relationsAcum = ""
        contentDot = ""

        for i in range(len(listStudent)):
            same = "{rank=same;"+"\""+ str(listStudent[i]['carnet'])+"\""+";"   #meter el carnet en el same junto con todos sus apuntes para ir ->
            label = f"\""+str(listStudent[i]['carnet'])+"\"[label=\""+str(listStudent[i]['carnet'])+"\", group=-1, style=filled, color=DarkOrange1];\n"   #crear el nodo del carnet
            labelsAcum += label
            if i < len(listStudent)-1:
                relationsAcum += f"\""+str(listStudent[i]['carnet'])+"\" -> \""+str(listStudent[i+1]['carnet'])+"\";\n"  #agregar relacion con el siguiente carnet
            for j in range(len(listStudent[i]['listNotes'])):
                same += "\""+str(listStudent[i]['listNotes'][j]['title']).strip() + str(j) +"\""+ ";"  #agregar los apuntes al same del carnet para que essten en la misma linea
                labelsAcum += f"\""+str(listStudent[i]['listNotes'][j]['title']).strip() + str(j)+"\"[label=\""+str(listStudent[i]['listNotes'][j]['title'])+"\", group="+str(j)+"];\n"  #crear el nodo del apunte
                if j < len(listStudent[i]['listNotes']) -1:
                    relationsAcum += f"\""+str(listStudent[i]['listNotes'][j]['title']).strip() + str(j)+"\" -> \""+str(listStudent[i]['listNotes'][j+1]['title']).strip() + str(j+1)+"\";\n"  #crear la relacion de los apuntes
                if j == 0:
                    relationsAcum += f"\""+str(listStudent[i]['carnet'])+"\" -> "+"\""+str(listStudent[i]['listNotes'][j]['title']).strip() + str(j) +"\""+ ";\n"  #crear realacion del carnet con el primer apunte
            same += "}\n"
            ranks += same
        print(ranks)
        print(labelsAcum)
        print(relationsAcum)
        contentDot = acumInfo + ranks + labelsAcum + relationsAcum + "\n}\n"

        #s = Source(contentDot, filename="../FrontEnd/SmartClass/src/assets/img/hash_table", format="svg")
        #s.view()



        f = open("../FrontEnd/SmartClass/src/assets/img/hash_table.dot", 'w')
        try:
            f.write(contentDot)
        finally:
            f.close()

        prog = "dot -Tsvg  ../FrontEnd/SmartClass/src/assets/img/hash_table.dot -o ../FrontEnd/SmartClass/src/assets/img/hash_table.svg"
        os.system(prog)


    def searchStudent(self, listStudent, carnet):
        for i in range(len(listStudent)):
            if listStudent[i]['carnet'] == carnet:
                return i
        return None
