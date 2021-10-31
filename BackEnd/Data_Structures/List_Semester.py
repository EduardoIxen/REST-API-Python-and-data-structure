from Data_Structures.Double_Linked_List import Double_Linked_List
from Obj.Semester import Semester
from Data_Structures.NodeList import NodeList


class List_Semester(Double_Linked_List):
    def insert(self, number):
        new_semester = Semester(number)
        new_node = NodeList(new_semester)
        if number == "1":
            if self.first is None:
                self.first = new_node
                self.first.next = self.last
                self.size += 1
            else:
                print(f"ADVERTENCIA// El semestre {number}, ya existe en la lista enlazada. (No se volvio a agregar)")
        elif number == "2":
            if self.last is None:
                self.last = new_node
                self.size += 1
            else:
                print(f"ADVERTENCIA// El semestre {number}, ya existe en la lista enlazada. (No se volvio a agregar)")

    def search(self, semester):
        if self.first is not None:
            if self.first.data.number == semester:
                return self.first
        if self.last is not None:
            if self.last.data.number == semester:
                return self.last
        return None
