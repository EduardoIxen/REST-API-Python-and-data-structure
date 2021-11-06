from BackEnd.Data_Structures.Double_Linked_List import Double_Linked_List
from BackEnd.Data_Structures.NodeList import NodeList
from BackEnd.Obj.Month import Month


class List_Month(Double_Linked_List):
    def insert(self, month):
        if self.search(month) is not None:
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

    def search(self, month):
        aux = self.first
        while aux is not None:
            if aux.data.numberM == month:#cambiar string a int
                return aux
            aux = aux.next

        return None

#retornar nodo para insertar en matriz dispersa