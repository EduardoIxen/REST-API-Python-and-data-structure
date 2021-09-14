from Data_Structures.Double_Linked_List import Double_Linked_List
from Data_Structures.NodeList import NodeList
from Obj.Task import Task

class List_Task(Double_Linked_List):
    def __init__(self):
        Double_Linked_List.__init__()
        self.row = 0
        self.column = 0

    def insert(self, row, column, task):
        self.row = row
        self.column = column
        new_node = NodeList(task)
        if self.first is None:
            self.first = new_node
            self.last = new_node
            self.size += 1
        else:
            self.last.next = new_node
            new_node.previus = self.last
            self.last = new_node
            self.size += 1

    def search(self):
        pass

    def getValue(self):
        return "Numero de tareas: "+str(self.size)

