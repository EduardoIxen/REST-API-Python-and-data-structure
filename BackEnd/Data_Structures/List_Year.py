from BackEnd.Data_Structures.Double_Linked_List import Double_Linked_List
from BackEnd.Obj.Year import Year
from BackEnd.Data_Structures.NodeList import NodeList


class List_Year(Double_Linked_List):

    def insert(self, year):
        if self.search(year) is not None:
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

    def search(self, year):
        aux = self.first
        while aux is not None:
            if aux.data.number_year == year:
                return aux
            aux = aux.next

        return None

