from Data_Structures.Double_Linked_List import Double_Linked_List

class Header(Double_Linked_List):
    def __init__(self):
        Double_Linked_List.__init__(self)

    def insert(self, new_node):
        if self.first is None: #list empty and retur node first
            self.first = new_node
            self.last = new_node
            return self.first
        elif int(new_node.getValue()) < int(self.first.getValue()):  #insert new first, smaller number
            self.first.previous = new_node
            new_node.next = self.first
            self.first = new_node
            return self.first
        elif int(new_node.getValue()) == int(self.first.getValue()): #new node is equal to first, return first
            return self.first
        elif int(new_node.getValue()) > int(self.last.getValue()): #add new node to the end
            self.last.next = new_node
            new_node.previous = self.last
            self.last = new_node
            return self.last
        else: #add new node to half
            tmp = self.first
            while tmp.next is not None:
                if int(new_node.getValue()) > int(tmp.getValue()) and int(new_node.getValue()) < int(tmp.next.getValue()):
                    tmp.next.previous = new_node
                    new_node.next = tmp.next
                    tmp.next = new_node
                    new_node.previous = tmp
                    return new_node
                elif str(new_node.getValue()) == str(tmp.getValue()): #node exist
                    return tmp
                tmp = tmp.next
            if int(new_node.getValue()) == int(tmp.getValue()): #compare the last
                return tmp

    def search(self, data):
        tmp = self.first
        while tmp is not None:
            if int(tmp.getValue()) == int(data):
                return tmp
            tmp = tmp.next
        return None

