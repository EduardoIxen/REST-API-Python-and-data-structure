from Data_Structures.NodeList import NodeList
from Obj.Year import Year
from Obj.Month import Month
from Obj.Semester import Semester


class Double_Linked_List:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def insert_year(self, year):
        if self.search_year(year):
            print(f"ADVERTENCIA// El año {year}, ya existe en la lista doblemente enlazada. (No se volvio a agregar)")
            return

        new_Year = Year(year)
        new_Node = NodeList(new_Year)
        if self.first is None:
            self.first = new_Node
            self.last = new_Node
            self.size += 1
        else:
            aux = self.first
            while aux != None:
                if aux.data.number_year < year:
                    if aux.next is None:
                        aux.next = new_Node
                        new_Node.previus = aux
                        self.size += 1
                        break
                elif aux.data.number_year > year:
                    if aux == self.first:
                        self.first = new_Node
                        new_Node.next = aux
                        aux.previus = new_Node
                        self.size += 1
                        break
                    else:
                        aux.previus.next = new_Node
                        new_Node.previus = aux.previus
                        aux.previus = new_Node
                        new_Node.next = aux
                        self.size += 1
                        break

                aux = aux.next

    def search_year(self, year):
        aux = self.first
        while aux is not None:
            if aux.data.number_year == year:
                return True
            aux = aux.next

        return False

    def insert_month(self, month):
        if self.search_month(month):
            print(f"ADVERTENCIA// El mes {month}, ya existe en la lista doblemente enlazada. (No se volvio a agregar)")
            return

        new_month = Month(month)
        new_Node = NodeList(new_month)
        if self.first is None:
            self.first = new_Node
            self.last = new_Node
            self.size += 1
        else:
            aux = self.first
            while aux != None:
                if aux.data.numberM < month:
                    if aux.next is None:
                        aux.next = new_Node
                        new_Node.previus = aux
                        self.size += 1
                        break
                elif aux.data.numberM > month:
                    if aux == self.first:
                        self.first = new_Node
                        new_Node.next = aux
                        aux.previus = new_Node
                        self.size += 1
                        break
                    else:
                        aux.previus.next = new_Node
                        new_Node.previus = aux.previus
                        aux.previus = new_Node
                        new_Node.next = aux
                        self.size += 1
                        break

                aux = aux.next

    def search_month(self, month):
        aux = self.first
        while aux is not None:
            if aux.data.numberM == month:
                return True
            aux = aux.next

        return False

    def insert_semester(self, number):
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
