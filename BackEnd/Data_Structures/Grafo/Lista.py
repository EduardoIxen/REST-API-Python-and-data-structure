from BackEnd.Data_Structures.Grafo.Nodo import Nodo


class Lista:
    def __init__(self, data, course):
        self.first = Nodo(data,0, course)
        self.last = self.first

    def addNode(self, data, ponderacion, course):
        newNode = Nodo(data, ponderacion, course)
        if self.isEmpty():
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode

    def print_list(self):
        if self.isEmpty():
            return False
        temp = self.first
        while True:
            print(temp.data, " => ", end="")
            if temp.next is not None:
                temp = temp.next
            else:
                break

    def deleteNode(self, data):
        if self.isEmpty():
            return False
        else:
            if self.first.data == data:
                if self.first.next is not None:
                    self.first = self.first.next
                    return True
                else:
                    self.first = None
                    return True
            else:
                current = self.first
                previous = None
                while current.data != data:
                    previous = current
                    current = current.next
                    if current is None:
                        return False
                previous.next = current.next
                if current == self.last:
                    self.last = previous
                return True


    def isEmpty(self):
        result = True if self.first is None else False
        return result
