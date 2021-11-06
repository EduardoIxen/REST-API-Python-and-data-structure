from BackEnd.Data_Structures.Grafo.Lista import Lista


class Queue(Lista):
    def __init__(self):
        Lista.__init__(self)

    def enqueue(self, data, ponderacion):
        self.addNode(data, ponderacion)

    def dequeue(self):
        if self.first is not None:
            aux = self.first
            self.deleteNode(self.first.data)
        else:
            print("----COla vacia---")
            return None
        return aux