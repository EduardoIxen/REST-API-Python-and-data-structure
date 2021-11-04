from BackEnd.Data_Structures.Hash_Table.Node import Node


class Hash_Table:
    def __init__(self, size):
        self.size = size
        self.first = None
        self.loadFactor = 0.0
        self.id = 0

    def insertHash(self, carnet, title, content):
        self.loadFactor = (self.id / self.size) * 100

        if self.loadFactor <= 50 and self.loadFactor >= 0:
            key = carnet % self.size
            self.insert(carnet, title, content, key)
        else:
            self.size += 2
            self.insertHash(carnet, title, content)

    def insert(self, carnet, title, content, key):
        new_node = Node(key, carnet, title, content)
        if self.first is None:
            self.first = new_node
            self.id += 1
            return

        if self.searchKey(key):
            i = 0
            position = self.searchPosition(new_node, i)
            self.insert(carnet, title, content, position)
        else:
            temp = self.first
            if new_node.key < temp.key:
                new_node.next = temp
                self.first = new_node
                self.id += 1
            else:
                while temp.next is not None:
                    temp2 = temp.next
                    if new_node.key < temp2.key:
                        temp.next = new_node
                        new_node.next = temp2
                        self.id += 1
                        break
                    temp = temp.next
                if temp.next is None:
                    temp.next = new_node
                    self.id += 1


    def searchPosition(self, current, i):
        position = (current.key + i * i) % self.size
        if self.searchKey(position):
            i += 1
            return self.searchPosition(current, i)
        return position

    def searchKey(self, key):
        temp = self.first
        while temp is not None:
            if key == temp.key:
                return True
            temp = temp.next
        return False
