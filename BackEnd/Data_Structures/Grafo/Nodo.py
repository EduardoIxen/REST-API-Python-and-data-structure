class Nodo:
    def __init__(self, data, ponderacion, course):
        self.data = data
        self.ponderacion = ponderacion
        self.course = course
        self.next = None
        self.previous = None