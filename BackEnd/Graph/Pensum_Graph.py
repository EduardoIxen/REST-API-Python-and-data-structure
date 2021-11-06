from graphviz import Digraph


class Pensum_Graph:
    def generateGraph(self, grafo):
        dot = Digraph(filename="graphPensum", format="svg")
        dot.graph_attr["rankdir"] = "LR"
        dot.attr('node', shape='rectangle')
        for vertice in grafo.vertices:
            #agregar nodo
            contentNode = str(vertice.first.data) + "\\n" +vertice.first.course.name
            dot.node(str(vertice.first.data), contentNode)
            if vertice.first is None:
                continue
            temp = vertice.first
            while True:
                #agregar relacion
                if temp != vertice.first:
                    dot.edge(str(vertice.first.data), str(temp.data), label=str(temp.ponderacion))
                if temp.next is not None:
                    temp = temp.next
                else:
                    break
        dot.render("../FrontEnd/SmartClass/src/assets/img/coursesPensum", view=False)


    def graphCourse(self, code, grafo):
        listRelations = []
        dot = Digraph(filename="graphPensum", format="svg")
        dot.graph_attr["rankdir"] = "LR"
        dot.attr('node', shape='rectangle')

        visitados = []
        pila = []
        pila.append(int(code))
        while pila:
            actual = pila.pop()
            if actual not in visitados:
                visitados.append(int(actual))
                contenido = str(actual) +"\\n"+ self.searchCourse(grafo, int(actual))
                dot.node(str(actual), contenido)
            for vertice in grafo.vertices:
                if vertice.first.data == actual:
                    temp = vertice.first
                    while temp is not None:
                        if temp != vertice.first:
                            if {"a":str(temp.data), "b":str(vertice.first.data)} not in listRelations:
                                listRelations.append({"a":str(temp.data), "b":str(vertice.first.data)})
                                dot.edge(str(temp.data), str(vertice.first.data), label=str(temp.ponderacion))
                            if int(temp.data) not in visitados:
                                pila.append(int(temp.data))
                        temp = temp.next

        dot.render("../FrontEnd/SmartClass/src/assets/img/graphCourse", view=False)

    def searchCourse(self, grafo, id):
        for nodo in grafo.vertices:
            if nodo.first.data == id:
                return nodo.first.course.name
        return ""