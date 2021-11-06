from BackEnd.Data_Structures.Double_Linked_List import Double_Linked_List
from BackEnd.Data_Structures.Sparse_Matrix.NodeM import NodeM

class List_Task(Double_Linked_List, NodeM):
    def __init__(self):
        NodeM.__init__(self)
        Double_Linked_List.__init__(NodeM)
        self.row = 0
        self.column = 0

    def insert(self, row, column, task):
        self.row = row
        self.column = column
        if self.first is None:
            self.first = task
            self.last = task
            self.size += 1
        else:
            self.last.next = task
            task.previous = self.last
            self.last = task
            self.size += 1

    def delete_task(self, position):
        if position == 1:
            if self.first.next is not None:
                self.first.next.previous = None
                self.first = self.first.next
                self.size -= 1
                return True
            else:
                self.first = None
                self.last = None
                self.size = 0
            return True
        if position == self.size:
            new_last = self.last.previous
            new_last.next = None
            self.last = new_last
            self.size -= 1
            return True

        temp = self.first
        count = 1
        while temp is not None:
            if position == count:
                if temp.next is not None:
                    if temp.previous is not None:
                        temp.previous.next = temp.next
                        temp.next.previous = temp.previous
                        self.size -= 1
                        return True

            count += 1
            temp = temp.next
        return False

    def search(self):
        pass

    def getValue(self):
        return "Numero de tareas: "+str(self.size)

    def print_v(self):
        pass

