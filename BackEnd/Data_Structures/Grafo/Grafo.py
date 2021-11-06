from BackEnd.Data_Structures.Grafo.Lista import Lista


class Grafo:
    def __init__(self):
        self.vertices = []

    def agregarVertice(self, data, course):
        arista = Lista(data, course)
        self.vertices.append(arista)

    def mostrarVertices(self):
        for vert in self.vertices:
            vert.print_list()
            print("\n")

    def crear_arista(self, verticeOrigen, verticeFinal, ponderacion):
        for vertice in self.vertices:
            if vertice.first.data == verticeOrigen:
                vertice.addNode(verticeFinal, ponderacion, None)
