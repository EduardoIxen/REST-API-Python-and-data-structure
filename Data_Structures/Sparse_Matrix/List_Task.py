from Data_Structures.Double_Linked_List import Double_Linked_List
from Data_Structures.NodeList import NodeList
from Data_Structures.Sparse_Matrix.NodeM import NodeM

class List_Task(Double_Linked_List, NodeM):
    def __init__(self):
        NodeM.__init__(self)
        Double_Linked_List.__init__(NodeM)
        self.row = 0
        self.column = 0

    def insert(self, row, column, task):
        self.row = row
        self.column = column
        #new_node = NodeList(task)
        if self.first is None:
            self.first = task
            self.last = task
            self.size += 1
        else:
            self.last.next = task
            task.previous = self.last
            self.last = task
            self.size += 1

    def search(self):
        pass

    def getValue(self):
        return "Numero de tareas: "+str(self.size)

    def print_v(self):
        pass

